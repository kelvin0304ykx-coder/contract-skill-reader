"""Prepare a new synthetic exercise or read DOCX without changing source files."""
from pathlib import Path
from zipfile import ZipFile,BadZipFile
from xml.etree import ElementTree as ET
import argparse,hashlib,importlib.util,importlib.metadata,json,shutil,sys,platform

ROOT=Path(__file__).resolve().parents[1]
W='{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
CASES={'redline':'01-代表乙方审改.md','intake':'02-未说明代表方.md','signing':'03-签署前核对.md'}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def text(n,view='current'):
 if view=='current' and n.tag in [W+'del',W+'moveFrom']:return ''
 if view=='original' and n.tag in [W+'ins',W+'moveTo']:return ''
 if n.tag in [W+'t',W+'delText']:return n.text or ''
 if n.tag==W+'tab':return '\t'
 if n.tag in [W+'br',W+'cr']:return '\n'
 return ''.join(text(c,view) for c in n)
def docx_read(p,view='current'):
 with ZipFile(p) as z:
  bad=z.testzip()
  if bad:raise ValueError('DOCX ZIP校验失败: '+bad)
  result={'sha256':sha(p),'view':view,'parts':[],'revisions':0,'comments':0,'drawing_objects':0}
  for name in sorted(z.namelist()):
   if name=='word/document.xml' or (name.startswith('word/') and any(Path(name).name.startswith(t) for t in ['header','footer','footnotes','endnotes','comments']) and name.endswith('.xml')):
    d=ET.fromstring(z.read(name));rows=[text(n,view) for n in d.iter(W+'p')]
    result['parts'].append({'part':name,'paragraphs':rows})
    result['revisions']+=sum(1 for n in d.iter() if n.tag in [W+'ins',W+'del',W+'moveTo',W+'moveFrom'])
    result['comments']+=sum(1 for n in d.iter(W+'comment'))
    result['drawing_objects']+=sum(1 for n in d.iter() if n.tag in [W+'drawing',W+'pict',W+'object'])
  result['read_limit']='图片及扫描内容不自动OCR；复杂域/布局须另行打开检查。'
  return result
def doctor(a):
 modules={}
 for dist,mod in [('python-docx','docx'),('lxml','lxml'),('typing_extensions','typing_extensions')]:
  found=importlib.util.find_spec(mod) is not None
  try:version=importlib.metadata.version(dist)
  except importlib.metadata.PackageNotFoundError:version=None
  modules[dist]={'available':found,'version':version}
 report={'python':platform.python_version(),'python_sufficient':sys.version_info>=(3,11),'requirements':modules,'codex_cli_on_path':shutil.which('codex') is not None,'office_cli':shutil.which('soffice') or shutil.which('libreoffice'),'visual_review':'需读者用实际Word/WPS/兼容软件另行打开全部标记和修订后视图，不由依赖检查证明','research_channel':'由读者自行配置；本包不测试登录、不提供账户；练习允许按缺原文渠道的边界运行','private_skill_dependency':False}
 report['python_dependencies_ready']=report['python_sufficient'] and all(x['available'] for x in modules.values())
 print(json.dumps(report,ensure_ascii=False,indent=2));return 0 if report['python_dependencies_ready'] else 1
def init(a):
 target=Path(a.dest).expanduser().resolve()
 if target.exists() or target.is_symlink():raise ValueError('目标已存在；请使用新的练习目录，不覆盖旧文件。')
 target.mkdir(parents=True)
 for n in ['原件','成果','过程记录','tools']:(target/n).mkdir()
 src=ROOT/'examples/原件/维护服务合同.docx';brief=ROOT/'examples/委托示例'/CASES[a.case]
 shutil.copy2(src,target/'原件/维护服务合同.docx');shutil.copy2(brief,target/'原件/委托说明.md')
 sk=target/'.agents/skills/legal-contract-review-reader';shutil.copytree(ROOT/'skills/legal-contract-review-reader',sk)
 shutil.copy2(Path(__file__),target/'tools/reader.py')
 record={'case':a.case,'original_sha256':sha(src),'brief_sha256':sha(brief),'skill_sha256':sha(sk/'SKILL.md'),'package_version':'0.1.0','privacy':'完全虚构示例；不对应真实客户；原件只读'}
 (target/'过程记录/练习初始化.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
 task='调用 $legal-contract-review-reader；先读取 .agents/skills/legal-contract-review-reader/SKILL.md 及相关引用，再读取原件/委托说明.md 和原件/维护服务合同.docx，按委托范围实际工作。成果另存成果/，内部映射、失败和检查记录保存过程记录/。只做当前委托，不读取其他练习结果。缺法律原文或文档软件时逐项说明，不编造已经检索/渲染。'
 (target/'任务.txt').write_text(task,encoding='utf-8')
 print(json.dumps({'created':str(target),'case':a.case,'task_file':str(target/'任务.txt'),'source_unchanged':sha(src)==record['original_sha256']},ensure_ascii=False,indent=2));return 0
def main():
 p=argparse.ArgumentParser(description=__doc__);s=p.add_subparsers(dest='command',required=True)
 s.add_parser('doctor',help='检查Python依赖，不安装、不联网、不测试账号')
 q=s.add_parser('init',help='复制包内虚构材料和Skill到全新练习目录');q.add_argument('--case',choices=CASES,required=True);q.add_argument('--dest',required=True)
 q=s.add_parser('read',help='只读DOCX及文字部件');q.add_argument('docx',type=Path);q.add_argument('--view',choices=['current','original'],default='current')
 a=p.parse_args()
 try:
  if a.command=='doctor':return doctor(a)
  if a.command=='init':return init(a)
  print(json.dumps(docx_read(a.docx,a.view),ensure_ascii=False,indent=2));return 0
 except (ValueError,OSError,BadZipFile,ET.ParseError) as e:
  print(json.dumps({'status':'error','message':str(e)},ensure_ascii=False),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())

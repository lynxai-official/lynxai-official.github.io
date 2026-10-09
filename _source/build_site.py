from pathlib import Path
from html import escape
from urllib.parse import quote
import json

ROOT = Path(__file__).resolve().parents[1]
CFG = json.loads((ROOT / 'site-settings.json').read_text('utf-8'))
CSS = (ROOT / '_source/site.css').read_text('utf-8')
RECEIPT = 'https://play.google.com/store/apps/details?id=com.roro.snapreceipt'
INSECT = 'https://play.google.com/store/apps/details?id=com.roro.bugid.insect_identifier'
PRIVACY_RECEIPT = 'https://sites.google.com/view/lynxai/개인정보처리방침'
PRIVACY_INSECT = 'https://sites.google.com/view/gonsikai/홈'
LOGO = '<svg viewBox="0 0 44 44" fill="none" aria-hidden="true"><path d="M7 7V37H37" stroke="#91EFEE" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><path d="M17 27L30 10H38L25 27" stroke="#B4A2FF" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
FAVICON = 'data:image/svg+xml,' + quote('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><rect width="44" height="44" rx="11" fill="#080b12"/><path d="M10 9v25h24" fill="none" stroke="#91efee" stroke-width="4" stroke-linecap="round"/><path d="m19 26 11-15h6L25 26" fill="none" stroke="#b4a2ff" stroke-width="3" stroke-linecap="round"/></svg>', safe='')

TEXT = {
 'ko': {
  'nav':['회사 소개','제품','사업자 정보'], 'contact':'문의하기','skip':'본문으로 이동','menu':'메뉴 열기',
  'hero':'일상에 닿는<br><span>인공지능.</span>',
  'lead':'LynxAI는 일상의 정보를 더 쉽게 다루는 소프트웨어를 만듭니다. 대한민국에서 시작해, 실제 서비스로 아이디어를 발전시킵니다.',
  'discover':'LynxAI 알아보기','apps':'공개 앱 보기','based':'대한민국','basedlabel':'Based in','founded':'Founded','appcount':'Apps on Google Play',
  'focushead':'작은 문제에서,<br>쓸모 있는 경험으로.',
  'focusintro':'기술을 쓰는 이유가 분명해야 합니다. LynxAI는 정보를 정리하고 주변을 이해하는, 일상 속 구체적인 순간에 집중합니다.',
  'focus1':'문서를 다루는 일','focus1body':'사진 속 영수증을 읽고 필요한 항목을 정리합니다. 반복되는 입력 작업을 줄이는 경험을 만듭니다.',
  'focus2':'세상을 알아가는 일','focus2body':'눈앞의 곤충을 사진으로 살펴보고 이름과 특징을 알아봅니다. 호기심이 이해로 이어지는 경험을 만듭니다.',
  'selected':'LynxAI가 만든 서비스','selectedintro':'아이디어를 실제로 사용할 수 있는 앱으로 이어갑니다. Google Play에서 현재 공개된 서비스를 확인할 수 있습니다.',
  'receipt':'영식이 AI','insect':'곤식이 AI','receiptshort':'영수증 인식과 데이터 정리','insectshort':'사진으로 알아보는 곤충',
  'receiptdesc':'영수증의 날짜·항목·금액을 추출하고 CSV로 정리합니다.','insectdesc':'사진 속 곤충의 이름과 특징을 알아보는 자연 관찰 앱입니다.',
  'store':'Google Play 보기','businesscall':'LynxAI를 더 자세히 확인하세요.','businesscallbody':'설립연도, 운영자, 사업자 정보와 국문·영문 증빙자료 문의를 한곳에서 확인할 수 있습니다.','businessbutton':'사업자 정보 확인',
  'footdesc':'일상에 닿는 인공지능.\n대한민국에서 시작한 소프트웨어 스튜디오.','privacy':'앱 지원 · 개인정보 안내','copyright':'© 2026 LynxAI. All rights reserved.',
  'companytitle':'작은 문제에 집중하고,<br>실제 제품으로 답합니다.',
  'companylead':'LynxAI는 2025년 대한민국에서 시작한 개인사업자 기반 소프트웨어 사업입니다. AI를 활용한 모바일 애플리케이션을 개발하고 운영합니다.',
  'identity':'하나의 사업,<br>연결된 이름들.','identitybody':'LynxAI는 대외적으로 사용하는 브랜드이며, Google Play에서는 LynxAI Studio라는 개발자명으로 앱을 공개하고 있습니다. 영식이 AI와 곤식이 AI는 이 브랜드 아래 운영되는 제품입니다.',
  'identitybody2':'사업자와 제품의 관계를 쉽게 확인할 수 있도록 운영자 정보, 사업자등록번호와 공식 앱 링크를 함께 안내합니다.',
  'founderrole':'운영 · 소프트웨어 개발','founder':'이만영','principletitle':'우리가 만드는 방식',
  'principles':[('실제 쓰임에서 출발','무엇을 더 넣을지보다 사용자가 어떤 일을 하려는지 먼저 생각합니다.'),('명확한 기능과 설명','제품이 하는 일과 사용하는 방법을 쉽게 이해할 수 있도록 구성합니다.'),('출시하고 개선','실제 사용할 수 있는 형태로 만들고, 기능과 경험을 지속해서 다듬어 갑니다.')],
  'companycontact':'제품, 협업, 사업자 정보에 대해 문의하세요.','companycontactbody':'아래 이메일로 문의 내용과 관련 제품을 알려주세요.',
  'brandlabel':'브랜드','developerlabel':'Google Play 개발자명','ownerlabel':'대표자','yearlabel':'설립연도','typelabel':'운영 형태','typevalue':'개인사업자','countrylabel':'사업 국가','countryvalue':'대한민국','numberlabel':'사업자등록번호','emaillabel':'대표 문의','legalnamelabel':'등록상호',
  'producttitle':'아이디어를,<br>사용할 수 있는 형태로.',
  'productlead':'LynxAI Studio에서 공개한 두 가지 모바일 앱입니다. 최신 기능, 이용 조건과 지원 정보는 각 앱의 Google Play 페이지에서 확인할 수 있습니다.',
  'receiptbody':'영수증을 촬영하거나 이미지로 불러와 날짜, 항목, 금액 등 필요한 정보를 정리하는 앱입니다. 출장비 정산이나 개인 지출 기록에 활용할 수 있습니다.',
  'receiptfeatures':['영수증 이미지에서 주요 항목 추출','분석 결과를 문자 또는 CSV로 저장','외국어 영수증 번역 기능'],
  'insectbody':'산책이나 자연 관찰 중 만난 곤충을 사진으로 알아보는 앱입니다. 이름과 특징을 살펴보고 관련 설명을 읽을 수 있습니다.',
  'insectfeatures':['사진을 이용한 곤충 식별','크기·서식지·먹이·행동 등 특징 설명','관찰 기록과 도감 기능'],
  'details':'앱 상세 정보','supporttitle':'앱 지원 및 개인정보','supportbody':'앱별 문의와 데이터 관련 요청은 아래 지원 경로를 이용해 주세요.','receiptprivacy':'영식이 개인정보처리방침','insectprivacy':'곤식이 개인정보처리방침','deletion':'영식이 계정·데이터 삭제 요청','insectsupport':'곤식이 앱 문의','policybody':'앱의 데이터 처리에 관한 내용은 각 앱에서 제공하는 개인정보처리방침을 확인해 주세요.',
  'documenttitle':'사업자 정보와<br>확인 자료.',
  'documentlead':'LynxAI의 운영 정보와 사업자 확인을 위한 자료 요청 경로를 안내합니다. 제품 정보는 공식 Google Play 링크에서 함께 확인할 수 있습니다.',
  'kodoc':'사업자등록증 · 국문','kodocbody':'대한민국 사업자등록 관련 국문 자료입니다. 사업자 확인에 필요한 범위를 알려주시면 해당 자료에 관해 안내합니다.',
  'endoc':'사업자 증빙 · 영문 참고자료','endocbody':'국문 원문과 함께 확인하는 영문 참고자료입니다. 정부 발급 영문 증명서와 참고 번역본을 구분해 안내합니다.',
  'request':'자료 요청하기','requeststate':'이메일 문의','docnotice':'영문 참고 번역본은 정부가 발급한 증명서가 아닙니다. 공식 확인이 필요한 경우 국문 원문 또는 정부 발급 영문 증명서를 기준으로 확인해 주세요.',
  'docsummary':'사업자 정보 요약','docsummarynote':'이 페이지는 사업자 정보를 안내하기 위한 요약이며, 정부가 발급한 사업자등록증이나 사업자등록증명을 대체하지 않습니다.',
  'doccontact':'사업자 확인이 필요하신가요?','doccontactbody':'요청 기관, 필요한 문서 언어와 확인 항목을 이메일로 알려주세요.',
 },
 'en': {
  'nav':['Company','Products','Business information'],'contact':'Contact','skip':'Skip to content','menu':'Open menu',
  'hero':'Intelligence,<br><span>for everyday life.</span>',
  'lead':'LynxAI builds software that makes everyday information easier to work with. Founded in South Korea, we turn practical ideas into working products.',
  'discover':'Meet LynxAI','apps':'Explore our apps','based':'South Korea','basedlabel':'Based in','founded':'Founded','appcount':'Apps on Google Play',
  'focushead':'Small problems.<br>Useful experiences.',
  'focusintro':'Technology should have a clear purpose. We focus on everyday moments: organizing information and understanding the world around us.',
  'focus1':'Working with documents','focus1body':'Read a receipt image and organize the details that matter. Make repetitive data entry easier to manage.',
  'focus2':'Exploring the world','focus2body':'Use a photo to discover an insect’s name and characteristics. Turn a moment of curiosity into understanding.',
  'selected':'Products from LynxAI','selectedintro':'Our ideas take shape as usable mobile apps. Explore the products currently published on Google Play.',
  'receipt':'Yeongsigi AI','insect':'Gonsigi AI','receiptshort':'Receipt recognition & organization','insectshort':'Photo-based insect identification',
  'receiptdesc':'Extract receipt dates, items and amounts, and organize results as CSV.','insectdesc':'A nature observation app for exploring an insect’s name and characteristics.',
  'store':'View on Google Play','businesscall':'Get to know the business behind LynxAI.','businesscallbody':'Find our founding year, operator, business registration details and contact route for Korean and English documentation.','businessbutton':'Business information',
  'footdesc':'Intelligence, for everyday life.\nAn independent software studio from South Korea.','privacy':'App support & privacy','copyright':'© 2026 LynxAI. All rights reserved.',
  'companytitle':'Focused on small problems.<br>Built into real products.',
  'companylead':'LynxAI is a software business established in South Korea in 2025 and operated as a registered sole proprietorship. We develop and operate AI-assisted mobile applications.',
  'identity':'One business.<br>Connected identities.','identitybody':'LynxAI is our public-facing brand. Our apps are published on Google Play under the developer name LynxAI Studio. Yeongsigi AI (영식이 AI) and Gonsigi AI (곤식이 AI) are products operated under this brand.',
  'identitybody2':'The operator, business registration number and official app links are provided together to make the relationship between the business and its products clear.',
  'founderrole':'Owner · Software development','founder':'Manyeong Lee','principletitle':'How we work',
  'principles':[('Start with a real task','Understand what a person wants to do before deciding which features to build.'),('Make the purpose clear','Explain what the product does and how people can use it.'),('Ship and improve','Build something usable, then continue refining the features and experience.')],
  'companycontact':'Talk to us about products, partnerships or business information.','companycontactbody':'Email us with your question and the relevant product.',
  'brandlabel':'Brand','developerlabel':'Google Play developer','ownerlabel':'Owner','yearlabel':'Established','typelabel':'Business type','typevalue':'Registered sole proprietorship','countrylabel':'Country','countryvalue':'South Korea','numberlabel':'Business registration no.','emaillabel':'Business contact','legalnamelabel':'Registered business name',
  'producttitle':'Ideas made<br>usable.',
  'productlead':'Two mobile apps published by LynxAI Studio. Visit each Google Play listing for current features, availability, terms and support information.',
  'receiptbody':'An app for organizing dates, items, amounts and other details from photographed or imported receipts. It can support expense reporting and personal spending records.',
  'receiptfeatures':['Extract key details from receipt images','Save results as text or CSV','Translation for foreign-language receipts'],
  'insectbody':'Explore insects encountered on walks or during nature observation. Use a photo to look up a name, characteristics and related explanations.',
  'insectfeatures':['Photo-based insect identification','Information about size, habitat, food and behavior','Observation records and collection features'],
  'details':'App details','supporttitle':'App support and privacy','supportbody':'Use the contacts below for product questions and data-related requests.','receiptprivacy':'Yeongsigi privacy policy','insectprivacy':'Gonsigi privacy policy','deletion':'Yeongsigi account / data deletion request','insectsupport':'Contact Gonsigi support','policybody':'For details about data processing, consult the privacy policy provided for each app.',
  'documenttitle':'Business information.<br>Supporting documents.',
  'documentlead':'Business details and contact information for verification requests. Official Google Play listings provide additional information about our published products.',
  'kodoc':'Korean business registration','kodocbody':'Korean-language business registration documentation. Tell us what information you need to verify when requesting a document.',
  'endoc':'English reference documentation','endocbody':'English reference material to read alongside the Korean original. Official English certificates and reference translations are identified separately.',
  'request':'Request a document','requeststate':'Contact by email','docnotice':'An English reference translation is not a government-issued certificate. For formal verification, refer to the Korean original or an official English certificate issued by the relevant authority.',
  'docsummary':'Business information at a glance','docsummarynote':'This page is an informational summary. It does not replace a business registration certificate issued by the relevant authority.',
  'doccontact':'Need to verify our business?','doccontactbody':'Email us with your organization, required document language and the details you need to confirm.',
 }
}

def esc(s): return escape(str(s), quote=True)
def mail(email, subject=None):
 return 'mailto:' + email + ('?subject=' + quote(subject) if subject else '')
def external(url, label, cls='text-link'):
 return f'<a class="{cls}" href="{esc(url)}" target="_blank" rel="noopener noreferrer">{label}<span class="sr-only"> (opens in a new tab)</span></a>'
def button(url, label, secondary=False):
 return f'<a class="button{" secondary" if secondary else ""}" href="{esc(url)}">{label}</a>'
def brand(): return f'{LOGO}<span>LynxAI<span class="brand-dot">.</span></span>'

def info(lang):
 t=TEXT[lang]
 rows=[(t['brandlabel'],CFG['brand']),(t['developerlabel'],CFG['developerBrand'])]
 if CFG['registeredBusinessName']: rows.append((t['legalnamelabel'],CFG['registeredBusinessName']))
 rows += [(t['ownerlabel'], CFG['founderKo']+' / '+CFG['founderEn']), (t['yearlabel'],CFG['foundedYear']), (t['typelabel'],t['typevalue']), (t['countrylabel'],t['countryvalue']), (t['numberlabel'],CFG['businessRegistrationNumber'])]
 return '<dl class="info-table">'+''.join(f'<div><dt>{esc(k)}</dt><dd>{esc(v)}</dd></div>' for k,v in rows)+f'<div><dt>{t["emaillabel"]}</dt><dd><a href="{mail(CFG["contactEmail"])}">{esc(CFG["contactEmail"])}</a></dd></div></dl>'

def app_rows(lang):
 t=TEXT[lang]
 return '<div class="product-list">'+''.join(f'<article class="product-row"><div class="product-monogram {"purple" if key=="insect" else ""}" aria-hidden="true">{mon}</div><div class="product-name"><h3>{t[key]}</h3><span>{t[key+"short"]}</span></div><p class="product-desc">{t[key+"desc"]}</p>{external(url,t["store"])}</article>' for key,mon,url in [('receipt','YS',RECEIPT),('insect','GS',INSECT)])+'</div>'

def callout(lang):
 t=TEXT[lang]
 return f'<div class="callout"><div><h2>{t["businesscall"]}</h2><p>{t["businesscallbody"]}</p></div>{button("documents.html",t["businessbutton"])}</div>'

def home(lang):
 t=TEXT[lang]
 return f'''<section class="hero"><div class="wrap"><div class="hero-grid"><div>
 <p class="kicker">Independent AI software studio</p><h1>{t['hero']}</h1><p class="lead">{t['lead']}</p><div class="buttons">{button('company.html',t['discover'])}{button('products.html',t['apps'],True)}</div></div>
 <div class="hero-art" aria-hidden="true"><div class="orbit-north">LYNXAI / EST. 2025</div><div class="orbit-outer"></div><div class="orb"></div><div class="orbit-tag"><span>FROM IDEA TO PRODUCT</span><strong>Intelligence, made intuitive.</strong></div><div class="orbit-caption">SOFTWARE · MOBILE · APPLIED AI</div></div></div>
 <div class="facts-strip"><div class="fact"><strong>{CFG['foundedYear']}</strong><span>{t['founded']}</span></div><div class="fact"><strong>{t['based']}</strong><span>{t['basedlabel']}</span></div><div class="fact"><strong>02</strong><span>{t['appcount']}</span></div></div></div></section>
 <section class="section"><div class="wrap"><div class="section-title"><div><p class="kicker">01 / Our focus</p><h2>{t['focushead']}</h2></div><p>{t['focusintro']}</p></div><div class="twocol"><article class="focus-card"><span class="number">DOCUMENTS & INFORMATION</span><h3>{t['focus1']}</h3><p>{t['focus1body']}</p><div class="accent-line"></div></article><article class="focus-card"><span class="number">CURIOSITY & DISCOVERY</span><h3>{t['focus2']}</h3><p>{t['focus2body']}</p><div class="accent-line"></div></article></div></div></section>
 <section class="section"><div class="wrap"><div class="section-title"><div><p class="kicker">02 / Selected products</p><h2>{t['selected']}</h2></div><p>{t['selectedintro']}</p></div>{app_rows(lang)}</div></section><section class="section"><div class="wrap">{callout(lang)}</div></section>'''

def intro(kicker,title,lead):
 return f'<section class="page-intro"><div class="wrap"><p class="kicker">{kicker}</p><h1>{title}</h1><p class="lead">{lead}</p></div></section>'

def company(lang):
 t=TEXT[lang]
 principles=''.join(f'<article class="principle"><span class="index">0{i+1}</span><h3>{h}</h3><p>{p}</p></article>' for i,(h,p) in enumerate(t['principles']))
 return intro('Company / LynxAI',t['companytitle'],t['companylead'])+f'''<section class="content-section"><div class="wrap content-grid"><div><h2>{t['identity']}</h2><p class="body-text">{t['identitybody']}</p><p class="body-text">{t['identitybody2']}</p><div class="founder"><div class="initials" aria-hidden="true">ML</div><div><h3>{esc(CFG['founderKo'] if lang=='ko' else CFG['founderEn'])}</h3><p>{t['founderrole']}</p></div></div></div><div>{info(lang)}</div></div></section><section class="section"><div class="wrap"><p class="kicker">Our approach</p><h2>{t['principletitle']}</h2><div class="principles">{principles}</div></div></section><section class="content-section"><div class="wrap"><div class="callout"><div><h2>{t['companycontact']}</h2><p>{t['companycontactbody']}</p></div>{button(mail(CFG['contactEmail']),t['contact'])}</div></div></section>'''

def products(lang):
 t=TEXT[lang]
 cards=[]
 for key,mon,url,ko_name in [('receipt','YS',RECEIPT,'영식이 AI'),('insect','GS',INSECT,'곤식이 AI')]:
  features=''.join(f'<li>{v}</li>' for v in t[key+'features'])
  cards.append(f'''<article class="app-detail {'violet' if key=='insect' else ''}" id="{key}"><div class="app-top"><div class="product-monogram {'purple' if key=='insect' else ''}" aria-hidden="true">{mon}</div><div><h2>{t[key]}</h2><p>{ko_name+' · ' if lang=='en' else ''}LynxAI Studio / Android</p></div></div><div class="app-body"><div><p class="body-text">{t[key+'body']}</p>{external(url,t['store'],'button small')}</div><ul class="features">{features}</ul></div></article>''')
 return intro('Products / LynxAI Studio',t['producttitle'],t['productlead'])+f'''<section class="content-section"><div class="wrap">{''.join(cards)}<div class="support-panel" id="support"><div><h2>{t['supporttitle']}</h2><p>{t['supportbody']}</p><div class="footer-links"><a href="{mail(CFG['receiptSupportEmail'],'영식이 AI 계정 / 데이터 삭제 요청')}">{t['deletion']}</a><a href="{mail(CFG['insectSupportEmail'],'곤식이 AI 앱 문의')}">{t['insectsupport']}</a></div></div><div><p>{t['policybody']}</p><div class="footer-links">{external(PRIVACY_RECEIPT,t['receiptprivacy'])}{external(PRIVACY_INSECT,t['insectprivacy'])}</div></div></div></div></section>'''

def documents(lang):
 t=TEXT[lang]
 return intro('Business / Documentation',t['documenttitle'],t['documentlead'])+f'''<section class="content-section"><div class="wrap"><div class="doc-grid"><article class="doc-card" data-doc="ko"><div class="doc-icon" aria-hidden="true">KO</div><h2>{t['kodoc']}</h2><p>{t['kodocbody']}</p><a class="button secondary small doc-action" href="{mail(CFG['contactEmail'],'LynxAI Korean business registration document request')}">{t['request']}</a><span class="doc-status">{t['requeststate']}</span></article><article class="doc-card" data-doc="en"><div class="doc-icon" aria-hidden="true">EN</div><h2>{t['endoc']}</h2><p>{t['endocbody']}</p><a class="button secondary small doc-action" href="{mail(CFG['contactEmail'],'LynxAI English business documentation request')}">{t['request']}</a><span class="doc-status">{t['requeststate']}</span></article></div><div class="notice" id="translation-notice">{t['docnotice']}</div></div></section><section class="content-section"><div class="wrap"><div class="document-information"><h2>{t['docsummary']}</h2>{info(lang)}<p class="fine">{t['docsummarynote']}</p></div></div></section><section class="content-section"><div class="wrap"><div class="callout"><div><h2>{t['doccontact']}</h2><p>{t['doccontactbody']}</p></div>{button(mail(CFG['contactEmail']),t['contact'])}</div></div></section>'''

BASE_JS='''const menu=document.querySelector('.menu');const links=document.querySelector('.navlinks');
if(menu&&links){menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));links.classList.toggle('is-open',open);});document.addEventListener('keydown',e=>{if(e.key==='Escape'){links.classList.remove('is-open');menu.setAttribute('aria-expanded','false');menu.focus();}});window.addEventListener('resize',()=>{if(window.innerWidth>760){links.classList.remove('is-open');menu.setAttribute('aria-expanded','false');}});}
'''

DOC_JS='''(async function(){
const settings=window.LYNXAI_DOCUMENTS||{};const en=document.documentElement.lang==='en';
const prefix=en?'docs/':'../docs/';const official=settings.englishType==='official';
if(official){const c=document.querySelector('[data-doc="en"]');c.querySelector('h2').textContent=en?'Official English business certificate':'정부 발급 사업자 증명 · 영문';c.querySelector('p').textContent=en?'An English-language business certificate issued by the relevant authority.':'관계 기관에서 발급한 영문 사업자 증명서입니다.';document.querySelector('#translation-notice').hidden=true;}
if(!/^https?:$/.test(location.protocol))return;
await Promise.all(['ko','en'].map(async lang=>{const file=settings[lang==='ko'?'korean':'english'];if(!file||!/^[-a-zA-Z0-9_.]+\\.pdf$/.test(file))return;
const url=prefix+file;try{const r=await fetch(url,{method:'HEAD',cache:'no-store'});if(!r.ok||!((r.headers.get('content-type')||'').toLowerCase().includes('application/pdf')))return;
const card=document.querySelector('[data-doc="'+lang+'"]');const a=card.querySelector('.doc-action');a.href=url;a.target='_blank';a.rel='noopener noreferrer';a.textContent=en?'View PDF':'PDF 보기';card.querySelector('.doc-status').textContent=lang==='ko'?(en?'Korean original · PDF':'국문 원본 · PDF'):(official?(en?'Official English certificate · PDF':'정부 발급 영문 증명서 · PDF'):(en?'Reference translation · PDF':'영문 참고 번역본 · PDF'));
}catch(e){/* Document requests remain available by email. */}}));
})();'''

PAGES={'index':home,'company':company,'products':products,'documents':documents}
for lang in ('en','ko'):
 t=TEXT[lang]
 prefix='../' if lang=='ko' else ''
 for name,render in PAGES.items():
  route=name+'.html'
  other=('ko/'+route) if lang=='en' else ('../'+route)
  language_links=''.join(f'<link rel="alternate" hreflang="{code}" href="{prefix}{folder}{route}">' for code,folder in (('en',''),('ko','ko/'),('x-default','')))
  title={'index': 'LynxAI — '+('일상에 닿는 인공지능' if lang=='ko' else 'Intelligence, for everyday life'), 'company':('회사 소개' if lang=='ko' else 'Company')+' | LynxAI','products':('제품' if lang=='ko' else 'Products')+' | LynxAI','documents':('사업자 정보' if lang=='ko' else 'Business information')+' | LynxAI'}[name]
  description=t[{'index':'lead','company':'companylead','products':'productlead','documents':'documentlead'}[name]]
  nav=''.join(f'<a href="{n}.html"'+(' aria-current="page"' if n==name else '')+f'>{label}</a>' for n,label in zip(('company','products','documents'),t['nav']))
  nav+=f'<a class="nav-contact" href="{mail(CFG["contactEmail"])}">{t["contact"]}</a>'
  footer_nav=''.join(f'<a href="{n}.html">{label}</a>' for n,label in zip(('company','products','documents'),t['nav']))
  canonical=''
  if CFG['siteUrl']:
   url=CFG['siteUrl'].rstrip('/')+'/' + ('ko/' if lang=='ko' else '')+route
   canonical=f'<link rel="canonical" href="{esc(url)}"><meta property="og:url" content="{esc(url)}">'
  organization={'@context':'https://schema.org','@type':'Organization','name':CFG['brand'],'alternateName':CFG['developerBrand'],'foundingDate':str(CFG['foundedYear']),'founder':{'@type':'Person','name':CFG['founderEn'],'alternateName':CFG['founderKo']},'email':CFG['contactEmail'],'address':{'@type':'PostalAddress','addressCountry':'KR'},'identifier':{'@type':'PropertyValue','propertyID':'South Korea business registration number','value':CFG['businessRegistrationNumber']}}
  if CFG['siteUrl']:organization['url']=CFG['siteUrl']
  css=CSS+'\n.sr-only{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;border:0}'
  docscript=f'<script src="{prefix}assets/document-settings.js"></script>' if name=='documents' else ''
  html=f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#080b12"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:locale" content="{'ko_KR' if lang=='ko' else 'en_US'}"><link rel="icon" type="image/svg+xml" href="{FAVICON}">{language_links}{canonical}<style>{css}</style><script type="application/ld+json">{json.dumps(organization,ensure_ascii=False).replace('</','<\\/')}</script></head>
<body class="{lang}"><a class="skip" href="#main">{t['skip']}</a><header class="header"><nav class="wrap nav" aria-label="{'주 메뉴' if lang=='ko' else 'Main navigation'}"><a class="brand" href="index.html" aria-label="LynxAI home">{brand()}</a><div class="navlinks" id="navigation">{nav}</div><a class="language" href="{other}" lang="{'ko' if lang=='en' else 'en'}" aria-label="{'한국어 페이지' if lang=='en' else 'English version'}">{'한국어' if lang=='en' else 'English'}</a><button class="menu" type="button" aria-label="{t['menu']}" aria-expanded="false" aria-controls="navigation"><span></span><span></span></button></nav></header>
<main id="main">{render(lang)}</main>
<footer class="footer"><div class="wrap"><div class="footer-main"><div><a class="brand" href="index.html">{brand()}</a><p>{t['footdesc'].replace(chr(10),'<br>')}</p></div><div><div class="footer-label">EXPLORE</div><div class="footer-links">{footer_nav}</div></div><div><div class="footer-label">GET IN TOUCH</div><div class="footer-links"><a href="{mail(CFG['contactEmail'])}">{esc(CFG['contactEmail'])}</a></div><p>{'Google Play 개발자명' if lang=='ko' else 'Google Play developer'}<br>LynxAI Studio</p></div></div><div class="footer-bottom"><span>{t['copyright']}</span><a href="products.html#support">{t['privacy']}</a><span>{'사업자등록번호' if lang=='ko' else 'Business registration no.'} {esc(CFG['businessRegistrationNumber'])}</span></div></div></footer>{docscript}<script>{BASE_JS}{DOC_JS if name=='documents' else ''}</script></body></html>'''
  out=ROOT/('ko' if lang=='ko' else '')/route
  out.parent.mkdir(exist_ok=True)
  out.write_text(html,'utf-8')
# Keep previously shared /en/ addresses working after English moves to the root.
for name in PAGES:
 target='../'+name+'.html'
 redirect=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0;url={target}"><title>LynxAI — English</title></head><body><p><a href="{target}">Continue to LynxAI</a></p><script>location.replace({json.dumps(target)}+location.search+location.hash);</script></body></html>'''
 (ROOT/'en').mkdir(exist_ok=True)
 (ROOT/'en'/(name+'.html')).write_text(redirect,'utf-8')
print('Built 8 bilingual pages (English default, Korean in /ko/) and 4 legacy /en/ redirects.')

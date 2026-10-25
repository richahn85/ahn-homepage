const button=document.querySelector('.menu-btn');
const menu=document.querySelector('#navigation');
function closeMenu(){button?.setAttribute('aria-expanded','false');menu?.classList.remove('open');}
button?.addEventListener('click',()=>{const open=button.getAttribute('aria-expanded')!=='true';button.setAttribute('aria-expanded',String(open));menu.classList.toggle('open',open);});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&button?.getAttribute('aria-expanded')==='true'){closeMenu();button.focus();}});
menu?.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
// Hash fragments never reach the server: preserve old inbound homepage links here.
const oldAnchors={support:'/people-first',probono:'/people-first',subscribe:'/ax-management-brief#subscribe','why-ahn':'/about#philosophy',expertise:'/ax-transformation#expertise','cardnews-series':'/insights#cardnews-series'};
if(location.pathname==='/'&&oldAnchors[location.hash.slice(1)])location.replace(oldAnchors[location.hash.slice(1)]);
if(location.pathname.replace(/\/$/,'')==='/people-first'&&location.hash==='#support')history.replaceState(null,'',location.pathname);
// V3: fixed contact bar on phones (not on the contact page itself).
// Language sites (/en/, /zh/, /ja/) get the bar in their own language.
const ctaText={ko:['빠른 문의','전화','이메일','강의·자문 문의','/contact'],en:['Quick contact','Call','Email','Book a lecture','/en/contact/'],zh:['快速咨询','电话','邮件','讲座·咨询','/zh/contact/'],ja:['お問い合わせ','電話','メール','講演・顧問のご相談','/ja/contact/']}[document.documentElement.lang.slice(0,2)]||null;
if(ctaText&&!/^\/((en|zh|ja)\/)?contact/.test(location.pathname)&&document.querySelector('header .nav')){const bar=document.createElement('nav');bar.className='mobile-cta';bar.setAttribute('aria-label',ctaText[0]);bar.style.gridTemplateColumns='1fr 1fr 1.6fr';bar.innerHTML=`<a href="tel:+82222601651">${ctaText[1]}</a><a href="mailto:richahn@dongguk.edu">${ctaText[2]}</a><a class="primary" href="${ctaText[4]}">${ctaText[3]}</a>`;document.body.append(bar);document.body.classList.add('has-mobile-cta');}

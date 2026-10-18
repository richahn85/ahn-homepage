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

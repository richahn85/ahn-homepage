const {chromium}=require('playwright');
const fs=require('fs');const path=require('path');
(async()=>{
 fs.mkdirSync(path.join(__dirname,'../../tmp/ahn-v2-baseline'),{recursive:true});
 const browser=await chromium.launch({headless:true,channel:"chrome"}); const page=await browser.newPage();
 const results=[];const errors=[];page.on('pageerror',e=>errors.push(e.message));
 const paths=['/','/about','/advisory','/ax-transformation','/executive-education','/cases','/insights','/professors-question','/ax-management-brief','/people-first','/contact',...['k-bpi','hyundai-crm','b2b-marketing','smart-tourism','safety-management','ai-transformation'].map(s=>'/cases/'+s),...['3','4','5'].map(s=>'/insights/safety-part-'+s)];
 for(const width of [1440,390,320]){
  await page.setViewportSize({width,height:1000});
  for(const route of paths){
   await page.goto('http://localhost:8765'+route);await page.evaluate(()=>document.fonts.ready);
   const check=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth,h1:document.querySelectorAll('h1').length,canonical:!!document.querySelector('[rel=canonical]'),missingAlt:[...document.images].filter(i=>!i.alt).length,brokenImages:[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.src),unlabelled:[...document.querySelectorAll('input:not([type=hidden]),select,textarea')].filter(x=>!x.closest('[hidden]')&&x.name!=='bot-field'&&!x.labels.length).map(x=>x.name),schemas:[...document.querySelectorAll('[type="application/ld+json"]')].map(s=>JSON.parse(s.textContent)).length}));
   results.push({width,route,...check});
   if(route==='/'&&(width===1440||width===390)){await page.evaluate(async()=>{for(const i of document.images){i.loading='eager';await i.decode().catch(()=>{});}});await page.screenshot({path:path.join(__dirname,'../../tmp/ahn-v2-baseline',`home-${width}.png`),fullPage:true});await page.screenshot({path:path.join(__dirname,'../../tmp/ahn-v2-baseline',`hero-${width}.png`)});}
  }
 }
 await page.goto('http://localhost:8765/contact');
 const invalid=await page.locator('form').evaluate(f=>!f.checkValidity());
 await page.getByRole('button',{name:'메뉴',exact:true}).click();const expanded=await page.getByRole('button',{name:'메뉴',exact:true}).getAttribute('aria-expanded');await page.keyboard.press('Escape');const closed=await page.getByRole('button',{name:'메뉴',exact:true}).getAttribute('aria-expanded');
 const forms=await page.locator('form').evaluate(f=>({name:f.getAttribute('name'),method:f.method,action:f.getAttribute('action'),fields:[...f.elements].map(x=>x.name).filter(Boolean)}));
 const failed=results.filter(r=>r.overflow||r.h1!==1||!r.canonical||r.missingAlt||r.brokenImages.length||r.unlabelled.length);
 fs.writeFileSync(path.join(__dirname,'../../tmp/ahn-v2-baseline/qa.json'),JSON.stringify({results,failed,errors,invalid,expanded,closed,forms},null,2));
 console.log(JSON.stringify({pages:paths.length,viewports:3,failed,errors,invalid,expanded,closed,forms},null,2));await browser.close();if(failed.length||errors.length||!invalid||expanded!=='true'||closed!=='false')process.exitCode=1;
})();


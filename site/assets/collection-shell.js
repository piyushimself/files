(()=>{"use strict";
const $=s=>document.querySelector(s),store={get(k){try{return localStorage.getItem(k)}catch{return null}},set(k,v){try{localStorage.setItem(k,v)}catch{}}};
const root=document.documentElement;
function setTheme(value){root.dataset.theme=value;store.set("rr-theme",value);const b=$("#rr-theme-toggle");if(b)b.textContent=value==="dark"?"Light mode":"Dark mode";document.querySelectorAll("iframe").forEach(f=>{try{f.contentWindow.postMessage({type:"rr-theme",theme:value},"*")}catch{}})}
const saved=store.get("rr-theme");setTheme(saved==="dark"||saved==="light"?saved:(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"));
$("#rr-theme-toggle")?.addEventListener("click",()=>setTheme(root.dataset.theme==="dark"?"light":"dark"));
let scale=parseFloat(store.get("rr-text-scale")||"1");if(!Number.isFinite(scale))scale=1;function applyScale(){root.style.setProperty("--body-scale",String(scale));store.set("rr-text-scale",String(scale))}
applyScale();$("#rr-text-smaller")?.addEventListener("click",()=>{scale=Math.max(.88,scale-.06);applyScale()});$("#rr-text-larger")?.addEventListener("click",()=>{scale=Math.min(1.2,scale+.06);applyScale()});
const current=document.body.dataset.current||"",list=$("#rr-nav-links"),search=$("#rr-nav-search");
fetch("../../data/catalog.json").then(r=>{if(!r.ok)throw Error("catalog");return r.json()}).then(data=>{
 const items=Array.isArray(data.items)?data.items:[];const index=items.findIndex(x=>x.href===current);
 const prev=$("#rr-prev"),next=$("#rr-next");
 if(index>0){prev.href="../../"+items[index-1].href;prev.hidden=false}else if(prev)prev.hidden=true;
 if(index>=0&&index<items.length-1){next.href="../../"+items[index+1].href;next.hidden=false}else if(next)next.hidden=true;
 function draw(q=""){list.replaceChildren();let last="";items.filter(x=>(x.title+" "+x.category).toLowerCase().includes(q)).forEach(x=>{if(x.category!==last){const h=document.createElement("div");h.className="rr-nav-category";h.textContent=x.category;list.append(h);last=x.category}const a=document.createElement("a");a.href="../../"+x.href;a.textContent=x.title;if(x.href===current)a.setAttribute("aria-current","page");list.append(a)})}
 draw();search?.addEventListener("input",()=>draw(search.value.trim().toLowerCase()));
}).catch(()=>{if(list)list.textContent="Collection navigation is temporarily unavailable."});
window.addEventListener("storage",e=>{if(e.key==="rr-theme"&&(e.newValue==="dark"||e.newValue==="light")){root.dataset.theme=e.newValue;if($("#rr-theme-toggle"))$("#rr-theme-toggle").textContent=e.newValue==="dark"?"Light mode":"Dark mode"}if(e.key==="rr-text-scale"){scale=parseFloat(e.newValue)||1;root.style.setProperty("--body-scale",String(scale))}});
})();

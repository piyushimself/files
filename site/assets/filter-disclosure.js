(()=> {
"use strict";
const KEY="rr-filters-open";
const selectors=[".controls-wrap",".filter-panel",".filters-panel",".filter-container",".filter-section",".filter-wrap",".filter-bar",".filters",".toolbar",".controls"];
const candidates=[...new Set(selectors.flatMap(s=>[...document.querySelectorAll(s)]))];
function score(el){
 const cls=String(el.className||"").toLowerCase();
 const txt=(el.innerText||"").slice(0,12000).toLowerCase();
 const inputs=el.querySelectorAll('input:not([type="hidden"]),select,textarea').length;
 const selects=el.querySelectorAll("select").length;
 const groups=el.querySelectorAll(".filter-group,[class*=filter-group],[class*=filter-row],[class*=filter-item]").length;
 const words=(txt.match(/search|filter|country|category|curriculum|status|genre|year|sort|watched|unwatched/g)||[]).length;
 if(!inputs||(!groups&&words<2&&!/filter|controls-wrap|toolbar/.test(cls)))return -1;
 if(el.closest(".rr-shell-header")||el.querySelectorAll("article,.film-card,.manga-card,.collection-card").length>8)return -1;
 let n=inputs*3+selects*2+groups*8+Math.min(words,12)*2;
 if(cls.includes("controls-wrap"))n+=100;
 else if(cls.includes("filter-panel")||cls.includes("filters-panel"))n+=90;
 else if(cls.includes("filter-container")||cls.includes("filter-section"))n+=75;
 else if(cls.includes("filter-wrap")||cls.includes("filter-bar"))n+=65;
 else if(cls.includes("filters"))n+=45;
 else if(cls.includes("toolbar"))n+=20;
 else if(cls.includes("controls"))n+=10;
 if(el.matches("header,nav"))n-=80;
 return n;
}
const ranked=candidates.map(el=>({el,n:score(el)})).filter(x=>x.n>=12).sort((a,b)=>b.n-a.n);
if(!ranked.length)return;
let panel=ranked[0].el;
for(let p=panel.parentElement;p&&p!==document.body;p=p.parentElement){if(candidates.includes(p)&&score(p)>=ranked[0].n-8){panel=p;break}}
if(panel.closest(".rr-filter-disclosure"))return;
const box=document.createElement("details");box.className="rr-filter-disclosure";box.dataset.rrFilterDisclosure="true";
const summary=document.createElement("summary");summary.className="rr-filter-summary";
const label=document.createElement("span");label.className="rr-filter-label";label.textContent="Filters & search";
const hint=document.createElement("span");hint.className="rr-filter-hint";hint.textContent="Show filters";
const icon=document.createElement("span");icon.className="rr-filter-chevron";icon.setAttribute("aria-hidden","true");
summary.append(label,hint,icon);
if(!panel.id)panel.id="rr-collection-filters";
summary.setAttribute("aria-controls",panel.id);
panel.parentNode.insertBefore(box,panel);box.append(summary,panel);
let saved=null;try{saved=localStorage.getItem(KEY)}catch{}
box.open=saved==="1";
function update(){hint.textContent=box.open?"Hide filters":"Show filters";summary.setAttribute("aria-expanded",String(box.open))}
update();
box.addEventListener("toggle",()=>{update();try{localStorage.setItem(KEY,box.open?"1":"0")}catch{}});
window.addEventListener("storage",e=>{if(e.key===KEY){box.open=e.newValue==="1";update()}});
})();
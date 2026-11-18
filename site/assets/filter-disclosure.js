(()=> {
"use strict";
const KEY="rr-filters-open";
const selectors=["#filters",".filter-bar",".arc-filters",".controls-wrap",".filter-panel",".filters-panel",".filter-container",".filter-section",".filter-wrap",".filters",".toolbar",".controls"];
function count(el){return el.querySelectorAll('input:not([type="hidden"]),select,textarea').length}
function install(){
 if(document.querySelector("details.rr-filter-disclosure"))return true;
 let panel=null;
 for(const selector of selectors){
  const found=[...document.querySelectorAll(selector)].filter(el=>count(el)>0);
  if(found.length){panel=found.sort((a,b)=>count(b)-count(a))[0];break}
 }
 if(!panel||!panel.parentNode)return false;
 const box=document.createElement("details");box.className="rr-filter-disclosure";box.dataset.rrFilterDisclosure="true";
 const summary=document.createElement("summary");summary.className="rr-filter-summary";
 const label=document.createElement("span");label.className="rr-filter-label";label.textContent="Filters & search";
 const hint=document.createElement("span");hint.className="rr-filter-hint";
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
 return true;
}
function start(){
 if(install())return;
 const observer=new MutationObserver(()=>{if(install())observer.disconnect()});
 observer.observe(document.documentElement,{childList:true,subtree:true});
 window.setTimeout(()=>observer.disconnect(),30000);
}
if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",start,{once:true});else start();
})();
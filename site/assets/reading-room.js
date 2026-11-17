(()=>{"use strict";
const $=s=>document.querySelector(s);
const state={items:[],category:"All",query:"",sort:"featured"};
const safeStore={get(k){try{return localStorage.getItem(k)}catch{return null}},set(k,v){try{localStorage.setItem(k,v)}catch{}}};
const theme=safeStore.get("rr-theme");
if(theme==="dark"||theme==="light")document.documentElement.dataset.theme=theme;
else if(matchMedia("(prefers-color-scheme: dark)").matches)document.documentElement.dataset.theme="dark";
$("#theme-toggle").addEventListener("click",()=>{const next=document.documentElement.dataset.theme==="dark"?"light":"dark";document.documentElement.dataset.theme=next;safeStore.set("rr-theme",next)});
let scale=1;
$("#text-smaller").addEventListener("click",()=>{scale=Math.max(.88,scale-.06);document.documentElement.style.setProperty("--body-scale",scale)});
$("#text-larger").addEventListener("click",()=>{scale=Math.min(1.2,scale+.06);document.documentElement.style.setProperty("--body-scale",scale)});
$("#last-updated").textContent=new Intl.DateTimeFormat(undefined,{year:"numeric",month:"long",day:"numeric"}).format(new Date());
const categories=["All","Cinema","Manga & Comics","Art","Reading & Literature","Learning","Family","Security","Interactive tools","Other"];
function renderFilters(){const root=$("#category-filters");root.replaceChildren();categories.forEach(cat=>{const b=document.createElement("button");b.className="filter-button";b.type="button";b.textContent=cat;b.setAttribute("aria-pressed",String(state.category===cat));b.addEventListener("click",()=>{state.category=cat;render()});root.append(b)})}
function render(){renderFilters();let rows=state.items.filter(x=>(state.category==="All"||x.category===state.category)&&(!state.query||[x.title,x.description,x.category,x.searchText].join(" ").toLowerCase().includes(state.query)));if(state.sort==="az")rows.sort((a,b)=>a.title.localeCompare(b.title));if(state.sort==="za")rows.sort((a,b)=>b.title.localeCompare(a.title));const root=$("#collection-grid");root.replaceChildren();$("#result-count").textContent=rows.length+" collections";if(!rows.length){const p=document.createElement("p");p.className="empty-state";p.textContent="No matching collections. Try another search or filter.";root.append(p);return}rows.forEach(x=>{const article=document.createElement("article");article.className="collection-item";const h=document.createElement("h3");const a=document.createElement("a");a.href=x.href;a.textContent=x.title;h.append(a);const p=document.createElement("p");p.textContent=x.description||"Explore this part of the library.";const meta=document.createElement("div");meta.className="collection-meta";const c=document.createElement("span");c.textContent=x.category;const t=document.createElement("span");t.textContent=x.kind||"Collection";meta.append(c,t);article.append(h,p,meta);root.append(article)})}
$("#library-search").addEventListener("input",e=>{state.query=e.target.value.trim().toLowerCase();render()});
$("#sort-select").addEventListener("change",e=>{state.sort=e.target.value;render()});
if("serviceWorker" in navigator){window.addEventListener("load",()=>navigator.serviceWorker.register("sw.js").catch(()=>{}))}\nfetch("data/catalog.json").then(r=>{if(!r.ok)throw Error("catalog unavailable");return r.json()}).then(data=>{state.items=Array.isArray(data.items)?data.items:[];render()}).catch(()=>{const root=$("#collection-grid");root.innerHTML='<p class="empty-state">The catalogue has not been built yet. Once the content checks and build complete, collections will appear here.</p>';});
})();
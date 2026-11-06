# Engine 89 — E89-DS — the source (session 206, Vol VIII Ch 53, the Phase-3 review)

The design source is src.txt (md5 e009da3bc3bfa8efb90473cc8ee00cfe, 5,494 B), written to
disk BEFORE any run — the Engine 82 source-loss lesson made procedural. This record
carries the as-run source. What is verbatim: the engine core (identical in every piece,
transcribed fresh per piece per the fresh-engine rule) and the main bodies of the dose
part 2 rev-2, review-hunt part B rev-2 (the run whose gate caught the table defect) and
rev-3, the injections, and the determinism buildAll(). What is disclosed as not verbatim:
the main bodies of the probe, molar, balance, dose part 1, and review-hunt part A pieces
were lost to the session's own context compaction before this record was written; their
outputs are frozen with md5 receipts (the transcripts record) and each row's construction
is fully determined by the design source plus its frozen output line — the dose and probe
rows they share were re-run verbatim inside the determinism piece's buildAll() below. The
honest gap is named, not papered over.

## The engine core (verbatim as-run, the rev-3 corrected form)

The one transcription defect of the battery, preserved for the record: the rev-2 run's
TH carry table carried rows six and seven as
  TH6 = [0,0,1,2,3,4,4,5,6,7]   (true: [0,0,1,1,2,3,3,4,4,5])
  TH7 = [0,0,1,2,3,3,4,5,5,6]   (true: [0,0,1,2,2,3,4,4,5,6])
— 6x3 carrying 2 for 1, 7x4 carrying 3 for 2, 7x7 carrying 5 for 4. The RH5b gate caught
it (an impossible 1.39999999 for 1,109,352/756,200); rev-3 re-transcribed, self-checked
all 200 entries against trivial literal single-digit arithmetic (a data-integrity check
OUTSIDE the value path, disclosed), and re-ran clean.

```typescript
type Q={d:number[];e:number};
const TL:number[][]=[[0,0,0,0,0,0,0,0,0,0],[0,1,2,3,4,5,6,7,8,9],[0,2,4,6,8,0,2,4,6,8],[0,3,6,9,2,5,8,1,4,7],[0,4,8,2,6,0,4,8,2,6],[0,5,0,5,0,5,0,5,0,5],[0,6,2,8,4,0,6,2,8,4],[0,7,4,1,8,5,2,9,6,3],[0,8,6,4,2,0,8,6,4,2],[0,9,8,7,6,5,4,3,2,1]];
const TH:number[][]=[[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,1,1,1,2,2,2],[0,0,0,1,1,2,2,2,3,3],[0,0,1,1,2,2,3,3,4,4],[0,0,1,1,2,3,3,4,4,5],[0,0,1,2,2,3,4,4,5,6],[0,0,1,2,3,4,4,5,6,7],[0,0,1,2,3,4,5,6,7,8]];
let tbad=0;for(let d=0;d<=9;d++){for(let q=0;q<=9;q++){const p=d*q;const lo=p%10;const hi=(p-lo)/10;if(TL[d][q]!==lo||TH[d][q]!==hi){tbad++;}}}
function ds(s:string):Q{const d:number[]=[];let dot=-1;for(let i=0;i<s.length;i++){const c=s[i];if(c==='.'){dot=d.length;continue;}d.push(c.charCodeAt(0)-48);}return{d:d,e:dot<0?0:d.length-dot};}
function cp(a:Q):Q{return{d:a.d.slice(),e:a.e};}
function strip(a:Q):Q{let k=0;while(k<a.d.length-1&&a.d[k]===0){k++;}if(k>0){a.d=a.d.slice(k);}return a;}
function al(a:Q,b:Q):void{while(a.e<b.e){a.d.push(0);a.e++;}while(b.e<a.e){b.d.push(0);b.e++;}}
function cmpD(x:number[],y:number[]):number{const a=x.slice();const b=y.slice();while(a.length>1&&a[0]===0){a.shift();}while(b.length>1&&b[0]===0){b.shift();}if(a.length!==b.length){return a.length<b.length?-1:1;}for(let i=0;i<a.length;i++){if(a[i]!==b[i]){return a[i]<b[i]?-1:1;}}return 0;}
function addD(x:number[],y:number[]):number[]{const a=x.slice();const b=y.slice();const n=Math.max(a.length,b.length);while(a.length<n){a.unshift(0);}while(b.length<n){b.unshift(0);}const out:number[]=[];let c=0;for(let i=n-1;i>=0;i--){const s=a[i]+b[i]+c;out.push(s>9?s-10:s);c=s>9?1:0;}if(c>0){out.push(1);}return out.reverse();}
function subD(x:number[],y:number[]):number[]{const a=x.slice();const b=y.slice();while(b.length<a.length){b.unshift(0);}const out:number[]=[];let br=0;for(let i=a.length-1;i>=0;i--){let v=a[i]-br-b[i];if(v<0){v+=10;br=1;}else{br=0;}out.push(v);}out.reverse();while(out.length>1&&out[0]===0){out.shift();}return out;}
function mulD(x:number[],q:number):number[]{const out:number[]=[];let c=0;for(let i=x.length-1;i>=0;i--){const v=TL[x[i]][q]+c;out.push(v>9?v-10:v);c=TH[x[i]][q]+(v>9?1:0);}if(c>0){out.push(c);}return out.reverse();}
function addAt(acc:number[],c:number,v:number):void{acc[c]+=v;while(acc[c]>9){acc[c]-=10;c++;if(c===acc.length){acc.push(0);}acc[c]+=1;}}
function mulQ(a:Q,b:Q):Q{const n=a.d.length;const m=b.d.length;const acc:number[]=[];for(let k=0;k<n+m;k++){acc.push(0);}for(let i=0;i<n;i++){for(let j=0;j<m;j++){const col=(n-1-i)+(m-1-j);const lo=TL[a.d[i]][b.d[j]];const hi=TH[a.d[i]][b.d[j]];if(lo>0){addAt(acc,col,lo);}if(hi>0){addAt(acc,col+1,hi);}}}acc.reverse();return strip({d:acc,e:a.e+b.e});}
function addQ(a:Q,b:Q):Q{const x=strip(cp(a));const y=strip(cp(b));al(x,y);return{d:addD(x.d,y.d),e:x.e};}
function divq(a:Q,b:Q,S:number):Q{const A=strip(cp(a));const B=strip(cp(b));const z=S+B.e-A.e;const N=A.d.slice();const D=B.d.slice();for(let k=0;k<z;k++){N.push(0);}for(let k=0;k<-z;k++){D.push(0);}let rem:number[]=[0];const quo:number[]=[];for(let i=0;i<N.length;i++){rem.push(N[i]);while(rem.length>1&&rem[0]===0){rem.shift();}let q=0;let qd:number[]=[];if(cmpD(rem,D)>=0){for(let c=9;c>=1;c--){const t=mulD(D,c);if(cmpD(rem,t)>=0){q=c;qd=t;break;}}}if(q>0){rem=subD(rem,qd);}quo.push(q);}while(quo.length>1&&quo[0]===0){quo.shift();}return{d:quo,e:S};}
function render(a:Q):string{const b=strip(cp(a));let s='';if(b.e>=b.d.length){s='0.';for(let k=0;k<b.e-b.d.length;k++){s+='0';}for(let k=0;k<b.d.length;k++){s+=String.fromCharCode(48+b.d[k]);}return s;}for(let k=0;k<b.d.length;k++){if(k===b.d.length-b.e){s+='.';}s+=String.fromCharCode(48+b.d[k]);}return s;}
function truncDisp(a:Q,dp:number):string{const s=render(a);const dot=s.indexOf('.');let ip=s;let fp='';if(dot>=0){ip=s.slice(0,dot);fp=s.slice(dot+1);}while(fp.length<dp){fp+='0';}fp=fp.slice(0,dp);if(dp===0){return ip;}return ip+'.'+fp;}
function halfUpDisp(a:Q,dp:number):string{const s=render(a);const dot=s.indexOf('.');let ip=s;let fp='';if(dot>=0){ip=s.slice(0,dot);fp=s.slice(dot+1);}while(fp.length<dp+1){fp+='0';}const guard=fp.charCodeAt(dp)-48;fp=fp.slice(0,dp);if(guard<5){if(dp===0){return ip;}return ip+'.'+fp;}const kept=ip+fp;const kd:number[]=[];for(let i=0;i<kept.length;i++){kd.push(kept.charCodeAt(i)-48);}const inc=addD(kd,[1]);let ks='';for(let i=0;i<inc.length;i++){ks+=String.fromCharCode(48+inc[i]);}if(dp===0){return ks;}while(ks.length<=dp){ks='0'+ks;}const iplen=ks.length-dp;return ks.slice(0,iplen)+'.'+ks.slice(iplen);}
function sdbm(s:string):number{let h=0;for(let i=0;i<s.length;i++){const c=s.charCodeAt(i);h=(c+(h<<6)+(h<<16)-h)|0;}return h;}
function parseF(f:string):Record<string,number>{const stack:Record<string,number>[]=[{}];let i=0;while(i<f.length){const c=f[i];if(c==='('){stack.push({});i++;continue;}if(c===')'){i++;let mm=0;let has=false;while(i<f.length&&f[i]>='0'&&f[i]<='9'){has=true;mm=mm*10+(f.charCodeAt(i)-48);i++;}if(!has){mm=1;}const top=stack.pop();if(top!==undefined){const parent=stack[stack.length-1];for(const k in top){parent[k]=(parent[k]||0)+top[k]*mm;}}continue;}if(c>='A'&&c<='Z'){let sym=c;i++;if(i<f.length&&f[i]>='a'&&f[i]<='z'){sym+=f[i];i++;}let n=0;let has=false;while(i<f.length&&f[i]>='0'&&f[i]<='9'){has=true;n=n*10+(f.charCodeAt(i)-48);i++;}if(!has){n=1;}const top=stack[stack.length-1];top[sym]=(top[sym]||0)+n;continue;}i++;}return stack[0];}
function mulCnt(x:number[],c:number):number[]{const t=(c-(c%10))/10;const o=c%10;let tens:number[]=[];let ones:number[]=[];if(t>0){tens=mulD(x,t);tens=tens.concat([0]);}if(o>0){ones=mulD(x,o);}if(t>0&&o>0){return addD(tens,ones);}if(t>0){return tens;}return ones;}
function massLane(f:string,tab:Record<string,Q>):Q{const cnt=parseF(f);let acc:Q={d:[0],e:0};for(const k in cnt){const base=tab[k];if(base===undefined){return{d:[-1],e:0};}const prod=mulCnt(base.d,cnt[k]);const q:Q={d:prod,e:base.e};acc=addQ(acc,q);}return acc;}
function massSide(list:string[],tab:Record<string,Q>):Q{let acc:Q={d:[0],e:0};for(const f of list){acc=addQ(acc,massLane(f,tab));}return acc;}
```

The element table, re-transcribed from the standard values and matched against the
chapter's held table:

```typescript
const ET:Record<string,Q>={H:ds('1.008'),C:ds('12.011'),O:ds('15.999'),Na:ds('22.990'),Ca:ds('40.078'),S:ds('32.065'),Cl:ds('35.450')};
```

## The review-hunt part B rev-3 main (verbatim as-run; the rev-2 main differs only in
printing the RH5b row against the same gate — its output is the FAIL of record)

```typescript
const r1=divq(ds('7656810'),ds('2900000'),8);
const t1=truncDisp(r1,4);const h1=halfUpDisp(r1,4);
const ok5a=(h1==='2.6403');
const r2=divq(ds('1109352'),ds('756200'),8);
const t2=truncDisp(r2,4);const h2=halfUpDisp(r2,4);
const ok5b=(t2==='1.4670'&&h2==='1.4670');
const LS6:string[]=['Ca3(C6H5O7)2','H2SO4','H2SO4','H2SO4','H2O','H2O','H2O','H2O','H2O','H2O'];
const RS6:string[]=['C6H8O7','C6H8O7','CaSO4H4O2','CaSO4H4O2','CaSO4H4O2'];
const left6=massSide(LS6,ET);const right6=massSide(RS6,ET);
const ok6=(render(left6)==='900.753'&&render(right6)==='900.753');
const l7=mulQ(ds('13.35'),ds('28.3495'));
let dig7='';for(let i=0;i<l7.d.length;i++){dig7+=String.fromCharCode(48+l7.d[i]);}
const ok7=(dig7+'0000'==='3784658250000');
```

## The injections main (verbatim as-run)

```typescript
const ETj:Record<string,Q>={Ca:ds('40.078'),Cl:ds('35.540')};          // J1 the transposition
const j1=massLane('CaCl2',ETj);const j1t=truncDisp(j1,2);const j1h=halfUpDisp(j1,2);
const caught1=!((j1t==='110.97')&&(j1h==='110.98'));
const j2=divq(ds('378.654825'),ds('3.785'),8);                          // J2 the splice
const j2t=truncDisp(j2,2);const j2h=halfUpDisp(j2,2);
const caught2=!((j2t==='99.99')&&(j2h==='99.99'));
const m2=addQ(ds('192.123'),ds('18.015'));                              // J3 the display corruption
const j3h=halfUpDisp(m2,2);const caught3=!(j3h==='210.15');
const j4=divq(ds('450'),ds('2.95735'),8);                               // J4 the point slip
const j4t=truncDisp(j4,3);const caught4=!(j4t==='15.216');
```

## The dose part 2 rev-2 main (verbatim as-run; the repaired lanes)

```typescript
const r8a=divq(ds('40'),ds('4'),4);const r8b=divq(ds('40'),ds('1'),4);
const r9=divq(ds('600'),ds('39'),8);
const r10=divq(ds('378.465825'),ds('3.785'),8);
const r11=divq(ds('100'),ds('10'),4);
const r13=divq(ds('144'),ds('29.5735'),8);
// gates: 10/10, 40/40, 15.38/15.38, 99.99/99.99, 10/10, 4.86/4.87; D12 by refusal
```

## The determinism main (verbatim as-run; buildAll() also carries the probe and dose
part 1 rows — the reconstruction of record for the compaction-lost pieces)

buildAll() constructs the probe rows P1-P5 (parse Ca3(C6H5O7)2; 192.123+18.015;
13.35x28.3495; 450/29.5735 S=8; the 210.138 displays) and the dose rows D1-D11, D13
(the lanes exactly as in the transcripts: 450/29.5735; 648/29.5735; 535.28035/6.48
at 1 and 0 dp; 24000/300; 18x9; 150+150+50; 32500/350; 150/162; 40/4; 40/1; 600/39;
378.465825/3.785; 100/10; 144/29.5735) plus the D12 refusal line, joins them with '\n',
and is run twice; the runs are compared byte-identical and by sdbm digest (90944599
both runs).

## The lost mains, disclosed

The probe, molar, balance, dose part 1, and review-hunt part A main bodies are not
reproduced here: the session's context compaction carried off their verbatim text before
this record was written. Their outputs are the frozen receipts of record (see the
transcripts); every row's operands, gates, and displays are printed in those outputs and
specified in the design source; the probe and dose rows they share were re-run inside
buildAll() above, byte-identical across two runs. Nothing is reconstructed silently.

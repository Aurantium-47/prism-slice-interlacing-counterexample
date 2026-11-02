#!/usr/bin/env python3
"""Render a certificate-driven README figure; no approximate roots are plotted."""
import os
import tempfile
os.environ.setdefault('MPLCONFIGDIR', tempfile.mkdtemp(prefix='prism-mpl-'))
from pathlib import Path
import json
from fractions import Fraction
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE=Path(__file__).resolve().parent
cert=json.loads((HERE.parent/'review/certificate.json').read_text())
P,Q=cert['P'],cert['Q']
assert (P['dimension'],Q['dimension'])==(10,11)
assert (len(P['hstar_ascending'])-1,len(Q['hstar_ascending'])-1)==(9,10)
intervals=[tuple(Fraction(c['root_intervals'][0][k]) for k in ('left','right')) for c in (P,Q)]
assert intervals==[(Fraction(-857),Fraction(-856)),(Fraction(-839),Fraction(-838))]
assert len(P['root_intervals'])==9 and len(Q['root_intervals'])==10
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'path'})
ink='#172c3b'; muted='#536777'; teal='#087f82'; blue='#4c5bc6'; line='#dbe4e9'; paper='#ffffff'
fig=plt.figure(figsize=(14,8.8),facecolor=paper)
def txt(x,y,s,size=18,color=ink,**kw):
    return fig.text(x,y,s,fontsize=size,color=color,**kw)
def box(x,y,w,h,fc):
    fig.add_artist(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012,rounding_size=0.012',facecolor=fc,edgecolor='none',transform=fig.transFigure,zorder=0))
txt(.055,.935,'EXACT COUNTEREXAMPLE  /  COORDINATE-SPLITTING INTERLACING',12,muted,weight='bold')
txt(.055,.878,'Real-rooted separately. Not interlacing.',30,weight='bold')
txt(.055,.827,r'$k=6\qquad\mathbf{c}=(1^{10},2)\quad\longrightarrow\quad\mathbf{c}^{\prime}=(1^{12})$',24)
txt(.73,.83,'Split one side length: 2 = 1 + 1',14,muted)
box(.055,.666,.425,.113,'#eef8f7'); box(.52,.666,.425,.113,'#f1f3fc')
txt(.073,.739,r'$P=H_{6,\mathbf{c}}$',23,teal,weight='bold')
txt(.073,.695,'Polytope dimension  10     |     Polynomial degree  9',14,teal)
txt(.54,.739,r'$Q=H_{6,\mathbf{c}^{\prime}}$',23,blue,weight='bold')
txt(.54,.695,'Polytope dimension  11     |     Polynomial degree  10',14,blue)
txt(.055,.611,'Leftmost-root zoom',21,weight='bold')
txt(.055,.576,'Only certified open intervals are shown; the other 17 roots are outside this window.',14,muted)
ax=fig.add_axes([.09,.365,.82,.16])
ax.set_facecolor(paper)
ax.set_xlim(-862,-832); ax.set_ylim(-.8,.8)
ax.set_yticks([])
for spine in ('top','left','right'): ax.spines[spine].set_visible(False)
ax.spines['bottom'].set_position(('data',0)); ax.spines['bottom'].set_color('#8a9da9')
ax.set_xticks([-860,-855,-850,-845,-840,-835])
ax.tick_params(axis='x',colors=muted,labelsize=13,pad=10,length=5)
for (l,r),color,lab in zip(intervals,[teal,blue],[r'$\alpha_1\in(-857,-856)$',r'$\beta_1\in(-839,-838)$']):
    a,b=float(l),float(r)
    ax.plot([a,b],[0,0],lw=9,color=color,solid_capstyle='butt',zorder=4)
    ax.plot([a,b],[0,0],linestyle='',marker='o',markersize=7,markerfacecolor='white',markeredgewidth=2,markeredgecolor=color,zorder=5)
    ax.text((a+b)/2,.42,lab,color=color,fontsize=18,ha='center')
ax.text(-832,-.27,'x',fontsize=14,color=muted,ha='right')
box(.055,.174,.89,.13,'#f5f7f9')
txt(.077,.254,'Interlacing would require',16,muted)
txt(.077,.204,r'$\beta_1\leq\alpha_1$',26)
txt(.46,.254,'The exact intervals instead give',16,muted)
txt(.46,.204,r'$\alpha_1 < -856 < -839 < \beta_1$',25,teal)
txt(.055,.117,'Evidence: integer coefficients + 19 disjoint rational sign-change intervals (9 + 10).',14,ink)
txt(.055,.079,'Scope: the splitting-interlacing assertion only; not general real-rootedness or unimodality.',13,muted)
txt(.055,.041,'Ferroni–McGinnis (2022), Conjecture 5.12  ·  Exact counterexample to splitting interlacing',11,muted,weight='bold')
fig.savefig(HERE/'prism-interlacing.svg',facecolor=paper)
fig.savefig(HERE/'prism-interlacing.png',dpi=150,facecolor=paper)
plt.close(fig)
print('Rendered SVG and PNG from exact certificate intervals.')

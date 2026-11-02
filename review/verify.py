#!/usr/bin/env python3
"""Independent geometry-to-root certificate; Python standard library only."""
from math import comb, factorial
from fractions import Fraction as F
from pathlib import Path
import json

def count_dp(c,m,k=6):
    target=k*m
    a=[1]+[0]*target
    for cap in c:
        b=[]; window=0
        for s in range(target+1):
            window+=a[s]
            if s>cap*m: window-=a[s-cap*m-1]
            b.append(window)
        a=b
    return a[target]

def count_ie(c,m,k=6):
    n=len(c); ans=0
    for mask in range(1<<n):
        shift=sum(c[j]*m+1 for j in range(n) if mask>>j&1)
        residual=k*m-shift
        if residual>=0: ans+=(-1)**mask.bit_count()*comb(residual+n-1,n-1)
    return ans

def value(a,x):
    out=0
    for v in reversed(a): out=out*x+v
    return out

def scaled(a,x):
    # q^degree f(p/q), evaluated directly with integer arithmetic.
    p,q=x.numerator,x.denominator
    return sum(v*p**j*q**(len(a)-1-j) for j,v in enumerate(a))

def reconstruct(c):
    n=len(c)
    counts=[count_dp(c,m) for m in range(n+3)]
    assert counts==[count_ie(c,m) for m in range(n+3)]
    h=[sum((-1)**i*comb(n,i)*counts[j-i] for i in range(min(j,n)+1)) for j in range(n+3)]
    assert all(v==0 for v in h[n:])
    while h[-1]==0: h.pop()
    # Further dilations not used to reconstruct numerator.
    for m in (17,23,31):
        actual=count_dp(c,m)
        predicted=sum(v*comb(m-j+n-1,n-1) for j,v in enumerate(h) if m>=j)
        assert actual==predicted==count_ie(c,m)
    grid=sorted({-F(i,10**j) for j in range(5) for i in range(1,1001)})+[F(0)]
    roots=[]
    for l,r in zip(grid,grid[1:]):
        vl,vr=scaled(h,l),scaled(h,r)
        assert vl and vr, 'grid root requires separate handling'
        if vl*vr<0:
            roots.append({'left':str(l),'right':str(r),'left_scaled':vl,'right_scaled':vr})
    assert len(roots)==len(h)-1
    assert all(F(v['right'])<0 for v in roots)
    assert all(F(a['right'])<=F(b['left']) for a,b in zip(roots,roots[1:]))
    ehr=[F(0)]*n
    for j,hj in enumerate(h):
        term=[F(hj,factorial(n-1))]
        for r in range(1,n):
            tmp=[F(0)]*(len(term)+1)
            for t,a in enumerate(term): tmp[t]+=a*(r-j); tmp[t+1]+=a
            term=tmp
        ehr=[a+b for a,b in zip(ehr,term)]
    assert all(value(ehr,F(m))==counts[m] for m in range(n+3))
    return {'ehrhart_power_coefficients_ascending':list(map(str,ehr)), 'c':c,'dimension':n-1,'denominator_exponent':n,'counts':counts,'hstar_ascending':h,'root_intervals':roots}

P=reconstruct([1]*10+[2]); Q=reconstruct([1]*12)
p=P['hstar_ascending']; q=Q['hstar_ascending']
assert len(p)==10 and len(q)==11 and p[-1]==q[-1]==1
v=value(p,-850); assert v>0
# Derive the half-line bound from the newly reconstructed coefficients.
# Q(-y)/y^8: y^2-q[9]y+q[8], negative remainder -sum odd terms j<=7.
assert all(a>=0 for a in q)
assert 2*850-q[9]>0
base=850**2-q[9]*850+q[8]
negative_sum=sum(q[j] for j in range(1,8,2))
bound=F(base)-F(negative_sum,850)
assert bound>0
assert F(P['root_intervals'][0]['right'])<-850
assert F(Q['root_intervals'][0]['left'])>-850
out={'P':P,'Q':Q,'P_minus850':v,'quadratic_at850':base,'negative_sum':negative_sum,'halfline_lower_bound':str(bound),'verdict':'All exact checks passed: simple negative roots, noninterlacing.'}
path=Path(__file__).with_name('certificate.json'); path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

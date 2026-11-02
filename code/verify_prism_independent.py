#!/usr/bin/env python3
"""Independent exact audit of the Ferroni--McGinnis Conj. 5.12 witness.

This computes Ehrhart counts directly by bounded-composition convolution;
it does not use inclusion--exclusion or hard-coded polynomial coefficients.
All root certificates are signs at rational endpoints, with integer arithmetic.
Python standard library only.
"""
import argparse
import json
from fractions import Fraction
from math import comb


def lattice_points(c,k,t):
    target=k*t
    a=[1]
    for cap in c:
        b=[0]*(min(target,len(a)-1+cap*t)+1)
        for i,v in enumerate(a):
            for j in range(min(cap*t,target-i)+1):
                b[i+j]+=v
        a=b
    return a[target] if target<len(a) else 0


def hstar(c,k):
    assert all(isinstance(v,int) and v>0 for v in c)
    assert 0<k<sum(c)
    # The slice has dimension len(c)-1, so its series denominator is (1-z)^len(c).
    n=len(c)
    counts=[lattice_points(c,k,t) for t in range(n+3)]
    h=[sum((-1)**j*comb(n,j)*counts[i-j]
           for j in range(min(n,i)+1)) for i in range(len(counts))]
    # General Ehrhart theory guarantees degree <= n-1. These are extra checks.
    assert all(v==0 for v in h[n:])
    while len(h)>1 and h[-1]==0:h.pop()
    return counts,h


def homogeneous_value(p,x):
    x=Fraction(x)
    a,b=x.numerator,x.denominator
    d=len(p)-1
    return sum(v*a**i*b**(d-i) for i,v in enumerate(p))


def root_certificate(p,intervals):
    result=[]
    for left,right in intervals:
        left,right=Fraction(left),Fraction(right)
        assert left<right
        lv,rv=homogeneous_value(p,left),homogeneous_value(p,right)
        assert lv*rv<0
        result.append({'left':str(left),'right':str(right),
                       'homogeneous_left_value':lv,'homogeneous_right_value':rv})
    assert len(intervals)==len(p)-1
    assert all(Fraction(intervals[i][1])<=Fraction(intervals[i+1][0])
               for i in range(len(intervals)-1))
    return result


def run():
    c=[1]*10+[2]
    cp=[1]*12
    assert cp==c[:-1]+[c[-1]-1,1]
    LP,P=hstar(c,6)
    LQ,Q=hstar(cp,6)
    P_intervals=[(-1000,-850),(-50,-20),(-10,-5),(-5,-2),(-1,'-1/2'),
                 ('-1/2','-1/5'),('-1/5','-1/10'),('-1/20','-1/50'),
                 ('-1/500','-1/1000')]
    Q_intervals=[(-850,-100),(-100,-50),(-20,-10),(-5,-2),(-2,-1),
                 (-1,'-1/2'),('-1/2','-1/5'),('-1/10','-1/20'),
                 ('-1/50','-1/100'),('-1/500','-1/1000')]
    pc=root_certificate(P,P_intervals)
    qc=root_certificate(Q,Q_intervals)
    assert len(Q)==len(P)+1
    assert Fraction(P_intervals[0][1])<=Fraction(Q_intervals[0][0])
    # Strict intervals imply minroot(P)<-850<minroot(Q), impossible for
    # interlacing of monic polynomials of degrees 9 and 10.
    return {'target':'Ferroni--McGinnis, Conjecture 5.12, interlacing clause',
            'source':'https://arxiv.org/pdf/2202.11808v1 (p.19)',
            'status':'exact counterexample; priority not assessed by this script',
            'k':6,'c':c,'c_prime':cp,'dimensions':[10,11],
            'Ehrhart_counts_P':LP,'Ehrhart_counts_Q':LQ,
            'P_ascending':P,'Q_ascending':Q,
            'P_minus850':homogeneous_value(P,-850),
            'P_real_root_intervals':pc,'Q_real_root_intervals':qc,
            'conclusion':'Both polynomials have simple negative real roots, but their roots do not interlace.'}


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--output')
    args=ap.parse_args()
    result=run()
    data=json.dumps(result,indent=2)+'\n'
    if args.output:
        with open(args.output,'w') as f:f.write(data)
        print(result['conclusion'])
    else:print(data,end='')

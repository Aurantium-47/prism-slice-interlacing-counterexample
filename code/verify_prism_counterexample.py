#!/usr/bin/env python3
"""Exact, dependency-free counterexample certificate for FM Conjecture 5.12.

Run: python3 verify_prism_counterexample.py
All coefficient and sign claims use integers or fractions. No floating roots.
"""
from fractions import Fraction
from math import comb
import json
from pathlib import Path

C=(1,)*10+(2,)
D=(1,)*12
K=6
P_EXPECTED=(1,661,31846,312146,927706,960774,347986,38686,901,1)
Q_EXPECTED=(1,912,62767,878932,3834832,6169360,3834832,878932,62767,912,1)

def lattice_count_dp(c,k,t):
    """Literal coefficient product, truncated at kt. Independent of IE."""
    target=k*t
    row=[1]+[0]*target
    for ci in c:
        nextrow=[0]*(target+1)
        for old_degree,old_count in enumerate(row):
            for value in range(min(ci*t,target-old_degree)+1):
                nextrow[old_degree+value]+=old_count
        row=nextrow
    return row[target]

def lattice_count_ie(c,k,t):
    """Inclusion-exclusion over actual subsets; no grouped rho recurrence."""
    n=len(c)
    answer=0
    for mask in range(1<<n):
        indices=[i for i in range(n) if mask>>i&1]
        left=k*t-sum(c[i]*t+1 for i in indices)
        if left>=0:
            answer+=(-1)**len(indices)*comb(left+n-1,n-1)
    return answer

def hstar(c,k):
    # Here 0<k<sum(c), so dimension = len(c)-1.
    n=len(c)
    assert 0<k<sum(c)
    values=[lattice_count_dp(c,k,t) for t in range(n)]
    assert values==[lattice_count_ie(c,k,t) for t in range(n)]
    h=[sum((-1)**j*comb(n,j)*values[i-j] for j in range(i+1)) for i in range(n)]
    while h[-1]==0: h.pop()
    return tuple(h),values

def evaluate(h,z):
    result=0
    for coefficient in reversed(h): result=result*z+coefficient
    return result

def shift_reflect(h,a):
    """Coefficients of h(-a-y), in ascending y-degree."""
    return [sum(h[j]*(-1)**j*comb(j,i)*a**(j-i) for j in range(i,len(h))) for i in range(len(h))]

def sign(x): return (x>0)-(x<0)

P_INTERVALS=[(-857,-856),(-34,-33),(-8,-7),('-5/2','-12/5'),(-1,'-9/10'),('-2/5','-3/8'),('-13/100','-12/100'),('-26/1000','-25/1000'),('-17/10000','-16/10000')]
Q_INTERVALS=[(-839,-838),(-57,-56),(-11,-10),('-37/10','-36/10'),('-16/10','-15/10'),('-67/100','-66/100'),('-28/100','-27/100'),('-93/1000','-92/1000'),('-18/1000','-17/1000'),('-12/10000','-11/10000')]

def certify_all_real(h,intervals):
    assert len(intervals)==len(h)-1
    result=[]
    previous=None
    for l,r in intervals:
        l,r=Fraction(l),Fraction(r)
        assert l<r<0
        if previous is not None: assert previous<l
        sl,sr=sign(evaluate(h,l)),sign(evaluate(h,r))
        assert sl*sr==-1
        result.append({'left':str(l),'right':str(r),'sign_left':sl,'sign_right':sr})
        previous=r
    return result

def main():
    p,ep=hstar(C,K);q,eq=hstar(D,K)
    assert p==P_EXPECTED and q==Q_EXPECTED
    shifted=shift_reflect(q,850)
    assert all(a>0 for a in shifted)
    p850=evaluate(p,-850)
    assert p850>0 and len(p)-1==9 and p[-1]==1
    p_intervals=certify_all_real(p,P_INTERVALS)
    q_intervals=certify_all_real(q,Q_INTERVALS)
    result={
      'claim':'The interlacing component of Ferroni--McGinnis Conjecture 5.12 is false.',
      'parameters':{'k':K,'c':C,'c_split':D},
      'dimension_p':len(C)-1,'dimension_q':len(D)-1,
      'ehrhart_p_at_0_through_dimension':ep,'ehrhart_q_at_0_through_dimension':eq,
      'p_coefficients_ascending':p,'q_coefficients_ascending':q,
      'p_at_minus850':p850,
      'q_at_minus850_minus_y_coefficients_ascending':shifted,
      'p_simple_negative_root_intervals':p_intervals,
      'q_simple_negative_root_intervals':q_intervals,
      'verified':True,
      'limits':['Does not refute real-rootedness of prism-slice h*-polynomials.','Does not settle hypersimplex real-rootedness or unimodality.','Does not certify novelty or priority.']
    }
    out=Path(__file__).resolve().parent.parent / 'results' / 'prism_counterexample_certificate.json'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS: two independent exact lattice enumerations agree.')
    print('PASS: exact h*-coefficient transform agrees with stated P and Q.')
    print('PASS: P(-850)>0 and all coefficients of Q(-850-y) are positive.')
    print('PASS: 9 and 10 disjoint negative rational sign intervals certify all roots simple and real.')
    print('CONCLUSION: P and Q do not interlace. See '+str(out))

if __name__=='__main__':main()

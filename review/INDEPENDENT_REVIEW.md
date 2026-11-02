# Independent exact audit: Ferroni–McGinnis splitting interlacing

**Verdict: the proposed counterexample is mathematically correct.** The claim disproved is the universal splitting-interlacing assertion, not universal real-rootedness. No priority/novelty conclusion is made here. This is an independent computational audit, not external peer review.

## Independence and reproducibility

The input read was a statement-only proposed-result summary. None of its scripts, root certificates, or expected coefficient arrays was used. `verify.py` is newly written and uses only Python's standard library. It constructs coefficients directly from geometric parameters, finds its own rational intervals, and writes `certificate.json`.

Run from any directory:

```
python3 review/verify.py
```

`../results/reproduce.log` records the release replay. The certificate includes full integer lattice-count sequences, h* coefficient arrays, ordinary Ehrhart coefficients in the power basis (exact rationals), and integer endpoint witnesses for all nineteen roots.

## Original-source applicability

Read original arXiv PDF text through the web tool, not the proposed report's quotations:

- [v1, 23 February 2022](https://arxiv.org/pdf/2202.11808v1), printed page 19, §5.3, Conjecture 5.12: positive integral c, final coordinate at least two, split into final coordinate minus one followed by one; the two h* polynomials are asserted real-rooted and interlacing.
- [v2, 23 May 2023](https://arxiv.org/pdf/2202.11808v2), printed page 20, same conjecture: real-rootedness is stated separately for positive integral c and k>0, followed by the same splitting-interlacing claim.

Thus the presentation of the real-rootedness clause differs slightly between versions, but their splitting assertion applies identically here. No condition excludes unit coordinates, central slices, or the resulting hypersimplex. The v1 definition is equation (2), page 2; v2 equation (1), page 1. Their generating-series numerator computations explicitly use exponent n in the denominator (v1 page 18; v2 page 20), consistent with dimension n−1.

Source limitation: PDF-text retrieval succeeded for both full papers, including definitions and conjecture. Optional screenshot requests failed with a cache-miss internal error, so visual screenshots were not verified or archived. No retry was attempted. This does not obstruct the extracted mathematical statements.

## Geometry and normalization

Set k=6, c=(1 repeated ten times,2), c'=(1 repeated twelve times). Both capacities sum to twelve and c/2, c'/2 lie strictly inside every coordinate bound on the respective sum-six hyperplanes. Consequently dimensions are 10 and 11.

Every vertex has at most one coordinate not at a bound: two free coordinates could be perturbed oppositely while preserving the sum. All bounded coordinates are integers, and the sum-six equation makes the remaining one integral. Both polytopes are therefore lattice polytopes. The ambient lattice count is the appropriate intrinsic affine-lattice count; there is no index or Euclidean-volume normalization to introduce.

For N coordinates and dilation m, count nonnegative integral u with sum 6m and u_i<=m c_i. The verifier computes this in two independent ways: bounded-composition dynamic programming and full subset inclusion-exclusion. Explicitly,

L(m)=sum_{S subset [N]} (-1)^|S| binom(6m-sum_{i in S}(m c_i+1)+N-1,N-1),

where a term is zero if its residual sum is negative. This includes m=0 correctly.

Since dimension is N−1, h_j=sum_{i=0}^j (-1)^i binom(N,i)L(j−i). Ehrhart's theorem ensures the numerator degree is at most N−1; computing through that degree determines it exactly. Additional computed zeros and independently checked dilations m=17,23,31 are consistency checks, not substitutes for the theorem.

The reconstructed ascending h* arrays are:

P: [1,661,31846,312146,927706,960774,347986,38686,901,1].

Q: [1,912,62767,878932,3834832,6169360,3834832,878932,62767,912,1].

They match the proposed arrays exactly. Denominators are respectively (1−x)^11 and (1−x)^12; degrees are respectively nine and ten. In particular, h* degree must not be confused with polytope dimension. Ordinary Ehrhart power coefficients were additionally reconstructed by L(m)=sum_j h_j binom(m+N−1−j,N−1) and checked against every initial count.

## Entire-halfline certificate

P is monic of odd degree nine and P(−850)=1625988474636775883423151>0. Thus it has a root strictly below −850.

For y>=850, retaining the leading quadratic and the negative terms of Q(−y)/y^8 gives

Q(−y)/y^8 >= y²−912y+62767−878932/y−6169360/y³−878932/y⁵−912/y⁷.

The quadratic is increasing there (derivative 2y−912>0), with value 10067 at 850. Since y^(−r)<=1/850 for r=1,3,5,7,

Q(−y)/y^8 >=10067−7928136/850=314407/425>0.

Every sign, exponent, and arithmetic value in this bound was derived/checked against the independently reconstructed Q, not an expected array. Consequently Q has no root at or below −850.

## All roots simple, real, negative

The verifier discovers disjoint rational intervals using an exact grid, without floating-point root finding. For endpoint p/q (q>0), its witness is q^d f(p/q), calculated as an integer. Every interval has strictly opposite endpoint signs. Nine intervals for P and ten for Q account for the full respective degrees: the intermediate value theorem gives at least one distinct real root in each interval, and the degree bound means exactly one in each and all are simple. All intervals are strictly negative.

The leftmost intervals are P: (−857,−856), Q: (−839,−838). The complete intervals and signed endpoint integers are in `certificate.json`.

For real-rooted polynomials of respective degrees nine and ten, interlacing requires the degree-ten polynomial's smallest root to be at or below the degree-nine polynomial's smallest root. The certified order reverses this necessary condition. Hence interlacing fails even in the weak (non-strict) sense.

## Scope of conclusion

This is an exact disproof of the coordinate-splitting interlacing part of Conjecture 5.12 in both checked versions. It neither disproves nor proves universal real-rootedness, nor settles hypersimplex unimodality. This automated independent derivation is not human peer review or a formal proof-assistant verification. Novelty is outside this audit's scope.

# Literature and target audit — 2026-11-02

## Verdict

**The proposed instance targets the original splitting-interlacing assertion, not an invented strengthening.** No earlier refutation or correction of that assertion was located in the bounded searches below. This is **not priority certification**. This audit checks source scope and literature, not an independent reconstruction of the numerical certificates.

## Original source and precise scope

- [arXiv v1](https://arxiv.org/pdf/2202.11808v1), 23 February 2022, p.19, Conjecture 5.12: positive integral coordinate capacities, final capacity at least two, and the operation replacing that final capacity by one less and a new unit coordinate. It jointly asserts real roots and interlacing for the resulting pair.
- [arXiv v2](https://arxiv.org/pdf/2202.11808v2), 23 May 2023, p.20: first asserts real-rootedness for positive capacities and positive k; then separately asserts interlacing under the same splitting operation. Thus the versions are **not literally identical formulations**, but the relevant splitting claim persists.
- [Published article](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/lattice-points-in-slices-of-prisms/BD4DAAE19B3FBECB840B658A189198ED), Canadian Journal of Mathematics **77(3), June 2025, 1013–1040**, DOI 10.4153/S0008414X24000233: §5.3, p.1034, retains the two-part formulation. The authors explicitly propose splitting chains ending at hypersimplices as a route toward their unimodality. The conjecture has no exclusion for unit capacities or central slices.

Application (our inference): k=6, c=(1^10,2) is positive integral, its last entry is 2, and its prescribed split is (1^12). Both total capacities are 12 and 0<6<12. Hence the counterexample, if its coefficients and root certificates check out, refutes the universal **interlacing clause** in all three versions. It does not refute the standalone real-rootedness clause. No degenerate or empty-polytope convention matters here.

Significance assessment (not a source claim): this is a focused correction of a numbered conjecture and of a proposed universal proof mechanism. It is not a solution of hypersimplex real-rootedness or unimodality, does not invalidate the paper's proved Ehrhart-positivity theorems, and does not warrant claims of a major long-standing problem solved or a predicted journal tier.

## Recent counterexamples are genuinely different targets

[Houshan Fu, arXiv:2609.37439v1](https://arxiv.org/html/2609.37439v1), 29 September 2026, Theorem 1.1 and §4, gives non-real-rooted matroid h*-polynomials, including parallel classes (4,561,600), and a family (4,a,a+29). These refute Ferroni's conjecture for **all matroids**, not the Ferroni–McGinnis splitting relation. The inspected text has no McGinnis match. Fu also reports Adiprasito–Zhang rank-three and eventual fixed-rank hypersimplex real-rootedness, citing HAL hal-05747878v1; this audit does not independently verify that HAL manuscript.

[Luís Ferroni, arXiv:2609.10513v2](https://arxiv.org/html/2609.10513v2), dated **29 October 2026**, constructs nonunimodal IDP h*-polynomials via **Cayley sums of boxes** (§2; Theorem 1.2). Additional results concern log-concavity of Ehrhart series and Gorenstein IDP h*-polynomials. These are not hyperplane sections of one box by definition, nor statements about paired-coordinate splitting. Text searches found neither McGinnis nor interlac. Its reference to another Question 5.12(b) is a Ferroni–Higashitani question, not the target conjecture.

Logical caution (our inference): sharing an ambient class such as IDP polytopes does not transfer a counterexample into the narrower prism-slice family. Conversely, the proposed pair, whose members are reportedly individually real-rooted, cannot itself be a counterexample to individual real-rootedness or unimodality.

## Citation leads actually checked

The publisher's cited-by widget displayed **“No CrossRef data available”**. Treat this as missing citation data, not zero citations. Two discovered citation leads were followed to primary sources:

1. [Deligeorgaki–McGinnis–Vindas-Meléndez, arXiv:2311.01640v3](https://arxiv.org/html/2311.01640v3), and [SIAM publication](https://epubs.siam.org/doi/10.1137/25M1738103), concern panhandle Ehrhart positivity and paving-matroid coefficient bounds. The introduction/abstract and targeted text search do not identify a resolution of the target splitting conjecture.
2. [Elena Tielker, Weighted Ehrhart Series and a Type-B Analogue of a Formula of MacMahon](https://link.springer.com/article/10.1007/s00454-025-00731-8), explicitly cites the target paper as reference 16. Its subject is weighted Ehrhart series of products of simplices/cross-polytopes; targeted text search for 5.12 returned no match. This is a citation, not evidence of a refutation.

These are not a complete citation census, and targeted searches are not equivalent to proof-by-proof reading of every citing paper.

## Search boundary and audit trail

Public web searches were performed on 2026-11-02 for the following literal or near-literal combinations:

- “Lattice points in slices of prisms” + “5.12”, counterexample, interlace, interlacing, correction;
- “Ferroni” “McGinnis” “interlacing” counterexample;
- “Ferroni” “McGinnis” “5.12”;
- “slices of prisms” conjecture disprove;
- “slices of prisms” erratum OR corrigendum;
- “2202.11808” “5.12”;
- “slices of prisms” real-rootedness 2026;
- the exact titles of the two citing papers above;
- Fu matroid h* real rooted 561 600 2026;
- Ferroni IDP counterexample Cayley 2026 unimodality.

The [arXiv record](https://arxiv.org/abs/2202.11808) still lists v2 as its latest version. No target-specific erratum, corrigendum or prior disproof was located. Several searches returned substantial irrelevant material, so absence of hits is weak evidence rather than exhaustive exclusion. Unindexed manuscripts, private discoveries, talks and inaccessible full texts remain outside this conclusion. Secondary search hits were used only as leads, not as authority for mathematical claims.

## Access limits

Adiprasito–Zhang, *Eventual unimodality of the hypersimplex*, HAL hal-05747878v1 was not independently inspected due to unavailable access. It is not a premise of this proof. No claim about that manuscript is independently certified here.

## Recommended defensible wording

“An exact counterexample to the coordinate-splitting interlacing clause of Ferroni–McGinnis Conjecture 5.12, with k=6 and (1^10,2)→(1^12). The two h*-polynomials remain individually real-rooted. Our bounded literature search found no prior refutation of this clause; priority is not certified.”

Use this only after the separate arithmetic audit confirms the claimed coefficients and root separation.

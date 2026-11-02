#!/usr/bin/env python3
"""Independent integer verification of the coordinate-splitting counterexample.

This program does not import the other verifier or its certificate.
Only the Python standard library is needed. All results are exact.
"""
from math import comb
from pathlib import Path
import json


def count_by_windows(capacities, k, dilation):
    target = k * dilation
    row = [1] + [0] * target
    for c in capacities:
        out, running = [], 0
        bound = c * dilation
        for j in range(target + 1):
            running += row[j]
            if j > bound:
                running -= row[j - bound - 1]
            out.append(running)
        row = out
    return row[target]


def choose_or_zero(n, r):
    return comb(n, r) if n >= r >= 0 else 0


def grouped_p(m):
    return sum((-1)**a * comb(10, a) * choose_or_zero((6-a)*m+10-a, 10)
               for a in range(6)) - sum(
        (-1)**a * comb(10, a) * choose_or_zero((4-a)*m+9-a, 10)
        for a in range(4))


def grouped_q(m):
    return sum((-1)**a * comb(12, a) * choose_or_zero((6-a)*m+11-a, 11)
               for a in range(6))


def numerator(lattice_counts, coordinate_count):
    return [sum((-1)**i * comb(coordinate_count, i) * lattice_counts[j-i]
                for i in range(min(j, coordinate_count)+1))
            for j in range(len(lattice_counts))]


def at(coefficients, value):
    answer = 0
    for coefficient in reversed(coefficients):
        answer = answer * value + coefficient
    return answer


def main():
    cp, cq = (1,)*10+(2,), (1,)*12
    lp = [count_by_windows(cp, 6, m) for m in range(15)]
    lq = [count_by_windows(cq, 6, m) for m in range(15)]
    assert lp == [grouped_p(m) for m in range(15)]
    assert lq == [grouped_q(m) for m in range(15)]
    hp, hq = numerator(lp, 11), numerator(lq, 12)
    p_expected = [1,661,31846,312146,927706,960774,347986,38686,901,1]
    q_expected = [1,912,62767,878932,3834832,6169360,3834832,878932,62767,912,1]
    assert hp == p_expected + [0]*5
    assert hq == q_expected + [0]*4
    p_value = at(hp, -850)
    assert p_value == 1625988474636775883423151 > 0
    quadratic = 850**2 - 912*850 + 62767
    negative_sum = 878932 + 6169360 + 878932 + 912
    bound_numerator = 850*quadratic - negative_sum
    assert quadratic == 10067 and negative_sum == 7928136
    assert bound_numerator == 628814 > 0
    result = {
        'method': 'sliding-window composition count and grouped inclusion-exclusion',
        'lattice_p_at_0_through_14': lp,
        'lattice_q_at_0_through_14': lq,
        'p_numerator_at_0_through_14': hp,
        'q_numerator_at_0_through_14': hq,
        'p_at_minus_850': p_value,
        'quadratic_minimum_on_y_ge_850': quadratic,
        'sum_of_negative_lower_coefficients': negative_sum,
        'positive_lower_bound_numerator': bound_numerator,
        'positive_lower_bound_denominator': 850,
        'status': 'PASS',
        'scope': 'Exact interlacing counterexample; no novelty or priority certification'
    }
    destination = Path(__file__).resolve().parent.parent / 'results' / 'independent_check.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print('PASS: independent counts, complete numerators, and elementary half-line certificate.')
    print(destination)


if __name__ == '__main__':
    main()

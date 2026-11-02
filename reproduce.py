#!/usr/bin/env python3
"""Replay all exact certificates without network access or third-party packages."""
import os
from pathlib import Path
import subprocess
import sys

if sys.flags.optimize or os.environ.get('PYTHONOPTIMIZE'):
    raise SystemExit('Run without -O or PYTHONOPTIMIZE: assertions are required.')
root = Path(__file__).resolve().parent
commands = [
    ['code/verify_prism_counterexample.py'],
    ['code/independent_check.py'],
    ['code/verify_prism_independent.py', '--output', 'results/independent_root_certificates.json'],
    ['review/verify.py'],
]
(root / 'results').mkdir(exist_ok=True)
lines = []
for command in commands:
    run = subprocess.run([sys.executable] + command, cwd=root, capture_output=True, text=True)
    if run.returncode:
        sys.stderr.write(run.stdout + run.stderr)
        raise SystemExit(run.returncode)
    lines.append('PASS: ' + ' '.join(command))
lines.append('PASS: all four exact verifiers completed; no floating-point proof or external dependency.')
text = '\n'.join(lines) + '\n'
(root / 'results/reproduce.log').write_text(text, encoding='utf-8')
print(text, end='')

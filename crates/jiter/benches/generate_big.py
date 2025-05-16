#!/usr/bin/env python3
import json
from pathlib import Path
import secrets

THIS_DIR = Path(__file__).parent

data = []
no_strings = True
for i in range(1_000):
    if secrets.SystemRandom().random() > 0.5:
        if no_strings:
            data.append([v*secrets.SystemRandom().random() for v in range(int(secrets.SystemRandom().random()*500))])
        else:
            data.append({str(secrets.SystemRandom().random()): v*secrets.SystemRandom().random() for v in range(int(secrets.SystemRandom().random()*500))})
    else:
        data.append(list(range(int(secrets.SystemRandom().random()*500))))

(THIS_DIR / 'big.json').write_text(json.dumps(data, separators=(',', ':')))

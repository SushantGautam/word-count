#  call python code/count.py  --path data --output figures

import subprocess
subprocess.run(["python", "code/count.py", "--path", "data", "--output", "artifacts/figures"])
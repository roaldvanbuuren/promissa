import subprocess, sys
for s in ["build_commitments.py", "build_delivery.py", "build_rates.py", "normalise.py"]:
    print(f"\n== {s}"); 
    if subprocess.run([sys.executable, s]).returncode: sys.exit(f"{s} failed")

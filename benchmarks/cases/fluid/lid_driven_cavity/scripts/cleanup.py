"""
Cleanup the directory by removing all *.vtu, *.vtp, and *.csv files

"""


from pathlib import Path

for fp in Path('./').glob("**/*.vtu"):
    fp.unlink()

for fp in Path('./').glob("**/*.vtp"):
    fp.unlink()

for fp in Path('./').glob("**/*.csv"):
    fp.unlink()
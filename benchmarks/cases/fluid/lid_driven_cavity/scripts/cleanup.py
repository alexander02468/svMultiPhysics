"""
Cleanup the directory by removing all temporary or created files.

"""


from pathlib import Path

for fp in Path('./').glob("**/*.vtu"):
    fp.unlink()

for fp in Path('./').glob("**/*.vtp"):
    fp.unlink()

for fp in Path('./').glob("**/*.csv"):
    fp.unlink()

for fp in Path('./').glob("**/*.png"):
    fp.unlink()

for fp in Path('./').glob("**/*.xml"):
    fp.unlink()

for fp in Path('./').glob("**/*.json"):
    fp.unlink()
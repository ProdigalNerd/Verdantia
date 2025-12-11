# Ensure the backend package is importable when running tests
import sys
from pathlib import Path

# Insert the backend package root (one level above tests)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

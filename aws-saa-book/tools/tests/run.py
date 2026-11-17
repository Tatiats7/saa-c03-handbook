#!/usr/bin/env python3
"""Run the tool's unit tests.

    python3 aws-saa-book/tools/tests/run.py            # all tests
    python3 aws-saa-book/tools/tests/run.py facts      # only tests/test_facts*.py

Each module owns tests/test_<module>.py (unittest). Every gate must have at least one
"must fail" test: a bad input that the gate is required to reject.
"""
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

if __name__ == "__main__":
    pattern = f"test_{sys.argv[1]}*.py" if len(sys.argv) > 1 else "test_*.py"
    suite = unittest.defaultTestLoader.discover(str(HERE), pattern=pattern)
    result = unittest.TextTestRunner(verbosity=1).run(suite)
    sys.exit(0 if result.wasSuccessful() and result.testsRun > 0 else 1)

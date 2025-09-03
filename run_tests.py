#!/usr/bin/env python3
"""
Test runner script for PromptLifter.
"""

import os
import subprocess
import sys


def run_tests():
    """Run the test suite."""
    print("🧪 Running PromptLifter Tests")
    print("=" * 50)

    # Check if pytest is installed
    try:
        import pytest
    except ImportError:
        print("❌ pytest not found. Installing test dependencies...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", ".[test]"], check=True
        )

    # Run tests
    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "tests/",
        "-v",
        "--tb=short",
        "--cov=promptlifter",
        "--cov-report=term-missing",
        "--cov-report=html:htmlcov",
    ]

    print("Running: " + " ".join(cmd))
    print()

    result = subprocess.run(cmd)

    if result.returncode == 0:
        print("\n✅ All tests passed!")
    else:
        print("\n❌ Some tests failed!")

    return result.returncode


def run_specific_tests(test_pattern=None):
    """Run specific tests."""
    cmd = [sys.executable, "-m", "pytest", "-v"]

    if test_pattern:
        cmd.append(f"tests/test_{test_pattern}.py")
    else:
        cmd.append("tests/")

    print(f"🧪 Running tests: {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific test file
        test_pattern = sys.argv[1]
        run_specific_tests(test_pattern)
    else:
        # Run all tests
        sys.exit(run_tests())

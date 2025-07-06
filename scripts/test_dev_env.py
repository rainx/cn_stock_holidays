#!/usr/bin/env python3
"""
Test script to verify the development environment is working correctly.

This script tests that all the debugging tools and IPython setup are working.
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")

    try:
        import cn_stock_holidays

        print("✓ cn_stock_holidays imported")

        import cn_stock_holidays.data

        print("✓ cn_stock_holidays.data imported")

        import cn_stock_holidays.data_hk

        print("✓ cn_stock_holidays.data_hk imported")

        import cn_stock_holidays.common

        print("✓ cn_stock_holidays.common imported")

        import cn_stock_holidays.meta_functions

        print("✓ cn_stock_holidays.meta_functions imported")

        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


def test_functions():
    """Test that key functions work."""
    print("\nTesting functions...")

    try:
        from cn_stock_holidays.data import is_trading_day
        from cn_stock_holidays.data_hk import is_half_day_trading_day
        from cn_stock_holidays.common import int_to_date

        from datetime import date

        # Test mainland China
        result = is_trading_day(date(2024, 1, 1))
        print(f"✓ is_trading_day(2024-01-01) = {result}")

        # Test Hong Kong half-day
        result = is_half_day_trading_day(date(2024, 12, 24))
        print(f"✓ is_half_day_trading_day(2024-12-24) = {result}")

        # Test date conversion
        result = int_to_date(20240101)
        print(f"✓ int_to_date(20240101) = {result}")

        return True
    except Exception as e:
        print(f"✗ Function error: {e}")
        return False


def test_ipython():
    """Test that IPython can be imported."""
    print("\nTesting IPython...")

    try:
        from IPython import start_ipython

        print("✓ IPython can be imported")
        return True
    except ImportError as e:
        print(f"✗ IPython import error: {e}")
        return False


def test_scripts():
    """Test that all scripts exist and are executable."""
    print("\nTesting scripts...")

    scripts = [
        "scripts/quick_test.py",
        "scripts/dev_shell.py",
        "scripts/ipython_config.py",
    ]

    all_exist = True
    for script in scripts:
        if Path(script).exists():
            print(f"✓ {script} exists")
        else:
            print(f"✗ {script} missing")
            all_exist = False

    return all_exist


def main():
    """Run all tests."""
    print("cn_stock_holidays Development Environment Test")
    print("=" * 50)

    tests = [
        test_imports,
        test_functions,
        test_ipython,
        test_scripts,
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1

    print("\n" + "=" * 50)
    print(f"Tests passed: {passed}/{total}")

    if passed == total:
        print("🎉 All tests passed! Development environment is ready.")
        print("\nYou can now use:")
        print("  python scripts/quick_test.py    # Quick functionality test")
        print("  python scripts/dev_shell.py     # Start IPython with modules")
        print("  uv run python scripts/dev_shell.py  # Using uv environment")
    else:
        print("❌ Some tests failed. Please check the errors above.")

    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

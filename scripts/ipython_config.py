"""
IPython configuration for cn_stock_holidays development.

This file provides custom IPython settings and startup commands
for a better development experience.

Usage:
    ipython --profile=cn_stock_holidays
    # or
    ipython -c "exec(open('scripts/ipython_config.py').read())"
"""

import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# IPython configuration
try:
    c = get_config()
except NameError:
    # This file is meant to be executed in IPython context
    # where get_config() is available
    print("This file should be executed in IPython context")
    c = None

# Enable auto-reload for development
c.InteractiveShellApp.exec_lines = [
    "%load_ext autoreload",
    "%autoreload 2",
    'print("=== cn_stock_holidays Development Environment ===")',
    'print("Auto-reload enabled for development")',
    'print("Available modules:")',
    'print("  - cn_stock_holidays.data (Mainland China)")',
    'print("  - cn_stock_holidays.data_hk (Hong Kong)")',
    'print("  - cn_stock_holidays.common (Utilities)")',
    'print("  - cn_stock_holidays.meta_functions (Cache)")',
    "print()",
]

# Import commonly used modules
c.InteractiveShellApp.exec_lines.extend(
    [
        "import cn_stock_holidays",
        "import cn_stock_holidays.data as data",
        "import cn_stock_holidays.data_hk as data_hk",
        "import cn_stock_holidays.common as common",
        "import cn_stock_holidays.meta_functions as meta",
        "",
        "# Import commonly used functions",
        "from cn_stock_holidays.data import is_trading_day, is_holiday, trading_days_between, get_trading_days",
        "from cn_stock_holidays.data_hk import is_trading_day as is_trading_day_hk, is_half_day_trading_day",
        "from cn_stock_holidays.common import parse_date, format_date, is_weekend",
        "from cn_stock_holidays.meta_functions import get_cache_info, clear_cache",
        "",
        'print("All modules imported successfully!")',
        'print("Try: help(data) or help(data_hk) for more information")',
        "print()",
    ]
)

# Enable rich display
c.InteractiveShell.ast_node_interactivity = "all"

# Enable auto-completion
c.IPCompleter.use_jedi = True
c.IPCompleter.greedy = True

# Set up aliases for common operations
c.AliasManager.user_aliases = [
    ("test", "python scripts/quick_test.py"),
    ("shell", "python scripts/dev_shell.py"),
    ("cache", "get_cache_info()"),
    ("clear-cache", "clear_cache()"),
    ("hk-test", 'is_trading_day_hk("2024-12-24")'),
    ("cn-test", 'is_trading_day("2024-01-01")'),
]

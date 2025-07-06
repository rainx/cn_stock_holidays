# UV Package Manager Guide

This project now supports [uv](https://github.com/astral-sh/uv), a fast Python package installer and resolver.

## Installation

First, install uv:

```bash
# macOS and Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Or using pip
pip install uv
```

## Quick Start

### Install dependencies

```bash
uv sync
```

### Install in development mode

```bash
uv sync --dev
```

### Run tests

```bash
uv run pytest
```

### Run the CLI tool

```bash
uv run get-day-list --help
```

### Install the package

```bash
uv pip install -e .
```

## Common Commands

### Development

```bash
# Install all dependencies including dev tools
uv sync --dev

# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov=cn_stock_holidays

# Format code
uv run black .

# Sort imports
uv run isort .

# Type checking
uv run mypy cn_stock_holidays/

# Linting
uv run flake8 cn_stock_holidays/
```

### Package Management

```bash
# Add a new dependency
uv add package-name

# Add a development dependency
uv add --dev package-name

# Remove a dependency
uv remove package-name

# Update dependencies
uv sync --upgrade
```

### Building and Publishing

```bash
# Build the package
uv build

# Build and publish to PyPI
uv publish
```

## Benefits of UV

1. **Speed**: UV is significantly faster than pip and other package managers
2. **Reliability**: Better dependency resolution and lock file management
3. **Modern**: Uses `pyproject.toml` as the standard configuration format
4. **Compatible**: Works with existing Python tooling and workflows
5. **Cross-platform**: Works on Windows, macOS, and Linux

## Migration from setup.py

The project now uses `pyproject.toml` instead of `setup.py`. The `setup.py` file has been removed as it's no longer needed. This provides:

- Better dependency specification
- Modern Python packaging standards
- Improved tool integration
- More flexible configuration
- Cleaner project structure

## CI/CD Integration

Update your GitHub Actions workflow to use uv:

```yaml
- name: Install uv
  uses: astral-sh/setup-uv@v1

- name: Install dependencies
  run: uv sync --dev

- name: Run tests
  run: uv run pytest
```

## Troubleshooting

### Common Issues

1. **UV not found**: Make sure uv is installed and in your PATH
2. **Lock file conflicts**: Delete `uv.lock` and run `uv sync` again
3. **Permission errors**: Use `uv sync --no-cache` to bypass cache issues

### Getting Help

- [UV Documentation](https://docs.astral.sh/uv/)
- [UV GitHub Repository](https://github.com/astral-sh/uv)
- [UV Discord Community](https://discord.gg/astral-sh)

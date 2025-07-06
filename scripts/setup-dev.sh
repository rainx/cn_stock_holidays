#!/bin/bash

# Setup development environment with uv

echo "Setting up development environment with uv..."

# Check if uv is installed
if ! command -v uv &>/dev/null; then
    echo "uv is not installed. Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc # or source ~/.zshrc for zsh
fi

# Install dependencies
echo "Installing dependencies..."
uv sync --dev

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
uv run pre-commit install

# Run initial tests
echo "Running initial tests..."
uv run pytest

echo "Development environment setup complete!"
echo ""
echo "Common commands:"
echo "  uv run pytest          # Run tests"
echo "  uv run black .         # Format code"
echo "  uv run isort .         # Sort imports"
echo "  uv run mypy cn_stock_holidays/  # Type checking"
echo "  uv run flake8 cn_stock_holidays/  # Linting"

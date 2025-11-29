.PHONY: help install run dev format lint

# Default target
help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies"
	@echo "  make run        - Run the Streamlit app"
	@echo "  make dev        - Run the Streamlit app in development mode (auto-reload)"
	@echo "  make format     - Format code with ruff"
	@echo "  make lint       - Lint code with ruff"

install:
	uv sync

run:
	uv run streamlit run main.py

dev:
	uv run streamlit run main.py --server.runOnSave true

format:
	uv run ruff format .

lint:
	uv run ruff check .
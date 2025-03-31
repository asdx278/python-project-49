install:
	uv sync

brain-games:
	uv run brain-games

build:
	uv build

package-install:
	uv tool install dist/*.whl

package-install-force:
	uv tool install --force dist/hexlet_code-0.4.0-py3-none-any.whl

lint:
	uv run ruff check brain_games
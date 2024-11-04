all: install transform serve

install:
	@cd transform && uv sync
	@cd transform/reports && npm install

transform:

	@cd transform && uv run sqlmesh plan
	@cp transform/db.db transform/reports/sources/uyv/db.db

serve:
	@cd transform/reports && npm run dev

explore:
	@cd explore && uv sync &&uv run marimo edit app.py

clean:
	@rm -rf transform/db.db
	@rm -rf transform/reports/node_modules
	@rm -rf explore/__pycache__
	@rm -rf explore/.venv


.PHONY: install transform serve clean
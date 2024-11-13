all: install refresh

refresh: transform serve

install:
	@cd transform && uv sync
	@cd transform/reports && npm install

transform:
	@cd transform && uv run sqlmesh run

serve:
	@cp transform/db.db transform/reports/sources/uyv/db.db
	@cd transform/reports && npm run dev

explore:
	@cd explore && uv sync &&uv run marimo edit app.py

clean:
	@rm -rf transform/db.db
	@rm -rf explore/__pycache__
	@rm -rf transform/logs
	@rm -rf transform/.cache


.PHONY: install transform serve clean
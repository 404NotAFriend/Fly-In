MAIN := src/main.py
VENV := venv
VENV_BIN := $(VENV)/bin
PYTHON := $(VENV_BIN)/python3
PIP = $(VENV_BIN)/python3 -m pip


$(VENV_BIN)/activate:
	python3 -m venv $(VENV)

install: $(VENV_BIN)/activate
	@$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAIN)

debug:
	$(PYTHON) -m pdb $(MAIN)

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache

lint:
	$(VENV_BIN)/flake8 .
	$(VENV_BIN)/mypy . \
	--warn-return-any \
	--warn-unused-ignores \
	--ignore-missing-imports \
	--disallow-untyped-defs \
	--check-untyped-defs

lint-strict:
	$(VENV_BIN)/flake8 .
	$(VENV_BIN)/mypy . --strict

.PHONY: install run debug lint lint-strict

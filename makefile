PYTHON = python3
SCRIPT = a_maze_ing.py
CONFIG = config.txt

install:
	pip install -r requirements.txt

run:
	$(PYTHON) $(SCRIPT) $(CONFIG)

debug:
	$(PYTHON) -m pdb $(SCRIPT) $(CONFIG)

clean:
	rm -rf __pycache__ .mypy_cache
	rm -rf */__pycache__
	rm -rf build dist *.egg-info

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs


lint-strict:
	flake8 .
	mypy . --strict

.PHONY: install run debug clean lint lint-strict

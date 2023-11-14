venv:
	test -d venv || python3 -m venv venv

init: venv
	. venv/bin/activate && python -m pip install -r requirements.txt

black:
	. venv/bin/activate && black --line-length=160 .

mypy:
	. venv/bin/activate && MYPYPATH=. mypy --config-file setup.cfg --show-error-codes .

mypy-strict:
	. venv/bin/activate && MYPYPATH=. mypy --config-file setup.cfg --strict --show-error-codes --check-untyped-defs .

pylint:
	. venv/bin/activate && pylint src/ test/

flake8:
	. venv/bin/activate && flake8 src/ test/ --count --show-source --statistics

tests:
	. ./venv/bin/activate && PYTHONPATH=src/ python -m pytest test

check: flake8 pylint mypy-strict

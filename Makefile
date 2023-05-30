install:
		pip install -U pip && pip install -Ur requirements.txt
test:
		python -m pytest
format:
		isort --atomic .
		black *.py
lint:
		pylint --disable=R,C main.py

all: install test format lint
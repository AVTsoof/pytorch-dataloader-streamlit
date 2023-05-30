install:
		pip install -U pip && pip install -Ur requirements.txt
test:
		python -m pytest
format:
		isort --atomic .
		black .
lint:
		pylint --disable=R,C **/*.py

all: install test format lint
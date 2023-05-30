install:
		pip install -U pip && pip install -Ur requirements.txt
test:
		pip install -U pytest
		python -m pytest
format:
		pip install -U isort black
		isort --atomic .
		black .
lint:
		pip install -U pylint
		pylint --disable=R,C **/*.py

all: install test format lint
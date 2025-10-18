# Makefile for Roulette Simulator Project

.PHONY: install lint format test coverage clean all

#Setup
install:
	pip install --upgrade pip
	pip install -r requirements.txt

#Code Quality
lint:
	pylint *.py

format:
	black *.py

#Testing
test:
	pytest --disable-warnings
	pytest -v

coverage:
	coverage run -m pytest
	coverage report -m

#Maintenance 
clean:
	rm -rf __pycache__ .pytest_cache .coverage htmlcov

# All-in-one
all: install lint test coverage

ex_ins: lint format test coverage

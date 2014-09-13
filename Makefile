MODULES=colorize

all: flakes test

test:: clear_coverage run_unit_tests run_integration_tests run_acceptance_tests

unit_test:: run_unit_tests

acceptance_test:: run_acceptance_tests

analysis:: pep8 flakes

flakes:
	@echo Searching for static errors...
	@flake8 --statistics --count ${MODULES}

coveralls::
	coveralls

publish::
	@python setup.py sdist bdist_egg bdist_wheel
#	@zip dist/colorize-$(shell python -c "import colorize; print colorize.__version__").zip colorize __main__.py

run_unit_tests:
	@echo Running Tests...
	@nosetests -dv --exe --with-xcoverage --cover-package=${MODULES} --cover-tests tests/unit  ${NOSE_OPTS}

run_integration_tests:
	@echo Running Tests...
	@nosetests -dv --exe --with-xcoverage --cover-package=${MODULES} --cover-tests tests/integration  ${NOSE_OPTS}

run_acceptance_tests:
	@echo Running Tests...
	@nosetests -dv --exe tests/acceptance  ${NOSE_OPTS}

clear_coverage:
	@echo Cleaning previous coverage...
	@coverage erase

PROJECT_NAME = promlab
TEST_FOLDER = tests
APPLICATION = promlab.main:app

.PHONY:default
default: help

.PHONY: help
help:
	@echo "	Env:"
	@echo "		run - Run application in development mode."

.PHONY: run
run:
	uvicorn $(APPLICATION) --reload

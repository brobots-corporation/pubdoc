
.PHONY: prepare_venv install run dist

include .dev.env

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python

prepare_venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: requirements.txt
	test -d $(VENV_NAME) || python -m venv $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r requirements.txt
	touch $(VENV_NAME)/bin/activate

install: prepare_venv
	
run: prepare_venv	
	${PYTHON} -m pubdoc dokuwiki --target ${PUBDOC_DOKUWIKI_TARGET} \
								--username ${PUBDOC_DOKUWIKI_USERNAME} \
								--password ${PUBDOC_DOKUWIKI_PASSWORD} \
								 --namespace 'Проект 2:Техническая документация' \
								 --data-dir './testdocs' \


dist:
	${PYTHON} setup.py sdist bdist_wheel
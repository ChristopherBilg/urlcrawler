#!/bin/bash

echo "Starting lint on crawl.py"
pylint crawl.py --score=no
pycodestyle crawl.py
flake8 crawl.py

echo "Starting lint on search.py"
pylint search.py --score=no
pycodestyle search.py
flake8 search.py

echo "Starting lint on test.py"
pylint test.py --score=no
pycodestyle test.py
flake8 test.py

echo "Finished linting all files"

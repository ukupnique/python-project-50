install:
	poetry install

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

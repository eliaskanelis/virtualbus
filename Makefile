.PHONY: pyblish
publish:
	rm -rf MANIFEST
	rm -rf dist
	python setup.py sdist

	twine upload dist/*

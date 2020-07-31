.PHONY: package
package:
	@./setup.py sdist

.PHONY: clean
clean:
	rm -rf MANIFEST
	rm -rf dist
	py3clean .

.PHONY: publish
publish: clean package
	twine upload dist/*


.PHONY: publish_test
publish_test: clean package
	twine upload --repository testpypi dist/*

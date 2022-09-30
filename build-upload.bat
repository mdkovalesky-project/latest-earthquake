@echo off
rmdir dist /A /Q
py -m build
py -m twine upload --repository pypi dist/*
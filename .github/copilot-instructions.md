# Style
Create within a python package style
* Use absolute imports for internal modules
* Create code inside the src directory

# Dependency Management
Whenever you add a new dependency, make sure to:
* Update the `install_requires` list in `setup.py`
* Run `pip install -e .` to install the new dependency in editable mode
* Update the `pyproject.toml` file
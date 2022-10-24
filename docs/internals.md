# Internals

Some notes on the internals of the package


## Packaging and installing

I am now using the modern form of [SetupTools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) which means everything is in `pyproject.toml`.

To **build** we run `python -m build`

To perform a **local install** run `pip install dist\ma2812-0.1.0-py3-none-any.whl --force-reinstall`

# Python Test

```bash
# Install
python -m vnv .YOUR_DIRECTORY_NAME
source .YOUR_DIRECTORY_NAME/bin/env # Linux

pip install flask pytest
pip freeze > requirements.txt
```

## Test Coverage

```bash
# Install
pip install pytest-cov
pip freeze > requirements.txt

# Run test
pytest --cov-report term --cov=YOUR_APP_NAME tests/
pytest --cov-report term --cov=app tests/

# Run missing tests
pytest --cov-report term-missing --cov=app tests/

# Generate a Report in HTML
# this will create a directory in the root of your project called "htmlcov"
pytest --cov-report html --cov=app tests/
```

When installed `flask`, `pytest`, and `pytest-cov`; they install a bunch of "unnecessary packages", like `bcc`

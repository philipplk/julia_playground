## Python environment with venv

Create

```bash
python -m venv .venv # naming the new environment ".venv" is convention
```

Activate

```bash
source .venv/bin/activate
```

### Keeping track of requirements / packages

Let's manually keep a list of all required packages in file `requirements.txt`.
You can install all requirements defined in `requirements.txt` with

```bash
pip install -r requirements.txt
```

Let's freeze all details on specific version numbers of the packages within our environment into a file `requirements_developer.txt` with

```bash
pip freeze > requirements_developer
```

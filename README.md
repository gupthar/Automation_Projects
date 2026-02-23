# Automation Project Repo

Quickstart
```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

To generate Allure reports after running tests:
Append this to the run command: --alluredir=allure-results
allure serve allure-results
# pytools-pipenv
[![Build Status](https://app.travis-ci.com/mauriciodoerr/pytools-pipenv.svg?branch=main)](https://app.travis-ci.com/mauriciodoerr/pytools-pipenv)
[![codecov](https://codecov.io/gh/mauriciodoerr/pytools-pipenv/branch/main/graph/badge.svg?token=XO14YR0VF0)](https://codecov.io/gh/mauriciodoerr/pytools-pipenv)
[![Updates](https://pyup.io/repos/github/mauriciodoerr/pytools-pipenv/shield.svg)](https://pyup.io/repos/github/mauriciodoerr/pytools-pipenv/)
[![Python 3](https://pyup.io/repos/github/mauriciodoerr/pytools-pipenv/python-3-shield.svg)](https://pyup.io/repos/github/mauriciodoerr/pytools-pipenv/)

Upgrade original project [GitHub Repo](https://github.com/mauriciodoerr/pytools) from pip + venv to pipenv

#### Make sure you are using pyenv and check for python not being the one for your SO but the one isolated via pyenv
```console
pyenv which python
```

## Install PipEnv
```console
pip install pipenv
```

Check for installation by executing
```console
pipenv
```

After that, make sure to change venv setup dir to be created within project files, otherwise it will be created in a system path chosen by pipenv.
> For ARM OSX is .zprofile which is the same as .bash_profile
```console
cd ~
vi .zprofile
```
Right under the line 'export PATH' include
```console
export PIPENV_VENV_IN_PROJECT=1
```
Save the file and execute:
```console
source .zprofile
echo $PIPENV_VENV_IN_PROJECT
```
The output should be 1

#### Installing PipEnv including lib requests
```console
pipenv install requests
```

#### Install Dev Dependencies
```console
pipenv install -d flake8 pytest coverage pytest-cov pytest-mock
```
Check if everything is ok by executing flake8 from pipenv
```console
pipenv run flake8
```

# pytools-pipenv
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
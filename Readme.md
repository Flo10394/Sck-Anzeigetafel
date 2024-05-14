# Python setup
1. Configure poetry:  
1.1 ```poetry config virtualenvs.in-project true```  
1.2 ```poetry config virtualenvs.prefer-active-python true```
2. Install pyenv-win:  
```Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"```
3. Install python and activate it for local folder:  
```pyenv install 3.12.3-win32```  
```pyenv local 3.12.3-win32 ```
4. Setup poetry venv:  
```poetry install```
5. Install some local packages (poetry error):  
5.1 ```poetry run pip install PyQt5```
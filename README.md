## explorer


> A simple python cli file browser

![a](https://img.shields.io/pypi/v/file-explorer?style=flat-square)

![gif.gif](https://i.loli.net/2019/10/30/yCE6UJ3sDFBTYcG.gif)

## usage

### quick start
```
pip3 install file-explorer
explorer ./ none
```
### command
`explorer path list`
- path: a path browser start to show
- list: suffix list
  - `none` : show all file
  - `.py`: show python file
  - `.py/.yml`: show python and yaml file
## deveolp

### clone source code to your computer
```
git clone https://github.com/WangTingZheng/explorer.git
cd explorer
pip3 install -r  requirements.txt
```
### edit suffix list in `run.py`
```python
from explorer.menu import *
lists=[".py"]
menu("./",lists)
```
`lists` is a setting list to let cli display the file you want. `lists=['.py']` means only display python file and folder that have python file, `[]` means display all

### run

``
python run.py
``
- Press `j` to move up
- Press `k` to move down
- Press `space` to select and deselect
- Press `enter` to confirm
## To-Do
- deal function design for different file
- ignore list




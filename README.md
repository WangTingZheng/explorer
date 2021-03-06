# <p align="center">📂explorer:  a simple python cli file browser</p>


<p align="center">
     <a href="">
        <img src="https://img.shields.io/pypi/v/file-explorer?style=flat-square">
    </a>
    <a href="">
        <img src="https://img.shields.io/badge/updating-brightgreen.svg">
    </a>
    <a href="https://github.com/python/cpython">
        <img src="https://img.shields.io/badge/Python-3.7.4-blue.svg">
    </a>
    <a href="https://github.com/WangTingZheng/explorer">
    <img src="https://img.shields.io/github/stars/WangTingZheng/explorer.svg?style=social">
        </a>
</p>
<p align="center">
    <a href="">
        <img src="https://i.loli.net/2019/10/31/y8ZrdnUbVSkAz2G.gif">
    </a>
</p>

## Usage

### quick start
```
pip3 install file-explorer
explorer ./ none
```
### commander
`explorer path list`
- path: a path browser start to show
- list: suffix list
  - `none` : show all file
  - `.py`: show python file
  - `.py/.yml`: show python and yaml file
## Develop

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
- deal with permission denied bug

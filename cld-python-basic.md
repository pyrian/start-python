# 1. 환경 설정
## python 설치 (https://www.python.org/downloads)
* python3 path 및 alias 추가 (.bash_profile 또는 .bashrc)

```
# python3 path 설정
PATH="/Library/Frameworks/Python.framework/Versions/3.6/bin:${PATH}"
export PATH

alias python=python3
alias pip=pip3
```
## pip, setuptools, easy_install
pip와 easy_installd은 PyPI(Python package Index)라는 패키지 저장소에서 패키지를 설치할 수 있게 해주는 Tool

* [pip vs easy_install](https://packaging.python.org/pip_easy_install/)


## virtualenv, virtualenvwrapper
프로젝트별로 분리된 가상 환경을 만들고, 필요한 패키지들을 관리할 수 있게 해주는 툴
#### 설치
```
$ pip install virtualenv
```
#### 기본 사용법
```
# 1. 가상환경 생성
$ cd my_project_folder
$ virtualenv my_project

# 2. pyhton interpreter
$ virtualenv -p /usr/bin/python3.6 my_project
또는
$ export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3.6

$ source my_project/bin/activate

$ deactivate
```

## IPython notebook
IPython notebook은 Jupyter Notebook으로 알려져 있으며, interactive computational 환경 제공

#### 사용
```
$ pip install jupyter

$ jupyter notebook
```

# 2. 기초 문법
* code fight -> arcade
* jarvis : https://pythonspot.com/en/personal-assistant-jarvis-in-python/
* requests, beautifulsoup

## 참고
* [Python package 관련 용어](https://packaging.python.org/glossary)
* [pip vs easy_istall](https://packaging.python.org/pip_easy_install/)
* [Python 환경설정](http://www.flowdas.com/blog/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-virtualenv/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [IPython notebook](https://jupyter.readthedocs.io/en/latest/running.html)
* [Fullstack development python](https://www.fullstackpython.com/application-dependencies.html)

# NLP-Moses deep learning base

This AI deep learn framework requires python 3.6>=.
To use this repo, first `git clone` repo. Then use your OS's python 3 version to establish a virtual environment:

`python -m venv venv`

or if your system uses both python2 and python3:

`python3 -m venv venv`

Once your virtual environment is setup, proceed to activate it (Linux/OSX): 

`source venv/bin/activate`

once your virtual environment is on, its time to start installing the dependancies. The following dependancies needed for using this framework is `numpy` and `tensorflow`. Additionally, this repo includes jupytar notebooks for easy learning and understanding. 

```
pip install numpy
pip install tensorflow
pip install notebook    ## jupyter-notebook

```

@NOTE: to activate jupyter notebook within a python virtual environment remember that you have to activate it via the bin directory in your venv directory:

`venv/bin/jupyter-notebook` 
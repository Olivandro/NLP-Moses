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

### Creating venv for specific Python version

If you are looking to establish a virtual environment that has a specific Python version outside of your System OS's version, you will need to install `virtualenv` globally on your system. This package has similar functionality to `venv`, however where they differ is that `virtualenv` allows for you to flag option `--python=PYTHON-VERSION`.

Please note, you must have the specific Python version binary installed on your computer, or you will receive an error message from `virtualenv` indicating that the path to the version you've specified does not exsit.

### @NOTE 

to activate jupyter notebook within a python virtual environment remember that you have to activate it via the bin directory in your venv directory:

`venv/bin/jupyter-notebook` 

Another note to make is that to preview the sorting of the sample data within jupyter notebook you will have to change your systems jupyter notebook configs to allow for large data sets to `print()`. The benefit for changing this config is to allow Jupyter notebook to preview your sorted data, to understand is you are sorting and formatting it correctly for the deep learning process. 
*WARNING!!* If you computer or system is old, not powerful enough, has a tendency to freeze with loading large file do not do this change of configs... you will crash your system. 

```
## If you do not have a jupyter config file use the below command to generate one
$ jupyter notebook --generate-config

## once generated use your perferred text editor and open this new config file and search
c.NotebookApp.iopub_data_rate_limit

## this config should be commented out. Uncomment and change from default
c.NotebookApp.iopub_data_rate_limit = 1000000 

## to
c.NotebookApp.iopub_data_rate_limit = 10000000
```
# KEEP Training Installation
### Table of Contents
1. [Introduction](#Introduction)
2. [Software Prerequisites](#SoftwarePrerequisites)
3. [Package Versions](#PackageVersions)
4. [Prerequisite Installation](#PrerequisiteInstallation)
5. [Installation From Scratch](#InstallFromScratch)

### <a id="Introduction">Introduction</a>
Below you will find the instructions on the installation of the Jupyter Notebook application responsible for training the neural network model used within KEEP. For the purpose of this tutorial all software and package prerequisites will be listed, and it will be assumed you are using the same versions. You may attempt installation using differing versions, but results may vary.

For many of the installation steps you should be familiar with using a command shell (CMD, PowerShell, Bash or equivalent).

### <a id="SoftwarePrerequisites">Software Prerequisites</a>
1. [Python](https://www.python.org/downloads/) = 3.8.5
2. [Visual Studio Build Tools 2019](https://visualstudio.microsoft.com/downloads/) (C++ Build Tools)

### <a id="PackageVersions">Package Versions</a>
1. [Virtualenv](https://pypi.org/project/virtualenv/) = 20.0.31 (Allows the creation of python virtual environments)
1. [Pytorch](https://pytorch.org/get-started/locally/) = 1.6.0 (Contains data structures for multi-dimensional tensors and mathematical operations)
2. [TorchVision](https://pytorch.org/get-started/locally/) = 0.7.0 (Package of commonly used datasets, model architectures and image transformations for computer vision)
3. [Fastai](https://fastai1.fast.ai/install.html) = 1.0.61 (Simplified API for Pytorch)
4. [SpaCy](https://spacy.io/) = 2.3.2 (Natural language processing software library)
5. [Scikit-learn](https://scikit-learn.org/stable/) = 0.23.2 (Machine learning software library)
6. [Pyodbc](https://pypi.org/project/pyodbc/) = 4.0.30 (Facilitates the access of ODBC databases)
7. [Xlrd](https://pypi.org/project/xlrd/) = 1.2.0 (Allows extraction of excel spreadsheet data)
8. [Jupyter](https://jupyter.org/) = 1.0.0 (Allows for the creation and sharing of documents that contain live code and markup)

### <a id="PrerequisiteInstallation">Prerequisite Installation</a>
Please refer to the [Prerequisite Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PrerequisiteInstallation.md) guide for details.

### <a id="InstallFromScratch">Installation From Scratch</a>
1. Begin with the [Prerequisite Installation](#PrerequisiteInstallation)
2. Create a folder to act as the root directory for KEEP and navigate to this folder in your shell
> Note: Ensure your shell is running in administrator mode or equivalent
```
cd path/to/folder
```
3. Install `virtualenv` using pip
```
pip install virtualenv
```
4. Create a `virtual python environment` to contain Python dependancies using the following command
> Note: A `virtual python environment` allows us to keep all our installed packages and dependancies local to the project we're working on, effectively allowing us to install different versions of packages for different projects without interference.
```
virtualenv ENVName-env (Replace ENVName-env with anything you'd like)
```
5. Activate the virtual environment you just created in order to start installing required packages
> Note: You will need to activate this virtual environment every time you want to work with this project from the cmd line or shell, you can deactive the environment when finished with the `deactivate` command.
```
.\ENVName-env\Scripts\activate
```
The output in the shell windows should now be prefaced with the environment name in brackets:
```
(ENVName-env) C:\Some\path>
```
6. Before we begin installing the required packages we need to upgrade the pip installer with the following command
```
python -m pip install --upgrade pip
```
7. Now we are ready to begin installing our required packages. First we'll install Pytorch
> Please refer to the [Pytorch Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PytorchInstallation.md) guide for details.
8. Verify Pytorch installation by first entering a Python shell using the following command
```
python
```
and run the following commands
```
>>> from __future__ import print_function
>>> import torch
>>> x = torch.rand(5, 3)
>>> print(x)
```
The output should look similar to the follow:
```
tensor([[0.3380, 0.3845, 0.3217],
        [0.8337, 0.9050, 0.2650],
        [0.2979, 0.7141, 0.9069],
        [0.1449, 0.1132, 0.1375],
        [0.4675, 0.3947, 0.1426]])
```
Additionally, if you installed Pytorch with CUDA, you can check if your GPU driver and CUDA are installed and accessible using the following command, which should return `True`. **If you chose not to install Pytorch with CUDA, skip this step.**
```
torch.cuda.is_available()
```
Once verified we can exit our Python shell
```
>>> exit()
```
9. Install Fastai 1.0.61 **(with your python virtual environment activated)**
```
pip install fastai==1.0.61
```
10. Install SpaCy 2.3.2 **(with your python virtual environment activated)**
```
pip install spacy==2.3.2
```
11. Install Scikit-learn 0.23.2 **(with your python virtual environment activated)**
```
pip install scikit-learn==0.23.2
```
12. Install Pyodbc 4.0.30 **(with your python virtual environment activated)**
```
pip install pyodbc==4.0.30
```
13. Install Xlrd 1.2.0 **(with your python virtual environment activated)**
```
pip install xlrd==1.2.0
```
14. Install Jupyter 1.0.0 **(with your python virtual environment activated)**
```
pip install jupyter==1.0.0
```
15. With the installation of the packages now complete, we can set a password for Jupyter to use using the following command
> Note: Jupyter will display where it has stored your hashed password. Make a mental note of this location, as it is the same location where Jupyter configuration files will be stored by default.
```
jupyter notebook password
```
16. Start jupyter server and log in with the password you created to verify installation
```
jupyter notebook
```
After running this command you should be redirected to a browser window automatically displaying the main jupyter homepage.

17. KEEP Training is now successfully installed. For instruction on how to create and run notebooks in Jupyter refer to the [KEEP Training Operation Manual](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/KEEPTrainingOperationManual.md)

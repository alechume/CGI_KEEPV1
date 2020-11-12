# KEEP Training Installation
### Table of Contents
1. [Introduction](#Introduction)
2. [Software Prerequisites](#SoftwarePrerequisites)
3. [Package Versions](#PackageVersions)
4. [Prerequisite Installation](#PrerequisiteInstallation)
5. [Building the Directory Structure](#DirectoryStructure)
6. [Installation From Scratch](#InstallFromScratch)
7. [Jupyter Configuration](#JupyterConfiguration)

### <a id="Introduction">Introduction</a>
Below you will find the instructions on the installation of the Jupyter Notebook application responsible for training the neural network model used by **KEEP App**. For the purpose of this tutorial, all software and package prerequisites will be listed, and it will be assumed you are using the same versions. You may attempt installation using differing versions, but results may vary.

It will also be assumed you are using the same directory structure for the project as described below. You may attempt to use a different directory structure, but you will need to be able to modify file-paths accordingly.

For many of the installation steps you should be familiar with using a command shell (cmd prompt, PowerShell, Bash or equivalent)

**WARNING:** Following this guide will not create a secure server and should only be used for accessing Jupyter **locally**. If you would like to learn how to secure your Jupyter server, refer to the [official documentation](https://jupyter-notebook.readthedocs.io/en/stable/public_server.html)

### <a id="SoftwarePrerequisites">Software Prerequisites</a>
1. [Python](https://www.python.org/downloads/) = 3.8.5
2. [Visual Studio Build Tools 2019](https://visualstudio.microsoft.com/downloads/) (C++ Build Tools)

### <a id="PackageVersions">Package Versions</a>
1. [Virtualenv](https://pypi.org/project/virtualenv/) = 20.0.31 (Allows the creation of python virtual environments)
2. [Pytorch](https://pytorch.org/get-started/locally/) = 1.6.0 (Contains data structures for multi-dimensional tensors and mathematical operations)
3. [TorchVision](https://pytorch.org/get-started/locally/) = 0.7.0 (Package of commonly used datasets, model architectures and image transformations for computer vision)
4. [Fastai](https://fastai1.fast.ai/install.html) = 1.0.61 (Simplified API for Pytorch)
5. [SpaCy](https://spacy.io/) = 2.3.2 (Natural language processing software library)
6. [Scikit-learn](https://scikit-learn.org/stable/) = 0.23.2 (Machine learning software library)
7. [Pyodbc](https://pypi.org/project/pyodbc/) = 4.0.30 (Facilitates the access of ODBC databases)
8. [Xlrd](https://pypi.org/project/xlrd/) = 1.2.0 (Allows extraction of excel spreadsheet data)
9. [Jupyter](https://jupyter.org/) = 1.0.0 (Allows for the creation and sharing of documents that contain live code and markup)

### <a id="PrerequisiteInstallation">Prerequisite Installation</a>
Please refer to the [Prerequisite Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PrerequisiteInstallation.md) guide for details.

### <a id="DirectoryStructure">Building the Directory Structure</a>
**KEEP Training's** directory structure will consist of a single **root** directory to act as a container, and 2 sub-directories, 1 containing the python virtual environment and 1 containing the Jupyter Notebook `.ipynb` folders and files.
1. Begin with the [Prerequisite Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PrerequisiteInstallation.md)
2. Create a folder named `KEEPTraining` that will act as our **root** directory
3. Inside the **root** directory, create a new folder named `Notebooks`
4. Open your **command shell** and navigate to the inside of the **root** directory in your shell
> Note: Ensure your shell is running in administrator mode or equivalent
5. Create a `virtual python environment` to contain Python dependancies using the following command
> Note: A `virtual python environment` allows us to keep all of our installed packages and dependancies local to the project we're working on, effectively allowing us to install different versions of packages for different projects without interference.
```
virtualenv KEEPTraining-env (You may replace KEEPTraining-env with anything you'd like)
```
6. Your directory structure should now match the following:
```
└── KEEPTraining            # Root directory
    ├── KEEPTraining-env    # Virtual python environment
    └── Notebooks           # Jupyter ipynb folder
```
7. You are now ready to begin [Installation From Scratch](#InstallFromScratch)

### <a id="InstallFromScratch">Installation From Scratch</a>
1. Open your **command shell** and navigate to the inside of the **root** directory
2. Activate the **virtual environment** you created in order to start installing the required packages
> Note: You will need to activate this virtual environment every time you want to work with this project, you can deactivate the environment when finished with the `deactivate` command
```
.\KEEPTraining-env\Scripts\activate
```
The output in your shell should now be prefaced with the environment name in brackets:
```
(KEEPTraining-env) C:\Some\path>
```
3. Before we begin installing the required packages we need to upgrade the pip installer with the following command
```
python -m pip install --upgrade pip
```
4. Now we are ready to begin installing our required packages. First we'll install Pytorch
> Please refer to the [Pytorch Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PytorchInstallation.md) guide for details
5. Verify Pytorch installation by first entering a Python shell using the following command
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
6. Install Fastai 1.0.61
```
pip install fastai==1.0.61
```
7. Install SpaCy 2.3.2
```
pip install spacy==2.3.2
```
8. Install Scikit-learn 0.23.2
```
pip install scikit-learn==0.23.2
```
9. Install Pyodbc 4.0.30
```
pip install pyodbc==4.0.30
```
10. Install Xlrd 1.2.0
```
pip install xlrd==1.2.0
```
11. Install Jupyter 1.0.0
```
pip install jupyter==1.0.0
```
12. With the installation of the packages now complete, we can set a password for Jupyter to use. Run the following command and follow the on-screen prompts
> Note: Jupyter will display where it has stored your hashed password. Make a mental note of this location, as it is the same location where Jupyter configuration files are stored
```
jupyter notebook password
```
13. Navigate to the inside of the **Notebooks** folder located in the **root** of the **KEEP Training** project
```
cd Notebooks
```
14. Start the Jupyter server and log in with the password you created to verify installation
```
jupyter notebook
```
After running this command you should be redirected to a browser window automatically displaying the main Jupyter homepage.

15. **KEEP Training** is now successfully installed. In the next section we will cover some **optional** configuration settings for the Jupyter server. If you would rather skip the **optional** configuration, you may now refer to the [KEEP Training Operation Manual](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/KEEPTrainingOperationManual.md) for how to create and run notebooks in Jupyter

### <a id="JupyterConfiguration">Jupyter Configuration</a>
In this section we will cover some basic Jupyter server configuration settings. All of the settings mentioned are **optional** and only provide quality-of-life improvements. First we will cover how to generate the configuration file, and then go over some of the options you may want to modify.
1. Generate the configuration file
	1. Open your **command shell** and navigate to the inside of the **root** directory of the **KEEP Training** project
	2. Activate the **KEEP Training virtual environment**
	```
	.\KEEPTraining-env\Scripts\activate
	```
	3. Generate the Jupyter configuration file using the following command
	```
	jupyter notebook --generate-config
	```
	4. Once Jupyter has finished generating the configuration it will display the location where it has been stored, navigate to this location and open the **jupyter_notebook_config.py** file in a text editor
	> Note: If you created a password during installation, this folder will also contain a jupyter_notebook_config.json file. This file stores the hashed password and should not be confused with the main config file which ends with `.py`
	5. Next we will find and modify several configuration settings. For each setting you will need to **un-comment** the line first, before making changes. **Hint: using the search function of your text editor will make finding the configuration settings much easier**
	6. Find each setting listed under the **Setting** heading of the following table and change the argument to match whatever is under the **Arugment** heading.
	> Note: The argument is everything after the "="" sign

	| Setting                                       | Arugment                          |
	| --------------------------------------------- | ----------------------------------|
	| c.NotebookApp.notebook_dir = ''               | = 'Full path to Notebooks folder' |
	| c.NotebookApp.open_browser = True             | = False                           |
	| c.NotebookApp.quit_button = True              | = False                           |
	| c.NotebookApp.terminals_enabled = True        | = False                           |

	<dl>
		<dt>c.NotebookApp.notebook_dir</dt>
		<dd>Specifies the full path to the main startup directory for the Jupyter application. This should be set to our Notebook directory we created during installation, located within the root of the KEEP Training project. For example "C:\\Users\\alec.hume\\Documents\\GitHub\\CGI_KEEPV1\\KEEPTraining\\Notebooks". </dd>
		<dt>c.NotebookApp.open_browser</dt>
		<dd>Specifies whether or not to open a browser automatically when the server first starts.</dd>
		<dt>c.NotebookApp.quit_button</dt>
		<dd>Allows us to enable or disable the Quit button on the Jupyter browser UI. If left enabled, a user could shut the Jupyter server down remotely from the UI.</dd>
		<dt>c.NotebookApp.terminals_enabled</dt>
		<dd>By default Jupyter allows the use of in-browser terminals. This setting simply disables that functionality, this does not make the server more secure, since everything that could otherwise be done in a terminal can be done in a notebook.</dd>
	</dl>

	For more configuration options and a more detailed explanation of the above mentioned options, refer to the [official documentation](https://jupyter-notebook.readthedocs.io/en/stable/config.html)

	7. Return to your **command shell** and navigate to the inside of the **Notebooks** folder located in the **root** of the **KEEP Training** project
	```
	cd Notebooks
	```
	8. Start the Jupyter server
	> Note: If you set the optional notebook_dir setting, you do not need to navigate into the Notebooks folder. You may start the Jupyter server from any location
	```
	jupyter notebook
	```

	9. **KEEP Training** is now successfully installed and configured. You may now refer to the [KEEP Training Operation Manual](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/KEEPTrainingOperationManual.md) for how to create and run notebooks in Jupyter

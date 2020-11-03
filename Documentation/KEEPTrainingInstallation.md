# KEEP Training Installation
### Table of Contents
1. [Introduction](#Introduction)
2. [Software Prerequisites](#SoftwarePrerequisites)
3. [Package Versions](#PackageVersions)
4. [Prerequisite Installation](#PrerequisiteInstallation)
5. [Building The Directory Structure](#DirectoryStructure)
6. [Installation From Scratch](#InstallFromScratch)
7. [KEEP Training IIS Configuration](#IISConfiguration)
	1. [Prerequisites](#IISPrerequisites)
	2. [Prerequisite Installation](#IISPrerequisiteInstallation)
	3. [Creating the Reverse Proxy](#CreateReverseProxy)
	4. [Jupyter Configuration](#JupyterConfiguration)

### <a id="Introduction">Introduction</a>
Below you will find the instructions on the installation of the Jupyter Notebook application responsible for training the neural network model used within KEEP. For the purpose of this tutorial all software and package prerequisites will be listed, and it will be assumed you are using the same versions. You may attempt installation using differing versions, but results may vary.

It will also be assumed you are using the same directory structure for the project as described below. You may attempt to use a different directory structure, but you will need to be able to modify file-paths accordingly.

For many of the installation steps you should be familiar with using a command shell (cmd prompt, PowerShell, Bash or equivalent), it will also be helpful to be familiar with Windows IIS (Internet Information Services) and its basic configuration, though not required.

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

### <a id="DirectoryStructure">Building The Directory Structure</a>
**KEEP Training's** directory structure will consist of a single **root** directory to act as a container, and 2 sub-directories, 1 containing the python virtual environment and 2 containing the Jupyter Notebook `.ipynb` folders and files.
1. Begin with the [Prerequisite Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PrerequisiteInstallation.md)
2. Create a folder named `KEEPTraining` that will act as our **root** directory
3. Inside the **root** directory, create a new folder named `Notebooks`
4. Open your **command shell** and navigate to the inside of the **root** directory in your shell
> Note: Ensure your shell is running in administrator mode or equivalent
5. Create a `virtual python environment` to contain Python dependancies using the following command
> Note: A `virtual python environment` allows us to keep all our installed packages and dependancies local to the project we're working on, effectively allowing us to install different versions of packages for different projects without interference.
```
virtualenv KEEPTraining-env (You may replace KEEPTraining-env with anything you'd like)
```
6. Your directory structure should now match the following:
```
└── KEEPTraining 			# Root directory
    ├── KEEPTraining-env 	# Virtual python environment
    └── Notebooks 			# Jupyter ipynb folder
```
7. You are now ready to begin [Installation From Scratch](#InstallFromScratch)

### <a id="InstallFromScratch">Installation From Scratch</a>
1. Open your **command shell** and navigate to the inside of the **root** directory in your shell
2. Activate the virtual environment you created in order to start installing required packages
> Note: You will need to activate this virtual environment every time you want to work with this project, you can deactive the environment when finished with the `deactivate` command
```
.\KEEPTraining-env\Scripts\activate
```
The output in your shell window should now be prefaced with the environment name in brackets:
```
(KEEPTraining-env) C:\Some\path>
```
3. Before we begin installing the required packages we need to upgrade the pip installer with the following command
```
python -m pip install --upgrade pip
```
4. Now we are ready to begin installing our required packages. First we'll install Pytorch
> Please refer to the [Pytorch Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PytorchInstallation.md) guide for details.
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
> Note: Jupyter will display where it has stored your hashed password. Make a mental note of this location, as it is the same location where Jupyter configuration files will be stored by default.
```
jupyter notebook password
```
13. Start jupyter server and log in with the password you created to verify installation
```
jupyter notebook
```
After running this command you should be redirected to a browser window automatically displaying the main jupyter homepage.

14. KEEP Training is now successfully installed. If you only intend to use KEEP Training locally, you can refer to the [KEEP Training Operation Manual](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/KEEPTrainingOperationManual.md) for how to create and run notebooks in Jupyter. If you would like to access KEEP Training externally, continue on to the [KEEP Training IIS Configuration](#IISConfiguration) section.

### <a id="IISConfiguration">KEEP Training IIS Configuration</a>
KEEP Training is a Jupyter Notebook application. Jupyter Notebooks applications use their own server and cannot be natively configured to run using IIS. To get around this, we can configure IIS to act as a **reverse proxy** for the Jupyter server so we can access it as we would any other website.

#### <a id="IISPrerequisites">Prerequisites</a>
1. [Windows IIS (Internet Information Services)](https://www.iis.net/) = 10.0
2. [WebSocket Protocal enabled for IIS](https://docs.microsoft.com/en-us/iis/configuration/system.webserver/websocket)
2. [URL Rewrite Module for IIS](https://www.iis.net/downloads/microsoft/url-rewrite) = 2.1
3. [Application Request Routing Module for IIS](https://www.iis.net/downloads/microsoft/application-request-routing) = 2.5

#### <a id="IISPrerequisiteInstallation">Prerequisite Installation</a>
We'll begin by installing **Windows IIS** (Internet Information Services) with **WebSocket Protocol** enabled. We will then need to install two additional modules: **URL Rewrite** and **Application Request Routing**.
1. Install Windows IIS (Internet Information Services) with WebSocket Protocol
	1. Open **Control Panel**
	2. In the **Control Panel** search box, type **windows features**
	3. Under **Programs and Features, click **Turn Windows features on or off**

	![Programs and Features](Images/KEEPTrainingInstallation/ProgramsAndFeatures.jpg)

	4. Check the box next to **Internet Information Services** and expand **World Wide Web Services** and **Application Development Features** menus. Check the box next to **WebSocket Protocol**

	![Windows Features](Images/KEEPTrainingInstallation/WindowsFeatures.jpg)

	5. Navigate to http://localhost/ in a browser. You should see the default Windows IIS landing page. **If you do not see the default landing page**
		1. Open **Control Panel**
		2. In the search box type **services**
		3. Under **Administrative Tools** click **View local services**
		4. Scroll down the list of services until you find **World Wide Web Publishing Service**
		5. Ensure the service is running, if not right click and select **Start**
2. Install URL Rewrite and Application Request Routing modules
	1. From the **Windows start menu**, search for **IIS Manager**
	2. In **IIS Manager**, click the **Web Platform Installer** icon

	![Web Platform Installer](Images/KEEPTrainingInstallation/WebPlatformInstaller.jpg)

	3. Search for **url rewrite**
	4. Click **Add** next to **URL Rewrite 2.1**
	5. Search for **application request routing**
	6. Click **Add** next to **Application Request Routing 2.5 with KB2589179**
	7. **If you do not see the Web Platform Installer icon**
		1. Download and install **URL Rewrite** and **Application Request Routing** from the following links:
			1. https://www.iis.net/downloads/microsoft/url-rewrite
			2. https://www.iis.net/downloads/microsoft/application-request-routing

#### <a id="CreateReverseProxy">Creating the Reverse Proxy</a>
TO DO

#### <a id="JupyterConfiguration">Jupyter Configuration</a>
TO DO
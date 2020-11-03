# KEEP Application Installation
### Table of Contents
1. [Introduction](#Introduction)
2. [Software Prerequisites](#SoftwarePrerequisites)
3. [Package Versions](#PackageVersions)
4. [Prerequisite Installation](#PrerequisiteInstallation)
5. [Installation From Scratch](#InstallFromScratch)
7. [Creating the Django Application](#CreateDjangoApp)
8. [Hosting KEEP App on IIS](#HostingKEEPAppIIS)
9. [Connecting KEEPApp to Jira](#ConnectKEEPAppJira)

### <a id="Introduction">Introduction</a>
Below you will find the instructions on the installation of the Django backend application responsible for using the model trained with KEEP Training. The installation of KEEP Training is NOT required, but a trained text classification model IS required. For the purpose of this tutorial all software and package prerequisites will be listed, and it will be assumed you are using the same versions. You may attempt installation using differing versions, but results may vary.

For many of the installation steps you should be familiar with using a command shell (CMD, PowerShell, Bash or equivalent). It will also be helpful to be familiar with Django application structure and files, though not required.

### <a id="SoftwarePrerequisites">Software Prerequisites</a>
1. [Python](https://www.python.org/downloads/) = 3.8.5
2. [Visual Studio Build Tools 2019](https://visualstudio.microsoft.com/downloads/) (C++ Build Tools)

### <a id="PackageVersions">Package Versions</a>
1. [Virtualenv](https://pypi.org/project/virtualenv/) = 20.0.31 (Allows the creation of python virtual environments)
1. [Pytorch](https://pytorch.org/get-started/locally/) = 1.6.0 (Contains data structures for multi-dimensional tensors and mathematical operations)
2. [TorchVision](https://pytorch.org/get-started/locally/) = 0.7.0 (Package of commonly used datasets, model architectures and image transformations for computer vision)
3. [Fastai](https://fastai1.fast.ai/install.html) = 1.0.61 (Simplified API for Pytorch)
4. [SpaCy](https://spacy.io/) = 2.3.2 (Natural language processing software library)
5. [Django](https://www.djangoproject.com/) = 2.1.10 (Django web framework used for handling prediction requests and returning results)
6. [Wfastcgi](https://pypi.org/project/wfastcgi/) = 3.0.0 (Allows python applications to be hosted via Windows IIS)

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
The output in the shell window should now be prefaced with the environment name in brackets:
```
(ENVName-env) C:\Some\path>
```
6. Before we begin installing the required packages we need to upgrade the pip installer with the following command
```
python -m pip install --upgrade pip
```
7. Now we are ready to begin installing our required packages. First we'll install Pytorch
> In general it is best to install the same version of Pytorch that was used to train the model. If you are unsure which version was used, you will either need to find out, or attempt to install the correct version through trial and error. Please refer to the [Pytorch Installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/PytorchInstallation.md) guide for details.
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
11. Install Django 2.1.10 **(with your python virtual environment activated)**
```
pip install django==2.1.10
```
12. Install wfastcgi 3.0.0 **(with your python virtual environment activated)**
```
pip install wfastcgi==3.0.0
```
13. The KEEP App package requirements are now successfully installed, you can now move on to creating the Django application backend for KEEP App.
> Please refer to the [Creating the Django Application](#CreateDjangoApp) section of this installation guide for details.

### <a id="CreateDjangoApp">Creating the Django Application</a>
1. From the root directory of the KEEP App project, create a new folder called `src` to keep the Django application files contained
2. From your shell, navigate to the root directory of the KEEP App project
```
cd path/to/folder
```
3. Activate the KEEP App virtual environment
```
.\ENVName-env\Scripts\activate (Replace ENVName-env with the name of the KEEP App virtual environment)
```
4. Create the main Django application inside the `src` folder by using the following command
> Note: This command will create a manage.py file and a subfolder with the same name as your project-name within the src folder. Take note of the location of the manage.py file, as this will be used for a number of commands later.
```
django-admin startproject project-name src (Replace project-name with whatever you'd like)
```
5. In your shell, navigate to the `src` folder you created
```
cd src
```
6. Most Django applications are broken up into smaller pieces called Apps, we will use the same principle with KEEP by creating a keep app within our Django project. From the `src` folder run the following command
```
django-admin startapp app-name (Replace app-name with anything you'd like i.e. keep)
```
7. Navigate to the `src` folder using the file-system. In the src folder you should see a similar structure:

![Src Folder Structure](Images/KEEPAppInstallation/SrcFolder.jpg)

8. Open the folder with the name that matches whatever app-name you set previously, it should look like the following:

![App Folder Structure](Images/KEEPAppInstallation/AppFolder.jpg)

9. Using your favorite text editor, open the `views.py` file and replace the contents with the following:
```Python
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from fastai.basic_train import load_learner
from torch import argmax
import os

model = load_learner(os.path.dirname(os.path.abspath(__file__)),'models/KEEPModel.pkl')

#POST requests to /model/ are fed into the model and returns the reponse.
#
@require_POST
@csrf_exempt
def predict(request):
	if request.method == 'POST':
		pred = argmax(model.predict(request.POST.get('details'))[2])
		return JsonResponse(int(pred), safe=False)
```
10. Create a new file named `urls.py` and fill it with the following:
```Python
from django.urls import path

from .views import predict

urlpatterns = [
	path('', predict, name='predict'),
]
```
11. Create a new folder named `models` and copy the `KEEPModel.pkl` file that was trained using KEEP Training into this folder
12. Return to the `src` folder and navigate to the folder matching the project-name you set previously (Not the app-name). The folder should contain the following files:

![Project Folder Structure](Images/KEEPAppInstallation/ProjectFolder.jpg)

13. Modify the `settings.py` file `INSTALLED_APPS` section to match the following:
```Python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Custom Apps
    'app-name', # Replace app-name with your specific app name
]
```
14. Modify the `urls.py` file to match the following:
```Python
from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('model/', include('app-name.urls')), # Replace app-name with your specific app name
]
```
15. Ensure all file modifications are saved
16. With your shell, navigate to the `src` folder which contains the `manage.py` file and run the following command
```
python manage.py runserver
```
When the django development server has successfully started you should see output similar to the following:
> Note: By default the Django development server runs on port 8000. If you need to use a different port, you can specify a URL and port combination for Django to use by modifying the runserver command. Example: `python manage.py runserver 127.0.0.1:85`
```
System check identified no issues (0 silenced).
October 27, 2020 - 15:24:04
Django version 2.1.10, using settings 'keepapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
17. Navigate to `http://127.0.0.1:8000/model/` you should be presented with a `405 error`. This indicates that you have successfully reached the django view, but since the view only accepts POST requests there is nothing to actually display.
18. With the Django server successfully installed and configured, you are now ready to move on to [Hosting KEEP App on IIS](#HostingKEEPAppIIS)

### <a id="HostingKEEPAppIIS">Hosting KEEP App on IIS</a>
1. Begin with [Installation From Scratch](#InstallFromScratch)
2. Install Windows IIS (Internet Information Services)
	1. Open Control Panel
	2. In the Control Panel search box, type **windows features**
	3. Under **Programs and Features** click **Turn Windows features on or off**
	4. Check the box next to **Internet Information Services** and expland the World Wide Web Services and Application Development Features menus. Check the box next to **CGI**
	
	![Windows Features](Images/KEEPAppInstallation/WindowsFeatures.jpg)
	
	5. Navigate to http://localhost in a browser, you should see the default Windows IIS landing page
		1. If you don't see the default page
		2. Go back to Control Panel
		3. In the search box type **services**
		4. Under **Administrative Tools** click **View local services**
		5. Scroll down the list of services until you find **World Wide Web Publishing Service**
		6. Ensure this service is running, if not right click on it and select **Start**
3. Configure FastCGI in IIS
	1. From the Windows start menu, search for IIS Manager
	2. From the menu on the left, select the server

	![Select the Server](Images/KEEPAppInstallation/SelectServer.jpg)
	
	3. With the server still selected, double-click the **FastCGI Settings** icon in the middle area
	4. In the menu on the right, click **Add Application...**
	5. In the **Full Path:** box enter the path to the `python.exe` file **of the virtual environment for your Django project** located in `path/to/project/root/ENVName-env/Scripts/python.exe`
	6. In the **Arugments:** box enter the path to the `wfastcgi.py` file **of the virtual environment for your Django project** located in `path/to/project/root/ENVName-env/Lib/site-packages/wfastcgi.py`
	
	![FastCGI Paths](Images/KEEPAppInstallation/FastCGIPaths.jpg)
	
	7. In the **FastCGI Properties:** section, click on **Environment Variables** and then click the "..." on the right to open the EnvironmentVariables Collection Editor
	8. Click **Add**
	9. In right section, change **Name** to **WSGI_HANDLER** in all caps (This must be exact)
	10. In the right section, set **Value** to **django.core.wsgi.get_wsgi_application()** (This must be exact)
	
	![WSGI HANDLER](Images/KEEPAppInstallation/WsgiHandler.jpg)
	
	11. Click **Add** again
	12. In the right section, change **Name** to **DJANGO_SETTINGS_MODULE** in all caps (This must be exact)
	13. In the right section, set **Value** to **projectname.settings**, you will need to replace **projectname** with the name of your main Django project. You can check this by looking at the first couple of lines in the `settings.py` of the Django project

	![Project Name](Images/KEEPAppInstallation/ProjectName.jpg)
	
	14. Your environment variables should now resemble the following:
	
	![Django Settings Module](Images/KEEPAppInstallation/DjangoSettingsModule.jpg)
	
	15. Click OK to close the EvironmentVariables Collection Editor and OK again to close the Add FastCGI Application screen
4. Add a new site to IIS
	1. In the left menu of IIS Manager, double-click on the server name to expand it
	2. Right-click on the **Sites** folder and select **Add Website...**
	3. In the **Site name:** box enter any name you would like
	4. Click the "..." button next to **Physical path:** and navigate to the folder that contains the `manage.py` file of your Django project
	5. For testing purposes, change **Port:** to something other than 80, for example 85
	
	![Add Website](Images/KEEPAppInstallation/AddWebsite.jpg)
	
	6. Click OK
5. Configure site handler mappings
	1. In the left menu of IIS Manager, double-click on the **Sites** folder to expand it
	2. Click on the name of the site you just added
	3. With the site selected, double-click the **Handler Mappings** icon in the middle area
	4. In the right menu, click **Add Module Mapping...**
	5. In **Request path:** enter `*`
	6. In **Module:** select **FastCgiModule** (not CgiModule)
	7. In **Executeable:** enter the path to the `python.exe` of your virtual environment, followed by a pipe ("|") symbol, immediately followed by the path to the `wfastcgi.py` file of your virtual environment. For example:
	> Note: Having spaces in any part of your path is not supported
	```
	C:\path\to\ENVName-env\Scripts\python.exe|C:\path\to\ENVName-env\Lib\site-packages\wfastcgi.py
	```
	8. In **Name:** enter any name you would like, for example **Django Handler**
	9. Your inputs should resemble the following:

	![Module Mapping](Images/KEEPAppInstallation/ModuleMapping.jpg)
	
	10. Click **Request Restrictions** and ensure **Invoke handler only if request is mapped to:** is un-checked
	11. Click OK to close the **Request Restrictions** screen
	12. Click OK to close the **Add Module Mapping** screen
	13. Click No to the **Do you want to create a FastCGI application for this executable?** warning
6. Configure folder permissions for IIS
	1. Navigate to the root folder of the project (The folder that contains the src folder)
	2. Right-click the root folder and select **Properties**
	3. Click the **Security** tab
	4. Under **Group or user names:**, click **Edit**
	5. In the new window, click **Add**
	6. Click **Locations** next to **From this location:**
	7. Click the top item in the list, and click OK
	8. In the **Enter the object names to select:** area, type **IUSR; IIS_IUSRS** exactly as shown
	9. Click Check Names

	![Permissions](Images/KEEPAppInstallation/Permissions.jpg)
	
	10. Click OK
	11. Click OK again
	12. **OPTIONAL** If your project resides somewhere on the file system where higher-level permissions are likely to overwrite the permissions you just configured, you can disable inheritance
		1. From the **Security** tab, click **Advanced**
		2. Near the bottom of the new window, click **Disable inheritance**
		3. Click **Convert inherited permissions into explicit permissions on this object**
		4. Click OK
	13. Click OK to close the properties screen
	> Note: We have only added Read and Execute permissions. For certain projects, it may be necessary to add Write and Modify permissions to IUSR and IIS_USRS as well
	14. You should now be able to access your Django application through http://localhost:85/model/ (replace 85 with whatever port you configured previously)
	15. If everything is working, you can now move on to adding a custom hostname binding
	> Note: KEEPApp has no static files, therefore static file configuration has been intentionally skipped
7. Adding a hostname binding
	> Note: Proper DNS configuration is required to properly serve websites with custom hostname bindings. We will be faking this by manually configuring our local hosts file. This will only work if we are accessing the site from the same machine it is being hosted on, proper DNS configuration will not be covered in this guide
	1. Return to IIS Manager
	2. Expand your server and the Sites folder
	3. Right-click on your website in the left menu
	4. Select **Edit Bindings**
	5. Click on the first binding in the list and Click **Edit** on the right side
	6. In the **Port:** box, enter 80
	7. In the **Host name:** box, enter your custom hostname
	
	![Hostname Binding](Images/KEEPAppInstallation/HostnameBinding.jpg)
	
	8. Click OK
	9. Click Close
	10. Click your website in the left menu of IIS Manager and then Click **Restart** in the right menu
	11. In the right menu under **Browse Website** you should now see the hostname you just configured
	
	![Browse Website](Images/KEEPAppInstallation/BrowseWebsite.jpg)
	
	12. Open the `settings.py` file of your Django project in your favorite text editor
	13. Modify `ALLOWED_HOSTS` to include your custom hostname
	
	![Allowed Hosts](Images/KEEPAppInstallation/AllowedHosts.jpg)
	
	14. If your DNS is already configured, you're done. Otherwise, we will modify our local hosts file, this should only ever be used for testing purposes
		1. From the windows start menu, search for **Notepad**
		2. Right-click **Notepad** and select **Run as Administrator**
		3. In Notepad, click **File > Open**
		4. Ensure **All Files** is select as the **file-type**
		5. Navigate to your local hosts file, usually located at `C:\Windows\System32\drivers\etc`
		6. Open the file named **hosts**
		7. Scroll to the bottom of the file and add a new entry for your custom hostname
		
		![Hosts](Images/KEEPAppInstallation/Hosts.jpg)
		
		8. Save the hosts file
	15. You should now be able to access your Django project from your custom hostname. Example: `alec.keepapi.com/model/`
	16. You can now move on to [Connecting KEEPApp to Jira](#ConnectKEEPAppJira)

### <a id="ConnectKEEPAppJira">Connecting KEEPApp to Jira</a>

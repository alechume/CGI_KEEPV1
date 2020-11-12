# Prerequisite Installation
1. Download and install `Python` (version 3.8.5), be sure to check your system information to determine if you need 64bit vs 32bit
	1. Go to https://www.python.org/downloads/ and download the **executable installer**
	2. Run the installer and follow the prompts
	3. Check the box to include **pip** during installation

	![Include Pip](Images/PrerequisiteInstallation/IncludePip.jpg)

	4. Check the box to **Install for all users** and **Add Python to environment variables**

	![Install All Users](Images/PrerequisiteInstallation/InstallAllUsers.jpg)

	5. Type `python -V` in cmd prompt, powershell, bash shell or equivalent to verify Python installation
	```
	Python 3.8.5
	```
2. Download and install `Visual Studio Build Tools 2019 (C++ Build Tools)`
	
	**This step is optional, if you encounter "Failed building wheel for ..." problems during python package installation, you will need to complete this step**
	1. Go to https://visualstudio.microsoft.com/downloads/
	2. Scroll down to **All Downloads**
	3. Click the dropdown for **Tools for Visual Studio 2019**
	4. Download **Build Tools for Visual Studio 2019**
	5. Run the build tools installer you just downloaded and follow the prompts until you reach the installation details screen
	> Note: If you have already installed Visual Studio build tools in the past, you will first need to click **Modify** when you reach the **Installed** screen 
	> 
	> ![Modify Visual Studio](Images/PrerequisiteInstallation/Modify.jpg)
	
	6. Check the box for **C++ build tools**, all other options can remain default.
	
	![Visual Studio Build Tools](Images/PrerequisiteInstallation/VisualStudioBuildTools.jpg)
	
	7. Click install
3. Install `virtualenv` using **Pip**
	1. Open a command shell (cmd prompt, PowerShell, bash or equivalent)
	2. Run the following command
	```
	pip install virtualenv
	```

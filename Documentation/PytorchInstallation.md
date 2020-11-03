# Pytorch Installation
### <a id="InstallPytorch">How to Install Pytorch</a>
For Pytorch installation with CUDA, you will be required to know which model of GPU the machine or server running KEEP has. If you are unsure, or do not have a CUDA capable GPU you may skip to step 3.
1. Determine if you have a CUDA capable GPU
	1. Navigate to https://developer.nvidia.com/cuda-gpus
	2. Scroll down and check the expandable tables for your specific GPU model
	3. Make note of the **Compute Capability** number next to your GPU model
	4. If you determine you do not have a CUDA capable GPU, skip to step 3
2. Determine which CUDA SDK to use
	1. Navigate to https://pytorch.org/get-started/locally/
	2. Make note of the Pytorch supported CUDA SDK's
	
	![Possible CUDA Versions](Images/KEEPTrainingInstallation/PossibleCUDAVersions.jpg)
	
	3. Navigate to https://en.wikipedia.org/wiki/CUDA#GPUs_supported
	4. Find the Pytorch supported SDK's in the list and cross-reference with the **Compute Capability** number from step 1 to determine which SDK to use, generally the higher the SDK the better
	> Note: This guide was tested using CUDA SDK 10.2, with Pytorch version 1.6.0
	5. Navigate to https://developer.nvidia.com/cuda-toolkit-archive and download and install the CUDA Toolkit with the matching number of the SDK you just determined, for example, if you determined you need to use CUDA SDK 10.2, download CUDA Toolkit 10.2. When downloading choose **exe (local)**.
3. Install Pytorch
	1. Navigate to https://pytorch.org/get-started/locally/
	2. Select the following options:
		1. Pytorch Build: Stable
		2. Your OS: What operating system KEEP will be running on
		3. Package: Pip
		4. Language: Python
		5. CUDA: The SDK number you determined in step 2, or None
		
		![Pytorch Options](Images/KEEPTrainingInstallation/PytorchOptions.jpg)
		
	3. Copy the output from **Run this Command** and run the command in your shell **while the virtual environment is activated**
	> Note: If you get an error during the running of this command about SSL certificates, you can modify the command to use Amazon AWS instead and try again. For example: 
	```
	pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
	```
	> would become: 
	```
	pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://s3.amazonaws.com/pytorch/whl/torch_stable.html
	```

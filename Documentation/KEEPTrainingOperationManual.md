# KEEP Training Operation Manual
### Table of Contents
1. [Introduction](#Introduction)
2. [Environment Prerequisites](#EnvironmentPrerequisites)
3. [Creating Your First Notebook](#CreateFirstNotebook)
4. [Using an Existing Notebook](#UseExistingNotebook)
5. [Re-training the KEEP Neural Network Model](#RetrainKEEPModel)

### <a id="Introduction">Introduction</a>
Below you will find instructions on the basic operation of KEEP Training. This is **NOT** the place to find an in-depth explanation of machine learning concepts, or how to correctly build custom neural network models. This manual is only meant to address the basic operation of KEEP Training to get you started.

Jupyter is a software package that allows developers to both write code and see their results on the same page. In our case it allows us to write and run Python code to train our models and combine it with Markdown, a type of light-weight text formatting language. Through Jupyter we can write the code required to train our model and see a visual representation of the output in real time. Training neural network models is complex and requires experimentation, Jupyter allows us to keep everything in one place.

### <a id="EnvironmentPrerequisites">Environment Prerequisites</a>
1. Complete [KEEP Training installation](https://github.com/alechume/CGI_KEEPV1/blob/main/Documentation/KEEPTrainingInstallation.md)
2. The Jupyter Notebook server is running

### <a id="CreateFirstNotebook">Creating Your First Notebook</a>
1. From the Jupyter browser window, select `Python 3` from the <kbd>New</kbd> dropdown menu
![New Notebook](Images/KEEPTrainingOperationManual/NewNotebook.jpg)
2. Type `print('Hello World!')` in the first line or `cell` of the newly created `Python 3` notebook
3. With the first `cell` highlighted, press <kbd>Shift</kbd> + <kbd>Enter</kbd> or press the <kbd>Run</kbd> button at the top of the page
![First Cell](Images/KEEPTrainingOperationManual/FirstCell.jpg)
4. In the second line of the notebook type `# This is a title!` and with the `cell` still highlighted, select `Markdown` from the **dropdown menu** near the top of the page
5. With the second `cell` highlighted, press <kbd>Shift</kbd> + <kbd>Enter</kbd> or press the <kbd>Run</kbd> button at the top of the page
![Second Cell](Images/KEEPTrainingOperationManual/SecondCell.jpg)
6. Congratulations! You have successfully created and ran your first notebook with `Python` code and `Markdown`. To edit the second `cell` with our title, simply double click on `cell`
> Note: Just like when you're writing Python scripts, you can import different packages as needed. For example `import fastai.vision.all import *` will import all of the fastai libraries associated with computer vision
7. You can rename your notebook by clicking on the document name near the top of the window
![Rename](Images/KEEPTrainingOperationManual/Rename.jpg)

### <a id="UseExistingNotebook">Using an Existing Notebook</a>
> NOTE: You will need to have a Notebook `.ipynb` file, and know where it is stored
1. From the Jupyter browser window, navigate to the location of the notebook `.ipynb` file you want to run and click on it
2. If you would like to re-run the notebook, click the button with the double arrows and click <kbd>Restart and Run All Cells</kbd>
![Rerun Notebook](Images/KEEPTrainingOperationManual/RerunNotebook.jpg)
3. To run individual `cells`, highlight the `cell` by clicking on it and press <kbd>Shift</kbd> + <kbd>Enter</kbd> or press the <kbd>Run</kbd> button at the top of the page
> NOTE: When you run a notebook, Jupyter will automatically save the output, therefore just because you see output from previous cells, you may not have access to their variables until you re-run the preceding cells. For example, if in cell 1 I have `x = 10` and in cell 2 I have `print(x)`, cell 2 will fail until I run cell 1 first.

### <a id="RetrainKEEPModel">Re-training the KEEP Neural Network Model</a>
> NOTE: Access to the Jira database will be required.
1. Read through [Creating Your First Notebook](#CreateFirstNotebook) and [Using an Existing Notebook](#UseExistingNotebook)
2. Download the [KEEPNeuralNetworkTraining](https://github.com/alechume/CGI_KEEPV1/tree/main/KEEPTraining/Notebooks/KEEPNeuralNetworkTraining) folder from the [Repository](https://github.com/alechume/CGI_KEEPV1), this file contains the Notebook and all supporting files. (KEEPTraining/Notebooks/KEEPNeuralNetworkTraining)
3. Place these files somewhere accessible to the Jupyter server. For example, within a notebooks folder in the root project directory
ADD PICTURE HERE
4. From the Jupyter browswer window, navigate to where you stored the KEEPNeuralNetworkTraining.ipynb file and click on it to open it
ADD PICTURE HERE
5. Change the **database connection string** and **query** to match your own Jira database connection.
ADD PICTURE HERE
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
2. You will need to obtain a copy of the **KEEPNeuralNetworkTraining** notebook and its supporting files. You can obtain this file from the [Repository](https://github.com/alechume/CGI_KEEPV1) in the [KEEPNeuralNetworkTraining](https://github.com/alechume/CGI_KEEPV1/tree/main/KEEPTraining/Notebooks/KEEPNeuralNetworkTraining) folder (../KEEPTraining/Notebooks/KEEPNeuralNetworkTraining).
3. Place these files somewhere accessible to the Jupyter server. For example, within a notebooks folder in the root project directory

![Download KEEP Notebook](Images/KEEPTrainingOperationManual/DownloadKEEPNotebook.jpg)

4. From the Jupyter browser window, navigate to where you stored the KEEPNeuralNetworkTraining.ipynb file and click on it to open it

![Open KEEP Notebook](Images/KEEPTrainingOperationManual/OpenKEEPNotebook.jpg)

5. Change the **database connection string** and **query** to match your own Jira database connection.

![Connection and Query](Images/KEEPTrainingOperationManual/ConnectionAndQuery.jpg)

6. You can now re-run the notebook by clicking the button with the double arrows and clicking <kbd>Restart and Run All Cells</kbd>

![Rerun Notebook](Images/KEEPTrainingOperationManual/RerunNotebook.jpg)

> NOTE: Training neural network models can take a significant amount of time and system resources. It is recommended that you do NOT attempt to train models on business-critical systems or servers.
7. You can monitor the progress of your notebook in real-time. For each `cell` containing code, Jupyter will display an `*` or a number indicating if it is processing or completed. For example, in the image below we can see that the `cell` containing `learn.unfreeze()` has completed, indicated by the number 11, and that the next `cell` with `learn.fit_one_cycle(...)` is currently being processed.

![Notebook Running](Images/KEEPTrainingOperationManual/NotebookRunning.jpg)

8. When the notebook has finished running, you can find the trained models in the output folder/directory `models`, located in the same directory as the notebook `.ipynb` file. For a more detailed explanation of what each model is used for and how they were trained, read the explanation within the notebook itself.
> NOTE: The main model responsible for performing predictions is the `KEEPModel.pkl` model.

![Model Output Directory](Images/KEEPTrainingOperationManual/ModelOutputDirectory.jpg)

9. When you've finished running the notebook, it is always a good idea to ensure you shut it down to free up system resources. You can do this by returning to the Jupyter browser window, navigating to where you stored the KEEPNeuralNetworkTraining.ipynb file, checking the box next to it and clicking the <kbd>Shutdown</kbd> button

![Shutdown Notebook](Images/KEEPTrainingOperationManual/ShutdownNotebook.jpg)

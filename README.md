# KEEP (Knowledge Enhancement and Evalution Project) V1
### Description
An application whose purpose is to intelligently determine the quality (high or low) of service tickets using a neural network model and catagorize them accordingly. This is version 1 of the project, using Fastai version 1.0.61. All root sub-directories contain a `README.md` file explaining the contents of the directory. KEEP is split into two main modules, **KEEP App** which is the Django backend application used to create predictions, and **KEEP Training** which is the Jupyter Notebook application responsible for training the neural network model used by **KEEP App**.

### Directory Scructure:
```
├── Documentation
│   ├── Images
│   │   ├── KEEPAppInstallation
│   │   │   └── (Image Files)
│   │   ├── KEEPTrainingInstallation
│   │   │   └── (Image Files)
│   │   └── KEEPTrainingOperationManual
│   │       └── (Image Files)
│   ├── KEEPAppInstallation.md
│   ├── KEEPTrainingInstallation.md
│   ├── KEEPTrainingOperationManual.md
│   └── README.md
├── KEEP App
│   ├── src
│   │   ├── keep
│   │   │   ├── migrations
│   │   │   │   └── (Migration Files)
│   │   │   ├── __init__.py
│   │   │   ├── admin.py
│   │   │   ├── apps.py
│   │   │   ├── models.py
│   │   │   ├── tests.py
│   │   │   ├── urls.py
│   │   │   └── views.py
│   │   ├── keepapi
│   │   │   ├── __init__.py
│   │   │   ├── settings.py
│   │   │   ├── urls.py
│   │   │   └── wsgi.py
│   │   └── manage.py
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
├── KEEP Training
│   ├── Notebooks
│   │   └── KEEPNeuralNetworkTraining
│   │       ├── data
│   │       │   └── (Data Files)
│   │       ├── images
│   │       │   └── (Image Files)
│   │       └── KEEPNeuralNetworkTraining.ipynb
│   ├── .gitignore
│   ├── README.md
│   └── requirements.txt
└── README.md
```

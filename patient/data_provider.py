import os
import pickle
import joblib

config = {
    'cancer': {
        'SVC': 'ml_models/svm_model.pkl',
        'KNearestNeighbours': 'ml_models/knn_model.pkl',
        'RandomForest': 'ml_models/rfc_model.pkl',
        'DecisionTree':'ml_models/dtree_model.pkl',
        'KMeansClassifier': 'ml_models/kmean_model.pkl',
    }}

dir = os.path.dirname(__file__)

def GetJobLibFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    else:
        print("file does not exit")

def GetPickleFile(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return pickle.load( open(os.path.join(dir, filepath), "rb" ) )
    return None

def GetAllClassifiers():
    return (GetSVMClassifier(),GetKNNClassifier(),GetKMeanClassifier(),GetDecisionTreeClassifier(),GetRandomForestClassifier())

def GetSVMClassifier():
    return GetJobLibFile(config['cancer']['SVC'])

def GetKNNClassifier():
    return GetJobLibFile(config['cancer']['KNearestNeighbours'])

def GetKMeanClassifier():
    return GetJobLibFile(config['cancer']['KMeansClassifier'])

def GetDecisionTreeClassifier():
    return GetJobLibFile(config['cancer']['DecisionTree'])

def GetRandomForestClassifier():
    return GetJobLibFile(config['cancer']['RandomForest'])
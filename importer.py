
#installs all necessary packages without the need of a conda environment 

import importlib.util
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if importlib.util.find_spec('numpy') is None:
    install('numpy')

if importlib.util.find_spec('pandas') is None:
    install('pandas')    

import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import os

if importlib.util.find_spec('seaborn') is None:
    install('seaborn') 

import seaborn as sns

if importlib.util.find_spec('matplotlib') is None:
    install('matplotlib')    

import matplotlib.pyplot as plt

if importlib.util.find_spec('sklearn') is None:
    install('sklearn')

if importlib.util.find_spec('math') is None:
    install('math') 

if importlib.util.find_spec('scipy') is None:
    install('scipy') 


import sklearn
import math
import scipy

import warnings
warnings.filterwarnings('ignore')


if importlib.util.find_spec('json') is None:
    install('json') 
    

if importlib.util.find_spec('re') is None:
    install('re') 
    
import json
import urllib.request
import re

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

if importlib.util.find_spec('joblib') is None:
    install('joblib') 

if importlib.util.find_spec('cgi') is None:
    install('cgi') 
    
if importlib.util.find_spec('cgitb') is None:
    install('cgitb') 
        

import joblib
import cgi
from cgi import FieldStorage
import cgitb



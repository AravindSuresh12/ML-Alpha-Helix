import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn
import math
import scipy

import warnings
warnings.filterwarnings('ignore')

import json
import urllib.request
import re

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

import joblib
import cgi
from cgi import FieldStorage
import cgitb



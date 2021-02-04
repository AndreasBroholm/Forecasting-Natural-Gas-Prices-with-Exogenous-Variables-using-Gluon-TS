#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.lines import Line2D

import seaborn as sns

import plotly.express as px
import plotly.graph_objects as go

import json
import math
import os
import datetime

import IPython
import IPython.display

from typing import Any, Callable, Dict, Sequence

import calplot

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

from pmdarima.arima import auto_arima

from gluonts.dataset.field_names import FieldName
from gluonts.dataset.util import to_pandas
from gluonts.model.deepar import DeepAREstimator
from gluonts.mx.trainer import Trainer
from gluonts.evaluation.backtest import make_evaluation_predictions
from gluonts.evaluation import Evaluator
from gluonts.dataset.common import ListDataset, MetaData, TrainDatasets, load_datasets

import warnings
import torch
import os
from torchvision import transforms
import copy
import numpy as np
import pandas as pd
import csv

# Main data folder
data_path = './'

# Will consist all of the raw data
data = {}

"""
@ get_time_series_df:
@ args:
@   - X: dataframe samples
@   - y: dataframe labels
@   - length: come on
@   - step: obvious 
@
@ returns:  time series dataframe
"""
def get_time_series_df(X, y, length = 5):
  ts_X, ts_y = [], []
  for l in range(0, len(X) - length, length):
    ts_X.append(X[l:l + length])
    ts_y.append(y[l + length-1])

  return np.array(ts_X), np.array(ts_y)

"""
@ paint_sensors: Paint sub-group of sensors that simulate our system
@ arg: sample - 64x32 matrix representing force sensors image
@ returns: None
"""
def paint_sensors(sample):
  for sensor in square_sensors:
    sample[sensor[0]][sensor[1]] = 1
  for sensor in line_sensors:
    for i in range(sensor[0], sensor[1] + 1):
      sample[i][sensor[2]] = 1


# For each Patient dir
for dir in os.listdir(data_path):
  if os.path.isfile(os.path.join(data_path, dir)):
    continue

  new_data, labels = None, None

  # For each data file
  for file in os.listdir(os.path.join(data_path, dir)):
    with open(os.path.join(data_path, dir, file), 'r') as f:
      for line in f.read().splitlines()[3:]:
        
        # First data
        if new_data is None:
          new_data = file_data
          labels = file_label
        else:
          new_data = np.concatenate((new_data, file_data), axis=0)
          labels = np.concatenate((labels, file_label), axis=0)

  data[dir] = (torch.from_numpy(new_data), torch.from_numpy(labels))
# -*- coding: utf-8 -*-
"""One_hot_encoding_clinical_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AGye0aLsmH8h78c756M7dboSWb3NoAcI
"""

import json
import numpy as np

# # Load data 
# def load_tester(path):
#     """Function to load JSON clinical data
#     path = directory to file or name of file if in same directory as code file
#     returns:
#     data = list of JSON data
#     """
#     with open(path) as f:
#         data = json.load(f)
#     return data

#from google.colab import drive
#drive.mount('/content/drive')

#data = load_tester('drive/My Drive/Reproducibility_Project/MultimodalPrognosis-master/data/original_clinical_dataset.json')

## Encode race
def encoding_race(race):
  """Function to apply hot-one-encoding on a certain race from clinical data.
  race = "white", "american indian or alaska native", "black or african american", "asian", "native hawaiian or other pacific islander", "Not Reported"
  Returns:
  1x5 hot-endcoding-vector
  """
  enc_vector = np.zeros(5)
  if race == "white":
    enc_vector[0] = 1
  elif race == "american indian or alaska native":
    enc_vector[1] = 1
  elif race == "black or african american":
    enc_vector[2] = 1
  elif race == "asian":
    enc_vector[3] = 1
  elif race == "native hawaiian or other pacific islander":
    enc_vector[4] = 1
  else:
    enc_vector = enc_vector
  
  return enc_vector

## Test code
#print(encoding_race(data[8299]['demographic']['race']))
#print(data[8299]['demographic']['race'])

## Encode gender
def encoding_gender(gender):
  """Function to apply hot-one-encoding on gender from clinical data.
  gender = "male", "female", "Not Reported"
  Returns:
  0 for male, 1 for female
  """
  if gender == "male":
    return np.array([0])
  elif gender == "female":
    return np.array([1])
  else: 
    return np.array([None]) 

## Test code
#print(encoding_gender(data[412]['demographic']['gender']))
#print(data[412]['demographic']['gender'])

## Encode vital_status
def encoding_vital_status(vital_status):
  """Function to apply hot-one-encoding on gender from clinical data.
  gender = "Dead", "Alive", "Not Reported"
  Returns:
  0 for Dead, 1 for Alive
  """
  if vital_status == "Dead":
    return np.array([0])
  elif vital_status == "Alive":
    return np.array([1])
  else: 
    return np.array([None]) 

## Test code
#print(encoding_vital_status(data[412]['demographic']['vital_status']))
#print(data[412]['demographic']['vital_status'])

## Encode cancer_type
def encoding_cancer_type(cancer_type):
  """Function to apply hot-one-encoding on a certain cancer type from clinical data.
  cancer_type = Cancer type of sample, TCGA abbreviations
  Returns:
  1x36 hot-endcoding-vector
  """
  enc_vector = np.zeros(36)
  if cancer_type == "LAML":
    enc_vector[0] = 1
  elif cancer_type == "ACC":
    enc_vector[1] = 1
  elif cancer_type == "BLCA":
    enc_vector[2] = 1
  elif cancer_type == "LGG":
    enc_vector[3] = 1 
  elif cancer_type == "BRCA":
    enc_vector[4] = 1
  elif cancer_type == "CESC":
    enc_vector[5] = 1
  elif cancer_type == "CHOL":
    enc_vector[6] = 1
  elif cancer_type == "LCML":
    enc_vector[7] = 1
  elif cancer_type == "COAD":
    enc_vector[8] = 1
  elif cancer_type == "CNTL":
    enc_vector[9] = 1
  elif cancer_type == "ESCA":
    enc_vector[10] = 1
  elif cancer_type == "FPPP":
    enc_vector[11] = 1
  elif cancer_type == "GBM":
    enc_vector[12] = 1
  elif cancer_type == "HNSC":
    enc_vector[13] = 1
  elif cancer_type == "KICH":
    enc_vector[14] = 1
  elif cancer_type == "KIRC":
    enc_vector[15] = 1
  elif cancer_type == "KIRP":
    enc_vector[16] = 1
  elif cancer_type == "LIHC":
    enc_vector[17] = 1
  elif cancer_type == "LUAD":
    enc_vector[18] = 1
  elif cancer_type == "LUSC":
    enc_vector[19] = 1
  elif cancer_type == "DLBC":
    enc_vector[20] = 1
  elif cancer_type == "MESO":
    enc_vector[21] = 1
  elif cancer_type == "MISC":
    enc_vector[22] = 1
  elif cancer_type == "OV":
    enc_vector[23] = 1
  elif cancer_type == "PAAD":
    enc_vector[24] = 1
  elif cancer_type == "PCPG":
    enc_vector[25] = 1
  elif cancer_type == "PRAD":
    enc_vector[26] = 1
  elif cancer_type == "READ": #COAD and READ same one-hot-encoding??
    enc_vector[8] = 1
  elif cancer_type == "SARC":
    enc_vector[27] = 1
  elif cancer_type == "SKCM":
    enc_vector[28] = 1
  elif cancer_type == "STAD":
    enc_vector[29] = 1
  elif cancer_type == "TGCT":
    enc_vector[30] = 1
  elif cancer_type == "THYM":
    enc_vector[31] = 1
  elif cancer_type == "THCA":
    enc_vector[32] = 1
  elif cancer_type == "UCS":
    enc_vector[33] = 1
  elif cancer_type == "UCEC":
    enc_vector[34] = 1
  elif cancer_type == "UVM":
    enc_vector[35] = 1
  else:
    enc_vector = enc_vector
  
  return enc_vector

## Test code
#print(encoding_cancer_type("UVM"))
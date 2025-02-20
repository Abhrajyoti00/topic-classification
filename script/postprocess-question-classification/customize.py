from cmind import utils
import os
import pandas as pd
from sklearn.metrics import f1_score, precision_score


def preprocess(i):

    os_info = i['os_info']

    env = i['env']

    return {'return':0}


def postprocess(i):
    correct = 0
    env = i['env']
    soln=pd.read_csv(env['CM_DATASET_SOLUTION_PATH'],header=0)["Tag"]
    model_soln=pd.read_csv(env['CM_ML_MODEL_ANSWER'],header=0)["List_of_ans"]
    model_soln_single_tag = pd.read_csv(env['CM_ML_MODEL_ANSWER'],header=0)["Tag"]
    for i in range(len(model_soln)):
        if(soln[i] in model_soln[i]):
            correct = correct + 1
    print("\tAccuracy by brute force approach is:"+str(correct/len(model_soln)))
    print("\n\tAccuracy of the result produced by model #1:"+str(f1_score(model_soln_single_tag, soln, average='micro'))+"\n")
    return {'return':0}

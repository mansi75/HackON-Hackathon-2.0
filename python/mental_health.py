import pandas as pd
import numpy as np
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn import linear_model

from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor

import sys

def mental(data):
    print("Inside mental method")
    train = pd.read_csv("/home/harish/Burnout_Predictor/Burnout_Prediction_Python/files/train.csv")
    train = pd.get_dummies(train, columns = ["Gender"], drop_first = True)
    train.rename(columns = {'Gender_Male': 'Gender'}, inplace = True)
    train = pd.get_dummies(train, columns = ["Company Type"], drop_first = True)
    train = pd.get_dummies(train, columns = ["WFH Setup Available"], drop_first = True)
    print("Initialize train")
	#train = train
    for col in ['Resource Allocation', 'Mental Fatigue Score']:
        train[col] = train[col].fillna(train[col].median())
    train = train.dropna(subset=['Burn Rate'])
    X = train.drop(['Employee ID','Date of Joining','Burn Rate'], axis=1)
    y = train['Burn Rate']
    print("Train files ready")
    #X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7,test_size = 0.3, random_state=100)
    test = pd.read_csv("/home/harish/Burnout_Predictor/Burnout_Prediction_Python/upload_files/"+data)
    test = pd.get_dummies(test, columns = ["Gender"], drop_first = True)
    test.rename(columns = {'Gender_Male': 'Gender'}, inplace = True)
    test = pd.get_dummies(test, columns = ["Company Type"], drop_first = True)
    test = pd.get_dummies(test, columns = ["WFH Setup Available"], drop_first = True)
    for col in ['Resource Allocation', 'Mental Fatigue Score']:
        test[col] = test[col].fillna(test[col].median())
    #test = test.dropna(subset=['Burn Rate'])
    X_test = test.drop(['Employee ID','Date of Joining'], axis=1)
    print("Test files ready")

    rf = RandomForestRegressor()


    rf.fit(X, y)


    y_pred = rf.predict(X_test)

    print("Prediction Ready")
    #rf_r2 = r2_score(y_test, y_pred)
    #rf_mae = mean_absolute_error(y_test, y_pred)

    prediction = pd.DataFrame(y_pred, columns=['Burn Rate']).to_csv('/home/harish/Burnout_Predictor/Burnout_Prediction_Python/prediction.csv')
    #print(rf_r2)
    #print(rf_mae)
    print("Prediction Done")



#print("Enter the path of the file")
#s = input()
s = sys.argv[1]
#print(s)
mental(s)






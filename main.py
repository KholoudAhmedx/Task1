import pandas as pd
import numpy as np
import os 
import tkinter as tk
from tkinter import *
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


def Preprocessing():

    # Read the data from the file
    dataframe = pd.read_excel('Dry_Bean_Dataset.xlsx')

    # Encoding catergorical data 
    label_encoder = LabelEncoder()
    dataframe['Class'] = label_encoder.fit_transform(dataframe['Class'])

    # Handle missing values
    #print(dataframe.isnull().sum()) # MajorAxisLenght has 1 missing value
    dataframe.fillna(dataframe.mean(),inplace=True)

    # Feature scaling
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(dataframe)
    #print(data_scaled)

    # Feature Extraction 
    Y = data_scaled[:, -1]
    X = data_scaled[:, 0:5]
 


    X_train, X_test, Y_train, Y_test = [], [],[],[]

    # Get the unique classes 
    unique_classes = np.unique(Y)
    #print(unique_classes)

    for class_number in unique_classes:

        class_data_X = X[Y== class_number]
        #print('-----------------------------------\n ')
        #print(class_data_X)

        class_data_Y = Y[Y == class_number]

        #print(class_data_Y)

        # Splitting data randomly 30 samples > train & 20 samples -> test
        train_data_X, train_data_Y, test_data_X, test_data_Y = train_test_split(class_data_X, class_data_Y, test_size=20)


        # Append train data of each class to the train_X & same for test
        X_train.append(train_data_X)
        Y_train.append(train_data_Y)
        X_test.append(test_data_X)
        Y_test.append(test_data_Y)

    X_train = np.concatenate(X_train)
    Y_train = np.concatenate(Y_train)
    # print('X_train: \n')
    # print(X_train)
    # print('Y_train: \n')
    # print(Y_train)
    X_test = np.concatenate(X_test)
    Y_test = np.concatenate(Y_test)
    # print(X_test)
    # print('-------------------------\n')
    # print(Y_test)
    return X_train, Y_train, X_test, Y_test

x_train, y_train, x_test, y_test = Preprocessing()
print('\nXtrain\n',x_train, '\nYtrain\n', y_train, '\nXtest\n', x_test, '\nYtest\n', y_test)


def Perceptron():
    return 0
def Adaline():
    return 0 
# GUI implementation
root = Tk()
root.title('Task1 Window')
root.geometry("500x400")
## Rest of the GUI here

# Feature entries
f1 = tk.IntVar()
f2 = tk.IntVar()
f3 = tk.IntVar()
f4 = tk.IntVar()
f5 = tk.IntVar()

area_checkbutton = tk.Checkbutton(root, text = 'Area', variable=f1, onvalue=1, offvalue=0)
area_checkbutton.pack()
perimeter_checkbutton = tk.Checkbutton(root, text = 'Perimeter', variable=f2, onvalue=1, offvalue=0)
perimeter_checkbutton.pack()
majoraxis_checkbutton = tk.Checkbutton(root, text = 'MajorAxisLength', variable=f3, onvalue=1, offvalue=0)
majoraxis_checkbutton.pack()
minoraxis_checkbutton = tk.Checkbutton(root, text = 'MinorAxisLength', variable=f4, onvalue=1, offvalue=0)
minoraxis_checkbutton.pack()
roudness_checkbutton = tk.Checkbutton(root, text = 'Roundness', variable=f5, onvalue=1, offvalue=0)
roudness_checkbutton.pack()

# Classes Entries
c1 = tk.IntVar()
c2 = tk.IntVar()
c3 = tk.IntVar()

bombay_checkbutton = Checkbutton(root, text = 'Bombay', variable=c1, onvalue=1, offvalue=0)
bombay_checkbutton.pack()
cali_checkbutton = Checkbutton(root, text= 'Cali', variable=c2, onvalue=1, offvalue=0)
cali_checkbutton.pack()
sira_checkbutton = Checkbutton(root, text='Sira', variable=c3, onvalue=1, offvalue=0)
sira_checkbutton.pack()

# Learning rate 
Learning_rate = Label(root, text="Learning rate")
Learning_rate.pack()
Learning_rate_entry = Entry(root)
Learning_rate_entry.pack()

# Number of epochs
epochs_label = Label(root, text="Number of epochs")
epochs_label.pack()
epochs_entry = Entry(root)
epochs_entry.pack()

# MSE
mse_label = Label(root, text="MSE")
mse_label.pack()
mse_entry = Entry(root)
mse_entry.pack()

# Add bais or not 
b = IntVar()

bais_checkbutton = Checkbutton(root,text="Add bais", variable=b, onvalue=1, offvalue=0)
bais_checkbutton.pack()

# Choose the algorithm
p = IntVar() # perceptron var
Ad = IntVar() # adaline var
Perceptron_radiobutton = Radiobutton(root, text="Perceptron", variable=p, value=1)
Perceptron_radiobutton.pack()


Adaline_radiobutton = Radiobutton(root, text="Adaline", variable=Ad, value=2)
Adaline_radiobutton.pack()
root.mainloop()
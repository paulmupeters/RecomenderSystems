#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 13:53:36 2018

@authors: Paul Peters & Jason 
"""
#UserID::MovieID::Rating::Timestamp
#N-fold cross validation
#RMSE, MAE test 
import numpy as np
import aignment1DataMining as func


N = 5
ratingsArray = []
movies = 3
users = 3

ratingsFile = open('ratings.dat')
for line in ratingsFile:
	splitted = line.split("::")	
	ratingsArray.append(splitted)
ratingsFile.close()
    
np_ratingsMatrix = np.array([[1,2,3, 23],[1, 3 , 4, 12], [2, 2,4,2], [2,3,4,2]
, [3,2,1,3], [3,3,3,3],[1,1,5,1]])      #np.array(ratingsArray,dtype = np.int32)



train_error_glAvg =np.zeros(N)
train_error_itAvg =np.zeros(N)
train_error_usAvg =np.zeros(N)
test_error_glAvg =np.zeros(N)
test_error_itAvg =np.zeros(N)
test_error_usAvg =np.zeros(N)
np.random.seed(69)

seqs=[x % N for x in range(len(np_ratingsMatrix))]
np.random.shuffle(seqs)



def cvGlobalAverage():
    for fold in range(N):
        training_data=np.array([x!=fold for x in seqs])
        test_data=np.array([x==fold for x in seqs])
        train=np_ratingsMatrix[training_data]
        test=np_ratingsMatrix[test_data]
        global_average = func.globalAverage(train)       
        #train and test error for global average
        train_error_glAvg[fold] = np.sqrt(np.mean((train[:,2]- global_average)**2))  
        test_error_glAvg[fold] = np.sqrt(np.mean((test[:,2]- global_average)**2))
    return test_error_glAvg, train_error_glAvg, global_average
    
def cvItemAverage():
        for fold in range(N):
            training_data=np.array([x!=fold for x in seqs])
            test_data=np.array([x==fold for x in seqs])
            train=np_ratingsMatrix[training_data]
            test=np_ratingsMatrix[test_data]
            tot_erra = 0
            tot_errb = 0
            print(train)
            item_average = func.itemAverage(train, movies)
            gb_avg = func.globalAverage(train)
            # calculate item average error for test and train set
            for i in range(1, len(train) + 1):
                it_err = np.sqrt(np.mean((train[np.where(train[:,1] == i)][:,2] - item_average[i - 1])**2))
                tot_erra += it_err
                if (test[np.where(test[:,1] == i)][:,2].size) == 0:
                    
                else:
                    it_errb = np.sqrt(np.mean((test[np.where(test[:,1] == i)][:,2] - item_average[i - 1])**2))
                tot_errb += it_errb
                if i == movies:
                    train_error_itAvg[fold] = tot_erra/len(train)
                    test_error_itAvg[fold] = tot_errb/len(test)
                    tot_erra = 0
                    tot_errb = 0
        return test_error_itAvg, train_error_itAvg, item_average
        
def cvUserAverage():
    for fold in range(N):
        training_data=np.array([x!=fold for x in seqs])
        test_data=np.array([x==fold for x in seqs])
        train=np_ratingsMatrix[training_data]
        test=np_ratingsMatrix[test_data]
        tot_erra = 0
        tot_errb = 0
        user_average = func.userAverage(np_ratingsMatrix, users)
        
       # calculate user average error for test and train set
        for i in range(1, users + 1):
            it_err = np.sqrt(np.mean((train[np.where(train[:,0] == i)][:,2] - user_average[i - 1])**2))
            tot_erra += it_err
            it_errb = np.sqrt(np.mean((test[np.where(test[:,0] == i)][:,2] - user_average[i - 1])**2))
            tot_errb += it_errb
            if i == users:
                train_error_usAvg[fold] = tot_erra/users
                test_error_usAvg[fold] = tot_errb/users
                tot_erra = 0
                tot_errb = 0
                
                
cvItemAverage()
        
        







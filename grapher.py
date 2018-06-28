#!/usr/bin/env python

import pandas as pd
from pandas import *
from datetime import datetime
import csv
import matplotlib.pyplot as plt


def graph():
    columns_to_graph = ['Posted Date', 'Amount']

    ######
    df = pd.read_csv('bank01.csv',
        dtype='object',
        sep='\s*,\s*',
        encoding='ascii',
        header=0,
        index_col=['Posted Date', 'Amount'],
        usecols=['Posted Date', 'Amount'],
        parse_dates=['Posted Date'],
        engine='python') # read in the guy
    #print (df) #    <-----
    df = df.reset_index()
    #print df['Amount']
    money_list = []
    date_list = []
    bad_indexes = []
    i = 0
    print '---'
    for x in df['Amount']:
        i +=1
        try:
            money_list.append(float(x))
        except ValueError:
            bad_indexes.append(i)
            #print "Not a float"
    #print bad_indexes
    i = 0
    for x in df['Posted Date']:
        i += 1
        if i not in bad_indexes:
            date_list.append(x)


    ##### do the other data!
    df2 = pd.read_csv('bank02.csv',
        dtype='object',
        sep='\s*,\s*',
        encoding='ascii',
        header=0,
        index_col=['Posted Date', 'Amount'],
        usecols=['Posted Date', 'Amount'],
        parse_dates=['Posted Date'],
        engine='python') # read in the guy
    #print (df2) #    <-----
    df2 = df2.reset_index()
    #print df2['Amount']
    money_list2 = []
    date_list2 = []
    bad_indexes2 = []
    i = 0
    print '---'
    for x in df2['Amount']:
        i +=1
        try:
            money_list2.append(float(x))
        except ValueError:
            bad_indexes2.append(i)
            #print "Not a float"
    #print bad_indexes
    i = 0
    for x in df2['Posted Date']:
        i += 1
        if i not in bad_indexes:
            date_list2.append(x)



    plt.plot(date_list, money_list, color="blue")
    print len(date_list2)
    print date_list2
    print len(money_list2)
    print money_list2
    plt.plot(date_list2, money_list2[:-1], color="red")
    plt.show()
    #for x in df['Date']:
        #print x




######
###### Entry Point
######
print '=== BANK GRAPHER ==='
graph()

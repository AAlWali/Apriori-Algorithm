# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:29:37 2020

@author: Abdelrahman Al-Wali
"""

import pandas as pd
from Config import config as C
from itertools import combinations
import random
import os

css = C.css
Sorting_of_rules = C.Sorting_of_rules
if Sorting_of_rules is True:
    sorting = 1
else:
    sorting = 2

"""Data extraction from data file"""
def data_extract():
    df = pd.read_csv(C.data_path,sep='\s+', header=None)
    df.to_csv(C.csv_file, header=None, index = False)
    data = pd.read_csv(C.csv_file, usecols = list(range(C.start_column,C.last_column)),header = None)
    data.columns=['0','1','2','3','4','5','6','7','8','9','10','11']
    return data


"""Get support of each level"""
def support_lvl(dataframe):
    count1 = []
    for i in dataframe:
        counts=dict()
        for x in dataframe[i]:
            x = str(x)
            x = x.replace(" ", "")
            if "[" not in x:
                x = "[" + x + "]"
            x = x + "[" + str(i) + "]"
            counts[x] = counts.get(x,0)+1
        i = dict(sorted(counts.items()))
        count1.append(i)    
    return count1

"""Elimination of values less than minimum support from list of dictionary"""
def elmination_of_values(list_of_dic,min_support):
    filtered_list=[]
    for n in list_of_dic:
        n={k: v for k, v in n.items() if v >= min_support}
        filtered_list.append(n)
    return filtered_list

"""Elmination of empty columns in dataframe after elimination of values that less than minimum support"""
def elimination_of_columns(dataframe,list_of_dic):
    count = 0
    x = []
    for i in list_of_dic:
        if i == {}:
            x.append(list_of_dic.index(i,count))
        count += 1
    dataframe.drop(dataframe.columns[x], axis=1, inplace=True)
    return dataframe

"""To make combination between attributes to higher the level"""
def make_combination(dataframe , level, original_data):
    data = original_data.copy()
    new_df=pd.DataFrame()
    common_values= ""
    flag=0
    counter_i=0
    counter_j=0
    stop=0
    for i in dataframe:
        counter_j=0


        for j in dataframe[counter_i+1:]:
           
            flagg=0
            while(counter_j <= counter_i):
                counter_j+=1
                flagg=1
                break
            if flagg==1:
                continue
     
        
            common_values= ""
            stop=0
            I=i.split(",")
            J=j.split(",")
          
            
            for k in range(level-2):
                
                  flag=0
                  if I[k]==J[k]:
                      flag=1      
                      if(k==(level-2-1)):
                           common_values += str(I[k])  
                      else:
                           common_values += str(I[k]) + "," 
                  else:
                      stop=1
                      break
                      
            if level == 2 or level == 1:
                flag = 1          
            if flag ==1: 

                common=common_values.split(",")
                if(level == 1):
                    return data
                elif(level==2):
                    new_df[str(i)+","+str(j)] = data[[str(i), str(j)]].values.tolist()
                elif(level==3):
                    new_df[str(common[0]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
               
                elif(level==4):           
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                    
                elif(level==5):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                    
                elif(level==6):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==7):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==8):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(common[5]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(common[5]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==9):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(common[5]) +","+ str(common[6]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(common[5]) , str(common[6]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==10):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(common[5]) +","+ str(common[6]) +","+ str(common[7]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(common[5]), str(common[6]), str(common[7]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==11):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(common[5]) +","+ str(common[6]) +","+ str(common[7]) +","+ str(common[8]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(common[5]), str(common[6]), str(common[7]) , str(common[8]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                
                elif(level==12):
                    new_df[str(common[0]) +","+ str(common[1]) +","+ str(common[2]) +","+ str(common[3]) +","+ str(common[4]) +","+ str(common[5]) +","+ str(common[6]) +","+ str(common[7]) +","+ str(common[8]) +","+ str(common[9]) +","+ str(I[level-2]) +"," + str(J[level-2])] = data[[str(common[0]) , str(common[1]) , str(common[2]) , str(common[3]) , str(common[4]) , str(common[5]), str(common[6]), str(common[7]) , str(common[8]) , str(common[9]) , str(I[level-2]) , str(J[level-2])]].values.tolist()
                             
                    
            counter_j+=1
            if stop==1:
                break
        counter_i+=1
    
    return new_df

"""Return all values in dictionary that exceeds minimum support"""
def return_values(list_of_dic):
    keys = list()
    for i in list_of_dic:
        for j,k in i.items():
            keys.append(j + "[" + str(k) + "]")
    return keys

"""Collective function that return lvl dataframe with only columns that exceeds minimum support"""
def collective_fun(previous_lvl,level,min_support,original_data):
    current_lvl = make_combination (previous_lvl, level, original_data)
    lvl_support = support_lvl(current_lvl)
    lvl_support = elmination_of_values(lvl_support,min_support)
    current_lvl = elimination_of_columns(current_lvl,lvl_support)
    return lvl_support,current_lvl

"""Return last lvl all values with support greater than minimum support"""
def return_last_lvl_values(lvl_0,min_support,original_data):
    support_lvls = list()
    previous_lvl = lvl_0
    current_lvl = pd.DataFrame()
    value = list()
    values = pd.DataFrame(columns = ['values','columns','support'])
    lvl_num = 0
    flag = 0
    if min_support < 1:
        min_support = min_support*5822
    for i in range(original_data.shape[1]):
        lvl_support, current_lvl = collective_fun(previous_lvl,i+1,min_support,original_data)
        if current_lvl.shape[1] == 0:
            lvl_num = i
            flag = 1
            break
        support_lvls.append(lvl_support)
        previous_lvl = current_lvl
    if flag == 0:
        lvl_num = 12
        lvl_support = support_lvl(current_lvl)
        lvl_support = elmination_of_values(lvl_support,min_support)
        value = return_values(lvl_support)
    else:
        lvl_support = support_lvl(previous_lvl)
        lvl_support = elmination_of_values(lvl_support,min_support)
        value = return_values(lvl_support)
        
    
    for i in range(len(value)):
        x = value[i].split('[')
        values = values.append({'values' : x[1][:-1] , 'columns' : x[2][:-1] , 'support' : x[3][:-1]} , ignore_index=True)
    return lvl_num, support_lvls, values

"""Return support of specific combinations"""
def return_support(to_find_support,support_lvl):
    lvl = (to_find_support.count(','))//2 + 1
    for i in support_lvl[lvl-1]:
        if to_find_support in i.keys():
            return i.get(to_find_support)

"""Calculate confidence of rule"""        
def confidence_of_rule(LHS,union_support,support_lvl):
    return (float(union_support)/float(return_support(LHS,support_lvl)))*100

"""Calculate lift of rule"""
def lift_of_rule(LHS,RHS,union_support,support_lvl):
    return  ( float(union_support) / 5822.0 ) / float( ( (return_support(LHS,support_lvl) / 5822.0 ) * ( return_support(RHS,support_lvl) / 5822.0 ) ) )

"""calculate leverage of rule"""
def leverage_of_rule(LHS,RHS,union_support,support_lvl):
    return ( float(union_support)/5822.0 - float( ( return_support(LHS,support_lvl) / 5822.0 ) * ( return_support(RHS,support_lvl) / 5822.0 ) ) )

"""Return all rules that have more than minimum confidence and prioritize them by lift or leverage descendingly"""
def make_rules_and_prioritize(dataframe,lvl_num,support_lvl,min_confidence):
    cols_n = {0: '[Unskilled_labourers]', 1: '[Social_class_A]', 2: '[Social_class_B1]', 3: '[Social_class_B2]',
              4: '[Social_class_C]', 5: '[Social_class_D]', 6: '[Rented_house]', 7: '[Home_owners]', 8: '[1_car]',
              9: '[2_cars]', 10: '[No_car]', 11: '[National_Health_Service]'
        }
    temp_values = list()
    temp_columns = list()
    values = ""
    columns = ""
    rules = list()
    if min_confidence <= 1:
        min_confidence = min_confidence*100
    for i in range(dataframe.shape[0]):
        union_support = dataframe.iloc[i][2]
        values = dataframe.iloc[i][0].split(',')
        columns = dataframe.iloc[i][1].split(',')
        for j in range(1,lvl_num):
            temp_values.append(list(combinations(values, j)))
            temp_columns.append(list(combinations(columns, j)))
        for k,l in zip(temp_values,temp_columns):
            for x,y in zip(k,l):
                LHS_values = "["
                LHS_columns = "["
                for a,b in zip(x,y):
                    LHS_values += a + ","
                    LHS_columns += b + ","
                LHS_values += "]"
                LHS_columns += "]"
                LHS_values = LHS_values[:-2] + LHS_values[-1:]
                LHS_columns = LHS_columns[:-2] + LHS_columns[-1:]
                confidence_of_current_rule = confidence_of_rule(LHS_values + LHS_columns,union_support,support_lvl)
                LHS = LHS_values + LHS_columns
                RHS = ""
                if confidence_of_current_rule >= min_confidence:
                    LHS_values = LHS_values.replace("[","")
                    LHS_values = LHS_values.replace("]","")
                    LHS_values = LHS_values.replace(",","")
                    LHS_columns = LHS_columns.replace("[","")
                    LHS_columns = LHS_columns.replace("]","")
                    list_of_LHS_columns = LHS_columns.split(",")
                    index_of_rest = list()
                    RHS_rule = ""
                    rest_values = ""
                    rest_columns = ""
                    for p in list_of_LHS_columns:
                        index_of_rest.append(columns.index(p))
                    rest_values = "["
                    rest_columns = "["
                    for p in range(len(values)):
                        if p not in index_of_rest:
                            RHS_rule += values[p] + cols_n.get(int(columns[p])) + "^"
                            rest_values += values[p] + ","
                            rest_columns += columns[p] + ","
                    rest_values += "]"
                    rest_columns += "]"
                    rest_values = rest_values[:-2] + rest_values[-1:]
                    rest_columns = rest_columns[:-2] + rest_columns[-1:]
                    RHS = rest_values + rest_columns
                    RHS_rule = RHS_rule[:-1]
                    LHS_rule = ""
                    for u,u1 in zip(LHS_values,LHS_columns.split(',')):
                        LHS_rule += u + cols_n.get(int(u1)) + "^"
                    LHS_rule = LHS_rule[:-1] + " " + "-->" + " "
                    rules.append([LHS_rule + RHS_rule,confidence_of_current_rule,lift_of_rule(LHS,RHS,union_support,support_lvl),leverage_of_rule(LHS,RHS,union_support,support_lvl)])
                LHS_columns = ""
                LHS_values = ""
        temp_values = list()
        temp_columns = list()
    rule = sorted(rules, key = lambda x: x[sorting] , reverse = True)
    rules = pd.DataFrame(rule, columns = ['Rule','Confidence','Lift','Leverage'])
    return rules

"""Converting output rules in dataframe into an HTML"""
def DataFrame_to_HTML(data, css = css):
    fn = str(random.random()*1000).split(".")[0] + ".html"
    try:
        os.remove(fn)
    except:
        None
    text_file = open(fn, "a")
    text_file.write(css)
    text_file.write(data.to_html())
    text_file.close()
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:30:24 2020

@author: Abdelrahman Al-Wali
"""

from Utils import data_extract,return_last_lvl_values,make_rules_and_prioritize,DataFrame_to_HTML

def main():
    data = data_extract()

    print("Please enter support value : ")
    min_support = float(input())
    print("Please enter confidence value : ")
    confidence = float(input())
    lvl_0 = data.copy()
    lvl_num,support_lvls,values = return_last_lvl_values(lvl_0,min_support,data)
    rules = make_rules_and_prioritize(values,lvl_num,support_lvls,confidence)
    DataFrame_to_HTML(rules)
    
if __name__ == "__main__":
    main()

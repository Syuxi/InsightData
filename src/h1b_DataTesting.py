#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:11:33 2018
Insight Data Engineering Coding Challange

Challange: 
Identify top occupation and states for H1B Visa applicant, 
by filtering immigration data and standerdize output.


@author: suo
"""

import csv
#=====Specify Data Path======================================================================
#data_path       = '/Users/suo/Downloads/Insight Data Application/input/H1B_FY_2016.csv'#5000
data_path       = './input/H1B_FY_2015_.csv' #500
#data_path       = '/Users/suo/Downloads/Insight Data Application/input/H1B_FY_2014_.csv'#3000
#data_path       = '/Users/suo/Downloads/Insight Data Application/input/H1B_FY_2015.csv' #500

#data_path      = '/Users/suo/Downloads/Insight Data Application/input/h1b_input.csv'
save_path_OCC   = './output/top_10_occupations.txt'
save_path_STATE = './output/top_10_states.txt'

#=====Start Digging Data======================================================================

with open (data_path,'r',encoding="utf-8") as f: # utf-8 to solve the ASCII issue
    header   = next(csv.reader(f, delimiter=';')) # save column names, the header   
    file     = csv.reader(f,delimiter=';') # read input csv file
    try:
        ind0 = header.index('LCA_CASE_NUMBER') # check 2014 data, and indexing the case_number column for further identification
    except:
        ind0 = header.index('CASE_NUMBER')     # indexing case_number for different version of data
    try:        
        ind1 = header.index('STATUS')
    except:
        ind1 = header.index('CASE_STATUS')
    try:           
        ind2 = header.index('LCA_CASE_SOC_CODE')
    except:
        ind2 = header.index('SOC_CODE')
    try:   
        ind3 = header.index('LCA_CASE_SOC_NAME')
    except:
        ind3 = header.index('SOC_NAME')        
    try:   
        ind4 = header.index('LCA_CASE_WORKLOC1_STATE')
    except:
        ind4 = header.index('WORKSITE_STATE')
   #=====Subset Data for Counting ==========================================================
   # Here, we make a list for our Subset Data based on the following criteria:
   # a. Visa Status equals Certified
   # b. All important field is not empty
   #
   # Then, we append it together as a sub-set for future counting as occ
   # Another important features that we are getting here is the number of certified cases, saved as SUM
   # SUM is used for future percentage calculating :)
   
    occ=[]  # make a list for our Subset Data 
    occ_list=[] # make a contemporary list for each line of the subset data 
    for lines in file: 
        if (len(lines)==len(header) and lines[ind1]=='CERTIFIED' and len(lines[ind0])!=0 and len(lines[ind1])!=0 and len(lines[ind2])!=0 
            and len(lines[ind3])!=0 and len(lines[ind4])!=0):
            occ_list= [lines[ind0]]+[lines[ind1]]+[lines[ind2]]+[lines[ind3]]+[lines[ind4]]
        occ.append(occ_list)     #append
        occ = [x for x in occ if x] #list comprehension
        SUM = (len(occ))#SUM OF CERTIFICATED CASES
    del(ind0,ind1,ind2,ind3,ind4)   # Delete the variable, in case files have different indexing    
    
    #=====DATA PROCESSING==========================================================
    #==============================================================================
    #1. FILE 1, Top10 OCC
    #To Get The First Element in a list(position_name)
    
    position = [str.encode(k[2]) for k in occ] # returns encoded version of the SOC_CODE string
    position_count = {x:position.count(x) for x in position} #count the occurrences using list comprehension
    position_rank = sorted((value,key.decode()) for (key,value) in position_count.items()) #sort based on the frequency
    position_rank.sort(reverse=True) #highest one listed at the 1st line
    position_rank_top10 = position_rank[0:10] #Get TOP 10
    del(position_rank) #delete the original huge list
    position_name=[]  #make a list to save occupation name corresponding to the occ_code
    for i in range(1,len(position_rank_top10)+1): 
        position_name_line = next(k[3] for k in occ if position_rank_top10[-i][1] in k) #find the top 10 job name
        position_name.append(position_name_line)  #append to the position_name list, which is what we want
    position_rank_top10.sort(key=lambda tup: tup[0]) 
    #==============================================================================
        #SECOND ELEMENT (t_count)
    t_count=[tup_count[0] for tup_count in position_rank_top10] # get the counting number for our second column in txt file
    #==============================================================================
        #THIRD ELEMENT (percent)
    percent= []
    percent_list=[x[0] for x in position_rank_top10] # get each occurrence in the top 10 list 
    percent_one=0 
    percent_mark=[] # make a list for the 2nd column
    for item in percent_list:
        percent_one = round((float(item)/SUM)*100,1) #calculate and rounded to the right decimal 
        percent.append(percent_one)       #append everything together
        percent_mark = list(map("{}%".format, percent)) # add a percentage mark to it
    del(percent_list,percent_one,position_rank_top10) #delete for state calculation
  
    OCC_list= list(zip(position_name, t_count,percent_mark)) #put it together
    OCC_list.sort(key=lambda k: (-k[1],k[0]))#Sorted by NUMBER first, and in case of a tie, alphabetically by TOP_OCCUPATIONS
    del(position_name_line,percent_mark)
    del(t_count)
    del(percent)
    
    #==============================================================================
    #2. FILE 2, TOP STATES
    state = [o[4] for o in occ] #find the statename in the subset list, as we gave the state name as ind4 
    state_count = {s:state.count(s) for s in state} #count the occurrences using list comprehension
    state_sort = sorted(state_count.items(),key=lambda x: x[1],reverse = True)#sort to get top10
    state_rank_top10 = state_sort[0:10] #only list the top 10
    del(state_sort,state,state_count) #delete the original huge list
    #=============================================================================
    #FIRST ELEMENT (state_name)
    state_name=[tup_count[0] for tup_count in state_rank_top10] #FIRST ELEMENT
    #=============================================================================
    #SECOND ELEMENT (t_count)
    state_count=[tup_count[1] for tup_count in state_rank_top10] #SECOND ELEMENT
    #==============================================================================
    #THIRD ELEMENT (percent)
    percent= []
    percent_list=[x[1] for x in state_rank_top10] # get each occurrence in the top 10 list
    for item in percent_list:
        percent_one = round((float(item)/SUM)*100,1)
        percent.append(percent_one)
        percent_mark = list(map("{}%".format, percent)) #add a percentage mark
    del(item,percent_list,percent_one,state_rank_top10)
    
    STATE_list= list(zip(state_name, state_count,percent_mark)) #put it together
    STATE_list.sort(key=lambda k: (-k[1],k[0]))     #Sorted by NUMBER first, and in case of a tie, alphabetically by TOP_STATES
    del(state_name,state_count,percent,percent_mark,SUM)   
    #=====DATA OUTPUT==============================================================
    #OUTPUT FILE1
    with open(save_path_OCC,'w+') as occ_result:
        occ_result.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
        for o in OCC_list:
            occ_result.write(';'.join(str(s) for s in o) + '\n')
        del(OCC_list)
        del(o)
        #OUTPUT FILE2
    with open(save_path_STATE,'w+') as state_result:
        state_result.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
        for o in STATE_list:
            state_result.write(';'.join(str(s) for s in o) + '\n')
        del(o,STATE_list)    
        del(occ,occ_list,save_path_OCC,save_path_STATE)
         
f.close()

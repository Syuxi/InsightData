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

with open (data_path,'r',encoding="utf-8") as f: # utf-8 to solve the ASCII issue
    header   = next(csv.reader(f, delimiter=';')) #header variable   
    file     = csv.reader(f,delimiter=';')
    try:
        ind0 = header.index('LCA_CASE_NUMBER')
    except:
        ind0 = header.index('CASE_NUMBER')        
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
        
    
    head_index=[ind0,ind1,ind2,ind3,ind4]#column id 

    #print(len(header))
#    del(header)
    occ=[]
    occ_list=[]
    for lines in file:
        if (len(lines)==len(header) and lines[ind1]=='CERTIFIED' and len(lines[ind0])!=0 and len(lines[ind1])!=0 and len(lines[ind2])!=0 
            and len(lines[ind3])!=0 and len(lines[ind4])!=0):
            occ_list= [lines[ind0]]+[lines[ind1]]+[lines[ind2]]+[lines[ind3]]+[lines[ind4]]
        occ.append(occ_list)
        occ = [x for x in occ if x]
        SUM = (len(occ))#SUM OF CERTIFICATED CASES
    del(ind0,ind1,ind2,ind3,ind4)        
    
    #=====DATA PROCESSING==========================================================
    #==============================================================================
    #1. FILE 1 , TOP OCC
        #FIRST ELEMENT (position_name)
    position = [str.encode(k[2]) for k in occ]
    position_count = {x:position.count(x) for x in position}
    position_rank = sorted((value,key.decode()) for (key,value) in position_count.items())
    position_rank.sort(reverse=True)
    #Get TOP 10, and delete the original huge list
    position_rank_top10 = position_rank[0:10]
    #print(position_rank)
    #del(position_rank)
    position_name=[]
#    position_name= [x[1] for x in position_rank_top10]
    for i in range(1,len(position_rank_top10)+1):
        position_name_line = next(k[3] for k in occ if position_rank_top10[-i][1] in k)
        position_name.append(position_name_line)  
    position_rank_top10.sort(key=lambda tup: tup[0])#,reverse=True)
        #position_name.reverse()
        #    print(position_name)        
    #==============================================================================
        #SECOND ELEMENT (t_count)
    t_count=[tup_count[0] for tup_count in position_rank_top10] #SECOND ELEMENT
    #    print(t_count)
    #==============================================================================
        #THIRD ELEMENT (percent)
    percent= []
    percent_list=[x[0] for x in position_rank_top10]
    percent_one=0
    percent_mark=[]
    for item in percent_list:
        percent_one = round((float(item)/SUM)*100,1)
        percent.append(percent_one)
        percent_mark = list(map("{}%".format, percent))
    #print(percent_mark)
    #del(percent_list,percent_one)#,position_rank_top10)
    
    OCC_list= list(zip(position_name, t_count,percent_mark))
    #Sorted by NUMBER first, and in case of a tie, alphabetically by TOP_OCCUPATIONS
    OCC_list.sort(key=lambda k: (-k[1],k[0]))
    #del(position_name_line,percent_mark)
    #del(t_count)
    #del(percent)
    
    #==============================================================================
    #2. FILE 2, TOP STATES
    state = [o[4] for o in occ]
    state_count = {s:state.count(s) for s in state}
    #print(state_count)
    state_sort = sorted(state_count.items(),key=lambda x: x[1],reverse = True)#sort to get top10
    state_rank_top10 = state_sort[0:10] #only list the top 10
    #print(state_rank_top10)
    del(state_sort,state,state_count) #delete the original huge list
    #=============================================================================
    #FIRST ELEMENT (state_name)
    state_name=[tup_count[0] for tup_count in state_rank_top10] #FIRST ELEMENT
    #print(state_name)
    #=============================================================================
    #SECOND ELEMENT (t_count)
    state_count=[tup_count[1] for tup_count in state_rank_top10] #SECOND ELEMENT
    #print(state_count)    
    #==============================================================================
        #THIRD ELEMENT (percent)
    percent= []
    percent_list=[x[1] for x in state_rank_top10]
    for item in percent_list:
        percent_one = round((float(item)/SUM)*100,1)
        percent.append(percent_one)
        percent_mark = list(map("{}%".format, percent)) #add a percentage mark
    #print(percent_mark)
    del(item,percent_list,percent_one,state_rank_top10)
    STATE_list= list(zip(state_name, state_count,percent_mark))
        #Sorted by NUMBER first, and in case of a tie, alphabetically by TOP_STATES
    STATE_list.sort(key=lambda k: (-k[1],k[0]))
    del(state_name,state_count,percent,percent_mark,SUM)   
    #=====DATA OUTPUT==============================================================
    #OUTPUT FILE1
    with open(save_path_OCC,'w+') as occ_result:
        occ_result.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
        for o in OCC_list:
            occ_result.write(';'.join(str(s) for s in o) + '\n')
        #del(OCC_list)
        del(o)
        #OUTPUT FILE2
    with open(save_path_STATE,'w+') as state_result:
        state_result.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE'+'\n')
        for o in STATE_list:
            state_result.write(';'.join(str(s) for s in o) + '\n')
        print('finish output top_10_states')
        del(o,STATE_list)    
        del(occ,occ_list,save_path_OCC,save_path_STATE)
         
f.close()
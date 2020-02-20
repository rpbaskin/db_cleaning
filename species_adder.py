#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 18:28:47 2018


This program adds species data to files with species data in the beginning,
@author: pbaskin
"""

import sys

# # # # # # # # # # # # # # # # # # #
#
#     METHODS
#
# # # # # # # # # # # # # # # # # # # 

"""
Cuts a single list into two lists of header and aa data
Takes the string (data), an empty headers (list1), and an empty aa (list2)
"""
def breakup(data, list1, list2):
    switch = 0
    for each in data:
        if switch == 0:
            list1.append(each)
            switch = 1
        elif switch == 1:
            list2.append(each)
            switch = 0


"""
Appends the species name into the data set
takes a list of data and appends the species name followed by a period 
"""
def speciesinput(speciesname, listofheaders):
    i = 0
    for each in listofheaders:
        listofheaders[i] = '>' + speciesname + '.' + each[1:]
        i+=1
# # # # # # # # # # # # # # # # # # # #
#
#       MAIN
#
# # # # # # # # # # # # # # # # # # # # 
            
if len(sys.argv) == 3:
#    try:
    file_name = sys.argv[1]
    print(file_name)
    my_file = open(file_name).read()
    outputname = 'mod_' + sys.argv[2] + '.anot.cono.pep.uniq.fa'
    print(outputname)
    OUT = open(outputname, 'w')
    
    textlist = my_file.split('\n')
    textlist.pop(-1)

    headers =[]
    data = []
    breakup(textlist, headers, data)
    speciesinput(sys.argv[2], headers)
    temp = []
    for i in zip(headers, data):
        for j in i:
            temp.append(j)
    for each in temp:
        OUT.write(each)
        OUT.write('\n')
#    except:
#        print("filename doesn't exist or path is incorrect")
    
else:
    print("USAGE: python3 species_adder path/to/filename/to/modify speciesname")
    

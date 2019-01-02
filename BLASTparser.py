#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:32:49 2018

BLASTparser


@author: pbaskin
"""
import sys 
import itertools
from collections import defaultdict

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#                                 METHODS
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def leaders(xs, top=10):
    counts = defaultdict(int)
    for x in xs:
        counts[x] += 1
    return sorted(counts.items(), reverse=True, key=lambda tup: tup[1])[:top]


def getTotalHits(string):
    indexstart = string.find("BLAST")
    indexend = string.find('\n\n#')
    number = 0 
    text = string[indexstart:indexend]
    textlist = text.split('\n')
    for each in textlist:
        number += 1
    return number-6
    
def getSUPFAM(string):
    
    supfams = []
    text = my_file.split('\n')
    for each in text:
        if each.find('# >') != -1:
            indexstart = each.find('SUPFAM:')
            indexend = each.find('TPM:')
            supfam = each[indexstart+7:indexend-1]
            supfams.append(supfam)
    return supfams

def getSUPFAM10(string):
    
    supfams = []
    text = my_file.split('\n')
    count = round(text/10)
    for each in text[0:count]:
        if each.find('# >') != -1:
            indexstart = each.find('SUPFAM:')
            indexend = each.find('TPM:')
            supfam = each[indexstart+7:indexend-1]
            supfams.append(supfam)
    return supfams

def getSUPFAM25(string):
    
    supfams = []
    text = my_file.split('\n')
    count = round(text/4)
    for each in text[0:count]:
        if each.find('# >') != -1:
            indexstart = each.find('SUPFAM:')
            indexend = each.find('TPM:')
            supfam = each[indexstart+7:indexend-1]
            supfams.append(supfam)
    return supfams

    
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#                                 MAIN BODY
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if len(sys.argv) == 3:
    
    path = sys.argv[0]
    indexpath = path.find('BLASTparser.py')
    paths = path[0:indexpath]
    file_name = sys.argv[1]
    my_file = open(file_name).read()
    outputname = 'stats.' + file_name + '.csv'
    OUT = open(outputname, 'w')
    
    
    
    
    
    
    
    totalhits = getTotalHits(my_file)
    temp = leaders(getSUPFAM(my_file))
    temp10 = leaders(getSUPFAM10(my_file))
    temp25 = leaders(getSUPFAM25(my_file))
    
    
    
    OUT.write("file input: " + file_name + '\n' + "database type: " + sys.argv[2] + '\n' + "total hits: " + str(totalhits) +',,,top 25%,,,top 10%\n')
    OUT.write("SupFam,num_hits,percent_hit\n")
    for a,b,c in itertools.izip(temp,temp25,temp10):
        OUT.write(str(a)[1:-1] + ',' + str(round(a[1]/totalhits*100,2))+'%' + ',' + str(b)[1:-1] + ',' +str(round(b[1]/totalhits*25,2))+'%' + ',' + str(c)[1:-1] + ',' + str(round(a[1]/totalhits*10,2))+'%')
        OUT.write('\n')
    
              
              
else:
    print("USAGE: python3 BLASTparser.py path/to/filetoparse databasetype(i.e. basic/ML/snails")

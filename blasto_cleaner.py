# -*- coding: utf-8 -*-
"""
Created on Fri Sept 28 12:36:44 2018


Cleans up databases for blasto functionality

COPYRIGHT (c) R Paul Baskin 28 September 2018
@author: rpbas
"""
import os.path
import sys
import re


# # # # # # # # #
#
#     METHODS
#
# # # # # # # # #

#Replaces a bad character in a string with good charaters
#Asks for a list, bad character, good character
def cleanupstring(listobj, bad, good):
    i=0
    for each in listobj:
        if bad in each:
            listobj[i] = each.replace(bad, good)
        i+=1
        
def rmtrin(d):
    i=0
    for each in d:
        if each.find('TRINITY') != -1:
            indexstart = each.find('TRINITY')
            indexend = each.find('SUPFAM:')
            d[i] = each[:indexstart+7]+each[indexend-1:]
            i+=1

#Prints out the data on a different line if the length is longer than 80
def chopper (string, value1, value2):
    if len(string) < value1 or len(string) == value1:
        OUT.write(string)
        OUT.write('\n')
    elif len(string)>value1 & len(string)<value2:
        OUT.write(string[0:80] + '\n')
        chopper(string[80:], 80,160)


#TODO
def dup_remove(headers, duplicate):
    i = 0
    values=[]
    final_list_d = []
    for num in duplicate:
        if num not in final_list_d:
            final_list_d.append(num)
            i+=1
        elif num in final_list_d:
            values.append(i)
            print("AA at line " +str((i*2)+2)+ " has a redundancy")
        else:
            raise Exception("It's neither in nor out")

    j=0
    if(values.count!=0):
        for each in values:
            headers.pop(each-j)


    i = 0
    for each in headers:
        headers[i] = '>' + str(i)+each[1:]
        i+=1

    rmtrin(headers)
    dbdict = dict(zip(headers,final_list_d))
    return dbdict



    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #
    #                                 MAIN BODY
    #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


if len(sys.argv) == 2:
    
    path = sys.argv[0]
    indexpath = path.find('db_cleaner_nodups.py')
    paths = path[0:indexpath]
    file_name = sys.argv[1]
    my_file = open(file_name).read()
    outputname = 'nodups_' + file_name
    OUT = open(outputname, 'w')
    

    #starts to chop up the input FASTA file for analysis
    #breaks the long string file into a list
    data = my_file.split('\n')
    data.pop(-1)
    #
    #
    #     THIS IS THE IMPORTANT PART
    #     if you want to change a specific character in the data set
    #
    i = 0
    for each in data:
        data[i] = each.upper()
        i += 1

#    cleanupstring(data,' ', '_')
    cleanupstring(data,'\t', '_')
#    cleanupstring(data, '"', '_')
#    cleanupstring(data, '*', '')
    #cleanupstring(data, '(', '_')
    #cleanupstring(data, ')', '_')
#    cleanupstring(data, '[', '_')
#    cleanupstring(data, ']', '_')
#    cleanupstring(data, '|', '_')
    i=0
    for each in data:
        if each == '':
            data.pop(i)
        i+=1

    headers = []
    aa = []
    switch = 0
    for each in data:
        if switch == 0:
            headers.append(each)
            switch = 1
        elif switch == 1:
            aa.append(each)
            switch = 0
    #zippers the two lists together
    headerset = []
    aaa = []
    dbdict = dup_remove(headers,aa)


    #Eliminates reducendies





    #Turns dictionary into a text file

    for key, value in dbdict.items():
        OUT.write(key)
        headerset.append(key)
        OUT.write('\n')
        OUT.write(value)
        aaa.append(value)
        OUT.write('\n')

    OUT.close()

    

#    #Run the program through signalp
#    cmd = '%s/signalp -t euk -f short -u .4 %s > OUT.signalp_out' % (paths, outputname)
#    print('running signalp')
#    os.system(cmd)
#
##        print("Signalp in incorrect location")
##        path = input('input path into folder containing signalp (ex: /home/user/destop/path/to/folder) >>')
##        cmd = '%s/signalp -t euk -f short -u .4 %s > OUT.signalp_out' % (path, outputname)
##        print('rerunning signalp')
##        os.system(cmd)
#
#    my_fileXXX = open('OUT.signalp_out').read()
#    signalp = []
#    #breaks into each row of data
#    step = my_fileXXX.split('\n')
#    #changes list into matrix
#    for each in step:
#        signalp.append(each.split())
#
#    #removes extra data
#    signalp.remove(signalp[0])
#    signalp.remove(signalp[0])
#    signalp.pop(-1)
#    #assigns values of restriction site and if it occurs
#    loc = []
#    yes = []
#    try:
#        for each in signalp:
#            loc.append(each[4])
#            yes.append(each[9])
#
#        print(loc)
#        print(yes)
#    except:
#        print('thinking')
#
#    print(len(aaa))
#
#    try:
#        i=0
#        for each in aaa:
#            #searches the signalp data, if there is a signal peptide, then it runs this block
#            if yes[i] == 'Y':
#                #finds and masks the signal sequence
#                    signal_sequence = each[0:(int(loc[i])-1)]
#                    masked_signal_sequence = signal_sequence.lower()
#                    aaa[i] = each.replace(signal_sequence, masked_signal_sequence)
#            i+=1
#    except:
#        print('Error, probable cause that signalp ran incorrectly due to similar ' + '\n' + 'header names, contact Paul Baskin')
#
#    #zippers the two lists together
#    dbdict2 = dict(zip(headerset,aaa))
#
#
#
#
#
#    #modifies the text file
#    OUT = open(outputname, 'w')
#    for key, value in dbdict2.items():
#        OUT.write(key)
#        OUT.write('\n')
#        chopper(value, 80, 160)
#    OUT.close()

    #TODO
    # =============================================================================
    #     #Folds the program.
    #     cmd = 'fold outputname'
    #     print(cmd)
    #     os.system(cmd)
    #
    # =============================================================================
    print('File nodubs_' + file_name + ' created.' )
    # =============================================================================
else:
    print("Usage python3 db_cleaner.py path/to/filename")

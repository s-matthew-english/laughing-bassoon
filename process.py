# this script is meant to operate on the output of the following command:
# 
# diff --report-identical-files --brief -r go-ethereum/ quorum/ >> diff_id_result.txt
# 
# from subprocess import check_output
# input_file = check_output(['diff', '--report-identical-files', '--brief', '-r', 'go-ethereum/', 'quorum/']).split('\n')

import re
import os

from difflib import SequenceMatcher



# function to return the % difference between common files
# that aren't identical
def percentage_difference(file1, file2):
    if ".git" in file1:
        return
    if "/tests/files/" in file1:
        return 
    else:
        # to close files after reading
        with open(file1) as f1, open(file2) as f2:
            text1 = f1.read()
            text2 = f2.read()
        m = SequenceMatcher(None, text1, text2)
        return m.ratio()

index = 0

with open("diff_id_result.txt", "r") as input_file:
    geth_files   = []
    geth_substring = "Only in go-ethereum/"
    quorum_files = []
    quorum_substring = "Only in quorum/"
    files_differ = dict() 
    differ_substring = "differ"
    files_identical = []
    identical_substring = "identical"


    for line in input_file:

        if differ_substring in line:
            print( index )
            regex = re.compile('{}(.*){}'.format(re.escape('and quorum/'), re.escape(' differ')))
            string_output = regex.findall(line)
            # files_differ.append( string_output[0] )
            file1 = os.path.join('go-ethereum', string_output[0])
            file2 = os.path.join('quorum', string_output[0])
            file_name = string_output[0]
            percent_diff = percentage_difference(file1, file2)
            files_differ[file_name] = percent_diff
            index = index + 1
        # if identical_substring in line:
        #     regex = re.compile('{}(.*){}'.format(re.escape('and quorum/'), re.escape(' are identical')))
        #     string_output = regex.findall(line)
        #     files_identical.append( string_output[0] )
        # if geth_substring in line:
        #     unique_to_geth = line[line.index(geth_substring) + len(geth_substring):]
        #     geth_files.append(unique_to_geth.rstrip('\n'))
        # if quorum_substring in line:
        #     unique_to_quorum = line[line.index(quorum_substring) + len(quorum_substring):]
        #     quorum_files.append(unique_to_quorum.rstrip('\n'))




# print('\n\nONLY IN QUORUM: ' + str( len(quorum_files) ) + '\n') 
# for quo_element in quorum_files: 
#     print( quo_element )
# print('\n\nONLY IN GO-ETHEREUM: ' + str( len(geth_files) ) + '\n')
# for geth_element in geth_files: 
#     print( geth_element )
# print('\n\nFILES IN BOTH, BUT DIFFERENT: ' + str( len(files_differ) ) + '\n')
# for diff_element in files_differ: 
#     print( diff_element )
# print('\n\nFILES ARE IDENTICAL: ' + str( len(files_identical) ) + '\n')
# for id_element in files_identical: 
#     print( id_element )

# print('\nONLY IN QUORUM: ' + str( len(quorum_files) ) ) 
# print('\nONLY IN GO-ETHEREUM: ' + str( len(geth_files) ) )
# print('\nFILES IN BOTH, BUT DIFFERENT: ' + str( len(files_differ) ) )
# print('\nFILES ARE IDENTICAL: ' + str( len(files_identical) ) + '\n')

for k, v in files_differ.iteritems():
    print k, v



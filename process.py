# this script is meant to operate on the output of the following command:
# 
# diff --brief -r go-ethereum/ quorum/ >> diff_result.txt
# 
import re

with open("diff_result.txt", "r") as input_file:
    geth_files   = []
    geth_substring = "Only in go-ethereum/"
    quorum_files = []
    quorum_substring = "Only in quorum/"
    files_differ = []
    files_substring = "Files go-ethereum/"

    for line in input_file:
        if geth_substring in line:
            unique_to_geth = line[line.index(geth_substring) + len(geth_substring):]
            geth_files.append(unique_to_geth.rstrip('\n'))
        if quorum_substring in line:
            unique_to_quorum = line[line.index(quorum_substring) + len(quorum_substring):]
            quorum_files.append(unique_to_quorum.rstrip('\n'))
        if files_substring in line:
            # find the files that are the same in both
            regex = re.compile('{}(.*){}'.format(re.escape('Files go-ethereum/'), re.escape(' and')))
            string_output = regex.findall(line)
            files_differ.append( string_output[0] )

print('\n\nONLY IN QUORUM:\n')
for quo_element in quorum_files: 
    print( quo_element )
print('\n\nONLY IN GO-ETHEREUM:\n')
for geth_element in geth_files: 
    print( geth_element )
print('\n\nFILES DIFFER:\n')
for diff_element in files_differ: 
    print( diff_element )







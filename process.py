# this script is meant to operate on the output of the following command:
# 
# diff --report-identical-files --brief -r go-ethereum/ quorum/ >> diff_id_result.txt
# 
import re

with open("diff_id_result.txt", "r") as input_file:
    geth_files   = []
    geth_substring = "Only in go-ethereum/"
    quorum_files = []
    quorum_substring = "Only in quorum/"
    files_differ = []
    differ_substring = "differ"
    files_identical = []
    identical_substring = "identical"

    for line in input_file:
        if geth_substring in line:
            unique_to_geth = line[line.index(geth_substring) + len(geth_substring):]
            geth_files.append(unique_to_geth.rstrip('\n'))
        if quorum_substring in line:
            unique_to_quorum = line[line.index(quorum_substring) + len(quorum_substring):]
            quorum_files.append(unique_to_quorum.rstrip('\n'))
        if differ_substring in line:
            regex = re.compile('{}(.*){}'.format(re.escape('and quorum/'), re.escape(' differ')))
            string_output = regex.findall(line)
            files_differ.append( string_output[0] )
        if identical_substring in line:
            regex = re.compile('{}(.*){}'.format(re.escape('and quorum/'), re.escape(' are identical')))
            string_output = regex.findall(line)
            files_identical.append( string_output[0] )

print('\n\nONLY IN QUORUM: ' + str( len(quorum_files) ) + '\n') 
for quo_element in quorum_files: 
    print( quo_element )
print('\n\nONLY IN GO-ETHEREUM: ' + str( len(geth_files) ) + '\n')
for geth_element in geth_files: 
    print( geth_element )
print('\n\nFILES IN BOTH, BUT DIFFERENT: ' + str( len(files_differ) ) + '\n')
for diff_element in files_differ: 
    print( diff_element )
print('\n\nFILES ARE IDENTICAL: ' + str( len(files_identical) ) + '\n')
for id_element in files_identical: 
    print( id_element )

print('\nONLY IN QUORUM: ' + str( len(quorum_files) ) ) 
print('\nONLY IN GO-ETHEREUM: ' + str( len(geth_files) ) )
print('\nFILES IN BOTH, BUT DIFFERENT: ' + str( len(files_differ) ) )
print('\nFILES ARE IDENTICAL: ' + str( len(files_identical) ) + '\n')







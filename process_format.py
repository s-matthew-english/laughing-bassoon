import re
import os

from difflib import SequenceMatcher
from filecmp import dircmp


class Node(object):
    def __init__(self):
        self.subdirs = {}
        self.files = []


def compare_directories(left, right, ignore=None):
    dcmp = dircmp(left, right, ignore=ignore)
    left_only, right_only, same_files, diff_files = Node(), Node(), Node(), Node()
    _accumulate_directories(dcmp, '/', left_only, right_only, same_files, diff_files)
    return left_only, right_only, same_files, diff_files


def _accumulate_directories(dcmp, dirname, left_only, right_only, same_files, diff_files):
    left_only.files = dcmp.left_only[:]
    right_only.files = dcmp.right_only[:]
    same_files.files = dcmp.same_files[:]
    diff_files.files = dcmp.diff_files[:]

    if len(dcmp.subdirs) > 0:
        for dirname in dcmp.subdirs:
            left_only.subdirs[dirname] = Node()
            right_only.subdirs[dirname] = Node()
            same_files.subdirs[dirname] = Node()
            diff_files.subdirs[dirname] = Node()
            _accumulate_directories(
                dcmp.subdirs[dirname],
                dirname,
                left_only.subdirs[dirname],
                right_only.subdirs[dirname],
                same_files.subdirs[dirname],
                diff_files.subdirs[dirname]
            )
            left_only.files.extend(left_only.subdirs[dirname].files)
            right_only.files.extend(right_only.subdirs[dirname].files)
            same_files.files.extend(same_files.subdirs[dirname].files)
            diff_files.files.extend(diff_files.subdirs[dirname].files)



if __name__ == '__main__':
    a, b, c, d = compare_directories('go-ethereum', 'quorum', ignore=['.git', 'tests'])

    

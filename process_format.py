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
    _accumulate_directories(
        dcmp,
        '/',
        left_only = left_only,
        right_only = right_only,
        same_files = same_files,
        diff_files = diff_files
    )
    return left_only, right_only, same_files, diff_files


def _accumulate_directories(dcmp, dirname, **nodes):
    node_names = 'left_only right_only same_files diff_files'.split()

    for name in node_names:
        nodes[name].files = getattr(dcmp, name)[:]

    if len(dcmp.subdirs) > 0:
        for dirname in dcmp.subdirs:
            for name in node_names:
                nodes[name].subdirs[dirname] = Node()

            _accumulate_directories(
                dcmp.subdirs[dirname],
                dirname,
                **{name : nodes[name].subdirs[dirname] for name in node_names}
            )
            for name in  node_names:
                nodes[name].files.extend(nodes[name].subdirs[dirname].files)


if __name__ == '__main__':
    a, b, c, d = compare_directories('go-ethereum', 'quorum')

    

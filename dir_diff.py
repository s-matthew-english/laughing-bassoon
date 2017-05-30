import re
import os

from difflib import SequenceMatcher
from filecmp import dircmp


class Node(object):
    def __init__(self):
        self.subdirs = {}
        self.files = []

    def __str__(self):
        return  '{\n   ' + Node._str(self, 1) + '}\n'

    @staticmethod
    def _str(node, depth):
        string = ''
        if len(node.files) > 0:
            string = '[' + ', '.join([os.path.basename(f) for f in node.files]) + ']'
        if len(node.subdirs) > 0:
            for subdir, subnode in node.subdirs.iteritems():
                string = '{string}\n{indent}{subdir}: {{\n{content_indent}{content}{indent}}}'.format(
                    string=string,
                    indent='   ' * depth,
                    subdir=subdir,
                    content_indent='   ' * (depth + 1),
                    content=Node._str(subnode, depth + 1)
                )
        return string + '\n'


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


def percentage_difference(file1, file2):
    with open(file1) as f1, open(file2) as f2:
        text1 = f1.read()
        text2 = f2.read()
    m = SequenceMatcher(None, text1, text2)
    return m.quick_ratio()


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
            for name in node_names:
                nodes[name].files.extend(
                    [os.path.join(dirname, x) for x in nodes[name].subdirs[dirname].files]
                )


if __name__ == '__main__':
    a, b, c, d = compare_directories('go-ethereum', 'quorum')
    print('GO-ETHEREUM ONLY: ' + str(len(a.files)) + '\n')
    print(a)
    print('------' + '\n')
    print('QUORUM ONLY: ' + str(len(b.files)) + '\n')
    print(b)
    print('------' + '\n')
    print('IDENTICAL FILES: ' + str(len(c.files)) + '\n')
    print(c)
    print('------' + '\n')
    print('IN BOTH, BUT DIFFERENT: ' + str(len(d.files)) + '\n')
    print(d)
    print('------' + '\n')
    print('RELATIVE DIFFERENCE FOR <<IN BOTH, BUT DIFFERENT>>:' + '\n')
    for f in d.files:
        print f, "=>", percentage_difference(os.path.join('go-ethereum', f), os.path.join('quorum', f)), '\n'

    

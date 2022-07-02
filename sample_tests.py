import unittest
from Linked_list_seq import ListSequence

# Change to True to visualize output
verbose = False

tests = (
        [('insert_last', 3), ('insert_first', 2), ('insert_last', 8), ('insert_first', 2), ('insert_last', 9), ('insert_first', 7), ('delete_last',), ('delete_last',), ('delete_first',)],
        [9, 8, 7, (2, 2, 0, 1, 0, 1, 0, 1)],
        )
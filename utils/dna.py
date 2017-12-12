"""Functions for representing DNA sequences."""

from __future__ import division
from __future__ import print_function

from collections import OrderedDict

import numpy as np
from six.moves import range

# Mapping of nucleotides to integers
CHAR_TO_INT = OrderedDict([('A', 0), ('G', 1), ('C', 2), ('U', 3)])
# Mapping of integers to nucleotides
INT_TO_CHAR = {v: k for k, v in CHAR_TO_INT.items()}

# Mapping of notations to integers
NOTA_TO_INT = OrderedDict([('(', 0), (')', 1), ('.', 2), (':', 3)])
# Mapping of integers to nucleotides
INT_TO_NOTA = {v: k for k, v in NOTA_TO_INT.items()}

def get_alphabet(special=False, reverse=False):
    """
    Return char->int alphabet.
    Parameters
    ----------
    special: bool
        If `True`, remove special 'N' character.
    reverse: bool
        If `True`, return int->char instead of char->int alphabet.
    Returns
    -------
    OrderedDict
        DNA alphabet.
    """
    alpha = OrderedDict(CHAR_TO_INT)
    if not special:
        del alpha['N']
    if reverse:
        alpha = {v: k for k, v in alpha.items()}
    return alpha
 

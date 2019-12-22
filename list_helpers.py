# Define few list helper functions.
import numpy as np

def list_append_list(list_1,list_2):
    """
    Given two lists of lists list_1 and list_2,
    take each element of list_2 and append to list_1.
    """
    for l1,l2 in zip(list_1,list_2):
        l1.append(l2)
        
def list_np(list_):
    """
    Convert to numpy
    """
    list__ = []
    for l in list_:
        list__.append(np.asarray(l))
    return list__

def list_mean(list_):
    """
    Take a list of numpy arrays and return a list of their means.
    """
    list_m = []
    for l in list_:
        list_m.append(l.mean(axis=0))
    return list_m

def list_std(list_):
    """
    Take a list of numpy arrays and return a list of their means.
    """
    list_s = []
    for l in list_:
        list_s.append(l.std(axis=0))
    return list_s

def list_log_spaced(list_):
    spacing = np.asarray([ 0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   11,    
                          13,   14,   17,   19,   22,   25,   29,   33,   38,   43,   49,    
                          56,   65,   74,   84,   96,  110,  125,  143,  164,  187,  213,    
                         243,  277,  316,  361,  412,  470,  536,  612,  698,  796,  908,    
                        1035, 1181, 1347, 1537, 1753, 1999])
    assert (type(list_) == list), "Give a list"
    list__ = []
    for l in list_ :
        indices = spacing[np.where(spacing < len(l))]
        list__.append(l[indices])
    return list__

def list_pairwise_dict(list_1, list_2):
    dict_ = {}
    for l1,l2 in zip(list_1,list_2):
        dict_[l1] = l2
    return dict_


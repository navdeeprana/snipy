# Define few list helper functions.
import numpy as np

def list_apply_condition(condition,list_in):
    return [l[condition] for l in list_in]

def list_apply_function(function,list_in):
    return [function(l) for l in list_in]

def list_append_list(list_1,list_2):
    for l1, l2 in zip(list_1,list_2):
        l1.append(l2)
        
def list_to_numpy(list_in,T=False):
    list_out = []
    for l in list_in:
        if T: list_out.append(np.asarray(l).T)
        else: list_out.append(np.asarray(l))
    return list_out

def list_np_mean(list_in):
    list_out = []
    for l in list_in:
        list_out.append(l.mean(axis=0))
    return list_out

def list_np_std(list_in):
    list_out = []
    for l in list_in:
        list_out.append(l.std(axis=0))
    return list_out

def list_np_log_spaced(list_in):
    spacing = np.asarray([ 0,    1,    2,    3,    4,    5,    6,    7,    8,    9,   11,    
                          13,   14,   17,   19,   22,   25,   29,   33,   38,   43,   49,    
                          56,   65,   74,   84,   96,  110,  125,  143,  164,  187,  213,    
                         243,  277,  316,  361,  412,  470,  536,  612,  698,  796,  908,    
                        1035, 1181, 1347, 1537, 1753, 1999])
    assert (type(list_in) == list), "Give a list"
    list_out = []
    for l in list_in :
        indices = spacing[np.where(spacing < len(l))]
        list_out.append(l[indices])
    return list_out

def list_pairwise_dict(list_1, list_2):
    dict_ = {}
    for l1,l2 in zip(list_1,list_2):
        dict_[l1] = l2
    return dict_

def list_uneven_strides(list_in,stamps,strides):
    list_out = []
    for l in list_in:
        sl, lout = 0, []
        for sr,jump in zip(stamps,strides):
            lout = lout + list(l[sl:sr:jump])
            sl   = sr
        list_out.append(np.asarray(lout))
    return list_out

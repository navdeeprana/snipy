# Define few list helper functions.


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

def list_stats(list_):
    """
    Take a list of numpy arrays and return a list of their means and stats.
    """
    list_m, list_s   = [], []
    for l in list_:
        list_m.append(l.mean(axis=0))
        list_s.append(l.std(axis=0))
    return list_m, list_s

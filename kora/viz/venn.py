""" Show elements in Venn Diagram """

from matplotlib_venn import venn3



def plot(A, B, U=['others'], names=['A', 'B', 'U']):
    """
    Show elements in 2 sets and optional others in U
    from https://stackoverflow.com/a/54604659/6729010
    """
    A = set(A)
    B = set(B)
    U = set(U) - A - B  # U can have all or only missing elements
    if len(names)==2:
        names.append('U')  # Add U if given only A, B 
    v = venn3([A,B,U], names)
    # set labels to be elements
    v.get_label_by_id('100').set_text(get_elem_str(A-B))
    v.get_label_by_id('110').set_text(get_elem_str(A&B))
    v.get_label_by_id('010').set_text(get_elem_str(B-A))
    v.get_label_by_id('001').set_text(get_elem_str(U))
    v.get_patch_by_id('001').set_color('white')
    return v


def get_elem_str(A: set):
    """ 1 column only, may use more in the futre """
    return '\n'.join(map(str,A))

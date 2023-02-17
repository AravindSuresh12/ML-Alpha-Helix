#UniProt testing case

import re 

def is_uniprot(pid):
    """
    Check whether or not the input protein ID is valid
    Args:
        pid [str]: a protein ID to check
    Returns:
        [bool] True if `pid` is a valid UniProt ID and otherwise False
    """
    
    bool=False
    
    if re.search('[OPQ]',pid[0]):
        if len(pid)==6:
            m1=re.search('[OPQ][0-9][A-Z,0-9][A-Z,0-9][A-Z,0-9][0-9]',pid)
            if m1 is not None:
                bool=True
            else:
                bool=False
        elif (len(pid)==8):
            if pid[6]=="-":
                m1=re.search('[OPQ][0-9][A-Z,0-9][A-Z,0-9][A-Z,0-9][0-9][-][0-9]',pid)
                if m1 is not None:
                    bool=True
            else:
                bool=False


    if re.search('[A-N,R-Z]',pid[0]):
        if len(pid)==6:
            m2=re.search('[A-N,R-Z][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9]',pid)
            if m2 is not None:
                bool=True
            else:
                bool=False
        elif (len(pid)==8) and (pid[6]=='-'):
            m2=re.search('[A-N,R-Z][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9]',pid)
            if m2 is not None:
                bool=True
            else:
                bool=False        
        elif len(pid)==10:
            m3=re.search('[A-N,R-Z][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9]',pid)
            if m3 is not None:
                bool=True
            else:
                bool=False
        elif (len(pid)==12) and (pid[10]=='-'):
            m3=re.search('[A-N,R-Z][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9][A-Z][A-Z,0-9][A-Z,0-9][0-9][-][0-9]',pid)
            if m3 is not None:
                bool=True
            else:
                bool=False

    return(bool)
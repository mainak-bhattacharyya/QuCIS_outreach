from iiserb_function import *


### 1a
def iiserb_grader1(M,N,O,E,F,G):
    
    try:
        aae(M@N@O, H@E@F@G@H)
    except:
        return 'E,F,G are not correct'
    else:
        if np.all(E == F):
            return 'Unitary matrices are not unique'
        elif np.all(E == G):
            return 'Unitary matrices are not unique'
        else:
            return 'Congratulations, your answer is correct \U0001F389'



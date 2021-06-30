
def length_of_lastword(str):
 
    str = str.split()
    if len(str) == 0:
            return 0;
    else:
     return len(str[-1]);



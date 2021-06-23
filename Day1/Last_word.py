# code to find the length of the last word in a sentence using while loop
def length_of_lastword(str):
 
    count = 0;
    length = len(str)-1;
    while(length != 0):
        if(str[length] == ' '):
            return count;
        else:
            count += 1;
        length -= 1;
    return count;

str = "Welcome to SkaeHub Technologies";
print("The length of last word is", length_of_lastword(str));

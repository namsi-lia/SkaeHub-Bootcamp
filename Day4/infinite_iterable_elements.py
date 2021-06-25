#code implementation of infinite iterators 

#import module:
import itertools

def iterable_data(iterable):
    return itertools.cycle(iterable)


lst =['Wants','Needs','benefits']

result=iterable_data(lst)


for i in result:
    print(i)


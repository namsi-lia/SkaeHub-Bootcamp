#code implementation of removing duplicates from list implemented using sort

fruits = ['orange', 'banana', 'pineapple', 'apple', 'orange', 'apple', 'guava', 'kiwi', 'litchi','banana']
fruits_update = list(set(fruits))
fruits_update.sort(key=fruits.index)
print(fruits_update)   


#record1 = [1,2,3]
#record2 = ['a','b','c']
#record3 = [3,2,1]

#dictionary = {'list1':record1, 'list2':record2, 'list3':record3}

#keys = ["record1", "record2", "record3"]
#values = [[1,2,3], ['a','b', 'c']]

#zipped = zip(keys, values)
#print(zipped)

S = 'spam'

for i in range(len(S)):
    print(S, end=' ')
    S = S[1:] + S[:1]
    
print() 

#LIST
randomlist=[1,4,67,32,98]
print(randomlist)
randomlist.extend([45,98,12])
print(randomlist)

for i in randomlist:
    print(i)

#DICTIONARY
sampledict={"name":"John", "age":25, "address":"New York"}
sampledict["phone"]=1234567890
print(sampledict)

#SET
sampleset={1,2,3,4,5}
sampleset.add(6)
sampleset.remove(3)
print(sampleset)

#TUPLE
sampletuple=(1,2,3,4)
print(len(sampletuple))
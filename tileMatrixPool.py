import time
tilePool = []
tilePoolCount = []

for i in range(0,11):
    for j in range(0,11):
        print '*********', i, '*', j, '=', i*j
        if i*j not in tilePool:
            tilePool.append(i*j)
            tilePoolCount.append(1)
        else:
            tilePoolCount[tilePool.index(i*j)]+=1
#        time.sleep(1)    
            
    print '-----------------'

print tilePool
print tilePoolCount
print len(tilePool), len(tilePoolCount)

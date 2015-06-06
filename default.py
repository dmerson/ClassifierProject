import kNN

group, labels = kNN.createDataSet()

print (group)

print (labels)
oneToTest=[0.0,1.0]
print (kNN.classify0(oneToTest,group,labels))

myDict={0:12,1:44,2:22,3:44}
print(len(myDict))
for i in range(0,len(myDict)):
        k = input("Enter the key")
        v = input("ENter the value")
        if(myDict[i] == v):

                print("Already exist")
		print(myDict)
        else:
                myDict.update({k:v})
                print("Updated")
		print(myDict)

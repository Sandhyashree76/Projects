list1=[1,2,3,5,6,7,10,12,15,19,1,78,8,8]
for i in range(0,len(list1)):
    for j in range(i+1,len(list1)):
        if(list1[i]==list1[j]):
            print(list1[j])

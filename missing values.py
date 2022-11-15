list1=[1,2,3,5,6,7,10]
missing_value=[]
for i in range (list1[0],list1[-1]+1):
    if i not in list1:
        missing_value.append(i)
print(missing_value)        
       

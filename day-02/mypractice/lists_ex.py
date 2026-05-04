a=[100,200,3.1,True]

print(type(a))
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[3])


a = [100, 200, 3.1, True,"Rahul"]
a.append(500)                                                               
for item in a:
    print(item)



clouds=list()
clouds.append("aws")
clouds.append("azure")

#for item in clouds:
print(clouds) 
print("length of cloud list:", len(clouds))
print(dir(clouds))
print(clouds.count.__doc__)
info = {
     "name": "Rahul kumar",
     "age" : 24,
     "city": "Bangalore",
     "package" : 3.5,                               
     "married" : False,
     "favourites" : ["python", "linux", "devops"]
     
}


print(info["city"])
print("I am married: ", info["married"])

info.update({"village": "alwalpur"})
print(info)

for items, value in info.items():
    print(items,value)    
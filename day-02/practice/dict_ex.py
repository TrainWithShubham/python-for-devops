info = {
    "name" : "Shubham Bhaiya", #str
    "city" : "Pune", #str
    "qualification": "Mtech",
    "age" : 29, # int
    "salary": 22.5, # float
    "married": True, # Bool
    "favourites" : ["teaching", "movies", 18]
}

print("I live in",info["city"])
print("I love ", info.get("favourite","Not Found"))

info.update({"channel": "TrainWithShubham"})

print(dir(info))

for key,value in info.items():
    print(key,value)
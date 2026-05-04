def read_logs():
    
    with open ("app.log", "r") as file :

     print(file.read())

read_logs() 
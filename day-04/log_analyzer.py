
import json

with open("app.log", "r") as log_file:
    content = log_file.read()

    counts = {
        "INFO": content.count("INFO"),
        "WARNING": content.count("WARNING"),
        "ERROR": content.count("ERROR"),
    }

    print(counts)


    with open("output.json", "w") as file:
        json.dump(counts, file)

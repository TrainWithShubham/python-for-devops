import json


class LogAnalyzer:
    
    
    def __init__(self, log_path, output_path):
       
        self.log_path = log_path
        self.output_path = output_path
        self.counts = {} # An empty dictionary to hold our results later


    def analyze(self):
       
        with open(self.log_path, "r") as log_file:
            content = log_file.read()

            
            self.counts = {
                "INFO": content.count("INFO"),
                "WARNING": content.count("WARNING"),
                "ERROR": content.count("ERROR"),
            }

    def show_results(self):
        
        print(self.counts)

    
    def save_to_file(self):
       
        with open(self.output_path, "w") as file:
            json.dump(self.counts, file)



my_analyzer = LogAnalyzer("app.log", "output.json")


my_analyzer.analyze()
my_analyzer.show_results()
my_analyzer.save_to_file()
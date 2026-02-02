import json

class LogAnalyzer: # creating class
    """
        class has 2 things
        data members (variables) & member functions (functions)
    """
    def __init__(self,file_name,output_file):
        self.file_name = file_name
        self.output_file = output_file

    def read_logs(self):
        #option 2
        with open(self.file_name,"r") as file: # file open
            return file.readlines() # file operation
        
    def write_json(self,counts):
        with open(self.output_file,"w+") as json_file:
            json.dump(counts,json_file)

    def analyze(self):
        log_count = {
            "INFO": 0,
            "WARNING":0,
            "ERROR":0
        }
        lines = self.read_logs()

        for line in lines:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"]+1})
            elif "WARNING" in line:
                log_count.update({"WARNING": log_count["WARNING"]+1})
            elif "ERROR" in line:
                log_count.update({"ERROR": log_count["ERROR"]+1})
            else:
                pass

        self.write_json(log_count)



# modular
log_1 = LogAnalyzer("app.log","output1.json") # creating object
log_count = log_1.analyze()

# reusable clear # extensible
log_1 = LogAnalyzer("app2.log","output2.json") # creating object
log_count = log_1.analyze()
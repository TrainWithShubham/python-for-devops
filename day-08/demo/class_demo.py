import json

class LogAnalyzer:
    def read_logs(self):
        with open("app.log","r") as f:
            return f.readlines()

    def analyze(self,log_count, data):
            
        for line in data:
            if "INFO" in line:
                log_count.update({"INFO": log_count["INFO"] + 1})
            elif "ERROR" not in line:
                log_count.update({"ERROR": log_count["ERROR"] + 1})
            elif "WARNING" not in line:
                log_count.update({"WARNING": log_count["WARNING"] + 1})
            else:
                pass

        return log_count

    
    def write_json(self,counts):
        with open("log_counts.json" , "w+") as json_file:
            json.dump(counts, json_file)

def main():
    analyzer = LogAnalyzer()

    log_count = {
        "INFO": 0,
        "ERROR":0,
        "WARNING":0
    }
    data = analyzer.read_logs()
    counts = analyzer.analyze(log_count,data)
    analyzer.write_json(counts)

if __name__ == "__main__":
    main()
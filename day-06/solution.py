import json
import argparse


class LogAnalyzer:
    
    
    def __init__(self, log_path, output_path=None, level=None):
        self.log_path = log_path
        self.output_path = output_path
        self.level = level
        self.counts = {}

    def analyze(self):
        """Reads the log file, handles missing files, and counts occurrences."""
        try:
            with open(self.log_path, "r") as log_file:
                content = log_file.read()

               
                if self.level:
                    self.counts = {self.level: content.count(self.level)}
                else:
                   
                    self.counts = {
                        "INFO": content.count("INFO"),
                        "WARNING": content.count("WARNING"),
                        "ERROR": content.count("ERROR"),
                    }
            return True 
            
        except FileNotFoundError:
            
            print(f"❌ Error: The file '{self.log_path}' was not found. Please check the path.")
            return False

    def show_results(self):
        """Prints the counts to the terminal."""
        print("\n📊 Log Analysis Summary:")
        for key, value in self.counts.items():
            print(f"  - {key}: {value}")

    def save_to_file(self):
        """Saves the dictionary to a JSON file if an output path was provided."""
        if self.output_path:
            with open(self.output_path, "w") as file:
                json.dump(self.counts, file, indent=4)
            print(f"\n✅ Results successfully saved to: {self.output_path}")


if __name__ == "__main__":
    

    parser = argparse.ArgumentParser(description="A DevOps CLI tool to analyze server logs.")

   
    parser.add_argument("--file", required=True, help="Path to the input log file (e.g., app.log)")
    parser.add_argument("--out", required=False, help="Path to save the JSON output (e.g., summary.json)")
    parser.add_argument("--level", required=False, choices=["INFO", "WARNING", "ERROR"], help="Filter by a specific log level")

   
    args = parser.parse_args()

    my_analyzer = LogAnalyzer(log_path=args.file, output_path=args.out, level=args.level)

    success = my_analyzer.analyze()
    
    if success:
        my_analyzer.show_results()
        
        if args.out:
            my_analyzer.save_to_file()
I have picked the code from day -06 where we have modify the code from day -05

1)Understanding what problem that script is solving

In my previous script everything was fine but we were assigned our specific file that we have toc heck the logs from that one log file only. What if we have new log files and we have to check the logs for that then we have to manually edit the code for analyzing different log file 


2)What is the problem?

we were not able to automate the code for any log file because it was name specific code for app.log  

3)What input does it need?

Here we are using the concept of argument where we are passing the argument making the script more functional

4)What output should it give?

It will analyze the file which we pass in argument 

________________________________________________________________________________________________________________________________________________________________________________________


🎯 1. What problem am I solving?

Here I am automating the process of reading log files instead of manually counting  how many are INFO,WARNING,and ERROR messages . My scripts can do same thing in milliseconds even with passing arguments as file name 


📥 2. What input does my script need?

It needs command-line arguments (flags) passed directly through the terminal via argparse.

Required Input: The path to the log file you want to read (e.g., --file app.log).

Optional Input 1: A specific log level to filter by (e.g., --level ERROR).

Optional Input 2: The name of a file to save the results into (e.g., --out summary.json).

📤 3. What output should my script give?

script provides two types of output depending on what the user asks for:

Terminal Output (Always): A clean, easy-to-read summary printed directly to the console showing the count of each log level.

File Output (Conditional): If the user provided the --out flag, it generates a physical .json file on the hard drive containing the dictionary of counts.

Validation Output: If the user types a file name that doesn't exist, it outputs a friendly error message instead of crashing the program.

⚙️ 4. What are the main steps?

When you press "Enter" in the terminal, your code executes these exact steps in order:

Catch the Flags (argparse):  reads the terminal command, validates that the inputs are allowed, and pass  them into the args object.

Build the Machine (Initialization): The script creates the my_analyzer object from your LogAnalyzer class and feeds it the file paths from argparse.

Read and Count (analyze): The machine safely opens the text file, scans the content, counts the requested log levels, and stores the numbers in its internal self.counts memory.

Display (show_results): The machine prints its internal memory to the screen.

Export (save_to_file): If an --out destination was provided, the machine formats its internal memory into JSON and saves it to the disk.

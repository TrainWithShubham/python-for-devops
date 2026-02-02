# Day 04 – File Handling & Log Analysis for DevOps

## Task

Today’s goal is to **work with files and analyze logs using Python**.

You will create a Python script that:
- Reads a log file (example: application or system log)
- Identifies and counts:
  - INFO
  - WARNING
  - ERROR messages
- Prints a summary to the **terminal**
- Writes the summary to an **output file**

This task introduces you to one of the most common DevOps activities: **log analysis**.


## Expected Output

- One Python script (example: `log_analyzer.py`)
- One input log file (example: `app.log`)
- One output file (example: `log_summary.txt` or `log_summary.json`)
- Output visible:
  - In terminal
  - In output file


## Guidelines

- Use:
  - File read operations (`open`, `read`, `readlines`)
  - String operations to search log levels
  - Dictionaries to maintain counts
  - Functions for clean structure
- Handle basic errors using `try / except`
  - File not found
  - Empty file
- Follow PEP8 and basic Python best practices
- Keep logic simple and readable


## Resources

- Python file handling:
  https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

- String methods:
  https://docs.python.org/3/library/stdtypes.html#string-methods

- PEP8 – Python Style Guide:
  https://peps.python.org/pep-0008/

- Sample logs (provided in repository or create your own)


## Why This Matters for DevOps

In real-world DevOps work:
- Logs are the **first place** you debug failures
- Production issues are diagnosed using log patterns
- Automated log analysis saves time and reduces manual effort

This task builds your foundation for:
- Monitoring
- Troubleshooting
- Incident response


## Submission

1. Add your script and log files inside the `day-04` folder
2. Ensure the script runs successfully
3. Verify that summary output is generated
4. Commit and push your changes to your fork


## Learn in Public

Share your progress on LinkedIn:
- Post a small code snippet from your log analysis script
- Share the output summary
- Write 2–3 lines on what you learned about logs and Python today

Optional:
- Tag **TrainWithShubham** or **Shubham Londhe**
- Use hashtags: `#PythonForDevOps #TrainWithShubham #DevOpsKaJosh` (Helps me to filter post and Like/ Comment / Repost / engage)


Happy Learning  
[TrainWithShubham](https://www.trainwithshubham.com/)

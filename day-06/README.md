# Day 06 – Building a CLI Tool for DevOps (argparse)

## Task

Today’s goal is to convert your Python script into a **CLI (Command Line Interface) tool**.

You will take your **Day 05 OOP Log Analyzer** and enhance it so it can be executed like a real DevOps tool using command-line arguments.

Your CLI tool should:
- Accept log file path using `--file`
- Accept output file path using `--out`
- (Optional) Accept log level filter using `--level` (example: ERROR)
- Print summary to terminal
- Write summary to an output file

This task helps you build tools that work like real DevOps utilities.


## Expected Output

- One Python script (example: `log_analyzer_cli.py`)
- Script should run like:
  - `python log_analyzer_cli.py --file app.log --out summary.txt`
- Output should be visible:
  - In terminal
  - In output file


## Guidelines

- Use:
  - `argparse` to parse CLI arguments
  - Functions and clean code structure
  - Your Day 05 class-based logic (reuse it, do not rewrite everything)
- Required arguments:
  - `--file` (log file path)
- Optional arguments:
  - `--out` (output file path)
  - `--level` (filter only one level like ERROR)
- Follow PEP8 and best practices
- Add basic validation:
  - If file is missing, show a friendly error message


## Resources

- argparse documentation:
  https://docs.python.org/3/library/argparse.html

- PEP8 – Python Style Guide:
  https://peps.python.org/pep-0008/

- Your Day 05 OOP script


## Why This Matters for DevOps

Most DevOps tools are CLI-based:
- kubectl
- terraform
- aws cli
- helm

DevOps engineers build internal CLI tools to:
- analyze logs quickly
- automate checks
- run scripts consistently across environments

This task trains you to write automation the DevOps way.


## Submission

1. Add your CLI-based script inside the `day-06` folder
2. Ensure the script runs using CLI arguments
3. Verify output is generated
4. Commit and push your changes to your fork


## Learn in Public

Share your progress on LinkedIn:
- Post a small snippet showing your `argparse` setup or CLI usage
- Share output (terminal + output file)
- Write 2–3 lines on what you learned today

Optional:
- Tag **TrainWithShubham** or **Shubham Londhe**
- Use hashtags: `#PythonForDevOps #TrainWithShubham #DevOpsKaJosh` (Helps me to filter post and Like/ Comment / Repost / engage)


Happy Learning  
[TrainWithShubham](https://www.trainwithshubham.com/)

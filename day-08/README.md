# Day 08 – AWS Automation with Python (Boto3 + CDK)

## Task

Today’s goal is to understand **how Python works with AWS**.

You will learn two important things that DevOps engineers do in real life:

1. Use **Python (Boto3)** to read information from AWS  
2. Understand how **Infrastructure as Code (IaC)** works using **AWS CDK** (Optional)

Do not worry — today is **safe and beginner-friendly**.
You are **NOT deleting or modifying** anything in AWS.


## Part 1 – AWS Automation using Python (Boto3)

You will write a Python script that:

- Connects to your AWS account
- Lists:
  - EC2 instances (instance ID and state)
  - S3 buckets (bucket names)
- Prints the output in the **terminal**
- Saves the output into a **JSON file**

This helps you understand how AWS services talk using APIs and how Python can automate that.


## Expected Output (Boto3)

- One Python script (example: `aws_resource_report.py`)
- One JSON file (example: `aws_report.json`)
- Output visible:
  - In terminal
  - In JSON file


## Part 2 – Introduction to Infrastructure as Code using AWS CDK [Optional]

This is completely optional for you, & in this part, you will **not focus on automation**, but on **understanding the idea**.

You will learn:
- What is Infrastructure as Code (IaC)
- How AWS CDK lets you define AWS resources using Python
- How CDK code is converted into CloudFormation

You will create a **very basic CDK example**:
- A simple CDK app
- One stack defining an S3 bucket

Deployment is **optional**.  
Understanding the flow is more important than running the command.


## Expected Output (CDK)

- One CDK app folder (example: `cdk-demo/`)
- One stack file (example: `cdk_demo_stack.py`)


## Optional – Hello World using AWS Lambda (Bonus)

This is **optional** and only for learning purposes.

You may:
- Create a simple AWS Lambda function
- Use Python runtime
- Return a basic "Hello World" response

This is only to understand:
- How Python runs in the cloud
- What “serverless” means

Note: This is **NOT mandatory** and can be skipped if you are new to AWS. This will be covered in-depth in [DevOps - Zero To Hero Josh Batch 10](https://bit.ly/devops-josh)


## Guidelines

- Use:
  - `boto3` only for **read-only operations** (even though it can be used to Create, Read, Update, Delete, Resources [CRUD]) - best to use IaC Tools for CRUD operations eg. Terraform, CloudFormation, etc.
  - AWS credentials already configured locally
- Do NOT:
  - Delete resources
  - Modify resources
- Keep scripts simple
- Focus on understanding, not memorizing syntax


## Resources

### AWS Setup
- AWS CLI & credentials configuration:  
  https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html

### Boto3
- Boto3 documentation:  
  https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

- EC2 with Boto3:  
  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html

- S3 with Boto3:  
  https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

### AWS CDK
- AWS CDK Introduction:  
  https://docs.aws.amazon.com/cdk/v2/guide/home.html

- CDK with Python:  
  https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html


## Why This Matters for DevOps

In real DevOps work:
- AWS is managed using APIs, not clicks
- Python is used to automate cloud tasks
- Infrastructure is written as code, not manual setup

Today’s learning helps you:
- Gain confidence with AWS
- Understand cloud automation
- Prepare for production DevOps work


## Submission

1. Add your Boto3 script inside the `day-08` folder
2. Ensure AWS credentials are working
3. Verify JSON report is generated
4. (Optional) Add your CDK demo folder
5. Commit and push your changes to your fork


## Learn in Public

Share your progress on LinkedIn:
- Share a small snippet of your Boto3 or CDK code
- Share terminal output or JSON output
- Write 2–3 lines on what you learned about AWS + Python

Optional:
- Tag **TrainWithShubham** or **Shubham Londhe**
- Use hashtags: `#PythonForDevOps #TrainWithShubham #DevOpsKaJosh`  (Helps me to filter post and Like/ Comment / Repost / engage)


Happy Learning  
[TrainWithShubham](https://www.trainwithshubham.com/)

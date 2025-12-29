# Day 09 – Building a Simple DevOps API with FastAPI (Capstone Project 1)

## Task 1

Today’s goal is to **convert your Python logic into a simple API**.

Till now, you have:
- Written Python scripts
- Run them from terminal
- Used AWS and automation

Today, you will learn how DevOps engineers:
- Wrap Python logic inside an API
- Expose it using HTTP endpoints
- Build internal tools for teams

You will use **FastAPI** to build a **simple DevOps-style API**.


## What You Will Build

You will create a small FastAPI application with endpoints like:

- `/health`  
  Returns a simple health status

- `/logs`  
  Runs your log analyzer logic and returns summary

- `/aws` (optional)  
  Returns AWS resource summary (from Day-08 logic)

This API will run **locally**.
Cloud deployment is optional and not mandatory.


## Expected Output

- One FastAPI application file (example: `main.py`)
- API running locally on:
  - `http://127.0.0.1:8000`
- Endpoints accessible via:
  - Browser
  - `curl`
  - Postman
- JSON responses from endpoints


## Guidelines

- Use:
  - `FastAPI`
  - `uvicorn` to run the app
- Keep endpoints **simple**
- Reuse your existing Python logic where possible
- Do NOT over-engineer
- Focus on understanding:
  - Request → Response flow
  - How Python logic becomes an API


## Resources

- FastAPI documentation:
  https://fastapi.tiangolo.com/

- FastAPI first steps:
  https://fastapi.tiangolo.com/tutorial/first-steps/

- Uvicorn:
  https://www.uvicorn.org/

- Your Day 04–Day 06 scripts


## Why This Matters for DevOps

In real DevOps work:
- Teams build internal tools and platforms
- APIs are used to trigger automation
- Monitoring, reporting, and health checks are exposed via APIs

FastAPI helps DevOps engineers:
- Build lightweight internal services
- Expose automation safely
- Integrate tools with dashboards and pipelines


## Submission

1. Add your FastAPI app inside the `day-09` folder
2. Ensure the app runs locally using `uvicorn`
3. Test endpoints using browser / curl / Postman
4. Commit and push your changes to your fork


## Learn in Public

Share your progress on LinkedIn:
- Share a screenshot of FastAPI docs page (`/docs`)
- Share one API response
- Write 2–3 lines on what you learned about APIs today

Optional:
- Tag **TrainWithShubham** or **Shubham Londhe**
- Use hashtags: `#PythonForDevOps #TrainWithShubham #DevOpsKaJosh` (Helps me to filter post and Like/ Comment / Repost / engage)


Happy Learning  
[TrainWithShubham](https://www.trainwithshubham.com/)

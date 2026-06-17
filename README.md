# Resume Matcher API

A FastAPI-based REST API that analyzes resume-to-job compatibility by extracting technical skills, calculating match scores, identifying skill gaps, and ranking multiple job descriptions.

## Features
- RESTful API built with FastAPI for resume-to-job analysis
- Rule-based skill extraction using regular expressions and keyword matching
- Automated comparison of resume skills against multiple job descriptions
- Match score calculation based on skill overlap percentages
- Skill gap analysis highlighting missing qualifications for each role
- Best-fit job identification using score-based ranking with skill-gap tie breaking
- Interactive API documentation generated automatically via Swagger/OpenAPI
- JSON-based request and response handling for easy integration with web applications

## Technologies
- Python
- FastAPI
- Uvicorn
- Git
- WSL/Linux

## Technical Highlights
- Backend developed in Python using FastAPI
- Pydantic models used for request validation and data serialization
- Regex-based parsing for ambiguous skills (e.g., C++, C#, Java)
- Set operations used for efficient skill matching and gap detection
- Uvicorn ASGI server for local API deployment and testing
- Developed and version-controlled using Git
- Executed in a Linux (WSL) development environment

## Project Evolution
This project began as a command-line Python application and was later refactored into a REST API using FastAPI to support structured JSON requests and responses.

## Future Enhancements

- Support PDF and DOCX resume uploads in addition to plain text input.
- Expand the skill database by storing skills in an external configuration file or database rather than hardcoding them.
- Implement NLP-based skill extraction using libraries to improve recognition of skills and reduce reliance on exact keyword matches.
- Add skill weighting to prioritize important technologies over less critical skills when calculating match scores.
- Introduce fuzzy matching to recognize related technologies and alternative skill names.
- Store analysis results in a PostgreSQL database for historical tracking and reporting.
- Develop a React frontend to provide a user-friendly interface for resume analysis.
- Deploy the API to a cloud platform such as AWS, Azure, or Render for public access.

## Technical Notes

- Skill extraction is performed once on the resume and reused across all job comparisons to avoid redundant processing.
- Set intersection and difference operations are used to efficiently compute matches and skill gaps.

## Installation

```bash
git clone <repository-url>
cd resume_job_comparison_tool

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```
## Running the API

```bash
uvicorn main:app --reload
```
Navigate to:

http://127.0.0.1:8000/docs

to access the interactive Swagger UI.

## Example Request

```json
{
  "resume": "I have 10 years of C++ and Python experience. I am skilled with Git version control, JavaScript and CSS.",
  "jobs": [
        "Must know HTML CSS and JavaScript.", 
        "Git is an asset, as well as familiarity with machine learning and OOP concepts", 
        "Proficient with Microsoft Office, namely Excel"
  ]
}
```
## Example Response

```json
{
  "results": [
    {
      "job_number": 1,
      "match_score": 66.67,
      "matched_skills": [
        "css",
        "javascript"
      ],
      "missing_skills": [
        "html"
      ]
    },
    {
      "job_number": 2,
      "match_score": 33.33,
      "matched_skills": [
        "git"
      ],
      "missing_skills": [
        "machine learning",
        "oop"
      ]
    },
    {
      "job_number": 3,
      "match_score": 0,
      "matched_skills": [],
      "missing_skills": [
        "excel",
        "microsoft"
      ]
    }
  ],
  "best_job": {
    "job_number": 1,
    "match_score": 66.67
  }
}
```
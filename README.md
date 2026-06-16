# Resume Matcher API

Built with FastAPI.

## Features
- RESTful API built with FastAPI for resume-to-job analysis
- Rule-based skill extraction using regular expressions and keyword matching
- Automated comparison of resume skills against multiple job descriptions
- Match score calculation based on skill overlap percentages
- Skill gap analysis highlighting missing qualifications for each role
- Best-fit job identification using score-based ranking and tie-breaking logic
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

## Run

uvicorn main:app --reload
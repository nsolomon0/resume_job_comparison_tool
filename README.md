# Resume Matcher API

A FastAPI-based REST API that analyzes resume-to-job compatibility by extracting technical skills, calculating match scores, identifying skill gaps, and ranking multiple job descriptions.

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

## Run

uvicorn main:app --reload
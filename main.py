from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

class AnalyzeRequest(BaseModel):
    resume:str
    jobs: List[str]

@app.get("/")
def root():
    return {"message": "Resume Comparison API"}

SKILLS = {
    "node.js","express","nextjs","python",
    "django","fastapi","flask","rest apis",
    "web services","postgresql","mongodb",
    "dynamodb","front-end","html","css","javascript","typescript","react",
    "angular","docker","git","aws",
    "communication","machine learning",".net",
    "data structures and algorithms","sql",
    "computer vision","cloud computing","linux",
    "graphql","problem-solving","ui/ux",
    "prompt engineering","tomcat","excel","matlab",
    "active directory","powershell","azure","microsoft",
    "oop","fpga","version control", "vs code"
}

OVERLAPPING_SKILLS = {
    "java": r"\bjava\b",
    "c++": r"c\+\+",
    "c#": r"c\#",
}

def get_skills (text):
    """Extract known technical skills from a text string."""
    found = set()
    text = text.lower()
    #regex search for special skills that may be confused as others/other words
    for skill,pattern in OVERLAPPING_SKILLS.items():
        if re.search(pattern,text):
            found.add(skill)
    #substring search for regular skills
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return found

@app.post("/analyze")
def analyze(data:AnalyzeRequest):
    """Compare a resume against multiple job descriptions."""
    resume_skills = get_skills(data.resume)
    
    results = []
    for i,job in enumerate(data.jobs):
        job_skills = get_skills(job)
        #logical and to isolate skills that appear in both skill sets
        matches = resume_skills & job_skills
        #calculate percentage of user skills that match job rescriptipn
        user_match = float(len(matches)/len(job_skills))*100 if job_skills else 0
        missing_skills = job_skills - resume_skills
        #organize values into results for output
        results.append({
            "job_number": i+1,
            "match_score": round(user_match,2),
            "matched_skills":sorted(matches),
            "missing_skills": sorted(missing_skills)
        })
        #find best job based on score and missing skills(in case of a tie)
        best_job = max(
            results, key=lambda x: (x["match_score"], -len(x["missing_skills"]))
        )
    #missing job description error
    if not data.jobs:
        return{
            "error":"Please enter at least 1 job description!"
        }
    return {
        "results": results,
        #format the best job option based on score
        "best_job":{
            "job_number": best_job["job_number"],
            "match_score": best_job["match_score"]
        }
    }
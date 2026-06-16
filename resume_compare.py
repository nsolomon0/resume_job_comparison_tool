#common skills encountered often in job requirement sections
#skills will be used to compare against both resume and provided job requirement
import re

SKILLS = {
    "node.js","express","nextjs","python",
    "django","fastapi","flask","rest apis",
    "web services","postgresql","mongodb",
    "dynamodb","front-end","html","css","javascript","typescript","react",
    "angular","docker","git","aws",
    "communication","machine learning",".net",
    "data structures and algorithms","sql",
    "computer vision","cloud computing","linux",
    "graphpql","problem-solving","ui/ux",
    "prompt engineering","tomcat","excel","matlab",
    "active directory","powershell","azure","microsoft",
    "oop","fpga","version control", "vs code"
}

OVERLAPED_SKILLS = {
    "java": r"\bjava\b",
    "c++": r"c\+\+",
    "c#": r"c\#",
    #"c": r"(?<!\w)c(?!\w)" #no words before or after the character 'c'
}

resume = input("Please paste the contents of your resume:")
j_desc = input("Please enter the job requirements:")

def get_skills (text):
    found = set()
    text = text.lower()
    #regex search for special skills that may be confused as others/other words
    for skill,pattern in OVERLAPED_SKILLS.items():
        if re.search(pattern,text):
            found.add(skill)
  
    #substring search for regular skills
    for skill in SKILLS:
        if skill in text:
            found.add(skill)

    return found


#isolate skills in resume and job requirements
resume_skills = get_skills(resume)
job_skills = get_skills(j_desc)
#print(resume_skills)
print("\nYour Skills:")
for skills in sorted(resume_skills):
    print(">",skills)

print("\nJob Requirement Skills:")
for skills in sorted(job_skills):
    print(">",skills)

#logical and to isolate skills that appear in both skill sets
matches = resume_skills & job_skills

#calculate percentage of user skills that match job rescriptipn
if len(job_skills)==0:
    user_match = 0;
else:
    user_match = float(len(matches)/len(job_skills)) * 100
    
print(f"\nYour match with this job: %{round(user_match,2)}")

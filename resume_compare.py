#common skills encountered often in job requirement sections
#skills will be used to compare against both resume and provided job requirement
import re

SKILLS = {
    "node.js","express","nestjs","python",
    "django","fastapi","flask","rest apis",
    "web services","postgresql","mongodb",
    "dynamodb","front-end","html5","css3",
    "scss","javascript","typescript","react",
    "angular","docker","git","aws",
    "communication","machine learning",".net",
    "data structures and algorithms","sql",
    "computer vision","cloud computing","linux",
    "grahppql","problem-solving","ui/ux",
    "prompt engineering","tomcat","excel","matlab",
    "active directory","powershell","azure","microsoft",
    "oop","fpga","version control"
}

OVERLAPED_SKILLS = {
    "java": r"\bjava\b",
    "c++": r"c\+\+",
    "c#": r"c\#",
    #"c": r"(?<!\w)c(?!\w)" #no words before or after the character 'c'
}

resume = input("Please paste the contents of your resume:")
j_desc = input("Please paste the job requirements:")

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



resume_skills = get_skills(resume)
job_skills = get_skills(j_desc)
print(resume_skills)
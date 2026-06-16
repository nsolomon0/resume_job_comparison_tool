#common skills encountered often in job requirement sections
#skills will be used to compare against both resume and provided job requirement
SKILLS = {
    "node.js","express","nestjs","python",
    "django","fastAPI","flask","rest apis",
    "web services","postgresql","mongodb",
    "dynamodb","front-end","html5","css3",
    "scss","javascript","typescript","react",
    "angular","docker","git","aws",
    "communication","machine learning",
    "c++","java","c#","c",".net",
    "data sctructures and algorithms","sql",
    "computer vison","cloud computing","linux",
    "grahpql","problem-solving","ui/ux",
    "prompt engineering","tomcat","excel","matlab",
    "active directory","powershell","azure","microsoft",
    "oop","fpga","version control"
}

resume = input("Please paste the contents of your resume:")
j_desc = input("Please paste the job requirements:")

your_skills = {
    skill for skill in SKILLS
    if skill in resume.lower()
}

job_skills = {
    skill for skill in SKILLS
    if skill in j_desc.lower()
}

print(your_skills)
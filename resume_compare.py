import re
#common skills encountered often in job requirement sections
#skills will be used to compare against both resume and provided job requirement

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

resume = input("Please enter resume skills:")
num = int(input("How many jobs would you like to compare your resume with?:"))
jobs = []
for i in range(num):
    j_desc = input(f"Please enter requirements for job #{i+1}:")
    jobs.append(j_desc)

def get_skills (text):
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

#isolate skills in resume
resume_skills = get_skills(resume)

print("\nYour Skills:")
for skills in sorted(resume_skills):
    print(">",skills)

results = []
for i,job in enumerate(jobs):
    job_skills = get_skills(job)
    #logical and to isolate skills that appear in both skill sets
    matches = resume_skills & job_skills
    #calculate percentage of user skills that match job rescriptipn
    user_match = float(len(matches)/len(job_skills))*100 if job_skills else 0

    print("\n------")
    print(f"Job {i+1}")
    print("------")
    print(f"Match Score: %{round(user_match,2)}")
    print(f"Matched Skills:")
    for skill in sorted(matches):
        print(">",skill)
    missing_skills = job_skills - resume_skills
    print("Skills you are missing:")
    for skill in missing_skills:
        print(">",skill)
    #store job comarison reults for determining best match
    results.append((i,user_match,len(matches),len(missing_skills)))

# job with highest match score is the best; if 2 jobs have the same score, choose the one with the fewer missing skills
best_job = max(results, key=lambda x: (x[1], -x[3]))
print("\n===========================================")
print(f"You have the best chances with Job{best_job[0]+1}: %{round(best_job[1],2)}")
print("===========================================")


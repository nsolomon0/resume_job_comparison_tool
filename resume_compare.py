def get_terms(text):
    return set(text.lower().replace(",","").split())

resume = input("Please paste the contents of your resume:")
j_desc = input("Please paste the job desciption you would like to compare your resume with:")

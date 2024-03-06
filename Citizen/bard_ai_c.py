from bardapi import Bard

API_KEY = 'cgjO5LLUqDmyoPHkNL2FqvsJOqIsyRxyeiCrPHLYxElI1ZJosKUPt-Cza41ou35vYq4btg.'

def bard_answer(search):
    global API_KEY
    try:
        bard = Bard(token = API_KEY)
        prompt = search 
        answer = bard.get_answer(prompt)['content']
        return answer
    except:
        return "Bard API key expired!"
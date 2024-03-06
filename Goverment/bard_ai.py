from bardapi import Bard
from nltk.tokenize import sent_tokenize


'''
while True:
    query = input("User: ")
    if query == 'bye':
        print("\nBYE!")
        break
    answer = bard.get_answer(query)["content"]
    print(f"Bard: {answer}\n\n")
'''

def bard_answer(summarization=False, classify=False, doc=''):
    API_KEY = 'cgjO5LLUqDmyoPHkNL2FqvsJOqIsyRxyeiCrPHLYxElI1ZJosKUPt-Cza41ou35vYq4btg.'
    try:
        bard = Bard(token = API_KEY)
        if summarization:
            prompt = f'Summarize the given below document and make it as easy and readable and understandable, only give the summarized answer to this prompt. Given document : \n {doc}' 
            answer = bard.get_answer(prompt)['content']
            return answer
    except:
        return "Bard API key expired!"

from rake_nltk import Rake

r = Rake() # Uses stopwords for english from NLTK, and all puntuation characters

def key(sentence):
    ans=""
    r.extract_keywords_from_text(sentence)
    list1=r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest
    for i in list1:
        ans+=i+"\n"
    return(ans)
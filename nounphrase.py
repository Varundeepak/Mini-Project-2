import nltk
from textblob import TextBlob
def noun(sentence):
    blob1=TextBlob(sentence)
    ans=""
    for np in blob1.noun_phrases:
        ans+=np+"\n"
    return(ans)
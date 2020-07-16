import nltk
from textblob import TextBlob
def text(sentence):
    blob1=TextBlob(sentence)
    list1=[]
    list1.append(blob1.sentiment.polarity)
    list1.append(blob1.sentiment.subjectivity)
    if( blob1.sentiment.polarity < -0.1 ) :
        list1.append("Negative")
    elif( blob1.sentiment.polarity > 0.1 ) : 
        list1.append("Positive")
    else:
        list1.append("Neutral")
    if( blob1.sentiment.subjectivity < 0.5 ) :
        list1.append("Objective")
    else:
        list1.append("Subjective")
    return(list1)
    
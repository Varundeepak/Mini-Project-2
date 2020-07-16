from afinn import Afinn
def aff(sentence):
    af = Afinn()
    sentiment=""
    score1=af.score(sentence)
    if score1>0:
        sentiment="Positive"
    elif score1<0:
        sentiment="Negative"
    else:
        sentiment="Neutral"
    ans=[score1,sentiment]
    return ans 
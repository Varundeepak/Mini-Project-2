import spacy
import en_core_web_sm
sp = spacy.load("en")
def pos(sentence):
    sen = sp(sentence)
    ans=""
    for word in sen:
        ans+=f'{word.text:{12}} {word.pos_:{10}} {word.tag_:{8}} {spacy.explain(word.tag_)}\n'
    return(ans)
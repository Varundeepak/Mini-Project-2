from pywsd.lesk import simple_lesk
import nltk
def wordsen(sentence,amb):
    answer = simple_lesk(sentence, amb, pos='n')
    return(answer.definition())
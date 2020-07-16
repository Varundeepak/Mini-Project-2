from textblob import Word
def define(word):
    list1=Word(word).definitions
    i=1
    ans=""
    for x in list1:
        ans+=str(i)+". "+x+"\n\n"
        i+=1
    return(ans)
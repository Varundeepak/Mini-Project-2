import tkinter as tk
import tkinter.font
import afinnsentiment as af
import vadersentimentanalysis as va
import textblobsentiment as txt
import nounphrase as noun
import partsofspeechtagger as parts
import keyphrase as key
import wordsense as word 
import definitions as define 
import os

    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()     #.pack() is changed to .grid()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Button(self, text="Twitter Sentiment Analysis",font=helv36,command=lambda: master.switch_frame(PageOne)).grid(row=0,column=0,sticky='E',padx=10,pady=10)
        tk.Button(self, text="Meme Sentiment Analysis",font=helv36,command=lambda: master.switch_frame(PageTwo)).grid(row=0,column=1,sticky='W',padx=10,pady=10)
        tk.Button(self, text="Sentiment Analysis Using AFINN",font=helv36,command=lambda: master.switch_frame(PageThree)).grid(row=1,column=0,sticky='E',padx=10,pady=10)
        tk.Button(self, text="Sentiment Analysis Using VADER",font=helv36,command=lambda: master.switch_frame(PageFour)).grid(row=1,column=1,sticky='W',padx=10,pady=10)
        tk.Button(self, text="Sentiment Analysis Using TextBlob",font=helv36,command=lambda: master.switch_frame(PageFive)).grid(row=2,column=0,sticky='E',padx=10,pady=10)
        tk.Button(self, text="Noun Phrase Extraction",font=helv36,command=lambda: master.switch_frame(PageSix)).grid(row=2,column=1,sticky='W',padx=10,pady=10)
        tk.Button(self, text="Parts of Speech Tagger",font=helv36,command=lambda: master.switch_frame(PageSeven)).grid(row=3,column=0,sticky='E',padx=10,pady=10)
        tk.Button(self, text="Key Phrase Extraction",font=helv36,command=lambda: master.switch_frame(PageEight)).grid(row=3,column=1,sticky='W',padx=10,pady=10)
        tk.Button(self, text="Word Sense Disambiguation",font=helv36,command=lambda: master.switch_frame(PageNine)).grid(row=4,column=0,sticky='E',padx=10,pady=10)
        tk.Button(self, text="Definitions",font=helv36,command=lambda: master.switch_frame(PageTen)).grid(row=4,column=1,sticky='W',padx=10,pady=10)

class PageOne(tk.Frame):
    def pageonecalculation():
        #execfile('twittersentiment.py')
        os.system('python twittersentiment.py')
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Twitter Sentiment Analysis", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Button(self,text="Click here to open the application in a new window",command=PageOne.pageonecalculation,font=helv36).grid(row=1,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=1,column=1,padx=10,pady=10)

class PageTwo(tk.Frame):
    def pagetwocalculation():
        #execfile('memesentiment.py')
        os.system('python memesentiment.py')
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Meme Sentiment Analysis", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Button(self,text="Click here to open the application in a new window",command=PageTwo.pagetwocalculation,font=helv36).grid(row=1,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).grid(row=1,column=1,padx=10,pady=10)
        
        

class PageThree(tk.Frame):
    def pagethreecalculation():
        PageThree.var1.set("")
        PageThree.var2.set("")
        sentence=PageThree.entry1.get()
        ans=af.aff(sentence)
        PageThree.var1.set(str(ans[0]))
        PageThree.var2.set(str(ans[1]))
        
    
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        PageThree.var1=tk.StringVar()
        PageThree.var1.set("")
        PageThree.var2=tk.StringVar()
        PageThree.var2.set("")
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Sentiment Analysis Using AFINN", font=('Helvetica', 18, "bold"))
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageThree.entry1=tk.Entry(self,font=helv36,width=50)
        PageThree.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self,text="Score : ",font=helv36).grid(row=2,column=0,padx=10,pady=10)
        PageThree.label1=tk.Label(self,text="",textvariable=PageThree.var1,font=helv36)
        PageThree.label1.grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self,text="Polarity : ",font=helv36).grid(row=3,column=0,padx=10,pady=10)
        PageThree.label2=tk.Label(self,text="",textvariable=PageThree.var2,font=helv36)
        PageThree.label2.grid(row=3,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageThree.pagethreecalculation,font=helv36).grid(row=4,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=4,column=1,padx=10,pady=10)
        
class PageFour(tk.Frame):
    def pagefourcalculation():
        PageFour.var1.set("")
        PageFour.var2.set("")
        sentence=PageFour.entry1.get()
        ans=va.vader(sentence)
        PageFour.var1.set(str(ans[0]))
        PageFour.var2.set(str(ans[1]))

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        PageFour.var1=tk.StringVar()
        PageFour.var1.set("")
        PageFour.var2=tk.StringVar()
        PageFour.var2.set("")
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Sentiment Analysis Using VADER", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageFour.entry1=tk.Entry(self,font=helv36,width=50)
        PageFour.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self,text="Score : ",font=helv36).grid(row=2,column=0,padx=10,pady=10)
        PageFour.label1=tk.Label(self,text="",textvariable=PageFour.var1,font=helv36)
        PageFour.label1.grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self,text="Polarity : ",font=helv36).grid(row=3,column=0,padx=10,pady=10)
        PageFour.label2=tk.Label(self,text="",textvariable=PageFour.var2,font=helv36)
        PageFour.label2.grid(row=3,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageFour.pagefourcalculation,font=helv36).grid(row=4,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=4,column=1,padx=10,pady=10)
        
class PageFive(tk.Frame):
    def pagefivecalculation():
        PageFive.var1.set("")
        PageFive.var2.set("")
        PageFive.var3.set("")
        PageFive.var4.set("")
        sentence=PageFive.entry1.get()
        ans=txt.text(sentence)
        PageFive.var1.set(str(ans[0]))
        PageFive.var2.set(str(ans[2]))
        PageFive.var3.set(str(ans[1]))
        PageFive.var4.set(str(ans[3]))

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        PageFive.var1=tk.StringVar()
        PageFive.var1.set("")
        PageFive.var2=tk.StringVar()
        PageFive.var2.set("")
        PageFive.var3=tk.StringVar()
        PageFive.var3.set("")
        PageFive.var4=tk.StringVar()
        PageFive.var4.set("")
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Sentiment Analysis Using TextBlob", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageFive.entry1=tk.Entry(self,font=helv36,width=50)
        PageFive.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self,text="Polarity Score : ",font=helv36).grid(row=2,column=0,padx=10,pady=10)
        PageFive.label1=tk.Label(self,text="",textvariable=PageFive.var1,font=helv36)
        PageFive.label1.grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self,text="Polarity : ",font=helv36).grid(row=3,column=0,padx=10,pady=10)
        PageFive.label2=tk.Label(self,text="",textvariable=PageFive.var2,font=helv36)
        PageFive.label2.grid(row=3,column=1,padx=10,pady=10)
        tk.Label(self,text="Subjectivity Score : ",font=helv36).grid(row=4,column=0,padx=10,pady=10)
        PageFive.label3=tk.Label(self,text="",textvariable=PageFive.var3,font=helv36)
        PageFive.label3.grid(row=4,column=1,padx=10,pady=10)
        tk.Label(self,text="Subjectivity : ",font=helv36).grid(row=5,column=0,padx=10,pady=10)
        PageFive.label4=tk.Label(self,text="",textvariable=PageFive.var4,font=helv36)
        PageFive.label4.grid(row=5,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageFive.pagefivecalculation,font=helv36).grid(row=6,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=6,column=1,padx=10,pady=10)
        
class PageSix(tk.Frame):
    def pagesixcalculation():
        PageSix.text1.delete('1.0', tk.END)
        sentence=PageSix.entry1.get()
        ans=noun.noun(sentence)
        PageSix.text1.insert(tk.INSERT,ans)

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Noun Phrase Extraction", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageSix.entry1=tk.Entry(self,font=helv36,width=50)
        PageSix.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageSix.pagesixcalculation,font=helv36).grid(row=2,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=2,column=1,padx=10,pady=10)
        PageSix.text1=tk.Text(self,font=helv36)
        PageSix.text1.grid(row=3,columnspan=3,rowspan=2,column=0)
        
class PageSeven(tk.Frame):
    def pagesevencalculation():
        PageSeven.text1.delete('1.0', tk.END)
        sentence=PageSeven.entry1.get()
        ans=parts.pos(sentence)
        PageSeven.text1.insert(tk.INSERT,ans)
        
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Parts of Speech Tagger", font=('Helvetica', 18, "bold")).grid(columnspan=3,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageSeven.entry1=tk.Entry(self,font=helv36,width=50)
        PageSeven.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageSeven.pagesevencalculation,font=helv36).grid(row=2,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=2,column=1,padx=10,pady=10)
        PageSeven.text1=tk.Text(self,font=helv36)
        PageSeven.text1.grid(row=3,columnspan=3,rowspan=2,column=0)
        
class PageEight(tk.Frame):
    def pageeightcalculation():
        PageEight.text1.delete('1.0', tk.END)
        sentence=PageEight.entry1.get()
        ans=key.key(sentence)
        PageEight.text1.insert(tk.INSERT,ans)
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Key Phrase Extraction", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageEight.entry1=tk.Entry(self,font=helv36,width=50)
        PageEight.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Button(self,text="Calculate",command=PageEight.pageeightcalculation,font=helv36).grid(row=2,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=2,column=1,padx=10,pady=10)
        PageEight.text1=tk.Text(self,font=helv36)
        PageEight.text1.grid(row=3,columnspan=3,rowspan=2,column=0)
        
class PageNine(tk.Frame):
    def pageninecalculation():
        PageNine.var1.set(str(""))
        sentence=PageNine.entry1.get()
        keyword=PageNine.entry2.get()
        ans=word.wordsen(sentence,keyword)
        PageNine.var1.set(str(ans))
        
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        PageNine.var1=tk.StringVar()
        PageNine.var1.set("")
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Word Sense Disambiguation", font=('Helvetica', 18, "bold")).grid(columnspan=2,sticky='N')
        tk.Label(self, text="Enter a sentence : ",font=helv36).grid(row=1,column=0,padx=10)
        PageNine.entry1=tk.Entry(self,font=helv36,width=50)
        PageNine.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Label(self, text="Enter the word to find meaning : ",font=helv36).grid(row=2,column=0,padx=10)
        PageNine.entry2=tk.Entry(self,font=helv36,width=50)
        PageNine.entry2.grid(row=2,column=1,padx=10,pady=10)
        tk.Label(self, text="Definition : ",font=helv36).grid(row=3,column=0,padx=10)
        PageNine.label1=tk.Label(self,text="",textvariable=PageNine.var1,font=helv36)
        PageNine.label1.grid(row=3,column=1,padx=10,pady=10)
        tk.Button(self,text="Meaning",command=PageNine.pageninecalculation,font=helv36).grid(row=4,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=4,column=1,padx=10,pady=10)
        
        
class PageTen(tk.Frame):
    def pagetencalculation():
        PageTen.text1.delete('1.0', tk.END)
        sentence=PageTen.entry1.get()
        ans=define.define(sentence)
        PageTen.text1.insert(tk.INSERT,ans)
        
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        helv36 = tk.font.Font(size=14)
        tk.Label(self, text="Definitions", font=('Helvetica', 18, "bold")).grid(columnspan=3,sticky='N')
        tk.Label(self, text="Enter a word : ",font=helv36).grid(row=1,column=0,padx=10)
        PageTen.entry1=tk.Entry(self,font=helv36)
        PageTen.entry1.grid(row=1,column=1,padx=10,pady=10)
        tk.Button(self,text="Find",command=PageTen.pagetencalculation,font=helv36).grid(row=2,column=0,padx=10,pady=10)
        tk.Button(self, text="Go back to start page",font=helv36,
                  command=lambda: master.switch_frame(StartPage)).grid(row=2,column=1,padx=10,pady=10)
        PageTen.text1=tk.Text(self,font=helv36)
        PageTen.text1.grid(row=3,columnspan=3,rowspan=2,column=0)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
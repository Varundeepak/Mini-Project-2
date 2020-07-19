import numpy as np
from keras.preprocessing import image

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from keras.models import load_model
import pytesseract
from textblob import TextBlob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

a=""
text=""
b=""

classifier = load_model('mycnnmodel.h5')
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
root = Tk()
root.geometry("550x350+300+150")
root.resizable(width=True, height=True)

def openfn():
    global a
    filename = filedialog.askopenfilename(title='open')
    a=filename
    return filename
def open_img():
    global text
    global b
    x = openfn()
    test_image = image.load_img(x, target_size = (64, 64))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_classes(test_image)
    #print(result)
    index=['negative','neutral','positive']
    #label = Label( root, text="Prediction : "+index[result[0]])
    #label.pack()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
    #print("Image Sentiment : ")
    #print(index[result[0]])
    text=pytesseract.image_to_string(a)
    #print(text)
    #print("Text Sentiment : ")
    analysis = TextBlob(text) 
    if analysis.sentiment.polarity > 0:
        b='positive'
    elif analysis.sentiment.polarity == 0:
        b='neutral'
    else:
        b='negative'
    label = Label( root, text="Image (whole image along with text) Prediction : "+index[result[0]])
    label.pack()
    label1 = Label( root, text="Text (only the text) Prediction : "+b)
    label1.pack()
    
    

btn = Button(root, text='open image', command=open_img).pack()

root.mainloop()
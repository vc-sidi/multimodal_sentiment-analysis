import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image
import numpy

from keras.models import load_model
model = load_model('2022-01-23T20-33-11Z_image_sent_model_v1.h5')
#dictionary to label all traffic signs class.
classes = { 
    0:'NEG',
    1:'NEU',
    2:'POS',
}
#initialise GUI
top=tk.Tk()
top.geometry('800x600')
top.title('Classificação Sentimento Imagem Tweet B-T4SA')
top.configure(background='#CDCDCD')
label=Label(top,background='#CDCDCD', font=('arial',15,'bold'))
sign_image = Label(top)

def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((128,128))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    image = image/255
    pred = model.predict([image])[0]
    if pred[0] > pred[1] and pred[0] > pred[2]:
        sign = 'Sentimento NEGATIVO'
    elif  pred[1] > pred[0] and pred[1] > pred[2]:
        sign = 'Sentimento NEUTRO'
    elif  pred[2] > pred[0] and pred[2] > pred[1]:
        sign = 'Sentimento POSITIVO'
    else:
        sign = 'Sentimento INDERTEMINADO'
    
        
    print(sign, pred)
    label.configure(foreground='#011638', text=f'{sign} {str(max(pred*100))} {str("%")}')

def show_classify_button(file_path):
    classify_b=Button(top,text="Classificar a Imagem",
   command=lambda: classify(file_path),
   padx=10,pady=5)
    classify_b.configure(background='#364156', foreground='white',
font=('arial',10,'bold'))
    classify_b.place(relx=0.79,rely=0.46)

def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),
    (top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image=im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass
upload=Button(top,text="Upload da imagem",command=upload_image,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('arial',10,'bold'))
upload.pack(side=BOTTOM,pady=50)
sign_image.pack(side=BOTTOM,expand=True)
label.pack(side=BOTTOM,expand=True)

heading = Label(top, text="Classificação Sentimento Imagem Tweet B-T4SA",pady=20, font=('arial',20,'bold'))
heading.configure(background='#CDCDCD',foreground='#364156')
heading.pack()
top.mainloop()
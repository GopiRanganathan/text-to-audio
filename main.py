from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from pypdf import PdfReader

def text_to_audio(text, path, language='en'):
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save(path)
    file_name.config(text='Audio saved successfully!')

def get_text():
    file_path = filedialog.askopenfilename(title="Choose PDF", filetypes=[("PDF files", "*.pdf")])
    filename = file_path.split('/')[-1]
    file_name.config(text=filename)
    text =''
    if file_path:
       reader = PdfReader(file_path)
       for page in reader.pages:
           text+=page.extract_text()
    text_to_convert.set(text)
    convert_btn.config(state='normal')


def convert_to_audio():
   file_path = filedialog.asksaveasfilename(title='Save Audio', defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
   text=text_to_convert.get()
   if text!='' and file_path:
       text_to_audio(text, file_path)
   else:
       file_name.config(text='Please choose a valid pdf file')
       return None
   
   
# -----------------------------UI-SETUP-------------------------------
window = Tk()
window.title("PDF To Audio Book")
window.minsize(height=300, width=500)
window.maxsize(height=300, width=500)
window.config(padx=70, pady=30)
text_to_convert = StringVar()
title = Label(text='PDF to AudioBook', font=('Arial', 29, 'bold'))
title.grid(row=0, column=0)
choose_file= Button(text="Choose PDF", bg="blue", fg='white', command=get_text)
choose_file.grid(row=1, column=0, padx=10, pady=10)
file_name = Label(text='No file chosen')
file_name.grid(row=2, column=0, pady=10)
convert_btn = Button(text="Convert to AudioBook", state='disabled', bg="green", fg='white', command=convert_to_audio)
convert_btn.grid(row=3, column=0)
window.mainloop()




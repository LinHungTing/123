from tkinter import*
windom=Tk()
windom.title("Salutation")
def button_event():
    btn["text"]="GOODBYE"
    
btn=Button(text="HELLO",bg="sky blue",command=button_event)
btn.grid(padx=100,pady=10)
windom.mainloop()
  
from tkinter import*
from tkinter import font
import qrcode


main_window=Tk() #Creating the main window
main_window.title("QR CODE GENERATOR APPLICATION")
main_window.geometry("1000x650")
main_window.resizable(False,False) #To ensure that the size of the window is unchangeable
main_window.config(bg="#000000")

def run():
    name = qr_name.get()
    text = link.get()
    qr=qrcode.make(text)
    qr.save("Qrcode/" + str(name)+".png")

    global Image
    Image=PhotoImage(file="Qrcode/"+ str(name)+".png")
    Image_view.config(image=Image)

Image_view=Label(main_window,bg="#FFFFFF")
Image_view.pack(padx=10,pady=10,side=RIGHT)

main_label = Label(main_window,text="Welcome, to Nate's QR Code Generator Application!",font="22",fg="#FFFFFF",bg="#000000")
main_label.place(x=125,y=230)
Label(main_window,text="Enter a title name for your QR CODE:",font="22",fg="#FFFFFF",bg="#000000").place(x=125,y=270)


qr_name = Entry(main_window,width=46)
qr_name.place(x=125,y=300)

Label(main_window,text="Enter a link for a website you would like to associate your link with:",font="22",fg="#FFFFFF",bg="#000000").place(x=125,y=330)

link = Entry(main_window,width=46)
link.place(x=125,y=360)

Button(main_window,text="GENERATE QR CODE",width=20,height=2,bg="#FFFFFF",fg="#000000",command=run).place(x=195,y=400)


main_window.mainloop()
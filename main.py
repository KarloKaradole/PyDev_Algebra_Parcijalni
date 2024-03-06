import tkinter as tk
from tkinter import IntVar, StringVar
from database_mngr import get_names_from_db, get_user

#region CONSTANTS

text_size_constant = ("Sagoe UI",18)

#endregion

main_window = tk.Tk()
main_window.title("Smart Key")
main_window.geometry("600x800")

#region FUNCTIONS

def show_pin_panel():
    pin_lbl_frame.pack(padx=20, pady=(20, 10))
    
def hide_pin_panel(panel):
    panel.pack_forget() #Ako se koristi grid: button_panel.grid.remove(). Ako se koristi place: button_panel.place.forget()
    #panel.tkraise() #opcija ako su okviri jedan ispod drugog kao karte
       
def leave(event):
    print(f"Mis nije iznad gumba. {event}")
    
def on_element_clicked(event):
    index = lbox_names.curselection()
    value = lbox_names.get(index)
    user = get_user(value.split(" ")[0])
    #TODO popuniti vrijednosti u widgetima preko Vars (StringVar, IntVar, ...)
    
    print(f"Index {index} Value: {value}")

def show_hello_frame():
    hello_frame.pack(padx=30, pady=30)
    
#endregion

#region PANELS

#Button Panel

button_lbl_frame = tk.LabelFrame(main_window,
                                 text="Button frame",
                                 padx=30,
                                 pady=30)
button_lbl_frame.pack(padx=20, pady=(20, 10))

lbl_welcome_message = tk.Label(button_lbl_frame,
                               font=text_size_constant,
                               text="Dobro dosli")
lbl_welcome_message.grid(row=0,column=0, columnspan=2)


ring_button = tk.Button(button_lbl_frame,
                        text="Pozvoni - sakrij",
                        command=lambda : (hide_pin_panel(pin_lbl_frame), show_hello_frame()))
ring_button.grid(row=1,column=0)

unlock_button = tk.Button(button_lbl_frame,
                        text="Otkljucaj",
                        command=show_pin_panel)
unlock_button.grid(row=1,column=1)


#region PIN Panel

pin_lbl_frame = tk.LabelFrame(main_window,
                          text="Pin frame",
                          padx=30,
                          pady=30)

#region Checkbutton
cb_expand_var = IntVar()
lbl_expand = tk.Label(pin_lbl_frame, text="Expand")
lbl_expand.grid(row=0,column=0)
cb_expand = tk.Checkbutton(pin_lbl_frame,variable = cb_expand_var)
cb_expand.grid(row=0, column=1)
#endregion


lbl_pin = tk.Label(pin_lbl_frame,
                   textvariable=cb_expand_var)
lbl_pin.grid(row=1,column=0)


lbl_name = tk.Label(pin_lbl_frame, text="Ime")
lbl_name.grid(row=2,column=0)
entry_name = tk.Entry(pin_lbl_frame)
entry_name.grid(row=2,column=1)

lbox_names = tk.Listbox(pin_lbl_frame)
lbox_names.grid(row=3,column=0)

names = ["Pero Peric", "Ana Anic", "Marko Maric", "Josip Josic", "Iva Ivic"]
names = get_names_from_db()

for name in names:
    lbox_names.insert(tk.END,name)
lbox_names.bind("<ButtonRelease-1>", on_element_clicked)
    
    
btn_demo = tk.Button(pin_lbl_frame,
                     text="Demo",
                     font=text_size_constant)
btn_demo.grid(row=4,column=0,pady=20)
btn_demo.bind("<Enter>", show_pin_panel)
btn_demo.bind("<Leave>", leave)

lbl_demo_var = StringVar()
lbl_demo_var.set("Pocetna vrijednost")
lbl_demo = tk.Label(pin_lbl_frame,
                    textvariable=lbl_demo_var,
                    font=text_size_constant)
lbl_demo.grid(row=5,column=0,pady=20)


#endregion

#region Hello Frame

hello_frame = tk.LabelFrame(main_window,
                            text="Hello frame",
                            padx=30,
                            pady=30)

hello_lbl = tk.Label(hello_frame,
                     font=text_size_constant,
                     text="HELLO")
hello_lbl.pack()

#endregion

#region Admin Panel

admin_panel = tk.Frame(main_window)
admin_panel.pack(padx=20, pady=(10, 20))

#endregion


if __name__ == "__main__":
    # funkcija koja ce kreirati bazu i napuniti je inicijalnim podatcima
    #create_tables()
    #database_seed()
    main_window.mainloop()
    

    

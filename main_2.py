import tkinter as tk
from tkinter import IntVar, StringVar
import itertools
from database_mngr import get_user, get_names_from_db

#region CONSTANTS

text_size_constant = ("Sagoe UI",24)

#endregion

main_window = tk.Tk()
main_window.title("Smart Key")
main_window.geometry("600x900")

#region FUNCTIONS

def show_pin_panel():
    pin_lbl_frame.pack(padx=10,pady=10)
    
def show_admin_panel():
    admin_lbl_frame.pack(padx=10,pady=10)
    
def hide_pin_panel(panel):
    panel.pack_forget()
       
def leave(event):
    print(f"Mis nije iznad gumba. {event}")
    
def on_element_clicked(event):
    index = admin_status_text.curselection()
    value = admin_status_text.get(index)
    user = get_user(value.split(" ")[0])
    #TODO popuniti vrijednosti u widgetima preko Vars (StringVar, IntVar, ...)
    
    print(f"Index {index} Value: {value}")

def open_hello_window():
    hello_window = tk.Toplevel(main_window)
    hello_window.title("Ring is ACTIVATED!")
    hello_window.geometry("800x140")
    
    loading_label = tk.Label(hello_window, font=text_size_constant)
    loading_label.pack(padx=30, pady=30)
    
    loading_symbols = itertools.cycle(['', '.', '..', '...'])
    
    def update_loading_label():
        loading_label.config(text="Someone is coming, we appreciate your patience!\n" + next(loading_symbols))
        hello_window.after(500, update_loading_label)
    
    update_loading_label()
    main_window.withdraw()  
    
def check_pin():
    entered_pin = entry_pin.get()
    future_pin_list = ["1234", "5678", "9876", "5432"]
    if entered_pin in future_pin_list:
        print("PIN exists in the future list.")
    else:
        print("PIN does not exist in the future list.")
        
def update_entry_pin(number):
    current_pin = entry_pin.get()
    if number == "C":
        entry_pin.delete(0, tk.END)
    elif number == "E":
        check_pin()
    elif len(current_pin) < 4:
        entry_pin.delete(0, tk.END)
        entry_pin.insert(0, current_pin + number)
        
def file_save():
    pass
    
def erase():
    pass
    
def exitall():
    main_window.destroy
#endregion

#region BUTTON PANEL
button_lbl_frame = tk.LabelFrame(main_window,                               
                                 padx=10,
                                 pady=20)
button_lbl_frame.pack(padx=10,pady=10)

lbl_welcome_message = tk.Label(button_lbl_frame,
                               font=text_size_constant,
                               text="WELCOME")
lbl_welcome_message.grid(row=0,column=5,padx=27)

rign_button = tk.Button(button_lbl_frame,
                        text="RING",
                        command=lambda: (hide_pin_panel(pin_lbl_frame), open_hello_window()),
                        width=15,
                        height=3)
rign_button.grid(row=1,column=1,sticky="SW",padx=25)

unlock_button = tk.Button(button_lbl_frame,
                        text="UNLOCK",
                        command=show_pin_panel,
                        width=15,
                        height=3)
unlock_button.grid(row=1,column=10,sticky="SE",padx=25)

#endregion

#region PIN PANEL
pin_lbl_frame = tk.LabelFrame(main_window,
                          padx=10,
                          pady=10)

# Right side - label
big_label = tk.Label(pin_lbl_frame,
                     text="Status:",
                     font=("Arial", 16))
big_label.grid(row=0, column=20, pady=10)

admin_status_text = tk.Text(pin_lbl_frame,
                      height=15,
                      width=34)
admin_status_text.grid(row=1, column=20,padx=10, rowspan=10)


# Left side - PIN
lbl_pin_entry = tk.Label(pin_lbl_frame,
                         text="PIN:",
                         font=("Arial", 16))
lbl_pin_entry.grid(row=0, column=0)
entry_pin = tk.Entry(pin_lbl_frame)
entry_pin.grid(row=0, column=1)

numbers = ['1', '2', '3','4', '5', '6','7', '8', '9',"C", '0', "E"]
row_num = 4
col_num = 0
for number in numbers:
    btn = tk.Button(pin_lbl_frame, text=number, width=9, height=3, command=lambda num=number: update_entry_pin(num))
    btn.grid(row=row_num, column=col_num, pady=1)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1
        

#endregion

unlock_button = tk.Button(pin_lbl_frame,
                        text="UNLOCK",
                        command=show_admin_panel,
                        width=15,
                        height=3)
unlock_button.grid(row=9,column=1,sticky="SE")

#region ADMIN PANEL
admin_lbl_frame = tk.LabelFrame(main_window,
                                padx=10,
                                pady=20)

admin_status_text = tk.Listbox(admin_lbl_frame,
                            height=15,
                            width=34)
admin_status_text.grid(row=1, column=0,padx=10,rowspan=5)

#TODO names = get_names_from_db()
names = ["Pero Peric", "Ana Anic", "Marko Maric", "Josip Josic", "Iva Ivic"]
for name in names:
    admin_status_text.insert(tk.END,name)

admin_first_name_text = tk.Label(admin_lbl_frame,
                                 font=("Arial", 16),
                                 text="Ime")
admin_first_name_text.grid(row=1,column=1,padx=10,pady=10)

admin_first_name_textbox = tk.Text(admin_lbl_frame,
                            height=2,
                            width=15)
admin_first_name_textbox.grid(row=1, column=2,padx=10,columnspan=2)


admin_last_name_text = tk.Label(admin_lbl_frame,
                                font=("Arial", 14),
                                text="Prezime")
admin_last_name_text.grid(row=2,column=1,padx=10,pady=10)

admin_last_name_textbox = tk.Text(admin_lbl_frame,
                            height=2,
                            width=15)
admin_last_name_textbox.grid(row=2, column=2,padx=10,columnspan=2)


admin_PIN_text = tk.Label(admin_lbl_frame,
                          font=("Arial", 14),
                          text="PIN")
admin_PIN_text.grid(row=3,column=1,padx=10,pady=10)

admin_PIN_textbox = tk.Text(admin_lbl_frame,
                            height=2,
                            width=15)
admin_PIN_textbox.grid(row=3, column=2,padx=10,columnspan=2)

#region Checkbutton
cb_expand_var = IntVar()
lbl_expand = tk.Label(admin_lbl_frame,
                      font=("Arial", 14),
                      text="Aktivan")
lbl_expand.grid(row=4,column=1)
cb_expand = tk.Checkbutton(admin_lbl_frame,
                           variable = cb_expand_var)
cb_expand.grid(row=4, column=2,columnspan=2)
#endregion

#region SAVE/OPEN/RESET

btn_save = tk.Button(admin_lbl_frame,
                     font=("Arial", 14),
                     text="SAVE",
                     command=file_save,
                     width=8)
btn_save.grid(row=5,column=1,rowspan=3)

btn_reset = tk.Button(admin_lbl_frame,
                      font=("Arial", 14),
                      text="DELETE",
                      command=erase,
                      width=7)
btn_reset.grid(row=5,column=2,rowspan=3)

btn_open = tk.Button(admin_lbl_frame,
                     font=("Arial", 14),
                     text="EXIT",
                     command=exitall,
                     width=6)
btn_open.grid(row=5,column=3,rowspan=3)

#endregion


#endregion

main_window.mainloop()

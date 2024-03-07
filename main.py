import tkinter as tk
import itertools
from database.user_data import user_data
import os

main_window = tk.Tk()
main_window.title("Smart Key")
main_window.geometry("600x900")

#region FUNCTIONS

def show_pin_panel():
    pin_lbl_frame.pack(padx=10,pady=10)
    
def show_admin_panel():
    admin_lbl_frame.pack(padx=10,pady=10)
    
def show_pin_admin_panel():
    system_admin_window = tk.Toplevel(main_window)
    system_admin_window.title("")
    system_admin_window.geometry("220x100")
    
    message_label = tk.Label(system_admin_window, text="Run system administration?",font=("Arial", 12))
    message_label.pack()
    
    yes_button = tk.Button(system_admin_window, text="Yes", width=10, height=2, command=lambda: (show_admin_panel(), close_window(system_admin_window)))
    yes_button.pack(side=tk.LEFT, padx=15)
    
    no_button = tk.Button(system_admin_window, text="No",width=15,height=2, command= lambda: (close_window(system_admin_window)))
    no_button.pack(side=tk.RIGHT, padx=15)
    
def close_window(window):
    window.destroy()
    
def hide_pin_panel(panel):
    panel.pack_forget()
         
def leave(event):
    print(f"Mis nije iznad gumba. {event}")
    
def on_element_clicked(event):
    index = admin_status_text.curselection()
    if index:
        selected_item = admin_status_text.get(index[0])
        details = selected_item.split(", ")
        admin_first_name_textbox.delete("1.0", tk.END)
        admin_first_name_textbox.insert(tk.END, details[1])
        admin_last_name_textbox.delete("1.0", tk.END)
        admin_last_name_textbox.insert(tk.END, details[0])
        admin_PIN_textbox.delete("1.0", tk.END)
        admin_PIN_textbox.insert(tk.END, details[2])
        active_inactive_textbox.delete("1.0", tk.END)
        active_inactive_textbox.insert(tk.END, details[3])
            
def open_hello_window():
    hello_window = tk.Toplevel(main_window)
    hello_window.title("Ring is ACTIVATED!")
    hello_window.geometry("800x140")
    
    loading_label = tk.Label(hello_window, font=("Sagoe UI",24))
    loading_label.pack(padx=30, pady=30)
    
    loading_symbols = itertools.cycle(['', '.', '..', '...'])
    
    def update_loading_label():
        loading_label.config(text="Someone is coming, we appreciate your patience!\n" + next(loading_symbols))
        hello_window.after(500, update_loading_label)
    
    update_loading_label()
    main_window.withdraw()  

def check_pin():
    global user_data
    entered_pin = entry_pin.get()
    if entered_pin in user_data.keys():
        if user_data[entered_pin]["(In)Active"] == 1:
            print_user_details(entered_pin)
        else:
            PIN_status_text.insert(tk.END, "\n\n\n\nPIN successfully entered but access not permitted.\n\n\n")
            PIN_status_text.tag_configure("center", justify="center", font=("Arial", 16))
            PIN_status_text.tag_add("center","1.0","end")
    if entered_pin == "9999":
        show_pin_admin_panel()
        #show_admin_panel()
    if entered_pin not in user_data.keys() and entered_pin != "9999":
        PIN_status_text.insert(tk.END, "\n\n\n\nPIN unsuccessful.\n\n\n")
        PIN_status_text.tag_configure("center", justify="center", font=("Arial", 16))
        PIN_status_text.tag_add("center","1.0","end")
           
def print_user_details(entered_pin):
    global user_data
    PIN_status_text.tag_configure("center", justify="center", font=("Arial", 16))
    PIN_status_text.insert(tk.END, "\nPIN successful.\nDoor opened.\n")
    PIN_status_text.tag_add("center","1.0","end")
    PIN_status_text.insert(tk.END, "\nWelcome!\n\n\n")
    PIN_status_text.tag_add("center","2.0","end")
    PIN_status_text.insert(tk.END, user_data[entered_pin]["FirstName"] + "\n")
    PIN_status_text.tag_add("center","3.0","end")
    PIN_status_text.insert(tk.END, user_data[entered_pin]["LastName"] + "\n")
    PIN_status_text.tag_add("center","4.0","end")
    
def update_entry_pin(number):
    current_pin = entry_pin.get()
    if number == "C":
        entry_pin.delete(0, tk.END)
        PIN_status_text.delete("1.0", tk.END)
    elif number == "E":
        PIN_status_text.delete("1.0", tk.END)
        check_pin()
    elif len(current_pin) < 4:
        entry_pin.delete(0, tk.END)
        entry_pin.insert(0, current_pin + number)
        
def file_save():
    index = admin_status_text.curselection()
    if index:
        selected_item = admin_status_text.get(index[0])
        details = selected_item.split(", ")
        pin = details[2]
        user = user_data.get(pin)
        if user:
            user['FirstName'] = admin_first_name_textbox.get("1.0", tk.END).strip()
            user['LastName'] = admin_last_name_textbox.get("1.0", tk.END).strip()
            user['PIN'] = admin_PIN_textbox.get("1.0", tk.END).strip()
            user['(In)Active'] = int(active_inactive_textbox.get("1.0", tk.END).strip())
            
            new_details = f"{user['LastName']}, {user['FirstName']}, {user['PIN']}, {user['(In)Active']}"
            admin_status_text.delete(index[0])
            admin_status_text.insert(index[0], new_details)

            database_path = os.path.join(os.path.dirname(__file__), 'database', 'user_data.py')
            with open(database_path, 'w') as f:
                f.write("user_data = {\n")
                for pin, data in user_data.items():
                    f.write(f"    '{pin}': {data},\n")
                f.write("}\n")

def erase():
    index = admin_status_text.curselection()
    
    if index:
        selected_item = admin_status_text.get(index[0])
        details = selected_item.split(", ")
        pin_to_remove = details[2]
        
        del user_data[pin_to_remove]

        admin_status_text.delete(index[0])

def exitall():
    main_window.destroy()
             
#endregion

#region BUTTON PANEL
button_lbl_frame = tk.LabelFrame(main_window,                               
                                 padx=10,
                                 pady=20)
button_lbl_frame.pack(padx=10,pady=10)

lbl_welcome_message = tk.Label(button_lbl_frame,
                               font=("Sagoe UI",24),
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

PIN_status_text = tk.Text(pin_lbl_frame,
                      height=15,
                      width=34)
PIN_status_text.grid(row=1, column=20,padx=10, rowspan=10)

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

#region PIN PANEL_ADMINISTRATOR

pin_admin_lbl_frame = tk.LabelFrame(main_window,
                                    text="System Administration",
                                    padx=10,
                                    pady=10)

unlock_pin_button = tk.Button(pin_admin_lbl_frame,
                        text="UNLOCK",
                        command=show_pin_admin_panel,
                        width=15,
                        height=3)
unlock_pin_button.grid(row=1,column=10,sticky="SE",padx=25)
#endregion

#region ADMIN PANEL
admin_lbl_frame = tk.LabelFrame(main_window,
                                padx=10,
                                pady=20)

admin_status_text = tk.Listbox(admin_lbl_frame,
                            height=15,
                            width=34)
admin_status_text.grid(row=1, column=0,padx=10,rowspan=5)


for pin, data in user_data.items():
    details =f"{data['LastName']}, {data['FirstName']}, {data['PIN']}, {data['(In)Active']}"
    admin_status_text.insert(tk.END,details)

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

active_inactive_text = tk.Label(admin_lbl_frame,
                          font=("Arial", 14),
                          text="Active/Inactive")
active_inactive_text.grid(row=4,column=1,padx=10,pady=10)

active_inactive_textbox = tk.Text(admin_lbl_frame,
                            height=2,
                            width=15)
active_inactive_textbox.grid(row=4, column=2,padx=10,columnspan=2)



admin_status_text.bind("<<ListboxSelect>>", on_element_clicked)

#region SAVE/OPEN/RESET

btn_save = tk.Button(admin_lbl_frame,
                     font=("Arial", 14),
                     text="SAVE",
                     command=file_save,
                     width=8)
btn_save.grid(row=6,column=1,rowspan=4)

btn_reset = tk.Button(admin_lbl_frame,
                      font=("Arial", 14),
                      text="DELETE",
                      command=erase,
                      width=8)
btn_reset.grid(row=6,column=2,rowspan=4,padx=5)

btn_open = tk.Button(admin_lbl_frame,
                     font=("Arial", 14),
                     text="EXIT",
                     command=exitall,
                     width=6)
btn_open.grid(row=6,column=3,rowspan=2)

#endregion


#endregion

main_window.mainloop()

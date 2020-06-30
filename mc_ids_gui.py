import json, os.path, requests
from tkinter import *


root = Tk()
root.title("Minecraft Ids")
root.minsize(305, 125)
root.maxsize(305, 125)
root.configure(bg='#131d27')
root.option_add('*font', ('comforta', 20, 'bold'))

user_input_tk = StringVar() 
output_tk = StringVar()


def search():
    r = requests.get('https://raw.githubusercontent.com/Arcensoth/mcdata/master/processed/reports/registries/item/item.json')
    ids_array = []

    for i in r.json()['values']:
        ids_array.append(i[10:])

    user_input = user_input_tk.get()

    user_input = user_input.lower()
    user_input = user_input.strip()
    user_input = user_input.replace(" ", "_")

    found = False

    for i in ids_array:
        if i == user_input:
            output = "Id: " + i
            found = True

    if found == False:
        output = "Block doesn't exist"
    
    print(output)
    output_label.configure(text = output)

input = Entry(root, text = user_input_tk, justify = CENTER, bg = "#243a52", fg = "#131d27", highlightbackground = "#243a52", highlightcolor = "#243a52", relief = FLAT).grid(row = 0,column = 0)
output_label = Label(root, text = "Id: air", compound = CENTER, relief = FLAT, width = 20, bg = "#243a52", fg = "#131d27")
output_label.grid(row = 2,column = 0)
search_button = Button(root, text = "Search", width = 20, padx = 0, pady = 0, compound = CENTER, bg = "#243a52", fg = "#131d27", highlightcolor = "#243a52", highlightbackground = "#243a52", activebackground = "#131d27", activeforeground = "#243a52",bd = 0, relief = FLAT, command = search).grid(row = 1,column = 0)

root.mainloop()
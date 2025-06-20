import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(str(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.geometry("300x400")
root.title("Python Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief="sunken", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons_frame = tk.Frame(root)
buttons_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

for row in buttons:
    f = tk.Frame(buttons_frame)
    f.pack(expand=True, fill="both")
    for char in row:
        b = tk.Button(f, text=char, font="Arial 18", height=2, width=5)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()

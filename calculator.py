import tkinter as tk

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("415x500")

# Display screen
entry = tk.Entry(root, width=21, font=("Arial", 24), borderwidth=2, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=14, pady=14)

# Runs the application
root.mainloop()
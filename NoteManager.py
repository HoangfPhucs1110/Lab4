import tkinter as tk
from tkinter import messagebox
import os

# Đường dẫn file lưu ghi chú
FILE_PATH = "notes.txt"

# Hàm lưu ghi chú vào file
def save_notes():
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        file.write(text_area.get("1.0", tk.END))
    messagebox.showinfo("Lưu ghi chú", "Ghi chú đã được lưu thành công!")

# Hàm tải ghi chú từ file
def load_notes():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

# Hàm xóa toàn bộ nội dung
def clear_notes():
    text_area.delete("1.0", tk.END)

# Giao diện người dùng
root = tk.Tk()
root.title("Quản lý ghi chú")
root.geometry("500x400")

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

btn_save = tk.Button(frame, text="Lưu ghi chú", command=save_notes)
btn_save.pack(side=tk.LEFT, padx=5)

btn_load = tk.Button(frame, text="Tải ghi chú", command=load_notes)
btn_load.pack(side=tk.LEFT, padx=5)

btn_clear = tk.Button(frame, text="Xóa ghi chú", command=clear_notes)
btn_clear.pack(side=tk.LEFT, padx=5)

# Tải ghi chú khi khởi động
load_notes()

root.mainloop()

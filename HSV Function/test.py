import tkinter as tk

# Hàm xử lý khi nhấn nút
def on_button_click(choice):
    print(f"Bạn đã chọn: {choice}")
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Lựa chọn tham số")

# Tạo các nút lựa chọn
button1 = tk.Button(root, text="Lựa chọn 1", command=lambda: on_button_click("Lựa chọn 1"))
button1.pack(pady=10)

button2 = tk.Button(root, text="Lựa chọn 2", command=lambda: on_button_click("Lựa chọn 2"))
button2.pack(pady=10)

button3 = tk.Button(root, text="Lựa chọn 3", command=lambda: on_button_click("Lựa chọn 3"))
button3.pack(pady=10)

# Chạy vòng lặp chính
root.mainloop()
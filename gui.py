import tkinter as tk
from region import run
from yamato import main
from PIL import ImageTk, Image

def run_button_click():
    global x, y, width, height
    string, result = main(x, y, width, height)

    text_widget.configure(state="normal")
    text_widget.insert("1.0", result + "\n" + "\n", "color_tag")
    text_widget.insert("1.0", string + "\n" + "\n")

    scrollbar.config(command=text_widget.yview)
    bright_green = "#00FF00"
    text_widget.tag_config("color_tag", foreground=bright_green)

    return

def clear_button_click():
    text_widget.configure(state="normal")
    text_widget.delete("1.0", "end")
    return

def select_range_button_click():
    global x, y, width, height
    x, y, width, height = run()
    text_widget.insert("1.0", f"x:{x}, y:{y}, width:{width}, height:{height}\n\n")
    return

root = tk.Tk()
root.title("yamato")
root.geometry("300x300")
root.resizable(0,0)
root.attributes("-topmost", True)

# 実行ボタン
run_button = tk.Button(text="実行", width=10, command=run_button_click)
run_button.pack()

#範囲選択ボタン
select_range_button = tk.Button(text="範囲選択", width=10, command=select_range_button_click)
select_range_button.configure(foreground="black")
select_range_button.pack()

# 文字消去ボタン
clear_button = tk.Button(text="クリア", width=10, command=clear_button_click)
clear_button.pack()

# テキストウィジェット作成
text_widget = tk.Text(root)
text_widget.pack(fill=tk.BOTH, expand=True)

# スクロールバーを作成する
scrollbar = tk.Scrollbar(text_widget, width=3)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# スクロールバーとTextウィジェットを連動させる
text_widget.config(yscrollcommand=scrollbar.set)

root.mainloop()
from pynput import mouse

num_press = 0
left_up_x, left_up_y, right_down_x, right_down_y = [0, 0, 0, 0]

def run():
    global num_press, left_up_x, left_up_y, right_down_x, right_down_y
    num_press = 0
    left_up_x, left_up_y, right_down_x, right_down_y = [0, 0, 0, 0]

    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
    
    width = right_down_x - left_up_x
    height = right_down_y - left_up_y
    print("範囲を選択しました")
    return left_up_x * 2, left_up_y * 2, width * 2, height * 2

def on_click(x, y, button, pressed):
    global num_press, left_up_x, left_up_y, right_down_x, right_down_y
    if pressed:
        # 1回目のクリックはウィンドウの切り替え用で何もしない
        if num_press == 0:
            num_press = 1
        # 2回目のクリックはスクリーンショットを撮る範囲の左上を指定
        elif num_press == 1:
            num_press = 2
            left_up_x, left_up_y = x, y
        # 3回目のクリックはスクリーンショットを撮る範囲の右下を指定して終了
        else:
            right_down_x, right_down_y = x, y
            return False

if __name__ == "__main__":
    run()

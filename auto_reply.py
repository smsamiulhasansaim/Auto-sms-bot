import tkinter as tk
import pyautogui
import threading
import time

AUTO_REPLY_MESSAGE = "Sorry about that "

running = False
message_count = 0

def start_sending():
    global running, message_count
    running = True
    message_count = 0

    def send_loop():
        global message_count
        time.sleep(0.1)
        while running:
            pyautogui.typewrite(AUTO_REPLY_MESSAGE, interval=0.01)
            pyautogui.press("enter")
            message_count += 1
            print(f"[{message_count}] Sent: {AUTO_REPLY_MESSAGE}")
            time.sleep(0.1)
    threading.Thread(target=send_loop, daemon=True).start()
    status_label.config(text="Started slower sending...")

def stop_sending():
    global running
    running = False
    status_label.config(text="Stopped.")

root = tk.Tk()
root.title("Ultra Fast Auto Reply")

label = tk.Label(root, text="Focus your chat window.\nClick Start to send messages.")
label.pack(padx=20, pady=10)

start_button = tk.Button(root, text="Start", command=start_sending)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_sending)
stop_button.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=5)

root.mainloop()

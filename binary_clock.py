#TODO: Make red and green change slowly througout the hour/minute instead of immediately
#TODO: Add a "Save Color" button that captures the current color value and saves it to a text file (e.g. saved_colors.txt)
#TODO: Change the foreground (text) color dynamically to have better contrast with any given background color
#TODO: Make color lable larger, consider changing font
#TODO: Remove title bar and use small quit button instead

import tkinter as tk
from threading import Thread
import time
from datetime import datetime
import os

second_text = ""
minute_text = ""
hour_text = ""

second_color = 0
minute_color = 0
hour_color = 0

bg_color = "#000000"
stop = False

dir = os.getcwd()

class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.divider_text = " : "
        self.create_widgets()

    def create_widgets(self):
        global second_text, minute_text, hour_text

        # self.winfo_toplevel().title("Binary Color Clock")

        self.save = tk.Button(self)
        self.save["text"] = "Save Color"
        self.save["command"] = self.save_color
        self.save["width"] = 9
        # self.save.grid(column=2, row=3)

        self.divider0 = tk.Label(self, text=self.divider_text, fg="black")
        self.divider1 = tk.Label(self, text=self.divider_text, fg="black")

        self.hour = tk.Label(self)
        self.hour["text"] = "0000 0000"
        self.hour["fg"] = "white"
        self.hour["width"] = 9
        self.hour.grid(column=0, row=1)

        self.divider0["fg"] = "white"
        self.divider0["width"] = 3
        self.divider0.grid(column=1, row=1)

        self.minute = tk.Label(self)
        self.minute["text"] = "0000 0000"
        self.minute["width"] = 9
        self.minute["fg"] = "white"
        self.minute.grid(column=2, row=1)

        self.divider1["fg"] = "white"
        self.divider1["width"] = 3
        self.divider1.grid(column=3, row=1)

        self.second = tk.Label(self)
        self.second["text"] = second_text
        self.second["fg"] = "white"
        self.second["width"] = 9
        self.second.grid(column=4, row=1)

        self.color_label = tk.Label(self)
        self.color_label["text"] = ""
        self.color_label["fg"] = "#E6E6E6"
        self.color_label["width"] = 9
        self.color_label.grid(column=0, row=2, columnspan=5, stick="ew")

        # self.blank0 = tk.Label(self)
        # self.blank0["width"] = 9
        # self.blank0.grid(column=0, row=2)
        # self.blank1 = tk.Label(self)
        # self.blank1["width"] = 3
        # self.blank1.grid(column=1, row=2)
        # self.blank3 = tk.Label(self)
        # self.blank3["width"] = 3
        # self.blank3.grid(column=3, row=2)
        # self.blank4 = tk.Label(self)
        # self.blank4["width"] = 9
        # self.blank4.grid(column=4, row=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.grid(row=2, column=2)

        self.master.after(0, self.update)

    def update(self):
        bg_color = "#" + format(round(hour_color), "02X") + format(round(minute_color), "02X") + format(round(second_color), "02X")

        self.second["text"] = second_text
        self.second["bg"] = bg_color

        self.minute["text"] = minute_text
        self.minute["bg"] = bg_color

        self.hour["text"] = hour_text
        self.hour["bg"] = bg_color

        self.color_label["text"] = bg_color
        self.color_label["bg"] = bg_color

        self.divider0["bg"] = bg_color
        self.divider1["bg"] = bg_color
        # self.blank0["bg"] = bg_color
        # self.blank1["bg"] = bg_color
        # self.blank3["bg"] = bg_color
        # self.blank4["bg"] = bg_color
        self.master.configure(background=bg_color)
        self.master.after(10, self.update)

    def save_color(self):
        save_file = open(dir + "/saved_colors.txt", "a+")
        print(bg_color, file=save_file)
        print(f"Saved color {bg_color}")
        save_file.close()

def _delete_window():
    #print("Delete Window")
    try:
        root.destroy()
    except:
        pass

def _destroy(event):
    global stop
    #print("Destroy")
    stop = True

def thread_test():
    global second_text, second_color
    global minute_text, minute_color
    global hour_text, hour_color
    global bg_color

    hr  = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second

    sec_ten = sec // 10
    sec_one = sec - (10 * sec_ten)
    min_ten = min // 10
    min_one = min - (10 * min_ten)
    hr_ten  = hr // 10
    hr_one  = hr - (10 * hr_ten)

    second_color = int((255 / 60) * sec)
    minute_color = int((255 / 60) * min)
    hour_color   = int((255 / 24) * hr)

    bg_color = "#" + format(hour_color, "02X") + format(minute_color, "02X") + format(second_color, "02X")

    while(not stop):
        hr  = datetime.now().hour
        min = datetime.now().minute
        sec = datetime.now().second

        sec_ten = sec // 10
        sec_one = sec - (10 * sec_ten)
        min_ten = min // 10
        min_one = min - (10 * min_ten)
        hr_ten  = hr // 10
        hr_one  = hr - (10 * hr_ten)

        second_text = format(sec_ten, "04b") + " " + format(sec_one, "04b")
        minute_text = format(min_ten, "04b") + " " + format(min_one, "04b")
        hour_text = format(hr_ten, "04b") + " " + format(hr_one, "04b")

        # c1 = (int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:], 16))
        c1 = (hour_color, minute_color, second_color)

        sec_color = (255 / 60) * sec
        min_color = (255 / 60) * min
        hr_color   = (255 / 24) * hr

        c2 = (hr_color, min_color, sec_color)

        #bg_color = "#" + hour_color + minute_color + second_color

        color_fade(c1, c2, 1, 100)
    # for _ in range(10):
    #     print("Threaded")
def color_fade(c1, c2, transition_time, steps=100):
    global second_color
    global minute_color
    global hour_color
    global bg_color

    delta_r = (c1[0] - c2[0]) / (steps * 3600)
    delta_g = (c1[1] - c2[1]) / (steps * 60)
    delta_b = (c1[2] - c2[2]) / (steps * 5)
    # print(f"C1: {c1} -- C2: {c2}")
    # print(f"({delta_r}, {delta_g}, {delta_b})")

    transition_step = transition_time / steps
    r, g, b = c1
    # g = c1[1]
    # b = c1[2]
    # print(f"({r}, {g}, {b})")

    for _ in range(steps):
        r -= delta_r
        g -= delta_g
        b -= delta_b

        second_color = b
        minute_color = g
        hour_color = r
        # ro = format(round(r), "02X")
        # go = format(round(g), "02X")
        # bo = format(round(b), "02X")
        #
        # bg_color = "#" + ro + go + bo
        time.sleep(transition_step)

test_thread = Thread(target=thread_test)
test_thread.start()

root = tk.Tk()
img = tk.Image("photo", file="clock.png")
root.tk.call("wm", "iconphoto", root._w,img)
root.title("Binary Color Clock")
root.protocol("WM_DELETE_WINDOW", _delete_window)
root.bind("<Destroy>", _destroy)
app = Application(master=root)
app.mainloop()

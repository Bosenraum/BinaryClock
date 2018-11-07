import tkinter as tk
from threading import Thread
import time
from datetime import datetime

second_text = ""
minute_text = ""
hour_text = ""

second_color = 0
minute_color = 0
hour_color   = 0

minute_active = False
hour_active = False

bg_color = ""
stop = False

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

        self.hello = tk.Button(self)
        self.hello["text"] = "Click here!"
        self.hello["command"] = self.say_hi
        #self.hello.grid(column=2, row=0)

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
        self.color_label.grid(column=2, row=2)

        self.blank0 = tk.Label(self)
        self.blank0["width"] = 9
        self.blank0.grid(column=0, row=2)
        self.blank1 = tk.Label(self)
        self.blank1["width"] = 3
        self.blank1.grid(column=1, row=2)
        self.blank3 = tk.Label(self)
        self.blank3["width"] = 3
        self.blank3.grid(column=3, row=2)
        self.blank4 = tk.Label(self)
        self.blank4["width"] = 9
        self.blank4.grid(column=4, row=2)

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        #self.quit.grid(row=2, column=2)

        self.master.after(0, self.update)

    def update(self):
        bg_color = "#" + format(int(hour_color), "02X") + format(int(minute_color), "02X") + format(int(second_color), "02X")

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
        self.blank0["bg"] = bg_color
        self.blank1["bg"] = bg_color
        self.blank3["bg"] = bg_color
        self.blank4["bg"] = bg_color
        self.master.configure(background=bg_color)
        self.master.after(10, self.update)

    def say_hi(self):
        print("Hello World!")

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
    global second_text
    global minute_text
    global hour_text
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

        # Format time for BCD
        second_text = format(sec_ten, "04b") + " " + format(sec_one, "04b")
        minute_text = format(min_ten, "04b") + " " + format(min_one, "04b")
        hour_text = format(hr_ten, "04b") + " " + format(hr_one, "04b")

        second_color = int((255 / 60) * sec)
        minute_color = int((255 / 60) * min)
        hour_color   = int((255 / 24) * hr)

        if not bg_color == "":
            c1 = (int(bg_color[1:3], 16), int(bg_color[3:5], 16), int(bg_color[5:], 16))
        else:
            c1 = (second_color, minute_color, hour_color)

        # c2 = (hour_color, minute_color, second_color)

        #bg_color = "#" + hour_color + minute_color + second_color
        if not minute_active:
            minute_color_change(c1[1], minute_color, 100)
        if not hour_active:
            hour_color_change(c1[2], hour_color, 100)

        second_fade(c1[0], second_color, 100)
    # for _ in range(10):
    #     print("Threaded")
def second_fade(b1, b2, steps=100):
    global second_color

    delta_b = (b1 - b2) / steps
    b = b1

    for _ in range(steps):
        b -= delta_b
        second_color = b
        time.sleep(1/steps)

def minute_color_change(g1, g2, steps=100):
    global minute_active
    minute_active = True
    minute_thread = Thread(target=lambda: minute_fade(g1, g2, steps))
    print("Starting minute thread")
    minute_thread.start()

def minute_fade(g1, g2, steps=100):
    global minute_active
    global minute_color

    delta_g = (g1 - g2) / steps
    g = g1

    for _ in range(steps):
        g -= delta_g
        minute_color = round(g)
        time.sleep(60/steps)

    minute_active = False

def hour_color_change(r1, r2, steps=100):
    global hour_active
    hour_active = True
    hour_thread = Thread(target=lambda: hour_fade(r1, r2, steps))
    print("Starting hour thread")
    hour_thread.start()

def hour_fade(r1, r2, steps=100):
    global hour_active
    global hour_color

    delta_r = (r1 - r2) / steps
    r = r1

    for _ in range(steps):
        r -= delta_r
        hour_color = round(r)
        time.sleep(3600/steps)

    hour_active = False

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

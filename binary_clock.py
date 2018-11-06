import tkinter as tk
from threading import Thread
import time

second_text = ""
minute_text = ""
hour_text = ""
bg_color = ""

class Application(tk.Frame):


    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.divider_text = " : "
        self.create_widgets()

    def create_widgets(self):
        global second_text, minute_text, hour_text

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
        self.master.after(100, self.update)

    def say_hi(self):
        print("Hello World!")

def thread_test():
    global second_text
    global minute_text
    global hour_text
    global bg_color

    sec_one = 0
    sec_ten = 0
    min_one = 5
    min_ten = 2
    hr_one  = 6
    hr_ten  = 1

    while(True):
        if sec_one < 9:
            sec_one += 1
        else:
            sec_one = 0
            if sec_ten < 5:
                sec_ten += 1
            else:
                sec_ten = 0
                if min_one < 9:
                    min_one += 1
                else:
                    min_one = 0
                    if min_ten < 5:
                        min_ten += 1
                    else:
                        min_ten = 0
                        if hr_one < 9 and hr_ten < 2:
                            hr_one += 1
                        elif hr_ten == 2 and hr_one < 4:
                            hr_one += 1
                        else:
                            hr_one = 0
                            if hr_ten < 2:
                                hr_ten += 1
                            else:
                                hr_ten = 0
        #print(second_text)
        second_text = format(sec_ten, "04b") + " " + format(sec_one, "04b")
        minute_text = format(min_ten, "04b") + " " + format(min_one, "04b")
        hour_text = format(hr_ten, "04b") + " " + format(hr_one, "04b")

        second_color = format(int((255 / 60) * (10*sec_ten + sec_one)), "02X")
        minute_color = format(int((255 / 60) * (10*min_ten + min_one)), "02X")
        hour_color = format(int((255 / 24) * (10*hr_ten + hr_one)), "02X")

        bg_color = "#" + hour_color + minute_color + second_color

        time.sleep(1)
    # for _ in range(10):
    #     print("Threaded")

test_thread = Thread(target=thread_test)
test_thread.start()

root = tk.Tk()
app = Application(master=root)
app.mainloop()

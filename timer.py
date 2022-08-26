import time
import tkinter
class Timer:
    def __init__(self, canvas):

        self.canvas = canvas
        self.ms = 10
        self.start_time = 0
        self.stop_time = 0
        self.flag = False
        self.after_id = 0
        self.label = tkinter.Label(self.canvas, text="0.00")
        self.label.place(x=950, y=10)

    def update_time(self):
        self.after_id = self.canvas.after(10, self.update_time)
        self.now_time = time.time()
        self.elapsed_time = self.now_time - self.start_time
        self.elapsed_time_str = "{:.2f}".format(self.elapsed_time)
        self.label.config(text=self.elapsed_time_str)

    def start(self):
        if not self.flag:
            self.flag = True
            self.start_time = time.time()
            self.after_id = self.label.after(10, self.update_time)

    def stop(self):
        if self.flag:
            self.label.after_cancel(self.after_id)
            self.flag = False

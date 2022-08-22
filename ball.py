import math
import random
import time
import tkinter

from timer import Timer


class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.timer = Timer(self.canvas)
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        self.speed = 0
        self.count = 0
        self.x = 0
        self.y = 0

        self.label = self.canvas.create_text(
            35, 20, text=f"Count:{self.count}", tag="text"
        )


    def start(self, evt):
        if self.speed != 0:
            return
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3
        self.angle = math.radians(random.choice(list(range(20, 65, 5))))
        self.direction = random.choice([1, -1])  # xの向きをランダムに。

        self.x = math.cos(self.angle) * self.speed * self.direction
        self.y = math.sin(self.angle) * self.speed
        self.timer.start()

    def c(self):
        self.count += 1
        self.canvas.delete("text")

        self.label = self.canvas.create_text(
            35, 20, text=f"Count:{self.count}", tag="text"
        )

    def end(self):
        self.canvas.create_text(
            self.canvas_width // 2,
            self.canvas_height // 2,
            text="GAME OVER",
            font=("", 40),
            fill="blue",
        )
        self.btn = tkinter.Button(
            self.canvas,
            text="Quit",
            command=self.ex,
            width=20,
            height=2,
            fg="blue",
            bg="cyan",
            font=("", 10),
        )
        self.btn.place(x=self.canvas_width // 2 - 90, y=self.canvas_height // 2 + 50)

    def ex(self):
        exit()

    def speeds(self):
        self.x *= 1.05
        self.y *= 1.05

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.speeds()
            self.fix(pos[0] - 0, 0)
        if pos[1] <= 0:
            self.speeds()
            self.fix(0, pos[1])
        if pos[2] >= self.canvas_width:
            self.speeds()
            self.fix(pos[2] - self.canvas_width, 0)

        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()
            self.end()
            self.timer.stop()

        paddle_pos = self.canvas.coords(self.paddle.id)
        if (
            pos[2] >= paddle_pos[0]
            and pos[0] <= paddle_pos[2]
            and paddle_pos[1] <= pos[3] <= paddle_pos[3]
        ):
            self.fix(0, pos[3] - paddle_pos[1])
            self.c()

    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))

        if diff_x != 0:
            self.x = -self.x

        if diff_y != 0:
            self.y = -self.y

    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        # messagebox.showinfo("Information", "wwwwwwwwwwwwwww")
        # exit()

import time
import tkinter

INTERVAL = 10

start_time = 0

start_flag = False

after_id = 0


def update_time():
    global start_time
    global app, label
    global after_id

    after_id = app.after(INTERVAL, update_time)

    now_time = time.time()

    elapsed_time = now_time - start_time

    elapsed_time_str = "{:.2f}".format(elapsed_time)

    label.config(text=elapsed_time_str)


def start():
    global app
    global start_flag
    global start_time
    global after_id

    if not start_flag:

        start_flag = True

        start_time = time.time()

        after_id = app.after(INTERVAL, update_time)


def stop():
    global start_flag
    global after_id

    if start_flag:

        app.after_cancel(after_id)

        start_flag = False


app = tkinter.Tk()
app.title("stop watch")
app.geometry("200x200")

label = tkinter.Label(
    app,
    text="0.00",
    width=6,
    font=("", 50, "bold"),
)
label.pack(padx=10, pady=10)

start_button = tkinter.Button(app, text="START", command=start)
start_button.pack(pady=5)

stop_button = tkinter.Button(app, text="STOP", command=stop)
stop_button.pack(pady=5)

app.mainloop()

from tkinter import *
import socket


def mouse_wheel(event, canvas):
    pc_name = str(socket.gethostname()).split("-")
    try:
        if pc_name[0] == "Macbooks":
            delta_event = event.delta
        else:
            delta_event = event.delta / 120
        canvas.yview_scroll(-1 * (delta_event), "units")
    except:
        pass


def Scroll_my_frame(root, width, height, color, no_frames, frame_width, frames_height):
    edit_Frame = LabelFrame(root)
    canvas = Canvas(edit_Frame, bg=color, width=width, height=height)
    main_scrollbar = Scrollbar(edit_Frame, orient="vertical", command=canvas.yview)
    scrolling_frame = LabelFrame(canvas, bg=color, width=width - 30, height=height - 30)
    scrolling_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )
    canvas.create_window((0, 0), window=scrolling_frame, anchor="nw")
    canvas.configure(yscrollcommand=main_scrollbar.set)
    canvas.bind_all("<MouseWheel>", lambda event, canvas=canvas: mouse_wheel(event, canvas))
    frames = []
    for i in range(no_frames):
        editFrame = LabelFrame(scrolling_frame, bg=color, width=frame_width, height=frames_height[i])
        editFrame.pack()
        frames.append(editFrame)

    edit_Frame.pack()
    edit_Frame.place(x=5, y=5)
    canvas.pack(side="left", fill="both", expand=True)
    main_scrollbar.pack(side=RIGHT, fill=Y)
    return frames

import os
from tkinter import *
from PIL import ImageTk, Image

FILE_PATH = "../ImageFiles/num_lanes_test.csv"
IMAGE_PATH = "../ImageFiles/direct_site_images"

currant_image_index = -1
images = os.listdir(IMAGE_PATH)
images.sort(key=lambda x: int(x.split(".")[0]))


def next_image():
    global currant_image_index, image_label, entry_label
    currant_image_index += 1
    entry_label.delete(0, 'end')
    entry_label.focus()
    if currant_image_index < len(images):
        _display_image()
    else:
        currant_image_index = len(images) - 1  # Prevent index out of range
        print("No more images.")


def _display_image():
    image_path = os.path.join(IMAGE_PATH, images[currant_image_index])
    image = Image.open(image_path)
    image = ImageTk.PhotoImage(image)
    global image_label
    image_label.config(image=image)
    image_label.image = image


def enter_value(image: str, lanes: str) -> None:
    new_line = f"\n{image}, {lanes},"
    with open(FILE_PATH, "a") as lanes_file:
        lanes_file.write(new_line)


def enter_image():
    global entry_label
    lanes = entry_label.get()
    enter_value(images[currant_image_index], lanes)
    next_image()


window = Tk()
window.title("Custom Image Annotator")
window.config(bg="black")

image_label = Label(width=300, height=300)
image_label.grid(row=0, column=0, columnspan=3)

next_image_button = Button(text="Skip", command=next_image, width=10)
next_image_button.grid(row=1, column=0)

entry_label = Entry(width=23)
entry_label.grid(row=1, column=1)

next_image_button = Button(text="Save", command=enter_image, width=10)
next_image_button.grid(row=1, column=2)

next_image()

window.mainloop()

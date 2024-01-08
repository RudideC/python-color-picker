import tkinter as tk
import pyperclip

window = tk.Tk()

window.title("Color picker")

def sliderUpdate(value):
    red = redSlider.get()
    green = greenSlider.get()
    blue = blueSlider.get()

    color = "#%02x%02x%02x" % (red, green, blue)
    canvas.config(bg = color)
    hexText.delete(0, tk.END)
    hexText.insert(0, color)

def copyToClipboard(text):
    pyperclip.copy(text)

def copyColorToClipboard():
    copyToClipboard(hexText.get())




redSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
greenSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)
blueSlider = tk.Scale(window, from_=0, to=255, command=sliderUpdate)

canvas = tk.Canvas(window, width=200, height=200)
canvas.config(bg = "#000000")

hexText = tk.Entry(window)
hexText.insert(0, "#000000")

button = tk.Button(window, text="Copy to clipboard", command=copyColorToClipboard)

redSlider.grid(row=1, column=1)
greenSlider.grid(row=1, column=2)
blueSlider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)
hexText.grid(row=3, column=1, columnspan=3)
button.grid(row=4, column=1, columnspan=3)

tk.mainloop()

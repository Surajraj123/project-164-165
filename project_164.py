from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("IMAGE VIEWER")
root.geometry("500x500")
root.configure(background = "black")

label_image = Label(root, bg = "orange", highlightthickness = 5, borderwidth = 2, relief = SOLID)
label_image.place(relx = 0.5, rely = 0.5, anchor = CENTER)

img_path = ""
def OpenImage():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Text File", filetypes = [("Image Files", "*.jpg *.gif *.png *.jpeg")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    label_image["image"] = img
    img.close()
    
def rotateImage():
    global img_path
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im.rotate(180))
    label_image["image"] = img
    print(img_path)
    img.close()
    
btn = Button(root, text = "Open Image", font = ("TimesNew Roman0", 12), bg = "grey", fg = "white", command = OpenImage, relief = SOLID, padx = 15)
btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

btn = Button(root, text = "Rotate Image", font = ("TimesNew Roman0", 12), bg = "grey", fg = "white", command = rotateImage, relief = SOLID, padx = 15)
btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)

label_footer = Label(root, text = "Created by Suraj Sahoo ", bg = "black", fg = "white")
label_footer.place(relx = 0.5, rely = 0.95, anchor = CENTER)

root.mainloop()
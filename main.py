from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1200x600+10+10")
        self.root.title("Face Recognition System")
        
        img1 = Image.open(r"D:\MyApp\python_project\face_student_attendane_system\app_images\bk_computer.jpg")
        img1 = img1.resize((600,120),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        frm_lbl = Label(self.root,image=self.photoimg1)
        frm_lbl.place(x = 0,y = 0,width=600,height=120)
        
        img1 = Image.open(r"D:\MyApp\python_project\face_student_attendane_system\app_images\bk_computer.jpg")
        img1 = img1.resize((600,120),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        frm_lbl = Label(self.root,image=self.photoimg1)
        frm_lbl.place(x = 0,y = 0,width=600,height=120)
        
        img1 = Image.open(r"D:\MyApp\python_project\face_student_attendane_system\app_images\bk_computer.jpg")
        img1 = img1.resize((600,120),Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        
        frm_lbl = Label(self.root,image=self.photoimg1)
        frm_lbl.place(x = 0,y = 0,width=600,height=120)





if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
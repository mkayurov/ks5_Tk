from tkinter import *
from tkinter import messagebox, filedialog
#from winsound import *


class Calculator():
	def __init__(self, button, parent, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel(parent)
		self.root["bg"] = "black"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.close_calculator)
		self.root.tk.eval('tk::PlaceWindow {0} widget {0}'.format(self.root, parent))
		# self.root.resizable(False, False)
		
		self.root.focus_set()
		self.draw_widgets_calc()
		
		
		
	def pressed_button(self, btn):
		self.title = btn
		print(self.title)
		
	def draw_widgets_calc(self):
		self.root.img = PhotoImage(file='images/calc_tablo.png')
		
		self.tablo = Label(self.root, image=self.root.img, bd=0)
		self.tablo.place(x=0, y=0)
		
		self.tablo.img_reset = PhotoImage(file='images/calc_reset.png')
		self.tablo.img_del_end = PhotoImage(file='images/calc_del_end.png')
		self.tablo.img_root = PhotoImage(file='images/calc_root.png')
		self.tablo.img_prec = PhotoImage(file='images/calc_prec.png')
		self.tablo.img_division = PhotoImage(file='images/calc_division.png')
		self.tablo.img_multiplay = PhotoImage(file='images/calc_multiply.png')
		self.tablo.img_minus= PhotoImage(file='images/calc_minus.png')
		self.tablo.img_dot= PhotoImage(file='images/calc_dot.png')
		self.tablo.img_result = PhotoImage(file='images/calc_result.png')
		self.tablo.img_plus = PhotoImage(file='images/calc_plus.png')
		
		
		self.display = Label(self.tablo, text='', width=12, font="Arial 24 bold", justify=RIGHT, bg="#95a768", fg="#3e3e3e", bd=0) # 13 символов
		self.display.place(x=30, y=48)
		
		
		self.btn_reset = Button(self.tablo, image=self.tablo.img_reset, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_reset.place(x=24, y=170)
		self.btn_del_end = Button(self.tablo, image=self.tablo.img_del_end, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("ck"))
		self.btn_del_end.place(x=90, y=170)
		self.btn_root = Button(self.tablo, image=self.tablo.img_root, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_root.place(x=156, y=170)
		self.btn_prec = Button(self.tablo, image=self.tablo.img_prec, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("%"))
		self.btn_prec.place(x=222, y=170)
		self.btn_result = Button(self.tablo, image=self.tablo.img_result, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("="))
		self.btn_result.place(x=156, y=370)
		self.btn_minus = Button(self.tablo, image=self.tablo.img_minus, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("-"))
		self.btn_minus.place(x=222, y=320)
		self.btn_plus = Button(self.tablo, image=self.tablo.img_plus, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("+"))
		self.btn_plus.place(x=222, y=370)
		self.btn_multiply = Button(self.tablo, image=self.tablo.img_multiplay, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("*"))
		self.btn_multiply.place(x=222, y=270)
		self.btn_dot = Button(self.tablo, image=self.tablo.img_dot, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("."))
		self.btn_dot.place(x=90, y=370)
		self.btn_division = Button(self.tablo, image=self.tablo.img_division, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("/"))
		self.btn_division.place(x=222, y=220)
		
		
		self.tablo.img_1 = PhotoImage(file='images/calc_1.png')
		self.tablo.img_2 = PhotoImage(file='images/calc_2.png')
		self.tablo.img_3 = PhotoImage(file='images/calc_3.png')
		self.tablo.img_4 = PhotoImage(file='images/calc_4.png')
		self.tablo.img_5 = PhotoImage(file='images/calc_5.png')
		self.tablo.img_6 = PhotoImage(file='images/calc_6.png')
		self.tablo.img_7 = PhotoImage(file='images/calc_7.png')
		self.tablo.img_8 = PhotoImage(file='images/calc_8.png')
		self.tablo.img_9 = PhotoImage(file='images/calc_9.png')
		self.tablo.img_0 = PhotoImage(file='images/calc_0.png')
		
		
		self.btn_1 = Button(self.tablo, image=self.tablo.img_1, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_1.place(x=24, y=321)
		self.btn_2 = Button(self.tablo, image=self.tablo.img_2, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_2.place(x=90, y=320)
		self.btn_3 = Button(self.tablo, image=self.tablo.img_3, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_3.place(x=156, y=320)
		self.btn_4 = Button(self.tablo, image=self.tablo.img_4, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_4.place(x=24, y=270)
		self.btn_5 = Button(self.tablo, image=self.tablo.img_5, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_5.place(x=90, y=270)
		self.btn_6 = Button(self.tablo, image=self.tablo.img_6, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_6.place(x=156, y=270)
		self.btn_7 = Button(self.tablo, image=self.tablo.img_7, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_7.place(x=24, y=220)
		self.btn_8 = Button(self.tablo, image=self.tablo.img_8, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_8.place(x=90, y=220)
		self.btn_9 = Button(self.tablo, image=self.tablo.img_9, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_9.place(x=156, y=220)
		self.btn_0 = Button(self.tablo, image=self.tablo.img_0, bg="#d9d9d9", activebackground="#d9d9d9", bd=0, command=lambda:self.pressed_button("c"))
		self.btn_0.place(x=24, y=370)
		

	def close_calculator(self):
		self.root.destroy()
		
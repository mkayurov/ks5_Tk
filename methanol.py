from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#from winsound import *
import os
import sqlite3


class MetanolCalculate:
	def __init__(self, button, parent, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel(parent)
		self.root["bg"] = "#b8c4bf"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
		self.root.resizable(False, False)
		self.root.tk.eval('tk::PlaceWindow {0} widget {0}'.format(self.root, parent))
		
		self.num_char1 = StringVar()
		self.num_char2 = StringVar()
		self.num_char1.trace("w", self.check_field1)
		self.num_char2.trace("w", self.check_field2)
		self.btn = button
	
		self.root.grab_set()
		self.root.focus_set()
		self.draw_widgets_metanol()
		
		
	def show_error(self, title_, info_):
		messagebox.showinfo(title_, info_)
		
		
	def show_info(self, title_, info_):
		messagebox.showinfo(title_, info_)
		
		
	def on_closing(self):
		self.btn.configure(state=NORMAL) 
		self.root.destroy()
  
		
	def read_data(self, level):
		""" функция соединяется с базой данных  принимает число(уровень метанола(см)) и возвращает объём метанола в м2 и процентах  """
		try:
			self.db = sqlite3.connect("methanol.db")
			self.cursor = self.db.cursor()
			print("соединение установлено")
		except Exception:
			self.show_error("Ошибка!", "файл базы данных отсутствует")
			return
		
		for i in self.cursor.execute(''' SELECT * FROM capacity '''):
			if int(level) == i[0]:
				vol = i[1]
				per = i[2]
				vol = vol.replace(",", ".")
				per = per.replace(",", ".")
				break
			else:
				continue
		self.cursor.close()
		self.db.close()
		return round(float(vol), 1), per	

		
	def draw_widgets_metanol(self):
		self.lbl_1 = Label(self.root, text="E-1", font="Ariel 10", bg="#b8c4bf")
		self.lbl_1.place(x=75, y=20)
		self.lbl_2 = Label(self.root, text="E-2", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_2.place(x=75, y=60)
		self.lbl_3 = Label(self.root, text="мм", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_3.place(x=195, y=20)
		self.lbl_4 = Label(self.root, text="мм", font="Ariel 10", justify=CENTER, bg="#b8c4bf")
		self.lbl_4.place(x=195, y=60)
		self.text_field_volume1 = Entry(self.root, textvariable=self.num_char1, font="Garamond 12 bold", justify=CENTER, width=10, bd=2, relief=RIDGE)
		self.text_field_volume1.place(x=105, y=20)
		self.text_field_volume2 = Entry(self.root, textvariable=self.num_char2, font="Garamond 12 bold", justify=CENTER, width=10, bd=2, relief=RIDGE)
		self.text_field_volume2.place(x=105, y=60)
		self.btn_met_calculate = Button(self.root, text="Расчитать", width=20, 
													fg="white", font="Ariel 10 bold", activebackground="#7d8481", 
													activeforeground="white", bg="#7d8481", relief=GROOVE,  
													command=lambda:self.get_volume(self.btn_met_calculate))
		self.btn_met_calculate.place(x=70, y=110)
		
	
	
	def check_field1(self, *args):
		"""  функция ограничивает ввод более 4-х цифр, максимальное, а так же других символов кроме цифр """
		char = self.num_char1.get()
		if char.isdigit():
			if len(char) == 4:
				if int(char) <= 2400:
					print("Заебись!")
					return 
					self.text_field_volume1.config(state="readonly")
				else:
					self.show_info("Ошибка!", "максимальный уровень емкости 2400 мм.")
					return
			else:
				self.text_field_volume1.delete("4", "end")	
		else:
			self.text_field_volume1.delete("0", "end")
			# self.show_error("Ошибка!", "недопустимый символ")
			return
	
	
	def check_field2(self, *args):
		"""проверка в реальном времени символы вводимые пользователем """
		char = self.num_char2.get()
		if char.isdigit():
			if len(char) == 4:
				if int(char) <= 2400:
					print("Заебись!")
					# self.text_field_volume2.config(state="readonly")
					return
				else:
					self.show_info("Ошибка!", "максимальный уровень емкости 2400 мм.")
					return
			else:
				self.text_field_volume2.delete("4", "end")	
		else:
			self.text_field_volume2.delete("0", "end")
			# self.show_error("Ошибка!", "недопустимый символ")
			return 
		
		
	def to_make_round(self, number):
		# функция округляет число в меньшую или большую сторону
		if int(number) < 10:
			number = '10'

		if int(number[-1]) >= 5:
			number = number[:-1]
			number = int(number)
			number += 1
			number = str(number)
			number += "0"
		else:
			number = number[:-1]
			number += "0"
			# print(number)
			print("Not")
		return number
			
			
	def get_volume(self, btn):
		print(self.num_char1.get())
		btn_title = btn.cget("text")
		text_vol1 = self.text_field_volume1.get()
		text_vol2 = self.text_field_volume2.get()
		
		if text_vol1 != "" and text_vol2 != "":
			text_vol1 = self.to_make_round(text_vol1)
			text_vol2 = self.to_make_round(text_vol2)
			print(text_vol1)
			print(text_vol2)
			try:
				volume1, persance1 = self.read_data(text_vol1)
				volume2, persance2 = self.read_data(text_vol2)
				sum_pers = float(volume1) + float(volume2)
			except Exception:
				self.show_error("Ошибка!", "Не найден файл базы данных")
				return
			self.show_info("Расчет выполнен", "Е-1:\t{} м3\n\t{} %\n\nЕ-2:\t{} м3\n\t{} %\n\nобщий объём:  {} м3          \n".format(volume1, 
																														persance1,
																														volume2, 
																														persance2, 
																														round(sum_pers, 1)))
			self.root.destroy()
			self.btn.configure(state=NORMAL) 
		else:
			self.show_info("Ошибка!", "заполни оба поля")
			return
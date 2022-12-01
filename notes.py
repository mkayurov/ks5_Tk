from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
#from winsound import *


class Notes:
	def __init__(self, button, parent, width, height, indentation_x, indentation_y, name_title):
		self.root = Toplevel(parent)
		self.root["bg"] = "#b8c4bf"
		self.root.title(name_title)
		self.root.geometry("{}x{}+{}+{}".format(width, height, indentation_x, indentation_y))
		self.root.protocol("WM_DELETE_WINDOW", self.exit_notepad)
		self.root.tk.eval('tk::PlaceWindow {0} widget {0}'.format(self.root, parent))
		
		self.btn = button
		# starting methods
		self.root.grab_set()
		self.root.focus_set()
		self.draw_widgets_notes()
		self.menu_bar()
	
	
	def show_error(self, title_, error_):
		messagebox.showerror(title_, error_)
	
	
	def save_file(self):
		try:
			self.file_path = filedialog.asksaveasfilename(defaultextension='.txt', initialdir='C:/PyProjects/ks5/saves')
			f = open(self.file_path, 'w', encoding='utf-8')
			text = self.text_field.get('1.0', END)
			f.write(text)
			f.close()
		except Exception:
			self.show_error('','Ошибка сохранения файла')
	
	
	def open_file(self):
		try:
			self.file_path = filedialog.askopenfilename(filetypes=[('Текстовый документ (*.txt)', '*.txt')], initialdir='C:/PyProjects/ks5/saves')
			if self.file_path:
				self.text_field.delete('1.0', END)
				self.text_field.insert('1.0', open(self.file_path, encoding='utf-8').read())
		except Exception:
			self.show_error('','Ошибка сохранения файла')
	
	def menu_bar(self):
		
		self.m_bar = Menu(self.root)
		self.root.config(menu=self.m_bar)
		
		self.file = Menu(self.m_bar, tearoff=0)
		self.m_bar.add_cascade(label="файл", menu=self.file, state=NORMAL)
		self.file.add_command(label="новый")
		self.file.add_command(label="открыть", command=self.open_file)
		self.file.add_command(label="сохранить", command=self.save_file)
		self.file.add_command(label="выход", command=self.exit_notepad)
		
		self.settings = Menu(self.m_bar, tearoff=0)
		self.m_bar.add_cascade(label="настройки", menu=self.settings)
		
		self.settings_theme =Menu(self.settings, tearoff=0)
		self.settings.add_cascade(label="цветовая тема", menu=self.settings_theme)
		self.settings_theme.add_command(label="темная", command=lambda:self.change_theme('dark'))
		self.settings_theme.add_command(label="светлая", command=lambda:self.change_theme('light'))
		self.settings_theme.add_command(label="стандартная", command=self.change_theme('default'))
		
		self.settings_font =Menu(self.settings, tearoff=0)
		self.settings.add_cascade(label="шрифт...", menu=self.settings_font)
		self.settings_font.add_command(label="Arial", command=lambda:self.change_fonts('Arial'))
		self.settings_font.add_command(label="CSMS", command=lambda:self.change_fonts('CSMS'))
		self.settings_font.add_command(label="Default", command=lambda:self.change_fonts('Default'))
	
	
	def change_fonts(self, font):
		self.fonts = {
			'Arial': {
				'font': 'Arial 14 bold'
			},
			'CSMS': {
				'font': ('Times New Roman', 14, 'bold')
			},
			'Default': {
				'font': ('Garamond', 14, 'bold')
			}
		}
		
		self.text_field['font'] = self.fonts[font]['font']
	
		
	def change_theme(self, theme):
		self.color_themes = {
			'dark': {
				'field_bg': '#1f1f1f', 'text_fg': '#2ec865', 'cursor': 'white', 'select_bg': 'gray'
			},
			'light': {
				'field_bg': '#f7e6a5', 'text_fg': '#353171', 'cursor': 'black', 'select_bg': '#8D917A'
				},
			'default': {
				'field_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': 'blue'
				}
		}
		
		
		self.text_field['bg'] = self.color_themes[theme]['field_bg']
		self.text_field['fg'] = self.color_themes[theme]['text_fg']
		self.text_field['insertbackground'] = self.color_themes[theme]['cursor']
		self.text_field['selectbackground'] = self.color_themes[theme]['select_bg']
			
	
	def draw_widgets_notes(self):
		self.frame = Frame(self.root)
		self.frame.pack(expand=1, fill='both')
		
		self.text_field = ScrolledText(self.frame, bg='black', fg='lime',  font="Garamond 14 bold", padx=10, pady=10, insertbackground='gray', selectbackground='gray', wrap=WORD, )
		self.text_field.pack(expand=1, fill='both', side=LEFT)
	
	
	def exit_notepad(self):
		#PlaySound("wav.wav", SND_ASYNC)
		if messagebox.askyesno("Внимание !", "Выйти уверены что хотите выйти?"):
			# self.save_file()
			self.btn.configure(state=NORMAL)
			self.root.destroy()
		else:
			return
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
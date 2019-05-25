import tmdbsimple as tmdb  
tmdb.API_KEY = '3aac901eabe71551bd666ed711135477'

import requests
from io import BytesIO

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import Entry

from moviepy.editor import *
import pygame

import arrow






def clear_page():
	for widget in window.winfo_children():
		widget.destroy()


def Home():
	clear_page()

	label = tk.Label(text="SNetflix")
	label.config(font=("Times", 60, "bold"))
	label.configure(background='red3')
	# "Times", "24", "bold italic"
	label.pack(side="top", fill="x", pady=10)

	# Button to go to browser
	Browse_B = tk.Button(window, text="Browse", command=Browse)
	Browse_B.config(font=("Times", 20, "bold"), width=20)
	Browse_B.configure(background='red')
	Browse_B.pack()

	# Button to go to update
	Update_B = tk.Button(window, text="Update", command=Update)
	Update_B.config(font=("Times", 20, "bold"), width=20)
	Update_B.configure(background='red')
	Update_B.pack()

	# Button to go to server to share movie
	Share_B = tk.Button(window, text="Share", command=Share)
	Share_B.config(font=("Times", 20, "bold"), width=20)
	Share_B.configure(background='red')
	Share_B.pack()

	# Button to go to server to set up stream
	Stream_B = tk.Button(window, text="Stream", command=Stream)
	Stream_B.config(font=("Times", 20, "bold"), width=20)
	Stream_B.configure(background='red')
	Stream_B.pack()

	# Button to exit
	Exit_B = tk.Button(window, text="Exit", command=window.destroy)
	Exit_B.config(font=("Times", 20, "bold"), width=20)
	Exit_B.configure(background='red')
	Exit_B.pack()


class Browse():
	def __init__(self):
		clear_page()

		search = tmdb.Search()
		response = search.movie(query='Divergent')

		id_test = search.results[0]['id']
		movie = tmdb.Movies(id_test)
		response1 = movie.info()



		today = arrow.now()
		movie_date = arrow.get(search.results[0]['release_date'])
		delta = today - movie_date



		print ("Title:", search.results[0]['title'])
		print ("Picture:")
		print ("Release date:", search.results[0]['release_date'])
		print ("Description:", search.results[0]['overview'])
		print ("Genre:", movie.genres[0]['name'], movie.genres[1]['name']) #Will need to check for multiple genres
		print ("Age:", delta.days)
		

		columns = ['Title', 'Poster', 'Description', 'Release']
		for c in range(len(columns)):
			tk.Label(text=columns[c], relief=tk.RIDGE, width=30).grid(row=0,column=c)

		title = search.results[0]['title']
		tk.Label(text=title, relief=tk.RIDGE, width=30, height=20).grid(row=1,column=0)

		response = requests.get("http://image.tmdb.org/t/p/w185/" + search.results[0]['poster_path'])
		img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
		tk.Label(window, image = img, width=210, height=300).grid(row=1,column=1)



		description = search.results[0]['overview']
		char_count = 0
		full_des = ""
		word = ""
		word_arr = []
		for x in description:
			if x != " ":
				word += x
			else:
				word_arr.append(word)
				word = ""
		word_arr.append(word)
		word = ""
		for x in word_arr:
			if (len(x)+char_count)<=20:
				full_des += x + " "
				char_count += len(x)
			else:
				full_des += str("\n") + x + " "
				char_count = 0
				# print (str("\n") + x + " ")
				
		tk.Label(text=full_des, relief=tk.RIDGE, width=30, height=20).grid(row=1,column=2, sticky='nw')

		release = search.results[0]['release_date']
		tk.Label(text=release, relief=tk.RIDGE, width=30, height=20).grid(row=1,column=3)

		self.search_box = Entry(window)
		self.search_box.insert(0, 'Search')
		self.search_box.grid(row=2, column=1, sticky=tk.W, pady=4)
		self.search_box.bind("<FocusIn>", self.clear_widget)
		tk.Button(window, text='Search', command=self.search_funtction).grid(row=2, column=1, sticky='e', pady=4)

		# word = self.search_box.get()
		# print (word)

		B = tk.Button(window, text='Play', command=self.Play_movie, bg="blue")
		B.grid(row=2, column=2)
	def clear_widget(self,event):
			if self.search_box == window.focus_get() and self.search_box.get() == 'Search':
					self.search_box.delete(0, tk.END)

	def search_funtction(self):
		print(self.search_box.get())

	def Play_movie(self):
		pygame.init()
		infoObject = pygame.display.Info()
		width, height = infoObject.current_w, infoObject.current_h
		# print (width, height)
		pygame.display.set_caption('Playing Movie')
		clip = VideoFileClip('Divergent.mp4')
		# clip.resize(width, height)
		clip.preview(fullscreen=True)                          #Uses moviePy

		pygame.quit()
		# B.configure(background = "green")


def Update():
	clear_page()
	# Button to go back home
	Exit_B = tk.Button(text="Home", command=Home)
	Exit_B.config(font=("Times", 20, "bold"), width=20)
	Exit_B.configure(background='red')
	Exit_B.pack()

def Share():
	clear_page()

def Stream():
	clear_page()


if __name__ == "__main__":
	window = tk.Tk()
	window.title("Caleb's Secret Netflix")
	window.geometry("1000x500")
	window.configure(background='red3')

	Home()

	window.mainloop()




	























# import tkinter as tk

# root = tk.Tk()
# root.grid_rowconfigure(0, weight=1)
# root.columnconfigure(0, weight=1)

# frame_main = tk.Frame(root, bg="gray")
# frame_main.grid(sticky='news')

# label1 = tk.Label(frame_main, text="Label 1", fg="green")
# label1.grid(row=0, column=0, pady=(5, 0), sticky='nw')

# label2 = tk.Label(frame_main, text="Label 2", fg="blue")
# label2.grid(row=1, column=0, pady=(5, 0), sticky='nw')

# label3 = tk.Label(frame_main, text="Label 3", fg="red")
# label3.grid(row=3, column=0, pady=5, sticky='nw')

# # Create a frame for the canvas with non-zero row&column weights
# frame_canvas = tk.Frame(frame_main)
# frame_canvas.grid(row=2, column=0, pady=(5, 0), sticky='nw')
# frame_canvas.grid_rowconfigure(0, weight=1)
# frame_canvas.grid_columnconfigure(0, weight=1)
# # Set grid_propagate to False to allow 5-by-5 buttons resizing later
# frame_canvas.grid_propagate(False)

# # Add a canvas in that frame
# canvas = tk.Canvas(frame_canvas, bg="yellow")
# canvas.grid(row=0, column=0, sticky="news")

# # Link a scrollbar to the canvas
# vsb = tk.Scrollbar(frame_canvas, orient="vertical", command=canvas.yview)
# vsb.grid(row=0, column=1, sticky='ns')
# canvas.configure(yscrollcommand=vsb.set)

# # Create a frame to contain the buttons
# frame_buttons = tk.Frame(canvas, bg="blue")
# canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

# # Add 9-by-5 buttons to the frame
# rows = 9
# columns = 5
# buttons = [[tk.Button() for j in range(columns)] for i in range(rows)]
# for i in range(0, rows):
# 		for j in range(0, columns):
# 				buttons[i][j] = tk.Button(frame_buttons, text=("%d,%d" % (i+1, j+1)))
# 				buttons[i][j].grid(row=i, column=j, sticky='news')

# # Update buttons frames idle tasks to let tkinter calculate buttons sizes
# frame_buttons.update_idletasks()

# # Resize the canvas frame to show exactly 5-by-5 buttons and the scrollbar
# first5columns_width = sum([buttons[0][j].winfo_width() for j in range(0, 5)])
# first5rows_height = sum([buttons[i][0].winfo_height() for i in range(0, 5)])
# frame_canvas.config(width=first5columns_width + vsb.winfo_width(),
# 										height=first5rows_height)

# # Set the canvas scrolling region
# canvas.config(scrollregion=canvas.bbox("all"))

# # Launch the GUI
# root.mainloop()



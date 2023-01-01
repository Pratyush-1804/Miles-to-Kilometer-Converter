# Create An Desktop Application That converts the miles into kilometers using tkinter
import tkinter

window = tkinter.Tk()
window.title("Miles To Kilometer Converter")
window.minsize(width=400,height=200)
# Creating the label
my_lable = tkinter.Label(text="Converter Application",bg="hotpink",fg="black")
my_lable.place(x = 150,y = 10)


my_lable1 = tkinter.Label(text="0 (KM)",bg="skyblue",fg="black")
my_lable1.place(x = 160,y = 35)

# Creating the input taker that takes the input from the user and help us in converting the miles into kiloimneters
my_input = tkinter.Entry()
my_input.place(x = 150,y = 70)

def change():
      new_input = int(my_input.get())
      my_lable1.config(text=  f" (KM) {new_input*1.60934}")



# Creating the button on which user clicks and converts the miles into kilometers
my_button = tkinter.Button(text="Convert",bg="black",fg="white",command=change)
my_button.place(x=190,y=105)


window.mainloop()
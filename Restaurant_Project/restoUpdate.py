import customtkinter
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from PIL import Image, ImageTk


def create_window():
    app = customtkinter.CTk()
    app.title("Restaurant")
    app.geometry("1200x600")
    app.config(bg="#001eff")
    app.resizable(False, False)
    font1 = ("Arial", 25, "bold")
    font2 = ("Arial", 15, "bold")
    font3 = ("Arial", 12, "bold")
    price_list = [10, 5, 15]
    total_price = 0
    global customer_entry,quantity_combox
    now = datetime.now() 
    date_time = now.strftime("%d/%m/%Y, %H:%M:%S")

    bill_frame = customtkinter.CTkFrame(app, width=800, height=800, fg_color="#ff0000")
    bill_frame.place(x=775, y=0)

    menu_label = customtkinter.CTkLabel(app, text="Restaurant Cafe", font=font1, text_color="#ffffff", bg_color="#001eff")
    menu_label.place(x=305, y=15)

    image1 = Image.open(r"C:\Users\Tunahan\Desktop\workplace\Restaurant_Project\soup.jpg")
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open(r"C:\Users\Tunahan\Desktop\workplace\Restaurant_Project\tea.jpg")
    photo2 = ImageTk.PhotoImage(image2)

    image3 = Image.open(r"C:\Users\Tunahan\Desktop\workplace\Restaurant_Project\cake.jpg")
    photo3 = ImageTk.PhotoImage(image3)

    img1_label = customtkinter.CTkLabel(app, image=photo1, text="SOUP\n Price: 10$", font=font2, text_color="#dce0f5", fg_color="#ff0000", width=0, height=0, corner_radius=20, compound=TOP, anchor=N)
    img1_label.place(x=0, y=100)

    img2_label = customtkinter.CTkLabel(app, image=photo2, text="Tea\n Price: 5$", font=font2, text_color="#dce0f5", fg_color="#ff0000", width=0, height=0, corner_radius=20, compound=TOP, anchor=N)
    img2_label.place(x=300, y=100)

    img3_label = customtkinter.CTkLabel(app, image=photo3, text="Cake\n Price: 15$", font=font2, text_color="#dce0f5", fg_color="#ff0000", width=0, height=0, corner_radius=20, compound=TOP, anchor=N)
    img3_label.place(x=500, y=100)

    quantity_combox=customtkinter.CTkComboBox(app,font=font3,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3","4","5"),state="readonly")
    quantity_combox.place(x=80,y=310)
    quantity_combox.set(0)

    quantity2_combox=customtkinter.CTkComboBox(app,font=font3,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3","4","5"),state="readonly")
    quantity2_combox.place(x=340,y=385)
    quantity2_combox.set(0)

    quantity3_combox=customtkinter.CTkComboBox(app,font=font3,text_color="#000000",fg_color="#FFFFFF",values=("0","1","2","3","4","5"),state="readonly")
    quantity3_combox.place(x=580,y=325)
    quantity3_combox.set(0)

    customer_label=customtkinter.CTkLabel(app,text="Customer Name: ",font=font2,text_color="#000000",fg_color="#ffffff")
    customer_label.place(x=0,y=450)

    customer_entry=customtkinter.CTkEntry(app,font=font2,text_color="#000000",fg_color="#ffffff",border_color="#000000",width=200)
    customer_entry.place(x=130,y=450)

    def pay():
        global total_price

        if(customer_entry.get()==""):
            messagebox.showwarning(title="Error",message="İsminizi girin lutfen!")
        else:
            total_price=int(quantity_combox.get())*price_list[0]+int(quantity2_combox.get())*price_list[1]+int(quantity3_combox.get())*price_list[2]
            if(total_price==0):
                messagebox.showwarning(title="Error",message="Urun secin lutfen!")
            else:
                name_label=customtkinter.CTkLabel(bill_frame,text=f"Customer Name: {customer_entry.get()}",font=font2,bg_color="#00ff66",width=320,anchor=W)
                name_label.place(x=0,y=150)
                price_label=customtkinter.CTkLabel(bill_frame,text=f"Price: {total_price} $",font=font2,bg_color="#00ff66",width=320,anchor=W)
                price_label.place(x=0,y=250)
                date_label=customtkinter.CTkLabel(bill_frame,text=f"Bill Date: {date_time}",font=font2,bg_color="#00ff66",width=320,anchor=W)
                date_label.place(x=0,y=350)      
            
    def new():
        customer_entry.delete(0,END)
        quantity_combox.set(0)
        quantity2_combox.set(0)
        quantity3_combox.set(0)

    def save():
        f=open(f"{customer_entry.get()} Bill","w")
        f.write(f"Customer Name: {customer_entry.get()}\n")
        f.write(f"Total Price: {total_price}$\n")
        f.write(f"Bill Date: {date_time}")
        messagebox.showinfo(title="Saved",message="Fatura kayit altina alindi")
    
    pay_button=customtkinter.CTkButton(app,command=pay,text="Pay Bill",font=font2,fg_color="#18cc33",hover_color="#703fba",cursor="hand2")
    pay_button.place(x=100,y=520)
    save_button=customtkinter.CTkButton(app,command=save,text="Save Bill",font=font2,fg_color="#18cc33",hover_color="#703fba",cursor="hand2")
    save_button.place(x=300,y=520)
    bill_button=customtkinter.CTkButton(app,command=new,text="New Bill",font=font2,fg_color="#18cc33",hover_color="#703fba",cursor="hand2")
    bill_button.place(x=500,y=520)
    app.mainloop()

if __name__ == "__main__":
    create_window()

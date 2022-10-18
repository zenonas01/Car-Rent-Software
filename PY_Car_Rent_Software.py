from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from PIL import Image, ImageTk



# MAIN_TAB
def mainTab():
    global root
    root = Tk()
    root.title("Car Rental System")

    wdt = 700
    hit = 400
    app_wdt = root.winfo_screenwidth()
    app_hit = root.winfo_screenheight()

    x = (app_wdt/2) - (wdt/2)
    y = (app_hit/2) - (hit/2)
    root.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
    root.resizable(0,0)
    root.config(bg="#ffd500")


    def Cars():
        mainTabLabel.destroy()
        CarsButton.destroy()
        CustomersButton.destroy()
        UsersButton.destroy()
        DashboardButton.destroy()
        root.destroy()
        #######################################################

        global root_Car
        root_Car = Tk()
        root_Car.title("Cars Tab")


        wdt = 700
        hit = 400
        app_wdt = root_Car.winfo_screenwidth()
        app_hit = root_Car.winfo_screenheight()

        x = (app_wdt/2) - (wdt/2)
        y = (app_hit/2) - (hit/2)
        root_Car.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
        root_Car.resizable(0,0)
        root_Car.config(bg="#ffd500")



        #Write code HERE

        def Back():
            root_Car.destroy()
            mainTab()
        

        # # # # # # # V A R I A B L E S # # # # # # #
        REGNUM = StringVar()
        BRAND = StringVar()
        MODEL = StringVar()
        BODY = StringVar()
        AVAILABLE = StringVar()
        PRICE = StringVar()

        # # # # # # # M E T H O D S # # # # # # #
        def DB():
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("CREATE TABLE IF NOT EXISTS `car` (car_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, regnum TEXT, brand TEXT, model TEXT, body TEXT, available TEXT, price TEXT)")
            pointer.execute("SELECT * FROM `car` ORDER BY `available` DESC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()

        def SubmitData():
            if  REGNUM.get() == "" or BRAND.get() == "" or MODEL.get() == "" or BODY.get() == "" or AVAILABLE.get() == "" or PRICE.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute(("INSERT INTO `car` (regnum, brand, model, body, available, price) VALUES(?, ?, ?, ?, ?, ?)"), (str(REGNUM.get()), str(BRAND.get()), str(MODEL.get()), str(BODY.get()), str(AVAILABLE.get()), int(PRICE.get())))
                connect.commit()
                pointer.execute("SELECT * FROM `car` ORDER BY `available` DESC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                REGNUM.set("")
                BRAND.set("")
                MODEL.set("")
                BODY.set("")
                AVAILABLE.set("")
                PRICE.set("") 

        def UPdateData():
            if AVAILABLE.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute("UPDATE `car` SET `regnum` = ?, `brand` = ?, `model` =?, `body` = ?,  `available` = ?, `price` = ? WHERE `car_id` = ?", (str(REGNUM.get()), str(BRAND.get()), str(MODEL.get()), str(BODY.get()), str(AVAILABLE.get()), int(PRICE.get()), int(car_id)))
                connect.commit()
                pointer.execute("SELECT * FROM `car` ORDER BY `available` DESC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                REGNUM.set("")
                BRAND.set("")
                MODEL.set("")
                BODY.set("")
                AVAILABLE.set("")
                PRICE.set("")

        def ONSelected(event):
            global car_id, UPdateWindow
            currentItem = tree.focus()
            contents =(tree.item(currentItem))
            selectedItem = contents['values']
            car_id = selectedItem[0]
            REGNUM.set("")
            BRAND.set("")
            MODEL.set("")
            BODY.set("")
            AVAILABLE.set("")
            PRICE.set("")
            REGNUM.set(selectedItem[1])
            BRAND.set(selectedItem[2])
            MODEL.set(selectedItem[3])
            BODY.set(selectedItem[4])
            PRICE.set(selectedItem[6])
            UPdateWindow = Toplevel()
            UPdateWindow.title("Car Rental System")
            UPdateWindow.config(bg="#ffd500")
            
            wdt = 400
            hit = 300
            app_wdt = root_Car.winfo_screenwidth()
            app_hit = root_Car.winfo_screenheight()
            x = ((app_wdt/2) + 450) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            UPdateWindow.resizable(0, 0)
            UPdateWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'NewWindow' in globals():
                NewWindow.destroy()

            # # # # # # # F R A M E S # # # # # # #
            Form_Title = Frame(UPdateWindow)
            Form_Title.pack(side=TOP)
            CarRentForm = Frame(UPdateWindow)
            CarRentForm.pack(side=TOP, pady=10)
            RadioGroup = Frame(CarRentForm)
            Yes = Radiobutton(RadioGroup, text="YES", variable=AVAILABLE, value="YES",  font=('arial', 14)).pack(side=LEFT)
            No = Radiobutton(RadioGroup, text="NO", variable=AVAILABLE, value="NO",  font=('arial', 14)).pack(side=LEFT)
            
            #===================LABELS==============================
            lbl_title = Label(Form_Title, text="Update Car", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_regnum = Label(CarRentForm, text="RegNum", font=('arial', 14), bd=5)
            lbl_regnum.grid(row=0, sticky=W)
            lbl_brand = Label(CarRentForm, text="Brand", font=('arial', 14), bd=5)
            lbl_brand.grid(row=1, sticky=W)
            lbl_model = Label(CarRentForm, text="Model", font=('arial', 14), bd=5)
            lbl_model.grid(row=2, sticky=W)
            lbl_body = Label(CarRentForm, text="Body", font=('arial', 14), bd=5)
            lbl_body.grid(row=3, sticky=W)
            lbl_available = Label(CarRentForm, text="Available", font=('arial', 14), bd=5)
            lbl_available.grid(row=4, sticky=W)
            lbl_price = Label(CarRentForm, text="Price", font=('arial', 14), bd=5)
            lbl_price.grid(row=5, sticky=W)

            #===================ENTRY===============================
            regnum = Entry(CarRentForm, textvariable=REGNUM, font=('arial', 14))
            regnum.grid(row=0, column=1)
            brand = Entry(CarRentForm, textvariable=BRAND, font=('arial', 14))
            brand.grid(row=1, column=1)
            model = Entry(CarRentForm, textvariable=MODEL,  font=('arial', 14))
            model.grid(row=2, column=1)
            body = Entry(CarRentForm, textvariable=BODY,  font=('arial', 14))
            body.grid(row=3, column=1)
            RadioGroup.grid(row=4, column=1)
            price = Entry(CarRentForm, textvariable=PRICE,  font=('arial', 14))
            price.grid(row=5, column=1)
            

            #==================BUTTONS==============================
            btn_updatecar = Button(CarRentForm, text="Update", width=50, bg="#00ff00", command=UPdateData)
            btn_updatecar.grid(row=6, columnspan=2, pady=10)


        def DeleteData():
            if not tree.selection():
                result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
            else:
                result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    currentItem = tree.focus()
                    contents =(tree.item(currentItem))
                    selectedItem = contents['values']
                    tree.delete(currentItem)
                    connect = sqlite3.connect("pythonCarSys.db")
                    pointer = connect.cursor()
                    pointer.execute("DELETE FROM `car` WHERE `car_id` = %d" % selectedItem[0])
                    connect.commit()
                    pointer.close()
                    connect.close()


        def AddNewWindow():
            global NewWindow
            REGNUM.set("")
            BRAND.set("")
            MODEL.set("")
            BODY.set("")
            AVAILABLE.set("")
            PRICE.set("")
            NewWindow = Toplevel()
            NewWindow.title("Car Rental System")
            NewWindow.config(bg="#ffd500")
            wdt = 400
            hit = 300
            screen_wdt = root_Car.winfo_screenwidth()
            screen_hit = root_Car.winfo_screenheight()
            x = ((app_wdt/2) - 455) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            NewWindow.resizable(0, 0)
            NewWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'UpdateWindow' in globals():
                UPdateWindow.destroy()
            

            #===================FRAMES==============================
            global FormTitle
            global CarRentForm
            FormTitle = Frame(NewWindow)
            FormTitle.pack(side=TOP)
            CarRentForm = Frame(NewWindow)
            CarRentForm.pack(side=TOP, pady=10)
            RadioGroup = Frame(CarRentForm)
            Yes = Radiobutton(RadioGroup, text="YES", variable=AVAILABLE, value="YES",  font=('arial', 14)).pack(side=LEFT)
            No = Radiobutton(RadioGroup, text="NO", variable=AVAILABLE, value="NO",  font=('arial', 14)).pack(side=LEFT)
            
            #===================LABELS==============================
            lbl_title = Label(FormTitle, text="Adding New Cars", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_regnum = Label(CarRentForm, text="RegNum", font=('arial', 14), bd=5)
            lbl_regnum.grid(row=0, sticky=W)
            lbl_brand = Label(CarRentForm, text="Brand", font=('arial', 14), bd=5)
            lbl_brand.grid(row=1, sticky=W)
            lbl_model = Label(CarRentForm, text="Model", font=('arial', 14), bd=5)
            lbl_model.grid(row=2, sticky=W)
            lbl_body = Label(CarRentForm, text="Body", font=('arial', 14), bd=5)
            lbl_body.grid(row=3, sticky=W)
            lbl_available = Label(CarRentForm, text="Available", font=('arial', 14), bd=5)
            lbl_available.grid(row=4, sticky=W)
            lbl_price = Label(CarRentForm, text="Price", font=('arial', 14), bd=5)
            lbl_price.grid(row=5, sticky=W)

            #===================ENTRY===============================
            regnum = Entry(CarRentForm, textvariable=REGNUM, font=('arial', 14))
            regnum.grid(row=0, column=1)
            brand = Entry(CarRentForm, textvariable=BRAND, font=('arial', 14))
            brand.grid(row=1, column=1)
            model = Entry(CarRentForm, textvariable=MODEL,  font=('arial', 14))
            model.grid(row=2, column=1)
            body = Entry(CarRentForm, textvariable=BODY,  font=('arial', 14))
            body.grid(row=3, column=1)
            RadioGroup.grid(row=4, column=1)
            price = Entry(CarRentForm, textvariable=PRICE,  font=('arial', 14))
            price.grid(row=5, column=1)
            

            #==================BUTTONS==============================
            btn_addcon = Button(CarRentForm, text="Save", width=50, bg="#00ff00", command=SubmitData)
            btn_addcon.grid(row=6, columnspan=2, pady=10)


        

        #============================FRAMES======================================
        Top = Frame(root_Car, width=500, bd=1, relief=SOLID)
        Top.pack(side=TOP)
        Mid = Frame(root_Car, width=500,  bg="#ffd500")
        Mid.pack(side=TOP)
        MidLeft = Frame(Mid, width=100)
        MidLeft.pack(side=LEFT, pady=10)
        MidLeftPadding = Frame(Mid, width=370, bg="#ffd500")
        MidLeftPadding.pack(side=LEFT)
        MidRight = Frame(Mid, width=100)
        MidRight.pack(side=RIGHT, pady=10)
        TableMargin = Frame(root_Car, width=500)
        TableMargin.pack(side=TOP)
        #============================LABELS======================================
        lbl_title = Label(Top, text="Car Rental System", bg="#ff0000", font=('arial', 16), width=500)
        lbl_title.pack(fill=X)



        #============================ENTRY=======================================
        #============================BACK========================================
        

        #============================BUTTONS=====================================
        btn_add = Button(MidLeft, text="+ ADD NEW", bg="#00ff00", command=AddNewWindow)
        btn_add.pack(side=LEFT)
        BackButton=Button(root_Car, text='BACK', font=('Impact',12), command=Back)
        BackButton.place(x= 325, y= 42)
        btn_delete = Button(MidRight, text="DELETE", bg="#ff0000", command=DeleteData)
        btn_delete.pack(side=RIGHT)


        #============================TABLES======================================
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("MemberID", "RegNum", "Brand", "Model", "Body", "Available", "Price"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('MemberID', text="MemberID", anchor=W)
        tree.heading('RegNum', text="RegNum", anchor=W)
        tree.heading('Brand', text="Brand", anchor=W)
        tree.heading('Model', text="Model", anchor=W)
        tree.heading('Body', text="Body", anchor=W)
        tree.heading('Available', text="Available", anchor=W)
        tree.heading('Price', text="Price", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=80)
        tree.column('#3', stretch=NO, minwidth=0, width=120)
        tree.column('#4', stretch=NO, minwidth=0, width=90)
        tree.column('#5', stretch=NO, minwidth=0, width=80)
        tree.column('#6', stretch=NO, minwidth=0, width=120)
        tree.column('#7', stretch=NO, minwidth=0, width=120)
        tree.pack()
        tree.bind('<Double-Button-1>', ONSelected)

        #============================INITIALIZATION==============================
        if __name__ == '__main__':
            DB()
            








    #################### C A R S   E N D ###################################










    def Customer():
        mainTabLabel.destroy()
        CarsButton.destroy()
        CustomersButton.destroy()
        UsersButton.destroy()
        DashboardButton.destroy()
        root.destroy()
        #######################################################

        root_Customer = Tk()
        root_Customer.title("Customer Tab")

        wdt = 730
        hit = 430
        app_wdt = root_Customer.winfo_screenwidth()
        app_hit = root_Customer.winfo_screenheight()

        x = (app_wdt/2) - (wdt/2)
        y = (app_hit/2) - (hit/2)
        root_Customer.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
        root_Customer.resizable(0,0)
        root_Customer.config(bg="#ffd500")



        #Write code HERE

        def Back():
            root_Customer.destroy()
            mainTab()
        

        # # # # # # # V A R I A B L E S # # # # # # #
        ID_PASS = StringVar()
        FULL_NAME = StringVar()
        DOB = StringVar()
        ADDRESS = StringVar()
        DEPOSIT = StringVar()
        TEL = StringVar()
        R_STEER = StringVar()
        _FROM = StringVar()
        UNTIL = StringVar()

        # # # # # # # M E T H O D S # # # # # # #
        def DB():
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("CREATE TABLE IF NOT EXISTS `customer` (customer_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_pass TEXT, full_name TEXT, dob TEXT, address TEXT, deposit TEXT, tel TEXT, r_steer TEXT, _from TEXT, until TEXT)")
            pointer.execute("SELECT * FROM `customer` ORDER BY `full_name` ASC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()

        def SubmitData():
            if  ID_PASS.get() == "" or FULL_NAME.get() == "" or DOB.get() == "" or ADDRESS.get() == "" or DEPOSIT.get() == "" or TEL.get() == "" or R_STEER.get() == "" or _FROM.get() == "" or UNTIL.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute(("INSERT INTO `customer` (id_pass, full_name, dob, address, deposit, tel, r_steer, _from, until) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)"), (str(ID_PASS.get()), str(FULL_NAME.get()), str(DOB.get()), str(ADDRESS.get()), str(DEPOSIT.get()), str(TEL.get()), str(R_STEER.get()), str(_FROM.get()), str(UNTIL.get())))
                connect.commit()
                pointer.execute("SELECT * FROM `customer` ORDER BY `full_name` ASC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                ID_PASS.set("")
                FULL_NAME.set("")
                DOB.set("")
                ADDRESS.set("")
                DEPOSIT.set("")
                TEL.set("") 
                R_STEER.set("")
                _FROM.set("")
                UNTIL.set("")

        def UPdateData():
            if R_STEER.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute("UPDATE `customer` SET `id_pass` = ?, `full_name` = ?, `dob` =?, `address` = ?,  `deposit` = ?, `tel` = ?, `r_steer` = ?,  `_from` = ?, `until` = ? WHERE `customer_id` = ?", (str(ID_PASS.get()), str(FULL_NAME.get()), str(DOB.get()), str(ADDRESS.get()), str(DEPOSIT.get()), str(TEL.get()), str(R_STEER.get()), str(_FROM.get()), str(UNTIL.get()), int(customer_id)))
                connect.commit()
                pointer.execute("SELECT * FROM `customer` ORDER BY `full_name` ASC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                ID_PASS.set("")
                FULL_NAME.set("")
                DOB.set("")
                ADDRESS.set("")
                DEPOSIT.set("")
                TEL.set("")
                R_STEER.set("")
                _FROM.set("")
                UNTIL.set("")

        def ONSelected(event):
            global customer_id, UPdateWindow
            currentItem = tree.focus()
            contents =(tree.item(currentItem))
            selectedItem = contents['values']
            customer_id = selectedItem[0]
            ID_PASS.set("")
            FULL_NAME.set("")
            DOB.set("")
            ADDRESS.set("")
            DEPOSIT.set("")
            TEL.set("")
            R_STEER.set("")
            _FROM.set("")
            UNTIL.set("")
            ID_PASS.set(selectedItem[1])
            FULL_NAME.set(selectedItem[2])
            DOB.set(selectedItem[3])
            ADDRESS.set(selectedItem[4])
            DEPOSIT.set(selectedItem[5])
            TEL.set(selectedItem[6])
            _FROM.set(selectedItem[8])
            UNTIL.set(selectedItem[9])
            UPdateWindow = Toplevel()
            UPdateWindow.title("Car Rental System")
            UPdateWindow.config(bg="#ffd500")
            
            wdt = 400
            hit = 400
            app_wdt = root_Customer.winfo_screenwidth()
            app_hit = root_Customer.winfo_screenheight()
            x = ((app_wdt/2) + 450) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            UPdateWindow.resizable(0, 0)
            UPdateWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'NewWindow' in globals():
                NewWindow.destroy()

            # # # # # # # F R A M E S # # # # # # #
            Form_Title = Frame(UPdateWindow)
            Form_Title.pack(side=TOP)
            CarRentForm = Frame(UPdateWindow)
            CarRentForm.pack(side=TOP, pady=10)
            RadioGroup = Frame(CarRentForm)
            Yes = Radiobutton(RadioGroup, text="YES", variable=R_STEER, value="YES",  font=('arial', 14)).pack(side=LEFT)
            No = Radiobutton(RadioGroup, text="NO", variable=R_STEER, value="NO",  font=('arial', 14)).pack(side=LEFT)
            
            #===================LABELS==============================
            lbl_title = Label(Form_Title, text="Update Customer", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_id_pass = Label(CarRentForm, text="Id_Pass", font=('arial', 14), bd=5)
            lbl_id_pass.grid(row=0, sticky=W)
            lbl_full_name = Label(CarRentForm, text="Full_Name", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=1, sticky=W)
            lbl_dob = Label(CarRentForm, text="DOB", font=('arial', 14), bd=5)
            lbl_dob.grid(row=2, sticky=W)
            lbl_address = Label(CarRentForm, text="Address", font=('arial', 14), bd=5)
            lbl_address.grid(row=3, sticky=W)
            lbl_deposit = Label(CarRentForm, text="Deposit", font=('arial', 14), bd=5)
            lbl_deposit.grid(row=4, sticky=W)
            lbl_tel = Label(CarRentForm, text="TEL", font=('arial', 14), bd=5)
            lbl_tel.grid(row=5, sticky=W)
            lbl_r_steer = Label(CarRentForm, text="R_Steer", font=('arial', 14), bd=5)
            lbl_r_steer.grid(row=6, sticky=W)
            lbl_from = Label(CarRentForm, text="From", font=('arial', 14), bd=5)
            lbl_from.grid(row=7, sticky=W)
            lbl_until = Label(CarRentForm, text="Until", font=('arial', 14), bd=5)
            lbl_until.grid(row=8, sticky=W)

            #===================ENTRY===============================
            id_pass = Entry(CarRentForm, textvariable=ID_PASS, font=('arial', 14))
            id_pass.grid(row=0, column=1)
            full_name = Entry(CarRentForm, textvariable=FULL_NAME, font=('arial', 14))
            full_name.grid(row=1, column=1)
            dob = Entry(CarRentForm, textvariable=DOB,  font=('arial', 14))
            dob.grid(row=2, column=1)
            address = Entry(CarRentForm, textvariable=ADDRESS,  font=('arial', 14))
            address.grid(row=3, column=1)
            deposit = Entry(CarRentForm, textvariable=DEPOSIT,  font=('arial', 14))
            deposit.grid(row=4, column=1)
            tel = Entry(CarRentForm, textvariable=TEL,  font=('arial', 14))
            tel.grid(row=5, column=1)
            RadioGroup.grid(row=6, column=1)
            _from = Entry(CarRentForm, textvariable=_FROM,  font=('arial', 14))
            _from.grid(row=7, column=1)
            until = Entry(CarRentForm, textvariable=UNTIL,  font=('arial', 14))
            until.grid(row=8, column=1)
            

            #==================BUTTONS==============================
            btn_updatecustomer = Button(CarRentForm, text="Update", width=50, bg="#00ff00", command=UPdateData)
            btn_updatecustomer.grid(row=9, columnspan=2, pady=10)


        def DeleteData():
            if not tree.selection():
                result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
            else:
                result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    currentItem = tree.focus()
                    contents =(tree.item(currentItem))
                    selectedItem = contents['values']
                    tree.delete(currentItem)
                    connect = sqlite3.connect("pythonCarSys.db")
                    pointer = connect.cursor()
                    pointer.execute("DELETE FROM `customer` WHERE `customer_id` = %d" % selectedItem[0])
                    connect.commit()
                    pointer.close()
                    connect.close()


        def AddNewWindow():
            global NewWindow
            ID_PASS.set("")
            FULL_NAME.set("")
            DOB.set("")
            ADDRESS.set("")
            DEPOSIT.set("")
            TEL.set("")
            R_STEER.set("")
            _FROM.set("")
            UNTIL.set("")
            NewWindow = Toplevel()
            NewWindow.title("Car Rental System")
            NewWindow.config(bg="#ffd500")
            wdt = 400
            hit = 400
            screen_wdt = root_Customer.winfo_screenwidth()
            screen_hit = root_Customer.winfo_screenheight()
            x = ((app_wdt/2) - 455) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            NewWindow.resizable(0, 0)
            NewWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'UpdateWindow' in globals():
                UPdateWindow.destroy()
            

            #===================FRAMES==============================
            global FormTitle
            global CarRentForm
            FormTitle = Frame(NewWindow)
            FormTitle.pack(side=TOP)
            CarRentForm = Frame(NewWindow)
            CarRentForm.pack(side=TOP, pady=10)
            RadioGroup = Frame(CarRentForm)
            Yes = Radiobutton(RadioGroup, text="YES", variable=R_STEER, value="YES",  font=('arial', 14)).pack(side=LEFT)
            No = Radiobutton(RadioGroup, text="NO", variable=R_STEER, value="NO",  font=('arial', 14)).pack(side=LEFT)
            
            #===================LABELS==============================
            lbl_title = Label(FormTitle, text="Adding New Customers", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_id_pass = Label(CarRentForm, text="Id_Pass", font=('arial', 14), bd=5)
            lbl_id_pass.grid(row=0, sticky=W)
            lbl_full_name = Label(CarRentForm, text="Full_Name", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=1, sticky=W)
            lbl_dob = Label(CarRentForm, text="DOB", font=('arial', 14), bd=5)
            lbl_dob.grid(row=2, sticky=W)
            lbl_address = Label(CarRentForm, text="Address", font=('arial', 14), bd=5)
            lbl_address.grid(row=3, sticky=W)
            lbl_deposit = Label(CarRentForm, text="Deposit", font=('arial', 14), bd=5)
            lbl_deposit.grid(row=4, sticky=W)
            lbl_tel = Label(CarRentForm, text="TEL", font=('arial', 14), bd=5)
            lbl_tel.grid(row=5, sticky=W)
            lbl_r_steer = Label(CarRentForm, text="R_Steer", font=('arial', 14), bd=5)
            lbl_r_steer.grid(row=6, sticky=W)
            lbl_from = Label(CarRentForm, text="From", font=('arial', 14), bd=5)
            lbl_from.grid(row=7, sticky=W)
            lbl_until = Label(CarRentForm, text="Until", font=('arial', 14), bd=5)
            lbl_until.grid(row=8, sticky=W)

            #===================ENTRY===============================
            id_pass = Entry(CarRentForm, textvariable=ID_PASS, font=('arial', 14))
            id_pass.grid(row=0, column=1)
            full_name = Entry(CarRentForm, textvariable=FULL_NAME, font=('arial', 14))
            full_name.grid(row=1, column=1)
            dob = Entry(CarRentForm, textvariable=DOB,  font=('arial', 14))
            dob.grid(row=2, column=1)
            address = Entry(CarRentForm, textvariable=ADDRESS,  font=('arial', 14))
            address.grid(row=3, column=1)
            deposit = Entry(CarRentForm, textvariable=DEPOSIT,  font=('arial', 14))
            deposit.grid(row=4, column=1)
            tel = Entry(CarRentForm, textvariable=TEL, font=('arial', 14))
            tel.grid(row=5, column=1)
            RadioGroup.grid(row=6, column=1)
            _from = Entry(CarRentForm, textvariable=_FROM,  font=('arial', 14))
            _from.grid(row=7, column=1)
            until = Entry(CarRentForm, textvariable=UNTIL,  font=('arial', 14))
            until.grid(row=8, column=1)
        
            

            #==================BUTTONS==============================
            btn_addcust = Button(CarRentForm, text="Save", width=50, bg="#00ff00", command=SubmitData)
            btn_addcust.grid(row=9, columnspan=2, pady=10)


        

        #============================FRAMES======================================
        Top = Frame(root_Customer, width=500, bd=1, relief=SOLID)
        Top.pack(side=TOP)
        Mid = Frame(root_Customer, width=500,  bg="#ffd500")
        Mid.pack(side=TOP)
        MidLeft = Frame(Mid, width=100)
        MidLeft.pack(side=LEFT, pady=10)
        MidLeftPadding = Frame(Mid, width=370, bg="#ffd500")
        MidLeftPadding.pack(side=LEFT)
        MidRight = Frame(Mid, width=100)
        MidRight.pack(side=RIGHT, pady=10)
        TableMargin = Frame(root_Customer, width=500)
        TableMargin.pack(side=TOP)
        #============================LABELS======================================
        lbl_title = Label(Top, text="Car Rental System", bg="#ff0000", font=('arial', 16), width=500)
        lbl_title.pack(fill=X)



        #============================ENTRY=======================================
        #============================BACK========================================
        

        #============================BUTTONS=====================================
        btn_add = Button(MidLeft, text="+ ADD NEW", bg="#00ff00", command=AddNewWindow)
        btn_add.pack(side=LEFT)
        BackButton=Button(root_Customer, text='BACK', font=('Impact',12), command=Back)
        BackButton.place(x= 325, y= 42)
        btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
        btn_delete.pack(side=RIGHT)


        #============================TABLES======================================
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("MemberID", "Id_Pass", "Full_Name", "DOB", "Address", "Deposit", "TEL", "R_Steer", "From", "Until"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('MemberID', text="MemberID", anchor=W)
        tree.heading('Id_Pass', text="Id_Pass", anchor=W)
        tree.heading('Full_Name', text="Full_Name", anchor=W)
        tree.heading('DOB', text="DOB", anchor=W)
        tree.heading('Address', text="Address", anchor=W)
        tree.heading('Deposit', text="Deposit", anchor=W)
        tree.heading('TEL', text="TEL", anchor=W)
        tree.heading('R_Steer', text="R_Steer", anchor=W)
        tree.heading('From', text="From", anchor=W)
        tree.heading('Until', text="Until", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=80)
        tree.column('#3', stretch=NO, minwidth=0, width=80)
        tree.column('#4', stretch=NO, minwidth=0, width=80)
        tree.column('#5', stretch=NO, minwidth=0, width=80)
        tree.column('#6', stretch=NO, minwidth=0, width=80)
        tree.column('#7', stretch=NO, minwidth=0, width=80)
        tree.column('#8', stretch=NO, minwidth=0, width=50)
        tree.column('#9', stretch=NO, minwidth=0, width=80)
        tree.column('#10', stretch=NO, minwidth=0, width=80)
        tree.pack()
        tree.bind('<Double-Button-1>', ONSelected)

        #============================INITIALIZATION==============================
        if __name__ == '__main__':
            DB()
            


    #################### C U S T O M E R    E N D ###################################





    def Users():
        mainTabLabel.destroy()
        CarsButton.destroy()
        CustomersButton.destroy()
        UsersButton.destroy()
        DashboardButton.destroy()
        root.destroy()
        #######################################################

        root_Users = Tk()
        root_Users.title("Users Tab")

        wdt = 700
        hit = 400
        app_wdt = root_Users.winfo_screenwidth()
        app_hit = root_Users.winfo_screenheight()

        x = (app_wdt/2) - (wdt/2)
        y = (app_hit/2) - (hit/2)
        root_Users.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
        root_Users.resizable(0,0)
        root_Users.config(bg="#ffd500")



        #Write code HERE

        def Back():
            root_Users.destroy()
            mainTab()
        

        # # # # # # # V A R I A B L E S # # # # # # #
        FULL_NAME = StringVar()
        USER_NAME = StringVar()
        PASSWD = StringVar()
        TEL = StringVar()

        # # # # # # # M E T H O D S # # # # # # #
        def DB():
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("CREATE TABLE IF NOT EXISTS `users` (users_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, full_name TEXT, user_name TEXT, passwd TEXT, tel TEXT)")
            pointer.execute("SELECT * FROM `users` ORDER BY `full_name` ASC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()

        def SubmitData():
            if  FULL_NAME.get() == "" or USER_NAME.get() == "" or PASSWD.get() == "" or TEL.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute(("INSERT INTO `users` (full_name, user_name, passwd, tel) VALUES(?, ?, ?, ?)"), (str(FULL_NAME.get()), str(USER_NAME.get()), str(PASSWD.get()), str(TEL.get())))
                connect.commit()
                pointer.execute("SELECT * FROM `users` ORDER BY `full_name` ASC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                FULL_NAME.set("")
                USER_NAME.set("")
                PASSWD.set("")
                TEL.set("")

        def UPdateData():
            tree.delete(*tree.get_children())
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("UPDATE `users` SET `full_name` = ?, `user_name` =?, `passwd` = ?, `tel` = ? WHERE `users_id` = ?", (str(FULL_NAME.get()), str(USER_NAME.get()), str(PASSWD.get()), str(TEL.get()), int(users_id)))
            connect.commit()
            pointer.execute("SELECT * FROM `users` ORDER BY `full_name` ASC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()
            FULL_NAME.set("")
            USER_NAME.set("")
            PASSWD.set("")
            TEL.set("")

        def ONSelected(event):
            global users_id, UPdateWindow
            currentItem = tree.focus()
            contents =(tree.item(currentItem))
            selectedItem = contents['values']
            users_id = selectedItem[0]
            FULL_NAME.set("")
            USER_NAME.set("")
            PASSWD.set("")
            TEL.set("")
            FULL_NAME.set(selectedItem[1])
            USER_NAME.set(selectedItem[2])
            PASSWD.set(selectedItem[3])
            TEL.set(selectedItem[4])
            UPdateWindow = Toplevel()
            UPdateWindow.title("Car Rental System")
            UPdateWindow.config(bg="#ffd500")
            
            wdt = 400
            hit = 225
            app_wdt = root_Users.winfo_screenwidth()
            app_hit = root_Users.winfo_screenheight()
            x = ((app_wdt/2) + 450) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            UPdateWindow.resizable(0, 0)
            UPdateWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'NewWindow' in globals():
                NewWindow.destroy()

            # # # # # # # F R A M E S # # # # # # #
            Form_Title = Frame(UPdateWindow)
            Form_Title.pack(side=TOP)
            CarRentForm = Frame(UPdateWindow)
            CarRentForm.pack(side=TOP, pady=10)
            
            #===================LABELS==============================
            lbl_title = Label(Form_Title, text="Update User", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_full_name = Label(CarRentForm, text="Full_Name", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=0, sticky=W)
            lbl_user_name = Label(CarRentForm, text="User_Name", font=('arial', 14), bd=5)
            lbl_user_name.grid(row=1, sticky=W)
            lbl_passwd = Label(CarRentForm, text="Password", font=('arial', 14), bd=5)
            lbl_passwd.grid(row=2, sticky=W)
            lbl_tel = Label(CarRentForm, text="Telephone", font=('arial', 14), bd=5)
            lbl_tel.grid(row=3, sticky=W)

            #===================ENTRY===============================
            full_name = Entry(CarRentForm, textvariable=FULL_NAME, font=('arial', 14))
            full_name.grid(row=0, column=1)
            user_name = Entry(CarRentForm, textvariable=USER_NAME, font=('arial', 14))
            user_name.grid(row=1, column=1)
            passwd = Entry(CarRentForm, textvariable=PASSWD,  font=('arial', 14))
            passwd.grid(row=2, column=1)
            tel = Entry(CarRentForm, textvariable=TEL,  font=('arial', 14))
            tel.grid(row=3, column=1)
            

            #==================BUTTONS==============================
            btn_updateUser = Button(CarRentForm, text="Update", width=50, bg="#00ff00", command=UPdateData)
            btn_updateUser.grid(row=4, columnspan=2, pady=10)


        def DeleteData():
            if not tree.selection():
                result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
            else:
                result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    currentItem = tree.focus()
                    contents =(tree.item(currentItem))
                    selectedItem = contents['values']
                    tree.delete(currentItem)
                    connect = sqlite3.connect("pythonCarSys.db")
                    pointer = connect.cursor()
                    pointer.execute("DELETE FROM `users` WHERE `users_id` = %d" % selectedItem[0])
                    connect.commit()
                    pointer.close()
                    connect.close()


        def AddNewWindow():
            global NewWindow
            FULL_NAME.set("")
            USER_NAME.set("")
            PASSWD.set("")
            TEL.set("")
            NewWindow = Toplevel()
            NewWindow.title("Car Rental System")
            NewWindow.config(bg="#ffd500")
            wdt = 400
            hit = 225
            screen_wdt = root_Users.winfo_screenwidth()
            screen_hit = root_Users.winfo_screenheight()
            x = ((app_wdt/2) - 455) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            NewWindow.resizable(0, 0)
            NewWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'UpdateWindow' in globals():
                UPdateWindow.destroy()
            

            #===================FRAMES==============================
            global FormTitle
            global CarRentForm
            FormTitle = Frame(NewWindow)
            FormTitle.pack(side=TOP)
            CarRentForm = Frame(NewWindow)
            CarRentForm.pack(side=TOP, pady=10)
            
            #===================LABELS==============================
            lbl_title = Label(FormTitle, text="Adding New User", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_full_name = Label(CarRentForm, text="Full_Name", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=0, sticky=W)
            lbl_user_name = Label(CarRentForm, text="User_Name", font=('arial', 14), bd=5)
            lbl_user_name.grid(row=1, sticky=W)
            lbl_passwd = Label(CarRentForm, text="Password", font=('arial', 14), bd=5)
            lbl_passwd.grid(row=2, sticky=W)
            lbl_tel = Label(CarRentForm, text="Telephone", font=('arial', 14), bd=5)
            lbl_tel.grid(row=3, sticky=W)

            #===================ENTRY===============================
            full_name = Entry(CarRentForm, textvariable=FULL_NAME, font=('arial', 14))
            full_name.grid(row=0, column=1)
            user_name = Entry(CarRentForm, textvariable=USER_NAME, font=('arial', 14))
            user_name.grid(row=1, column=1)
            passwd = Entry(CarRentForm, textvariable=PASSWD,  font=('arial', 14))
            passwd.grid(row=2, column=1)
            tel = Entry(CarRentForm, textvariable=TEL,  font=('arial', 14))
            tel.grid(row=3, column=1)
        
            

            #==================BUTTONS==============================
            btn_adduser = Button(CarRentForm, text="Save", width=50, bg="#00ff00", command=SubmitData)
            btn_adduser.grid(row=4, columnspan=2, pady=10)


        

        #============================FRAMES======================================
        Top = Frame(root_Users, width=500, bd=1, relief=SOLID)
        Top.pack(side=TOP)
        Mid = Frame(root_Users, width=500,  bg="#ffd500")
        Mid.pack(side=TOP)
        MidLeft = Frame(Mid, width=100)
        MidLeft.pack(side=LEFT, pady=10)
        MidLeftPadding = Frame(Mid, width=370, bg="#ffd500")
        MidLeftPadding.pack(side=LEFT)
        MidRight = Frame(Mid, width=100)
        MidRight.pack(side=RIGHT, pady=10)
        TableMargin = Frame(root_Users, width=500)
        TableMargin.pack(side=TOP)
        #============================LABELS======================================
        lbl_title = Label(Top, text="Car Rental System", bg="#ff0000", font=('arial', 16), width=500)
        lbl_title.pack(fill=X)



        #============================ENTRY=======================================
        #============================BACK========================================
        

        #============================BUTTONS=====================================
        btn_add = Button(MidLeft, text="+ ADD NEW", bg="#00ff00", command=AddNewWindow)
        btn_add.pack(side=LEFT)
        BackButton=Button(root_Users, text='BACK', font=('Impact',12), command=Back)
        BackButton.place(x= 325, y= 42)
        btn_delete = Button(MidRight, text="DELETE", bg="#ff0000", command=DeleteData)
        btn_delete.pack(side=RIGHT)


        #============================TABLES======================================
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("MemberID", "Full_Name", "User_Name", "Passwd", "TEL"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('MemberID', text="MemberID", anchor=W)
        tree.heading('Full_Name', text="Full_Name", anchor=W)
        tree.heading('User_Name', text="User_Name", anchor=W)
        tree.heading('Passwd', text="Passwd", anchor=W)
        tree.heading('TEL', text="TEL", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=150)
        tree.column('#3', stretch=NO, minwidth=0, width=150)
        tree.column('#4', stretch=NO, minwidth=0, width=150)
        tree.column('#5', stretch=NO, minwidth=0, width=150)
        tree.pack()
        tree.bind('<Double-Button-1>', ONSelected)

        #============================INITIALIZATION==============================
        if __name__ == '__main__':
            DB()



    ################################## U S E R S   E N D  #################################






    ############################# D A S H B O A R D ########################################






    def Dashboard():
        mainTabLabel.destroy()
        CarsButton.destroy()
        CustomersButton.destroy()
        UsersButton.destroy()
        DashboardButton.destroy()
        root.destroy()
        #######################################################

        root_Dash = Tk()
        root_Dash.title("Users Tab")


        wdt = 700
        hit = 400
        app_wdt = root_Dash.winfo_screenwidth()
        app_hit = root_Dash.winfo_screenheight()

        x = (app_wdt/2) - (wdt/2)
        y = (app_hit/2) - (hit/2)
        root_Dash.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
        root_Dash.resizable(0,0)
        root_Dash.config(bg="#ffd500")



        #Write code HERE

        def Back():
            root_Dash.destroy()
            mainTab()
        

        # # # # # # # V A R I A B L E S # # # # # # #
        NOTE = StringVar()
        DATE = StringVar()

        # # # # # # # M E T H O D S # # # # # # #
        def DB():
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("CREATE TABLE IF NOT EXISTS `dash` (dash_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, note TEXT, date TEXT)")
            pointer.execute("SELECT * FROM `dash` ORDER BY `date` ASC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()

        def SubmitData():
            if  NOTE.get() == "" or DATE.get() == "":
                result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
            else:
                tree.delete(*tree.get_children())
                connect = sqlite3.connect("pythonCarSys.db")
                pointer = connect.cursor()
                pointer.execute(("INSERT INTO `dash` (note, date) VALUES(?, ?)"), (str(NOTE.get()), str(DATE.get())))
                connect.commit()
                pointer.execute("SELECT * FROM `dash` ORDER BY `date` ASC")
                fetch = pointer.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data))
                pointer.close()
                connect.close()
                NOTE.set("")
                DATE.set("")

        def UPdateData():
            tree.delete(*tree.get_children())
            connect = sqlite3.connect("pythonCarSys.db")
            pointer = connect.cursor()
            pointer.execute("UPDATE `dash` SET `note` = ?, `date` =? WHERE `dash_id` = ?", (str(NOTE.get()), str(DATE.get()), int(dash_id)))
            connect.commit()
            pointer.execute("SELECT * FROM `dash` ORDER BY `date` ASC")
            fetch = pointer.fetchall()
            for data in fetch:
                tree.insert('', 'end', values=(data))
            pointer.close()
            connect.close()
            NOTE.set("")
            DATE.set("")
            

        def ONSelected(event):
            global dash_id, UPdateWindow
            currentItem = tree.focus()
            contents =(tree.item(currentItem))
            selectedItem = contents['values']
            dash_id = selectedItem[0]
            NOTE.set("")
            DATE.set("")
            NOTE.set(selectedItem[1])
            DATE.set(selectedItem[2])
            UPdateWindow = Toplevel()
            UPdateWindow.title("Car Rental System")
            UPdateWindow.config(bg="#ffd500")
            
            wdt = 400
            hit = 180
            app_wdt = root_Dash.winfo_screenwidth()
            app_hit = root_Dash.winfo_screenheight()
            x = ((app_wdt/2) + 450) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            UPdateWindow.resizable(0, 0)
            UPdateWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'NewWindow' in globals():
                NewWindow.destroy()

            # # # # # # # F R A M E S # # # # # # #
            Form_Title = Frame(UPdateWindow)
            Form_Title.pack(side=TOP)
            CarRentForm = Frame(UPdateWindow)
            CarRentForm.pack(side=TOP, pady=10)
            
            #===================LABELS==============================
            lbl_title = Label(Form_Title, text="Update Dashboard", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_full_name = Label(CarRentForm, text="Note", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=0, sticky=W)
            lbl_user_name = Label(CarRentForm, text="Date", font=('arial', 14), bd=5)
            lbl_user_name.grid(row=1, sticky=W)

            #===================ENTRY===============================
            full_name = Entry(CarRentForm, textvariable=NOTE, font=('arial', 14))
            full_name.grid(row=0, column=1)
            user_name = Entry(CarRentForm, textvariable=DATE, font=('arial', 14))
            user_name.grid(row=1, column=1)
            

            #==================BUTTONS==============================
            btn_updateUser = Button(CarRentForm, text="Update", width=50, bg="#00ff00", command=UPdateData)
            btn_updateUser.grid(row=3, columnspan=2, pady=10)


        def DeleteData():
            if not tree.selection():
                result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
            else:
                result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
                if result == 'yes':
                    currentItem = tree.focus()
                    contents =(tree.item(currentItem))
                    selectedItem = contents['values']
                    tree.delete(currentItem)
                    connect = sqlite3.connect("pythonCarSys.db")
                    pointer = connect.cursor()
                    pointer.execute("DELETE FROM `dash` WHERE `dash_id` = %d" % selectedItem[0])
                    connect.commit()
                    pointer.close()
                    connect.close()


        def AddNewWindow():
            global NewWindow
            NOTE.set("")
            DATE.set("")
            NewWindow = Toplevel()
            NewWindow.title("Car Rental System")
            NewWindow.config(bg="#ffd500")
            wdt = 400
            hit = 180
            screen_wdt = root_Dash.winfo_screenwidth()
            screen_hit = root_Dash.winfo_screenheight()
            x = ((app_wdt/2) - 455) - (wdt/2)
            y = ((app_hit/2) + 20) - (hit/2)
            NewWindow.resizable(0, 0)
            NewWindow.geometry("%dx%d+%d+%d" % (wdt, hit, x, y))
            if 'UpdateWindow' in globals():
                UPdateWindow.destroy()
            

            #===================FRAMES==============================
            global FormTitle
            global CarRentForm
            FormTitle = Frame(NewWindow)
            FormTitle.pack(side=TOP)
            CarRentForm = Frame(NewWindow)
            CarRentForm.pack(side=TOP, pady=10)
            
            #===================LABELS==============================
            lbl_title = Label(FormTitle, text="Adding New Note", font=('arial', 16), bg="#ff0000",  width = 300)
            lbl_title.pack(fill=X)
            lbl_full_name = Label(CarRentForm, text="Note", font=('arial', 14), bd=5)
            lbl_full_name.grid(row=0, sticky=W)
            lbl_user_name = Label(CarRentForm, text="Date", font=('arial', 14), bd=5)
            lbl_user_name.grid(row=1, sticky=W)

            #===================ENTRY===============================
            full_name = Entry(CarRentForm, textvariable=NOTE, font=('arial', 14))
            full_name.grid(row=0, column=1)
            user_name = Entry(CarRentForm, textvariable=DATE, font=('arial', 14))
            user_name.grid(row=1, column=1)
        
            

            #==================BUTTONS==============================
            btn_adduser = Button(CarRentForm, text="Save", width=50, bg="#00ff00", command=SubmitData)
            btn_adduser.grid(row=2, columnspan=2, pady=10)


        

        #============================FRAMES======================================
        Top = Frame(root_Dash, width=500, bd=1, relief=SOLID)
        Top.pack(side=TOP)
        Mid = Frame(root_Dash, width=500,  bg="#ffd500")
        Mid.pack(side=TOP)
        MidLeft = Frame(Mid, width=100)
        MidLeft.pack(side=LEFT, pady=10)
        MidLeftPadding = Frame(Mid, width=370, bg="#ffd500")
        MidLeftPadding.pack(side=LEFT)
        MidRight = Frame(Mid, width=100)
        MidRight.pack(side=RIGHT, pady=10)
        TableMargin = Frame(root_Dash, width=500)
        TableMargin.pack(side=TOP)
        #============================LABELS======================================
        lbl_title = Label(Top, text="Car Rental System", bg="#ff0000", font=('arial', 16), width=500)
        lbl_title.pack(fill=X)



        #============================ENTRY=======================================
        #============================BACK========================================
        

        #============================BUTTONS=====================================
        btn_add = Button(MidLeft, text="+ ADD NEW", bg="#00ff00", command=AddNewWindow)
        btn_add.pack(side=LEFT)
        BackButton=Button(root_Dash, text='BACK', font=('Impact',12), command=Back)
        BackButton.place(x= 325, y= 42)
        btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
        btn_delete.pack(side=RIGHT)


        #============================TABLES======================================
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        tree = ttk.Treeview(TableMargin, columns=("MemberID", "Note", "Date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        scrollbary.config(command=tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        tree.heading('MemberID', text="MemberID", anchor=W)
        tree.heading('Note', text="Note", anchor=W)
        tree.heading('Date', text="Date", anchor=W)
        tree.column('#0', stretch=NO, minwidth=0, width=0)
        tree.column('#1', stretch=NO, minwidth=0, width=0)
        tree.column('#2', stretch=NO, minwidth=0, width=450)
        tree.column('#3', stretch=NO, minwidth=0, width=110)
        tree.pack()
        tree.bind('<Double-Button-1>', ONSelected)

        #============================INITIALIZATION==============================
        if __name__ == '__main__':
            DB()


    ####################### D A S H B O A R D   E N D S ######################################


    mainTabLabel=Label(root, text='WELCOME TO CAR RENTAL SYSTEM', font=('Impact',25), bg="#ff0000")
    mainTabLabel.pack()
    CarsButton=Button(root, text='       CARS       ', font=('Impact',20), bg="#fa2020", command=Cars)
    CarsButton.place(x= 45, y=80)
    CustomersButton=Button(root, text=' CUSTOMER  ', font=('Impact',20), bg="#fa2020", command=Customer)
    CustomersButton.place(x= 45, y=160)
    UsersButton=Button(root, text='     USERS       ', font=('Impact',20), bg="#fa2020", command=Users)
    UsersButton.place(x= 45, y=240)
    DashboardButton=Button(root, text='DASHBOARD', font=('Impact',20), bg="#fa2020", command=Dashboard)
    DashboardButton.place(x= 45, y=320)


    load = Image.open("Auto.png")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render, borderwidth=0)
    img.image = render
    img.place(x=250, y=70)   

    


mainTab()

root.mainloop()

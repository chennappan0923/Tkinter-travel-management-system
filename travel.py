from tkinter import*
from tkinter import ttk
import random
import time;
import datetime
from tkinter import messagebox
import pymysql

class Travel:

    def __init__(self,root):

        self.root = root
        self.root.title("Travel management system")
        self.root.geometry("1350x750+0+0")
        self.root.configure(bg="black")

        Dateoforder=StringVar()
        Dateoforder.set(time.strftime("%d/%m/%Y"))
        Receipt_Ref=StringVar()
        PaidTax=StringVar()
        subTotal=StringVar()
        TotalCost=StringVar()

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=StringVar()
        var12=StringVar()
        var13=StringVar()

        Firstname=StringVar()
        Surname=StringVar()
        Address=StringVar()
        PostalCode=StringVar()
        Telephone=StringVar()
        Mobile=StringVar()
        Email=StringVar()

        Airport_Tax=StringVar()
        Mile=StringVar()
        Travel_Ins=StringVar()
        Luggage=StringVar()

        Standard=StringVar()
        Economy=StringVar()
        FirstClass=StringVar()


        Airport_Tax.set("0")
        Mile.set("0")
        Travel_Ins.set("0")
        Luggage.set("0")

        Standard.set("0")
        Economy.set("0")
        FirstClass.set("0")
    #=================================== Define Function=========================================
        def iExit():
            iExit=messagebox.askyesno('Travel management System','confirm if you wnat to exit?')
            if iExit > 0:
                root.destroy()
                return
        def Reset():
            Airport_Tax.set("0")
            Mile.set("0")
            Travel_Ins.set("0")
            Luggage.set("0")

            Standard.set("0")
            Economy.set("0")
            FirstClass.set("0")

            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostalCode.set("")
            Telephone.set("")
            Mobile.set("")
            Email.set("")

            PaidTax.set("")
            subTotal.set("")
            TotalCost.set("")
            self.txtReceipt.delete("1.0",END)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set("0")
            var12.set("0")
            var13.set("0")

            self.cboDeparture.current(0)
            self.cboDestination.current(0)
            self.cboAccommodation.current(0)

            self.txtAirportTax.configure(state=DISABLED)
            self.txtchkMile.configure(state=DISABLED)
            self.txttravelling_insurance.configure(state=DISABLED)
            self.txtluggage.configure(state=DISABLED)

            self.txtStandard.configure(state=DISABLED)
            self.txtEconomy.configure(state=DISABLED)
            self.txtfirstclass.configure(state=DISABLED)
        

        def Receipt():
            self.txtReceipt.delete("1.0",END)
            x=random.randint(10853,500831)
            randomRef= str(x)
            Receipt_Ref.set("Travel Bill: " + randomRef)

            self.txtReceipt.insert(END,"Rceipt Ref:\t\t\t\t " + Receipt_Ref.get() + "\n")
            self.txtReceipt.insert(END,"Date :\t\t\t\t " + Dateoforder.get() + "\n")
            self.txtReceipt.insert(END,"Flight:\t\t\t\t " + "Travelling Details \n")
            self.txtReceipt.insert(END,"Firstname:\t\t\t\t " + Firstname.get() + "\n")
            self.txtReceipt.insert(END,"Surname :\t\t\t\t " + Surname.get() + "\n")
            self.txtReceipt.insert(END,"Address :\t\t\t\t " + Address.get() + "\n")
            self.txtReceipt.insert(END,"PostalCode:\t\t\t\t " + PostalCode.get() + "\n")
            self.txtReceipt.insert(END,"Telephone :\t\t\t\t " + Telephone.get() + "\n")
            
            self.txtReceipt.insert(END,"Email:\t\t\t\t " + Email.get() + "\n")
            self.txtReceipt.insert(END,"Mobile :\t\t\t\t " + Mobile.get() + "\n")
            self.txtReceipt.insert(END,"Address :\t\t\t\t " + Address.get() + "\n")
            self.txtReceipt.insert(END,"Standard:\t\t\t\t " + Standard.get() + "\n")
            self.txtReceipt.insert(END,"Economy :\t\t\t\t " + Economy.get() + "\n")
            
            self.txtReceipt.insert(END,"Firstclass:\t\t\t\t " + FirstClass.get() + "\n")
            self.txtReceipt.insert(END,"Paid :\t\t\t\t " + PaidTax.get() + "\n")
            self.txtReceipt.insert(END,"SubTotal :\t\t\t\t " + subTotal.get() + "\n")
            self.txtReceipt.insert(END,"Total cost :\t\t\t\t " + TotalCost.get() + "\n")

        def Airport_tax():
            global paid1
            if var1.get() == 1:
                self.txtAirportTax.configure(state=NORMAL)
                Item1=float(50)

                Airport_Tax.set("Rs" +  str(Item1))
                paid1 = Airport_Tax.get()
                
            elif var1.get() == 0:
                self.txtAirportTax.configure(state=DISABLED)
                Airport_Tax.set("0")

        def mile():
            global Item2
            if var2.get() == 1:
                self.txtchkMile.configure(state=NORMAL)
                Item2=(2345)

                Mile.set( str(Item2))
               
            elif var2.get() == 0:
                self.txtchkMile.configure(state=DISABLED)
                Mile.set("0")

        def travel_insurance():
            global Item3
            if var3.get() == 1:
                self.txttravelling_insurance.configure(state=NORMAL)
                Item3=float(50)
                Travel_Ins.set("Rs" + str(Item3))

            elif var3.get() == 0:
                self.txttravelling_insurance.configure(state=DISABLED)
                Travel_Ins.set("0")

        def luggage():
            global Item4
            if var4.get() == 1:
                self.txtluggage.configure(state=NORMAL)
                Item4=float(75)
                Luggage.set("Rs " + str(Item4))

            elif var4.get() == 0:
                self.txtluggage.configure(state=DISABLED)
                Luggage.set("0")

        def Standard_fees():
            global Item5
            if var5.get() == 1:
                self.txtEconomy.configure(state=NORMAL)
                Item5=float(2500)
                Standard.set("Rs" +  str(Item5))

            elif var5.get() == 0:
                self.txtEconomy.configure(state=DISABLED)
                Standard.set("0")

        def Economy_fees():
            global Item6
            if var6.get() == 1:
                self.txtStandard.configure(state=NORMAL)
                Item6=float(3500)
                Economy.set("Rs" + str(Item6))

            elif var6.get() == 0:
                self.txtStandard.configure(state=DISABLED)
                Economy.set("0")

        def Firstclass_fees():
             global Item7
             if var7.get() == 1:
                 
                 self.txtfirstclass.configure(state=NORMAL)
                 Item7=float(4500)
                 FirstClass.set("Rs" + str(Item7))

             elif var7.get() == 0:
                 self.txtfirstclass.configure(state=DISABLED)
                 FirstClass.set("0")

    #=============================Data base==============================================
        
        def data():
            if Firstname.get()=="" or Surname.get() == "" or Address.get() == "" or PostalCode.get()=="" or Telephone.get()==""or Mobile.get()=="" or Email.get()=="":
                messagebox.showerror("Travel Management System","please fill all data")
            else:
                sqlcon=pymysql.connect(host='localhost',user='root',password='Admin@123',database='student_data')
                cur=sqlcon.cursor()
                cur.execute("insert into travel2 values(%s,%s,%s,%s,%s,%s,%s)",(
                Firstname.get(),
                Surname.get(),
                Address.get(),
                PostalCode.get(),
                Telephone.get(),
                Mobile.get(),
                Email.get()))
                
                sqlcon.commit()
                sqlcon.close()
                messagebox.showinfo("Travel Management System",'Data stored successfully')
            
    #============================================================================                
        MainFrame=Frame(self.root)
        MainFrame.grid()

        Top = Frame(MainFrame, bd=20,width=1350,relief=RIDGE)
        Top.pack(side=TOP)

        self.lblTitle=Label(Top,font=('arial',70,'bold'),text=" Travel Management System ")
        self.lblTitle.grid()
        #===========================================================================================
        CustomerDetailsFrame=LabelFrame(MainFrame,width=1350,height=500,bd=20,pady=5,relief=RIDGE)
        CustomerDetailsFrame.pack(side=BOTTOM)

        FrameDetails=Frame(CustomerDetailsFrame,width=880,height=400,bd=10,pady=5,relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        Customername=LabelFrame(FrameDetails,width=150,height=250,bd=20,pady=5,font=('arial',12,'bold'),text="Customer_Name",relief=RIDGE)
        Customername.grid(row=0,column=0)

        TravelFrame=LabelFrame(FrameDetails,width=300,height=250,bd=15,pady=5,font=('arial',12,'bold'),text="Travel_Deatails",relief=RIDGE)
        TravelFrame.grid(row=0,column=1)

        TicketFrame=LabelFrame(FrameDetails,width=300,height=150,bd=5,relief=FLAT)
        TicketFrame.grid(row=1,column=0)

        CostFrame=LabelFrame(FrameDetails,width=150,height=150,bd=5,relief=FLAT)
        CostFrame.grid(row=1,column=1)
        #===========================================================================================
        Receipt_ButtonFrame=LabelFrame(CustomerDetailsFrame,width=450,height=400,bd=10,relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)

        ReceiptFrame=LabelFrame(Receipt_ButtonFrame,width=350,height=300,pady=5,font=('arial',12,'bold'),text="Recipt",relief=RIDGE)
        ReceiptFrame.grid(row=0,column=0)

        ButtonFrame=LabelFrame(Receipt_ButtonFrame,width=350,height=100,relief=RIDGE)
        ButtonFrame.grid(row=1,column=0)
        #===========================================Customer Name================================================
        self.lblFirstname=Label(Customername,bd=7,font=('arial',12,'bold'),text="Firstname")
        self.lblFirstname.grid(row=0,column=0,sticky='w')

        self.txtFirstname=Entry(Customername,bd=7,font=('arial',12),textvariable=Firstname,
                                insertwidth=2,justify=LEFT)
        self.txtFirstname.grid(row=0,column=1)

        self.lblSurname=Label(Customername,bd=7,font=('arial',12,'bold'),text="Surname")
        self.lblSurname.grid(row=1,column=0,sticky='w')

        self.txtSurname=Entry(Customername,bd=7,font=('arial',12),textvariable=Surname,
                                insertwidth=2,justify=LEFT)
        self.txtSurname.grid(row=1,column=1)

        self.lblAddress=Label(Customername,bd=7,font=('arial',12,'bold'),text="Address")
        self.lblAddress.grid(row=2,column=0,sticky='w')

        self.txtAddress=Entry(Customername,bd=7,font=('arial',12),textvariable=Address,
                                insertwidth=2,justify=LEFT)
        self.txtAddress.grid(row=2,column=1)

        self.lblPostalCode=Label(Customername,bd=7,font=('arial',12,'bold'),text="PostalCode")
        self.lblPostalCode.grid(row=3,column=0,sticky='w')

        self.txtPostalCode=Entry(Customername,bd=7,font=('arial',12),textvariable=PostalCode,
                                insertwidth=2,justify=LEFT)
        self.txtPostalCode.grid(row=3,column=1)

        self.lblTelephone=Label(Customername,bd=7,font=('arial',12,'bold'),text="Telephone")
        self.lblTelephone.grid(row=4,column=0,sticky='w')

        self.txtTelephone=Entry(Customername,bd=7,font=('arial',12),textvariable=Telephone,
                                insertwidth=2,justify=LEFT)
        self.txtTelephone.grid(row=4,column=1)

        self.lblMobile=Label(Customername,bd=7,font=('arial',12,'bold'),text="Mobile")
        self.lblMobile.grid(row=5,column=0,sticky='w')

        self.txtMobile=Entry(Customername,bd=7,font=('arial',12),textvariable=Mobile,
                                insertwidth=2,justify=LEFT)
        self.txtMobile.grid(row=5,column=1)

        self.lblEmail=Label(Customername,bd=7,font=('arial',12,'bold'),text="Email")
        self.lblEmail.grid(row=6,column=0,sticky='w')

        self.txtEmail=Entry(Customername,bd=7,font=('arial',12),textvariable=Email,
                                insertwidth=2,justify=LEFT)
        self.txtEmail.grid(row=6,column=1)
        #=========================================Flight information==================================================
        self.lblDeparture=Label(TravelFrame,bd=7,font=('arial',12,'bold'),text="Departure")
        self.lblDeparture.grid(row=0,column=0,sticky='w')
        self.cboDeparture=ttk.Combobox(TravelFrame,textvariable=var11,state="readonly",font=('arial',12),width=14)
        self.cboDeparture['values']=('','Tuticorin','Chennai','Mumbai','Delhi','Kolkatta','Banglore','Hydrabad','Lucknow')
        self.cboDeparture.current(0)
        self.cboDeparture.grid(row=0,column=1)

        self.lblDestination=Label(TravelFrame,bd=7,font=('arial',12,'bold'),text="Destination")
        self.lblDestination.grid(row=1,column=0,sticky='w')
        self.cboDestination=ttk.Combobox(TravelFrame,textvariable=var12,state="readonly",font=('arial',12),width=14)
        self.cboDestination['values']=('','Tuticorin','Chennai','Mumbai','Delhi','Kolkatta','Banglore','Hydrabad','Lucknow')
        self.cboDestination.current(0)
        self.cboDestination.grid(row=1,column=1)

        self.lblAccommodation=Label(TravelFrame,bd=7,font=('arial',12,'bold'),text="Accommodation")
        self.lblAccommodation.grid(row=2,column=0,sticky='w')
        self.cboAccommodation=ttk.Combobox(TravelFrame,textvariable=var13,state="readonly",font=('arial',12),width=14)
        self.cboAccommodation['values']=('','1','2','3','4')
        self.cboAccommodation.current(0)
        self.cboAccommodation.grid(row=2,column=1)
        #===========================================================================================
        self.chkAirportTax=Checkbutton(TravelFrame,text="Airport tax",variable=var1,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=Airport_tax).grid(row=3,column=0,sticky='w')
        self.txtAirportTax=Entry(TravelFrame,bd=7,font=('arial',12),textvariable=Airport_Tax,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtAirportTax.grid(row=3,column=1)

        self.chkMile=Checkbutton(TravelFrame,text="Air Mile",variable=var2,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=mile).grid(row=4,column=0,sticky='w')
        self.txtchkMile=Entry(TravelFrame,bd=7,font=('arial',12),textvariable=Mile,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtchkMile.grid(row=4,column=1)

        self.travelling_insurance=Checkbutton(TravelFrame,text="travel_insurance",variable=var3,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=travel_insurance).grid(row=5,column=0,sticky='w')
        self.txttravelling_insurance=Entry(TravelFrame,bd=7,font=('arial',12),textvariable=Travel_Ins,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txttravelling_insurance.grid(row=5,column=1)

        self.luggage=Checkbutton(TravelFrame,text="Ext.Luggage",variable=var4,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=luggage).grid(row=6,column=0,sticky='w')
        self.txtluggage=Entry(TravelFrame,bd=7,font=('arial',12),textvariable=Luggage,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtluggage.grid(row=6,column=1)
        
         #===========================================Payment Information================================================
        self.lblPaidTax=Label(CostFrame,bd=7,font=('arial',12,'bold'),text="Paid Tax\t")
        self.lblPaidTax.grid(row=0,column=2,sticky='w')

        self.txtPaidTax=Entry(CostFrame,bd=7,font=('arial',12),textvariable=PaidTax,
                                insertwidth=2,justify=LEFT)
        self.txtPaidTax.grid(row=0,column=3)

        self.lblSubtotal=Label(CostFrame,bd=7,font=('arial',12,'bold'),text="SubTotal\t")
        self.lblSubtotal.grid(row=1,column=2,sticky='w')

        self.txtSubtotal=Entry(CostFrame,bd=7,font=('arial',12),textvariable=subTotal,
                                insertwidth=2,justify=LEFT)
        self.txtSubtotal.grid(row=1,column=3)

        self.lbltotal=Label(CostFrame,bd=7,font=('arial',12,'bold'),text="TotalCost\t")
        self.lbltotal.grid(row=2,column=2,sticky='w')

        self.txttotal=Entry(CostFrame,bd=7,font=('arial',12),textvariable=TotalCost,
                                insertwidth=2,justify=LEFT)
        self.txttotal.grid(row=2,column=3)
         #===========================================================================================
        self.chkStandard=Checkbutton(TicketFrame,text="Standard",variable=var5,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=Standard_fees).grid(row=0,column=0,sticky='w')
        self.txtStandard=Entry(TicketFrame,bd=7,font=('arial',12),textvariable=Standard,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtStandard.grid(row=0,column=1)

        self.chkSingle=Checkbutton(TicketFrame,text="Single",variable=var6,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold')).grid(row=0,column=2,sticky='w')
        self.chkEconomy=Checkbutton(TicketFrame,text="Economy",variable=var7,onvalue=1,offvalue=0,command=Economy_fees,
                                       font=('arial',12,'bold')).grid(row=1,column=0,sticky='w')
        self.txtEconomy=Entry(TicketFrame,bd=7,font=('arial',12),textvariable=Economy,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtEconomy.grid(row=1,column=1)
        
        self.chkReturn=Checkbutton(TicketFrame,text="Return",variable=var8,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold')).grid(row=1,column=2,sticky='w')
        
        self.chkfirstclass=Checkbutton(TicketFrame,text="FirstClass",variable=var9,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold'),command=Firstclass_fees).grid(row=2,column=0,sticky='w')
        self.txtfirstclass=Entry(TicketFrame,bd=7,font=('arial',12),textvariable=Economy,
                                insertwidth=2,state=DISABLED,justify=LEFT)
        self.txtfirstclass.grid(row=2,column=1)
        
        self.chksplneeds=Checkbutton(TicketFrame,text="Special Needs",variable=var10,onvalue=1,offvalue=0,
                                       font=('arial',12,'bold')).grid(row=2,column=2,sticky='w')             
         #=============================================Receipt==============================================
        self.txtReceipt=Text(ReceiptFrame,width=50,height=21, font=('arial',10,'bold'))
        self.txtReceipt.grid(row=0,column=0)
        #==============================================Buttons=============================================
        self.btnTotal=Button(ButtonFrame,padx=18,bd=7,font=('arial',14,'bold'),width=4,command=data,
                             text="Save").grid(row=0,column=0)
        self.btnTotal=Button(ButtonFrame,padx=18,bd=7,font=('arial',14,'bold'),width=4,
                             text="Print",command=Receipt).grid(row=0,column=1)
        self.btnTotal=Button(ButtonFrame,padx=18,bd=7,font=('arial',14,'bold'),width=4,
                             text="Reset",command=Reset).grid(row=0,column=2)
        self.btnTotal=Button(ButtonFrame,padx=18,bd=7,font=('arial',14,'bold'),width=4,
                             text="Exit",command=iExit).grid(row=0,column=3)

            #===========================================================================================


if __name__=="__main__":
    root=Tk()
    application = Travel(root)
    root.mainloop()

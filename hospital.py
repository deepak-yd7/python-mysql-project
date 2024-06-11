from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry('1540x800+0+0')

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PAtientName=StringVar()
        self.DateofBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=('architectural',40,'bold'))
        lbltitle.pack(side=TOP,fill=X)
# ----------------------------------dataframe-------------------------------------------------------------------------------------------------
        
        Dataframe=Frame(self.root,bd=15,relief=RIDGE)
        Dataframe.place(x=0,y=110,width=1920,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=('architectural',12,'bold'),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=('architectural',12,'bold'),text="Preception")
        DataframeRight.place(x=990,y=5,width=460,height=350)

#-----------------------------------buttonframe-----------------------------------------------------------------------------------------------

        self.Buttonframe=Frame(self.root,bd=12,relief=RIDGE)
        self.Buttonframe.place(x=0,y=520,width=1920,height=80)

#-----------------------------------DetailFrame-----------------------------------------------------------------------------------------------

        Detailframe=Frame(self.root,bd=15,relief=RIDGE)
        Detailframe.place(x=0,y=600,width=1920,height=150)

#------------------------------------Dataframeleft label-------------------------------------------------------------------------------------

        lblNameTablet=Label(DataframeLeft,text="Name of Tablet",font=('architectural',12,'bold'),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)

        comNametablet=ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,state="readonly",font=('architectural',12,'bold'),width=33)
        comNametablet["values"]=("Nice","Corona Vacacine","Acetaminophen","Aderall","Amlodipine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataframeLeft,font=('architectural',12,'bold'),text="Reference No.",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataframeLeft,font=('architectural',12,'bold'),text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataframeLeft,font=('architectural',12,'bold'),text="No of tablets:",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=('architectural',12,'bold'),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissuedate=Label(DataframeLeft,font=('architectural',12,'bold'),text="Issue Date:",padx=2,pady=6)
        lblissuedate.grid(row=5,column=0,sticky=W)
        txtissuedate=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.Issuedate,width=35)
        txtissuedate.grid(row=5,column=1)

        lblExpDate=Label(DataframeLeft,font=('architectural',12,'bold'),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataframeLeft,font=('architectural',12,'bold'),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect=Label(DataframeLeft,font=('architectural',12,'bold'),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.sideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo=Label(DataframeLeft,font=('architectural',12,'bold'),text="Further Information:",padx=2,pady=6)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0,column=3)

        lblDrivingMachine=Label(DataframeLeft,font=('architectural',12,'bold'),text="Blood Pressure:",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.DrivingUsingMachine,width=35)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage=Label(DataframeLeft,font=('architectural',12,'bold'),text="Storage Avice:",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataframeLeft,font=('architectural',12,'bold'),text="Medication:",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataframeLeft,font=('architectural',12,'bold'),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataframeLeft,font=('architectural',12,'bold'),text="NHS Number:",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName=Label(DataframeLeft,font=('architectural',12,'bold'),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.PAtientName,width=35)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth=Label(DataframeLeft,font=('architectural',12,'bold'),text="Date of Birth:",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.DateofBirth,width=35)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress=Label(DataframeLeft,font=('architectural',12,'bold'),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=('architectural',12,'bold'),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)

#----------------------------------------------Dataframe----------------------------------------------------------

        self.txtprescription=Text(DataframeRight,font=('architectural',12,'bold'),width=23,height=16,padx=2,pady=6)
        self.txtprescription.grid(row=0,column=0)

#----------------------------------------------Button------------------------------------------------------------

        btnprescription=Button(self.Buttonframe,text="Prescription",bg="green",command=self.prescription,font=('Arial',12,'bold'),width=23,height=15,padx=2,pady=6)
        btnprescription.grid(row=0,column=0)     

        btnprescriptionData=Button(self.Buttonframe,text="Prescription Data",command=self.prescriptionData,bg="pink",font=('Arial',12,'bold'),width=23,height=15,padx=2,pady=6)
        btnprescriptionData.grid(row=0,column=1)
        
        btnUpdate=Button(self.Buttonframe,text="Update",command=self.Update,bg="orange",font=('Arial',12,'bold'),width=23,height=15,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(self.Buttonframe,command=self.Delete,text="Delete",bg="blue",font=('Arial',12,'bold'),width=23,height=15,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClean=Button(self.Buttonframe,text="Clean",command=self.clear,bg="yellow",font=('Arial',12,'bold'),width=23,height=15,padx=2,pady=6)
        btnClean.grid(row=0,column=4)

        btnExit=Button(self.Buttonframe,command=self.exit,bg="red",font=('Arial',12,'bold'),width=23,height=15,text="exit",padx=2,pady=6)
        btnExit.grid(row=0,column=5)


#-------------------------------------------------table----and scrollbar-------------------------------------------------------------------
        scroll_x=ttk.Scrollbar(Detailframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber",
                                                             "pname","dob","address",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lots")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("address",text="Address")      

        self.hospital_table["show"]="headings"

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

        #---------------------------------------Functinality Database------------------------------------------


    def prescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="deepak123",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.ref.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.nhsNumber.get(),
                                                                                                self.PAtientName.get(),
                                                                                                self.DateofBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                ))
            conn.commit()
            self.fetch_data
            conn.close()
            messagebox.showinfo("success,record has been recorded")


    def Update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deepak123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,NumberofTablets=%s,Lot=%s,Issuedate=%s,ExpDate=%s,DailyDose=%s,StorageAdvice=%s,nhsNumber=%s,PAtientName=%s,DateofBirth=%s,PatientAddress=%s where ref = %s",(
                                                                                                self.Nameoftablets.get(),
                                                                                                self.Dose.get(),
                                                                                                self.NumberofTablets.get(),
                                                                                                self.Lot.get(),
                                                                                                self.Issuedate.get(),
                                                                                                self.ExpDate.get(),
                                                                                                self.DailyDose.get(),
                                                                                                self.StorageAdvice.get(),
                                                                                                self.nhsNumber.get(),
                                                                                                self.PAtientName.get(),
                                                                                                self.DateofBirth.get(),
                                                                                                self.PatientAddress.get(),
                                                                                                self.ref.get()
                                                                                                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update,Record has been updated Successfully")




    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deepak123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in row:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PAtientName.set(row[10])
        self.DateofBirth.set(row[11])
        self.PatientAddress.set(row[12])

    
    def prescription(self):
        self.txtprescription.insert(END,"Name of tablets:\t\t\t" + self.Nameoftablets.get()+"\n")
        self.txtprescription.insert(END,"reference number :\t\t\t" + self.ref.get()+"\n")
        self.txtprescription.insert(END,"Dose:\t\t\t" + self.Dose.get()+"\n")
        self.txtprescription.insert(END,"Number of tablets :\t\t\t" + self.NumberofTablets.get()+"\n")
        self.txtprescription.insert(END,"Lot:\t\t\t" + self.Lot.get()+"\n")
        self.txtprescription.insert(END,"Issue date:\t\t\t" + self.Issuedate.get()+"\n")
        self.txtprescription.insert(END,"Exp date:\t\t\t" + self.ExpDate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t" + self.DailyDose.get()+"\n")
        self.txtprescription.insert(END,"side effect:\t\t\t" + self.sideEffect.get()+"\n")
        self.txtprescription.insert(END,"Further information:\t\t\t" + self.FurtherInformation.get()+"\n")
        self.txtprescription.insert(END,"storage Advice:\t\t\t" + self.StorageAdvice.get()+"\n")
        self.txtprescription.insert(END,"Driving using machine:\t\t\t" + self.DrivingUsingMachine.get()+"\n")
        self.txtprescription.insert(END,"patient id:\t\t\t" + self.PatientId.get()+"\n")
        self.txtprescription.insert(END,"nhs Number:\t\t\t" + self.nhsNumber.get()+"\n")
        self.txtprescription.insert(END,"Patient name:\t\t\t" + self.PAtientName.get()+"\n")
        self.txtprescription.insert(END,"Date of birth:\t\t\t" + self.DateofBirth.get()+"\n")
        self.txtprescription.insert(END,"Patient Adress:\t\t\t" + self.PatientAddress.get()+"\n")

    def Delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="deepak123",database="mydata")
        my_cursor=conn.cursor()
        query= "delete from hospital where ref=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Deleted","patient has been deleted sucessfully")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PAtientName.set("")
        self.DateofBirth.set("")
        self.PatientAddress.set("")
        self.txtprescription.delete("1.0",END)

    def exit(self):
        exit=messagebox.askyesno("Hospital management system","confirm you want to exit")
        if exit>0:
            root.destroy()
            return           







root=Tk()
ob=Hospital(root)
root.mainloop()
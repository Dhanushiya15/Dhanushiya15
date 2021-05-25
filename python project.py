from tkinter import *
from tkinter import messagebox
import math,random,os
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x800+0+0")
        self.root.title("SIT CANTEEN")
        bg_color="#074465"
        title=Label(self.root,text="SIT CANTEEN",bd=12,relief=GROOVE,bg=bg_color,fg="red",font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #food
        self.VegMeals=IntVar()
        self.NonVegMeals=IntVar()
        self.VegFriedRice=IntVar()
        self.VegNoodles=IntVar()
        self.VegPulao=IntVar()
        self.Chapathi=IntVar()
        #=============snack========================
        self.Fritters=IntVar()
        self.Sandwich=IntVar() 
        self.VegRoll=IntVar()
        self.PaniPuri=IntVar()
        self.Samosa=IntVar()
        self.tea=IntVar()
        #=============Cold Drinks====================
        self.Tea=IntVar()
        self.Coffee=IntVar()
        self.Lemonade=IntVar()
        self.CocaCola=IntVar()
        self.Smoothie=IntVar()
        self.sprite=IntVar()
        #=============Total Product Price and Tax variables====================
        self.Food_price=StringVar()
        self.Snack_price=StringVar()
        self.Beverages_price=StringVar()

        self.Food_tax=StringVar()
        self.Snack_tax=StringVar()
        self.Beverages_tax=StringVar()
        #=============Customer Detail================
        
        #=============Customer Detail================
          
        
        #=============Cosmetics Frame================
        F2=LabelFrame(self.root,bd=10,relief=GROOVE,text="Food",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=3,y=75,width=200,height=280)
        bath_lbl=Label(F2,text="VegMeals",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        bath_txt=Entry(F2,width=10,textvariable=self.VegMeals,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        face_crm_lbl=Label(F2,text="NonVegMeals",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        face_crm_txt=Entry(F2,width=10,textvariable=self.NonVegMeals,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        face_w_lbl=Label(F2,text="VegFriedRice",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        face_w_txt=Entry(F2,width=10,textvariable=self.VegFriedRice,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        hair_s_lbl=Label(F2,text="VegNoodles",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        hair_s_txt=Entry(F2,width=10,textvariable=self.VegNoodles,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        hair_gel_lbl=Label(F2,text="VegPulao",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        hair_gel_txt=Entry(F2,width=10,textvariable=self.VegPulao,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        body_lbl=Label(F2,text="Chapathi",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        body_txt=Entry(F2,width=10,textvariable=self.Chapathi,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Grocery Frame================
        F3=LabelFrame(self.root,bd=10,relief=GROOVE,text="Snack",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=185,y=75,width=185,height=280)
        g1_lbl=Label(F3,text="Fritters",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        g1_txt=Entry(F3,width=10,textvariable=self.Fritters,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        g2_lbl=Label(F3,text="Sandwich",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        g2_txt=Entry(F3,width=10,textvariable=self.Sandwich,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        g3_lbl=Label(F3,text="VegRoll",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        g3_txt=Entry(F3,width=10,textvariable=self.VegRoll,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        g4_lbl=Label(F3,text="PaniPuri",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        g4_txt=Entry(F3,width=10,textvariable=self.PaniPuri,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        g5_lbl=Label(F3,text="Samosa",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        g5_txt=Entry(F3,width=10,textvariable=self.Samosa,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        g6_lbl=Label(F3,text="tea",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        g6_txt=Entry(F3,width=10,textvariable=self.tea,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)

        #=============Cold Drink Frame================
        F4=LabelFrame(self.root,bd=10,relief=GROOVE,text="Beverages",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=330,y=75,width=200,height=280)
        c1_lbl=Label(F4,text="Tea",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        c1_txt=Entry(F4,width=10,textvariable=self.Tea,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=8,pady=10)

        c2_lbl=Label(F4,text="Coffee",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        c2_txt=Entry(F4,width=10,textvariable=self.Coffee,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=8,pady=10)

        c3_lbl=Label(F4,text="Lemonade",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c3_txt=Entry(F4,width=10,textvariable=self.Lemonade,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=8,pady=10)
        
        c4_lbl=Label(F4,text="CocaCola",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        c4_txt=Entry(F4,width=10,textvariable=self.CocaCola,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=8,pady=10)
        
        c5_lbl=Label(F4,text="Smoothie",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        c5_txt=Entry(F4,width=10,textvariable=self.Smoothie,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=8,pady=10)

        c6_lbl=Label(F4,text="Sprite",font=("times new roman",15,"bold"),bg=bg_color,fg="yellow").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        c6_txt=Entry(F4,width=10,textvariable=self.sprite,font=("times new roman",12,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10,pady=10)
        
        #=============Bill Area Frame================
        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=490,y=75,width=320,height=285)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        #=============Button Frame================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="Bill Menu",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=3,y=350,width=700,height=140)
        m1_lbl=Label(F6,text="Total Food Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky="w")
        m1_txt=Entry(F6,width=15,textvariable=self.Food_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Snack Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=20,pady=1,sticky="w")
        m2_txt=Entry(F6,width=15,textvariable=self.Snack_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Beverages Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=20,pady=1,sticky="w")
        m3_txt=Entry(F6,width=15,textvariable=self.Beverages_price,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        c1_lbl=Label(F6,text="Food Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=3,padx=20,pady=1,sticky="w")
        c1_txt=Entry(F6,width=15,textvariable=self.Food_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=0,column=4,padx=10,pady=1)

        c2_lbl=Label(F6,text="Snack Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=3,padx=20,pady=1,sticky="w")
        c2_txt=Entry(F6,width=15,textvariable=self.Snack_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=1,column=4,padx=10,pady=1)

        c3_lbl=Label(F6,text="Beverages Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=3,padx=20,pady=1,sticky="w")
        c3_txt=Entry(F6,width=15,textvariable=self.Beverages_tax,font="arial 10 bold",bd=7,relief=SUNKEN).grid(row=2,column=4,padx=10,pady=1)
        btn_f=Frame(self.root,bd=7,relief=GROOVE)
        btn_f.place(x=3,y=480,width=510,height=80)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.VegMeals.get()*100
        self.c_fc_p=self.NonVegMeals.get()*150
        self.c_fw_p=self.VegFriedRice.get()*80
        self.c_spr_p=self.VegNoodles.get()*80
        self.c_g_p=self.VegPulao.get()*110
        self.c_l_p=self.Chapathi.get()*180
        self.total_Food_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.Food_price.set("Rs. "+str(self.total_Food_price))
        self.c_tax=round(self.total_Food_price*0.05,2)
        self.Food_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.Fritters.get()*30
        self.g_fo_p=self.Sandwich.get()*50
        self.g_w_p=self.PaniPuri.get()*20
        self.g_d_p=self.VegRoll.get()*40
        self.g_s_p=self.Samosa.get()*15
        self.g_t_p=self.tea.get()*150
        self.total_Snack_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.Snack_price.set("Rs. "+str(self.total_Snack_price))
        self.g_tax=round(self.total_Snack_price*0.1,2)
        self.Snack_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.Tea.get()*20
        self.cd_c_p=self.Coffee.get()*25
        self.cd_f_p=self.Lemonade.get()*40
        self.cd_th_p=self.CocaCola.get()*40
        self.cd_l_p=self.Smoothie.get()*70
        self.cd_s_p=self.sprite.get()*60
        self.total_Beverages_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.Beverages_price.set("Rs. "+str(self.total_Beverages_price))
        self.cd_tax=round(self.total_Beverages_price*0.05,2)
        self.Beverages_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_Food_price+
            self.total_Snack_price+
            self.total_Beverages_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t WELCOME TO SIT CANTEEN")
        
        self.textarea.insert(END,f"\n=================================")
        self.textarea.insert(END,f"\n Product\t       QTY\t       Price")
        self.textarea.insert(END,f"\n=================================")
    def bill_area(self):
        if self.VegMeals.get()!=0:
            self.textarea.insert(END,f"\n VegMeals\t\t{self.VegMeals.get()}\t{self.c_s_p}")
        if self.NonVegMeals.get()!=0:
            self.textarea.insert(END,f"\n NonVegMeals \t\t{self.NonVegMeals.get()}\t{self.c_fc_p}")
        if self.VegFriedRice.get()!=0:
            self.textarea.insert(END,f"\n VegFriedRice \t\t{self.VegFriedRice.get()}\t{self.c_fw_p}")
        if self.VegNoodles.get()!=0:
            self.textarea.insert(END,f"\n VegNoodles \t\t{self.VegNoodles.get()}\t{self.c_s_p}")
        if self.VegPulao.get()!=0:
            self.textarea.insert(END,f"\n VegPulao \t\t{self.VegPulao.get()}\t{self.c_g_p}")
        if self.Chapathi.get()!=0:
            self.textarea.insert(END,f"\n Chapathi\t\t{self.Chapathi.get()}\t{self.c_l_p}")
            #===Grocery=====
        if self.Fritters.get()!=0:
            self.textarea.insert(END,f"\n Fritters   \t\t{self.Fritters.get()}\t{self.g_r_p}")
        if self.Sandwich.get()!=0:
            self.textarea.insert(END,f"\n Sandwich\t\t{self.Sandwich.get()}\t{self.g_fo_p}")
        if self.VegRoll.get()!=0:
            self.textarea.insert(END,f"\n VegRoll   \t\t{self.VegRoll.get()}\t{self.g_d_p}")
        if self.PaniPuri.get()!=0:
            self.textarea.insert(END,f"\n PaniPuri  \t\t{self.PaniPuri.get()}\t{self.g_w_p}")
        if self.Samosa.get()!=0:
            self.textarea.insert(END,f"\n Samosa  \t\t{self.Samosa.get()}\t{self.g_s_p}")
        if self.tea.get()!=0:
            self.textarea.insert(END,f"\n tea   \t\t{self.tea.get()}\t{self.g_t_p}")
            
            #===Cold Drink=====
        if self.Tea.get()!=0:
            self.textarea.insert(END,f"\n Tea   \t\t{self.Tea.get()}\t{self.cd_m_p}")
        if self.Coffee.get()!=0:
            self.textarea.insert(END,f"\n Coffee   \t\t{self.Coffee.get()}\t{self.cd_c_p}")
        if self.Lemonade.get()!=0:
            self.textarea.insert(END,f"\n Lemonade  \t\t{self.Lemonade.get()}\t{self.cd_f_p}")
        if self.CocaCola.get()!=0:
            self.textarea.insert(END,f"\n Thumbs Up\t\t{self.CocaCola.get()}\t{self.cd_th_p}")
        if self.Smoothie.get()!=0:
            self.textarea.insert(END,f"\n Smoothie\t\t{self.Smoothie.get()}\t{self.cd_l_p}")
        if self.sprite.get()!=0:
            self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t{self.cd_s_p}")
        self.textarea.insert(END,f"\n---------------------------------")
        if self.Food_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Food Tax \t\t\t{self.Food_tax.get()}")
            
        if self.Snack_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Snack Tax \t\t\t{self.Snack_tax.get()}")
                
        if self.Beverages_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Beverages Tax\t\t\t{self.Beverages_tax.get()}")
        self.textarea.insert(END,f"\n Total Bill  \t\t\tRs. {self.total_bill}")
        self.textarea.insert(END,f"\n----------------------------------")
    
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.textarea.get('1.0',END)
            f1=open("D:\\project\\bill_app\\invoice\\"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no. :{self.bill_no.get()} saved successfullt")
        else:
            return
    def find_bill(self):
        present="no"
        for i in os.listdir("D:\\project\\bill_app\\invoice\\"):
            if i.split(".")[0]==self.search_bill.get():
                f1=open(f"D:\\project\\bill_app\\invoice\\{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill No")
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Cosmatics======================
            self.VegMeals.set(0)
            self.NonVegMeals.set(0)
            self.VegFriedRice.set(0)
            self.VegNoodles.set(0)
            self.VegPulao.set(0)
            self.Chapathi.set(0)
            #=============Grocery========================
            self.Fritters.set(0)
            self.Sandwich.set(0) 
            self.VegRoll.set(0)
            self.PaniPuri.set(0)
            self.Samosa.set(0)
            self.tea.set(0)
            #=============Cold Drinka====================
            self.Tea.set(0)
            self.Coffee.set(0)
            self.Lemonade.set(0)
            self.CocaCola.set(0)
            self.Smoothie.set(0)
            self.sprite.set(0)
            #=============Total Product Price and Tax variables====================
            self.Food_price.set("")
            self.Snack_price.set("")
            self.Beverages_price.set("")

            self.Food_tax.set("")
            self.Snack_tax.set("")
            self.Beverages_tax.set("")
            #=============Customer Detail================
            self.c_name.set("")
            self.c_phon.set("")
            self.bill_no.set("")
            x=random.randint(1000,9999)
            self.bill_no.set(str(x))
            self.search_bill.set("")
            self.welcome_bill()
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()





root=Tk()
obj=Bill_App(root)

root.mainloop()
'''
        btn_f.place(x=820,width=510,height=180)
        total_btn=Button(btn_f,text="Total",command=self.total,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=0,padx=5,pady=5)
        gbill_btn=Button(btn_f,command=self.bill_area,text="Generate Bill",bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(btn_f,text="Clear",command=self.clear_data,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(btn_f,text="Exit",command=self.Exit_app,bg="cadetblue",fg="white",pady=10,width=10,bd=4,font="arial 10 bold").grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    def total(self):
        self.c_s_p=self.soap.get()*40
        self.c_fc_p=self.face_cream.get()*120
        self.c_fw_p=self.face_wash.get()*60
        self.c_spr_p=self.spray.get()*180
        self.c_g_p=self.gell.get()*140
        self.c_l_p=self.Chapathi.get()*180
        self.total_cosmatic_price=float(
                                    self.c_s_p+
                                    self.c_fc_p+
                                    self.c_fw_p+
                                    self.c_spr_p+
                                    self.c_g_p+
                                    self.c_l_p
                                  )
        self.cosmetic_price.set("Rs. "+str(self.total_cosmatic_price))
        self.c_tax=round(self.total_cosmatic_price*0.05,2)
        self.cosmetic_tax.set("Rs. "+str(self.c_tax))
        self.g_r_p=self.rice.get()*80
        self.g_fo_p=self.food_oil.get()*180
        self.g_w_p=self.PaniPuri.get()*60
        self.g_d_p=self.VegRoll.get()*240
        self.g_s_p=self.Samosa.get()*45
        self.g_t_p=self.tea.get()*150
        self.total_grocery_price=float(
                                    self.g_r_p+
                                    self.g_fo_p+
                                    self.g_w_p+
                                    self.g_d_p+
                                    self.g_s_p+
                                    self.g_t_p
                                  )
        self.grocery_price.set("Rs. "+str(self.total_grocery_price))
        self.g_tax=round(self.total_grocery_price*0.1,2)
        self.grocery_tax.set("Rs. "+str(self.g_tax))
        self.cd_m_p=self.Tea.get()*60
        self.cd_c_p=self.Coffee.get()*60
        self.cd_f_p=self.Lemonade.get()*50
        self.cd_th_p=self.Coca Cola.get()*45
        self.cd_l_p=self.Smoothie.get()*40
        self.cd_s_p=self.sprite.get()*60
        self.total_cold_drink_price=float(
                                    self.cd_m_p+
                                    self.cd_c_p+
                                    self.cd_f_p+
                                    self.cd_th_p+
                                    self.cd_l_p+
                                    self.cd_s_p
                                   )
        self.cold_drink_price.set("Rs. "+str(self.total_cold_drink_price))
        self.cd_tax=round(self.total_cold_drink_price*0.05,2)
        self.cold_drink_tax.set("Rs. "+str(self.cd_tax))
        self.total_bill=float(
            self.total_cosmatic_price+
            self.total_grocery_price+
            self.total_cold_drink_price+
            self.c_tax+
            self.g_tax+
            self.cd_tax
        )
    
            #===cosmatics=====
        if self.soap.get()!=0:
            self.textarea.insert(END,f"\n Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get()!=0:
            self.textarea.insert(END,f"\n Face Cream\t\t{self.face_cream.get()}\t\t{self.c_fc_p}")
        if self.face_wash.get()!=0:
            self.textarea.insert(END,f"\n Face Wash \t\t{self.face_wash.get()}\t\t{self.c_fw_p}")
        if self.spray.get()!=0:
            self.textarea.insert(END,f"\n Hair Spray\t\t{self.spray.get()}\t\t{self.c_s_p}")
        if self.gell.get()!=0:
            self.textarea.insert(END,f"\n Hair Gell \t\t{self.gell.get()}\t\t{self.c_g_p}")
        if self.Chapathi.get()!=0:
            self.textarea.insert(END,f"\n Body Chapathi\t\t{self.Chapathi.get()}\t\t{self.c_l_p}")
            #===Grocery=====
        if self.rice.get()!=0:
            self.textarea.insert(END,f"\n Rice   \t\t{self.rice.get()}\t\t{self.g_r_p}")
        if self.food_oil.get()!=0:
            self.textarea.insert(END,f"\n Food Oil\t\t{self.food_oil.get()}\t\t{self.g_fo_p}")
        if self.VegRoll.get()!=0:
            self.textarea.insert(END,f"\n VegRoll   \t\t{self.VegRoll.get()}\t\t{self.g_d_p}")
        if self.PaniPuri.get()!=0:
            self.textarea.insert(END,f"\n PaniPuri  \t\t{self.PaniPuri.get()}\t\t{self.g_w_p}")
        if self.Samosa.get()!=0:
            self.textarea.insert(END,f"\n Suger  \t\t{self.Samosa.get()}\t\t{self.g_s_p}")
        if self.tea.get()!=0:
            self.textarea.insert(END,f"\n Tea   \t\t{self.tea.get()}\t\t{self.g_t_p}")
            
            #===Cold Drink=====
        if self.Tea.get()!=0:
            self.textarea.insert(END,f"\n Tea   \t\t{self.Tea.get()}\t\t{self.cd_m_p}")
        if self.Coffee.get()!=0:
            self.textarea.insert(END,f"\n Coffee   \t\t{self.Coffee.get()}\t\t{self.cd_c_p}")
        if self.Lemonade.get()!=0:
            self.textarea.insert(END,f"\n Lemonade  \t\t{self.Lemonade.get()}\t\t{self.cd_f_p}")
        if self.Coca Cola.get()!=0:
            self.textarea.insert(END,f"\n Thumbs Up\t\t{self.Coca Cola.get()}\t\t{self.cd_th_p}")
        if self.Smoothie.get()!=0:
            self.textarea.insert(END,f"\n Smoothie\t\t{self.Smoothie.get()}\t\t{self.cd_l_p}")
        if self.sprite.get()!=0:
            self.textarea.insert(END,f"\n Sprite  \t\t{self.sprite.get()}\t\t{self.cd_s_p}")
        self.textarea.insert(END,f"\n--------------------------------------")
        if self.cosmetic_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Cosmatic Tax \t\t\t{self.cosmetic_tax.get()}")
            
        if self.grocery_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n Grocery Tax \t\t\t{self.grocery_tax.get()}")
                
        if self.cold_drink_tax.get()!="Rs. 0.0":
            self.textarea.insert(END,f"\n ColdDrink Tax\t\t\t{self.cold_drink_tax.get()}")
        self.textarea.insert(END,f"\n Total Bill  \t\t\t Rs. {self.total_bill}")
        self.textarea.insert(END,f"\n---------------------------------------")
       
         
    def clear_data(self):
        op=messagebox.askyesno("clear","Do you want to Reset Entries?")
        if op>0:
            #=============Cosmatics======================
            self.soap.set(0)
            self.face_cream.set(0)
            self.face_wash.set(0)
            self.spray.set(0)
            self.gell.set(0)
            self.Chapathi.set(0)
            #=============Grocery========================
            self.rice.set(0)
            self.food_oil.set(0) 
            self.VegRoll.set(0)
            self.PaniPuri.set(0)
            self.Samosa.set(0)
            self.tea.set(0)
            #=============Cold Drinka====================
            self.Tea.set(0)
            self.Coffee.set(0)
            self.Lemonade.set(0)
            self.Coca Cola.set(0)
            self.Smoothie.set(0)
            self.sprite.set(0)
            #=============Total Product Price and Tax variables====================
            self.cosmetic_price.set("")
            self.grocery_price.set("")
            self.cold_drink_price.set("")

            self.cosmetic_tax.set("")
            self.grocery_tax.set("")
            self.cold_drink_tax.set("")
            #=============Customer Detail================
            
    def Exit_app(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()





root=Tk()
obj=Bill_App(root)

root.mainloop()
'''

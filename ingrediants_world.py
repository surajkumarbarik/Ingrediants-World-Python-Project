from tkinter import *
from tkinter import ttk

root=Tk()

root.geometry("1040x800")
root.minsize(1370,800)
# root.iconbitmap('a1.png')


def deleteall():
    root.geometry("1040x800")
    root.minsize(1370, 800)
    bg_clr="#074463"


    root.title("INGREDIANTS WORLD")
    # root.iconbitmap('a1.png')
    l1=Label(root,text="I N G R E D I A N T S \n W O R L D", bd=12,relief=GROOVE,bg=bg_clr,
             fg="white",font=("times new roman", 30, "bold"),pady=2).pack(fill=X)


    f1=LabelFrame(root,bg=bg_clr,relief=GROOVE,bd=10)
    f1.place(x=0,y=120,height=530,width=910)

    f5=LabelFrame(root,bg=bg_clr,relief=GROOVE,bd=10)
    f5.place(x=0,y=645,height=90,width=910)


    l2 = Label(f1, text="       W E L C O M E  !", bd=12, bg=bg_clr,
                   fg="cyan", font=("Bahnschrift SemiBold", 60, "bold"))
    l2.grid()

    f2 = Frame(root, bd=10, relief=GROOVE)
    f2.place(x=910, y=120, height=610, width=450)
    item_title = Label(f2, text="THE INGREDIANTS", font="arial 20 bold", bd=7, relief=GROOVE).pack(fill=X)


    def startfun():
        # global f2
        # def deletefunc():
        #     f2.grid_forget()
        #
        # deletefunc()

        f2 = Frame(root, bd=10, relief=GROOVE)
        f2.place(x=910, y=120, height=610, width=450)
        item_title = Label(f2, text="THE INGREDIANTS", font="arial 20 bold", bd=7, relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(f2, orient=VERTICAL)
        txtarea = Text(f2, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txtarea.yview)
        # txtarea.pack()

        def quitfun():
            x=1
            print("T H A N K  Y O U")
            exit()

        exit_btn = Button(f5, bd=5, relief=GROOVE, text="EXIT", bg="cadetblue", fg="white", width=10,
                         font="arial 15 bold", command=quitfun).grid(row=11, column=5, padx=15, pady=5, sticky=W)


        def secclck():
            if mysection.get()=='Basic Meals':
                def dishclck():
                    if mydish.get()=='Rice':
                        def prsnclck():
                            ch=myprsn.get()
                            def ingrdnt():
                                txt=Text(f2)
                                txt.insert(INSERT,"\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< RICE IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT,"Rice=\t\t\t\t%d" %(ch * 120) +" gm\nWater=      \t\t\t\t%d" %ch +" ltr\nSalt=   \t\t\t\t1 spoon")
                                txt.insert(END,"\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()
                        person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr, fg="yellow")
                        person_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

                        myprsn = IntVar()
                        prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"), textvariable=myprsn)
                        prsn_cmbx.grid(row=6, column=0, sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                    elif mydish.get() == 'Dal':
                        def prsnclck():
                            ch = myprsn.get()
                            def ingrdnt():
                                txt = Text(f2)
                                txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< DAL IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT, "Harad Dal= \t\t\t\t%d" %(ch * 50) +"gm\nWater= \t\t\t\t%d" %(ch * 70) +"ml \nSalt= \t\t\t\t%d" %ch+"spoon\nTurmeric= \t\t\t\t%.2f" %(ch * 0.25)+"spoon\nTomatto= \t\t\t\t%d" %ch+ "gm\nOnion= \t\t\t\t%.2f" %(ch * 0.25)+ "piece \nOil= \t\t\t\t%.2f" %(ch * 1.5)+"spoon\nChilli= \t\t\t\t 2 piece\nPhutan= \t\t\t\t%.2f" %(ch * 0.75)+ "spoon\nJeera= \t\t\t\t%.2f" %(ch * 0.5)+ "spoon")
                                txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()

                        person_label=Label(f1,text="PERSON ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                        person_label.grid(row=6,column=0,padx=10,pady=10,sticky="w")

                        myprsn=IntVar()
                        prsn_option=[1,2,3,4,5,6,7,8,9,10]
                        prsn_cmbx = ttk.Combobox(f1,value=prsn_option,font=("times new roman",14,"bold"),textvariable=myprsn)
                        prsn_cmbx.grid(row=6,column=0,sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)



                dishes_label=Label(f1,text="DISHES ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                dishes_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

                mydish=StringVar()
                dishes_option=['Rice','Dal']
                dishes_cmbx = ttk.Combobox(f1,value=dishes_option,font=("times new roman",14,"bold"),textvariable=mydish)
                dishes_cmbx.grid(row=4,column=0,sticky="e")

                dishbtn=ttk.Button(f1,text="NEXT",command=dishclck)
                dishbtn.grid(row=5,column=0,sticky="e")

            elif mysection.get()== 'Prime Dishes':
                def catclck():
                    if mycatagory.get()=='Veg':
                        def dishclck():
                            if mydish.get()=='Dalma':
                                def prsnclck():
                                    ch=myprsn.get()
                                    def ingrdnt():
                                        txt=Text(f2)
                                        txt.insert(INSERT,"\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                          "================================================\n\n"
                                                          "  <<<< DALMA IS NOW READY FOR YOU >>>>\n\n"
                                                          "================================================\n"
                                                          "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                          "================================================\n")
                                        txt.insert(INSERT,"Harad Dal=\t\t\t\t%d"%(ch*50)+ " gm\nPotato=\t\t\t\t%d"%(ch*50)+
                                  "gm\nWatermmellon=\t\t\t\t%d"%(ch*2)+ " gm \nCaroot=\t\t\t\t%d"%ch+ " piece\nJhudanga=\t\t\t\t%d"%(ch*50)+
                                  " gm\nBrinjal \t\t\t\t%d"%(ch*50)+ " gm\nTej Patta=\t\t\t\t 2 piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nDry Chilli=\t\t\t\t 2 piece\nPhutan=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.5)+
                                  " gm\nWater=\t\t\t\t%d"%(ch*70)+ " ml \nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\nTomatto=\t\t\t\t%d"%ch+ "piece\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nChilli=\t\t\t\t 2 piece\nPhutan=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.5)+ "spoon")
                                        txt.insert(END,"\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()
                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr, fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"), textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Allu Vaja':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< ALLU VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Potato=\t\t\t\t%d"%ch+ " piece\nWater= \t\t\t\t100 ml \nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nChilli=\t\t\t\t 2 piece\nPhutan=\t\t\t\t%.2f"%(ch*0.75)+" spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Kobi Vaja':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< KOBI VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Cauliflower=\t\t\t\t%d"%(ch*60)+ " gm\nWater=\t\t\t\t%d"%(ch*100)+ " ml \nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nChilli=\t\t\t\t 2 piece\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nRed Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Saga Vaja':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< SAGA VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Amarnath Leaves(Leutia Saga)=\t\t\t\t%d"%(ch*175)+ " gm\nWater= \t\t\t\t100 ml\nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ "piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nDry Chilli=\t\t\t\t 2 piece\nGarlic=\t\t\t\t5 piece")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Potala Vaja':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< POTALA VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Pointed Gourd(Potala)=\t\t\t\t%d"%(ch*3)+ " piece\nWater= \t\t\t\t100 ml\nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nGreen Chilli=\t\t\t\t 2 piece\nPhutan=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nRoasted Cumin Powder=\t\t\t\t0.5 spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Kadali Vaja':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< KADALI VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Raw Banana=\t\t\t\t%d"%(ch*2)+ " piece\nWater= \t\t\t\t100 ml\nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nDry Red Chilli=\t\t\t\t 2 piece\nPhutan=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nRoasted Cumin Powder=\t\t\t\t%d"%ch+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Jhudanga Vaja':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< JHUDANGA VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Yard Long Beans=\t\t\t\t%d"%(ch*50)+ " gm\nWater=\t\t\t\t%d"%(ch*100)+ " ml\nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nChilli=\t\t\t\t 2 piece\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nRed Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Mix Veg':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MIX VEG IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Paneer=\t\t\t\t%d"%(ch*8)+ " piece\nBadam=\t\t\t\t%d"%(ch*7)+ " piece \nPatato=\t\t\t\t%d"%ch+ " piece\nCarrot=\t\t\t\t%.2f"%(ch*0.5)+ " piece\nMatar=\t\t\t\t%d"%(ch*10)+ " gm \nCapsicum=\t\t\t\t%.2f"%(ch*0.5)+
        " piece\nCauliflower=\t\t\t\t%d"%(ch*35)+ " gm\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+ " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
        " spoon\nTej Patta=\t\t\t\t 2 piece\nKasuri Methi=\t\t\t\t%d"%(ch*75)+ " gm\nGinger Garlic Paste=\t\t\t\t%d"%ch+ " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
        "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Kobi Curry':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< KOBI CURRY IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Patato=\t\t\t\t%d"%ch+ " piece\nCauliflower=\t\t\t\t%d"%(ch*150)+ " gm\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+
        " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\nOnion=\t\t\t\t%.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
        " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
        "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Soyabin Curry':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< SOYABEAN CURRY IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Patato=\t\t\t\t%d"%ch+ " piece\nSoyabean=\t\t\t\t%d"%(ch*150)+ " gm\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+
        " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
        " spoon\ntomato=\t\t\t\t%d"%ch+ " piece\nOnion=\t\t\t\t%.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
        " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+
        " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
        "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+ " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Allu Kasaa':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< ALLU KASAA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Patato=\t\t\t\t%.2f"%(ch*1.5)+ " piece\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+
                                  " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\ntomato=\t\t\t\t%d"%ch+ " piece\nOnion=\t\t\t\t%d"%ch+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
                                  " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
                                  "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                                  " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Paneer Masala':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< PANEER MASALA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Patato=\t\t\t\t%d"%ch+ " piece\nPaneer=\t\t\t\t%d"%(ch*100)+ " gm\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+
                                  " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\ntomato=\t\t\t\t%d"%ch+ " piece\nOnion=\t\t\t\t%.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+" spoon\nCashews=\t\t\t\t%d"%(ch*8)+
                                  " piece\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t%d"%(ch*2)+
                                  " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
                                  "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                                  " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                            elif mydish.get() == 'Mushroom Masala':

                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MUSHROOM MASALA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT,
                                                   "Mushroom=\t\t\t\t%d"%(ch*200)+ " gm\nWater=\t\t\t\t%d"%(ch*150)+ "ml \nSalt=\t\t\t\t%d"%ch+
                                  " spoon\nTurmeric=\t\t\t\t%.2f"%(ch*0.25)+
                                  " spoon\ntomato=\t\t\t\t%d"%ch+ " piece\nOnion=\t\t\t\t%.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t%.2f"%(ch*1.5)+
                                  " spoon\nRed Chilli Powder=\t\t\t\t%d"%ch+ " spoon\nJeera=\t\t\t\t%.2f"%(ch*0.75)+ " spoon\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+ " spoon\nCashews=\t\t\t\t%d"%(ch*8)+
                                  " piece\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t%d"%(ch*2)+
                                  " spoon\nGreen Chilli=\t\t\t\t%d"%ch+
                                  "piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                                  " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                        dishes_label = Label(f1, text="DISHES ", font=("times new roman", 25, "bold"), bg=bg_clr, fg="yellow")
                        dishes_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

                        mydish = StringVar()
                        dishes_option = ['Dalma', 'Allu Vaja', 'Kobi Vaja', 'Saga Vaja', 'Potala Vaja',
                                     'Kadali Vaja',  'Jhudanga Vaja', 'Mix Curry', 'Kobi Curry', 'Soyabin Curry',  'Allu Kasaa',
                                     'Paneer Masala', 'Mushroom Masala']
                        dishes_cmbx = ttk.Combobox(f1, value=dishes_option, font=("times new roman", 14, "bold"),textvariable=mydish)
                        dishes_cmbx.grid(row=6, column=0, sticky="e")

                        dishbtn = ttk.Button(f1, text="NEXT", command=dishclck)
                        dishbtn.grid(row=7, column=0, sticky="e")

                    elif mycatagory.get()=='Non-Veg':
                        def dishclck():
                            if mydish.get() == 'Macha Vaja':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MACHA VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Fish(Machaa)=\t\t\t\t %d"%(ch*2)+ " piece\nSalt=\t\t\t\t %d"%(ch*2)+ " spoon\nTurmeric=\t\t\t\t %d"%(ch*2)+
                                      " spoon\nOil=\t\t\t\t %d"%(ch*4)+
                                      " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Macha Besara':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MACHA BESARA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Fish(Macha)=\t\t\t\t %d"%(ch*2)+ " piece\nWater=\t\t\t\t 100 ml \nSalt=\t\t\t\t %d"%ch+ " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.25)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nChilli=\t\t\t\t 2 piece\nMustard Seed=\t\t\t\t %d"%(ch*1.5)+ " spoon\nTomato=\t\t\t\t %d"%ch+" piece\nRed Chilli Powder=\t\t\t\t %d"%ch+
                                      " spoon\nPhutan=\t\t\t\t %d"%ch+" spoon\nCoriander Powder=\t\t\t\t %d"%ch+" spoon\nCumin Powder=\t\t\t\t %d"%ch+" spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Macha Curry':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MACHA CURRY IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Patato=\t\t\t\t %0.2f"%(ch*0.5)+ " piece\nFish(Macha)=\t\t\t\t %d"%(ch*2)+ " piece\nWater=\t\t\t\t %d"%(ch*150)+ "ml \nSalt=\t\t\t\t %d"%ch+
                                      " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nRed Chilli Powder=\t\t\t\t %d"%ch+ " spoon\nJeera=\t\t\t\t %0.2f"%(ch*0.75)+
                                      " spoon\nKashmir Chilli Powder=\t\t\t\t %0.2f"%(ch*0.5)+
                                      " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nGreen Chilli=\t\t\t\t %d"%ch+
                                      " piece\nCoriander Powder=\t\t\t\t %d"%ch+ " spoon\nCumin Powder=\t\t\t\t %d"%ch+ " spoon\nGaram Masala=\t\t\t\t %d"%ch+
                                      " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Chingudi Vaja':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< CHINGUDI VAJA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Chingudi=\t\t\t\t %d"%(ch*4)+ " piece\nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nSalt=\t\t\t\t %d"%(ch*2)+ " spoon\nTurmeric=\t\t\t\t %d"%(ch*2)+
                                      " spoon\nOil=\t\t\t\t %d"%(ch*4)+
                                      " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Chingudi Curry':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< CHINGUDI CURRY IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Prawn(Chingudi)=\t\t\t\t %d"%(ch*4)+ " piece\nWater=\t\t\t\t %d"%(ch*150)+ "ml \nSalt=\t\t\t\t %d"%ch+
                                      " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nRed Chilli Powder=\t\t\t\t %d"%ch+ " spoon\nJeera=\t\t\t\t %0.2f"%(ch*0.75)+
                                      " spoon\nKashmir Chilli Powder=\t\t\t\t %0.2f"%(ch*0.5)+
                                      " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nGreen Chilli=\t\t\t\t %d"%ch+
                                      " piece\nCoriander Powder=\t\t\t\t %d"%ch+ " spoon\nCumin Powder=\t\t\t\t %d"%ch+ " spoon\nGaram Masala=\t\t\t\t %d"%ch+
                                      " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Egg Fry':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< EGG CURRY IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Boiled Egg=\t\t\t\t %d"%(ch*2)+ " piece\nWater=\t\t\t\t %d"%(ch*150)+ "ml \nSalt=\t\t\t\t %d"%ch+
                                      " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nRed Chilli Powder=\t\t\t\t %d"%ch+ " spoon\nJeera=\t\t\t\t %0.2f"%(ch*0.75)+
                                      " spoon\nKashmir Chilli Powder=\t\t\t\t %0.2f"%(ch*0.5)+
                                      " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nGreen Chilli=\t\t\t\t %d"%ch+
                                      " piece\nCoriander Powder=\t\t\t\t %d"%ch+ " spoon\nCumin Powder=\t\t\t\t %d"%ch+ " spoon\nGaram Masala=\t\t\t\t %d"%ch+
                                      " spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Chicken Masala':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< CHICKEN MASALA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Chicken=\t\t\t\t %d"%(ch*200)+ " gm\nWater=\t\t\t\t %d"%(ch*150)+ "ml \nSalt=\t\t\t\t %d"%ch+
                                      " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nRed Chilli Powder=\t\t\t\t %d"%ch+ " spoon\nJeera=\t\t\t\t %0.2f"%(ch*0.75)+
                                      " spoon\nKashmir Chilli Powder=\t\t\t\t %0.2f"%(ch*0.5)+
                                      " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nGreen Chilli=\t\t\t\t %d"%ch+
                                      " piece\nCoriander Powder=\t\t\t\t %d"%ch+ " spoon\nCumin Powder=\t\t\t\t %d"%ch+ " spoon\nGaram Masala=\t\t\t\t %d"%ch+
                                      " spoon\nChicken Masala=\t\t\t\t %d"%ch+" spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                            elif mydish.get() == 'Mutton Masala':
                                def prsnclck():
                                    ch = myprsn.get()

                                    def ingrdnt():
                                        txt = Text(f2)
                                        txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MUTTON MASALA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                        txt.insert(INSERT, "Mutton=\t\t\t\t %d"%(ch*200)+ " gm\nWater=\t\t\t\t %d"%(ch*150)+ "ml \nSalt=\t\t\t\t %d"%ch+
                                      " spoon\nTurmeric=\t\t\t\t %0.2f"%(ch*0.25)+
                                      " spoon\nOnion=\t\t\t\t %0.2f"%(ch*0.5)+ " piece \nOil=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nRed Chilli Powder=\t\t\t\t %d"%ch+ " spoon\nJeera=\t\t\t\t %0.2f"%(ch*0.75)+
                                      " spoon\nKashmir Chilli Powder=\t\t\t\t %0.2f"%(ch*0.5)+
                                      " spoon\nTej Patta=\t\t\t\t 2 piece\nGinger Garlic Paste=\t\t\t\t %d"%(ch*1.5)+
                                      " spoon\nGreen Chilli=\t\t\t\t %d"%ch+
                                      " piece\nCoriander Powder=\t\t\t\t %d"%ch+ " spoon\nCumin Powder=\t\t\t\t %d"%ch+ " spoon\nGaram Masala=\t\t\t\t %d"%ch+
                                      " spoon\nMeat/Mutton Masala=\t\t\t\t %d"%ch+" spoon")
                                        txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                        txt.pack()

                                    ingrdnt()

                                person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr,
                                                     fg="yellow")
                                person_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")

                                myprsn = IntVar()
                                prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"),
                                                         textvariable=myprsn)
                                prsn_cmbx.grid(row=8, column=0, sticky="e")

                                prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)


                        dishes_label = Label(f1, text="DISHES ", font=("times new roman", 25, "bold"), bg=bg_clr, fg="yellow")
                        dishes_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

                        mydish = StringVar()
                        dishes_option = ['Macha Vaja', 'Macha Besara', 'Macha Curry', 'Chingudi Vaja', 'Chingudi Curry',
                                 'Egg Fry', 'Chicken Masala', 'Mutton Masala']
                        dishes_cmbx = ttk.Combobox(f1, value=dishes_option, font=("times new roman", 14, "bold"),
                                                   textvariable=mydish)
                        dishes_cmbx.grid(row=6, column=0, sticky="e")

                        dishbtn = ttk.Button(f1, text="NEXT", command=dishclck)
                        dishbtn.grid(row=7, column=0, sticky="e")


                catagory_label=Label(f1,text="CATAGORY ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                catagory_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

                mycatagory=StringVar()
                ctgr_option=['Veg','Non-Veg']
                ctgr_cmbx = ttk.Combobox(f1,value=ctgr_option,font=("times new roman",14,"bold"),textvariable=mycatagory)
                ctgr_cmbx.grid(row=4,column=0,sticky="e")
                ctgr_btn = ttk.Button(f1, text="NEXT", command=catclck)
                ctgr_btn.grid(row=5, column=0, sticky="e")

            elif mysection.get()=='Special Flavour':
                def dishclck():
                    if mydish.get()=='Dahi Pakhala':
                        def prsnclck():
                            ch=myprsn.get()
                            def ingrdnt():
                                txt=Text(f2)
                                txt.insert(INSERT,"\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< DAHI PAKHALA IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT,"Rice=\t\t\t\t%d"%(ch*2)+ " cup\nSalt=\t\t\t\t%d"%(ch*2)+ " spoon(as taste)\nGreen Chilli=\t\t\t\t%d"%(ch*2)+
                          " piece\nCurry Leaves=\t\t\t\t5,6 pieces\nDry Red Chilli=\t\t\t\t%d"%(ch*2)+" pieces\nCurd(Dahi)=\t\t\t\t%d"%(ch*150)+" gm\nPhutana=\t\t\t\t%d"%ch+" spoon")
                                txt.insert(END,"\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()
                        person_label = Label(f1, text="PERSON ", font=("times new roman", 25, "bold"), bg=bg_clr, fg="yellow")
                        person_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")

                        myprsn = IntVar()
                        prsn_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                        prsn_cmbx = ttk.Combobox(f1, value=prsn_option, font=("times new roman", 14, "bold"), textvariable=myprsn)
                        prsn_cmbx.grid(row=6, column=0, sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                    elif mydish.get() == 'Veg Biryani':
                        def prsnclck():
                            ch = myprsn.get()
                            def ingrdnt():
                                txt = Text(f2)
                                txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< VEG BIRYANI IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT, "Basmati Rice=\t\t\t\t%d"%(ch*2)+" cup\nPaneer=\t\t\t\t%d"%(ch*6)+ " piece\nBadam=\t\t\t\t%d"%(ch*7)+ " piece \nPatato=\t\t\t\t%d"%ch+ " piece\nCarrot=\t\t\t\t%.2f"%(ch*0.5)+" piece\nSoyabean=\t\t\t\t%d"%(ch*8)+" piece\nMatar=\t\t\t\t%d"%(ch*10)+ " gm \nCapsicum=\t\t\t\t%.2f"%(ch*0.5)+
                              " piece\nCauliflower=\t\t\t\t%d"%(ch*35)+ " gm\nWater=\t\t\t\t%d"%(ch*6)+" cup\nOnion=\t\t\t\t%d"%(ch*2)+
                          " pieces\nOil=\t\t\t\t%d"%(ch*8)+" spoon\nYogurt(curd)=\t\t\t\t%d"%(ch*200)+" gm\nTomato Puree=\t\t\t\t%d"%(ch*6)+
                          " spoon\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+" spoon\nGhee=\t\t\t\t%d"%(ch*2)+" spoon\nSalt=\t\t\t\t%.2f"%(ch*3.25)+
                          " spoon\nCloves & Cardamom=\t\t\t\t8/9 pieces\nMint Leaves=\t\t\t\t1 cup\nCoriander Leaves=\t\t\t\t%d"%ch+" cup\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
                              " spoon\nTej Patta=\t\t\t\t2 piece\nGreen Chilli=\t\t\t\t%d"%ch+
                              " piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                              " spoon\nBiryani Masala=\t\t\t\t1 packet\nDahi Raita=\t\t\t\t%d"%(ch*2)+" cup")
                                txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()

                        person_label=Label(f1,text="PERSON ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                        person_label.grid(row=6,column=0,padx=10,pady=10,sticky="w")

                        myprsn=IntVar()
                        prsn_option=[1,2,3,4,5,6,7,8,9,10]
                        prsn_cmbx = ttk.Combobox(f1,value=prsn_option,font=("times new roman",14,"bold"),textvariable=myprsn)
                        prsn_cmbx.grid(row=6,column=0,sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                    elif mydish.get() == 'Chicken Biryani':
                        def prsnclck():
                            ch = myprsn.get()
                            def ingrdnt():
                                txt = Text(f2)
                                txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< CHICKEN BIRYANI IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT, "Basmati Rice=\t\t\t\t%d"%(ch*2)+" cup\nLeg Piece Chicken=\t\t\t\t%d"%(ch*250)+" gm\nWater=\t\t\t\t%d"%(ch*6)+" cup\nOnion=\t\t\t\t%d"%(ch*2)+
                          " pieces\nOil=\t\t\t\t%d"%(ch*4)+" spoon\nYogurt(curd)=\t\t\t\t%d"%(ch*200)+" gm\nTomato Puree=\t\t\t\t%d"%(ch*6)+
                          " spoon\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+" spoon\nGhee=\t\t\t\t%d"%(ch*2)+" spoon\nSalt=\t\t\t\t%.2f"%(ch*3.25)+
                          " spoon\nCloves & Cardamom=\t\t\t\t8/9 pieces\nMint Leaves=\t\t\t\t1 cup\nCoriander Leaves=\t\t\t\t%d"%ch+" cup\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
                              " spoon\nTej Patta=\t\t\t\t2 piece\nGreen Chilli=\t\t\t\t%d"%ch+
                              " piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                              " spoon\nChicken Masala=\t\t\t\t%d"%ch+" spoon\nBiryani Masala=\t\t\t\t1 packet")
                                txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()

                        person_label=Label(f1,text="PERSON ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                        person_label.grid(row=6,column=0,padx=10,pady=10,sticky="w")

                        myprsn=IntVar()
                        prsn_option=[1,2,3,4,5,6,7,8,9,10]
                        prsn_cmbx = ttk.Combobox(f1,value=prsn_option,font=("times new roman",14,"bold"),textvariable=myprsn)
                        prsn_cmbx.grid(row=6,column=0,sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                    elif mydish.get() == 'Mutton Biryani':
                        def prsnclck():
                            ch = myprsn.get()
                            def ingrdnt():
                                txt = Text(f2)
                                txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< MUTTON BIRYANI IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT, "Basmati Rice=\t\t\t\t%d"%(ch*2)+" cup\nLarge Size Mutton=\t\t\t\t%d"%(ch*250)+" gm\nWater=\t\t\t\t%d"%(ch*6)+" cup\nOnion=\t\t\t\t%d"%(ch*2)+
                          " pieces\nOil=\t\t\t\t%d"%(ch*4)+" spoon\nYogurt(curd)=\t\t\t\t%d"%(ch*200)+" gm\nTomato Puree=\t\t\t\t%d"%(ch*6)+
                          " spoon\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+" spoon\nGhee=\t\t\t\t%d"%(ch*2)+" spoon\nSalt=\t\t\t\t%.2f"%(ch*3.25)+
                          " spoon\nCloves & Cardamom=\t\t\t\t8/9 pieces\nMint Leaves=\t\t\t\t1 cup\nCoriander Leaves=\t\t\t\t%d"%ch+" cup\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
                              " spoon\nTej Patta=\t\t\t\t2 piece\nGreen Chilli=\t\t\t\t%d"%ch+
                              " piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                              " spoon\nMeat Masala=\t\t\t\t%d"%ch+" spoon\nBiryani Masala=\t\t\t\t1 packet\nDahi Raita=\t\t\t\t%d"%(ch*2)+" cup")
                                txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()

                        person_label=Label(f1,text="PERSON ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                        person_label.grid(row=6,column=0,padx=10,pady=10,sticky="w")

                        myprsn=IntVar()
                        prsn_option=[1,2,3,4,5,6,7,8,9,10]
                        prsn_cmbx = ttk.Combobox(f1,value=prsn_option,font=("times new roman",14,"bold"),textvariable=myprsn)
                        prsn_cmbx.grid(row=6,column=0,sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)

                    elif mydish.get() == 'Prawn Biryani':
                        def prsnclck():
                            ch = myprsn.get()
                            def ingrdnt():
                                txt = Text(f2)
                                txt.insert(INSERT, "\t   WELCOME TO INGREDIENTS WORLD\n\n\n"
                                                           "================================================\n\n"
                                                           "  <<<< PRAWN BIRYANI IS NOW READY FOR YOU >>>>\n\n"
                                                           "================================================\n"
                                                           "INGREDIENTS\t\t\t\tQUANTITY\n"
                                                           "================================================\n")
                                txt.insert(INSERT, "Basmati Rice=\t\t\t\t%d"%(ch*2)+" cup\nBagda Prawn(Chingudi)=\t\t\t\t%d"%(ch*4)+" piece\nWater=\t\t\t\t%d"%(ch*6)+" cup\nOnion=\t\t\t\t%d"%(ch*2)+
                          " pieces\nOil=\t\t\t\t%d"%(ch*4)+" spoon\nYogurt(curd)=\t\t\t\t%d"%(ch*200)+" gm\nTomato Puree=\t\t\t\t%d"%(ch*6)+
                          " spoon\nGinger Garlic Paste=\t\t\t\t%.2f"%(ch*1.5)+" spoon\nGhee=\t\t\t\t%d"%(ch*2)+" spoon\nSalt=\t\t\t\t%.2f"%(ch*3.25)+
                          " spoon\nCloves & Cardamom=\t\t\t\t8/9 pieces\nMint Leaves=\t\t\t\t1 cup\nCoriander Leaves=\t\t\t\t%d"%ch+" cup\nKashmir Chilli Powder=\t\t\t\t%.2f"%(ch*0.5)+
                              " spoon\nTej Patta=\t\t\t\t2 piece\nGreen Chilli=\t\t\t\t%d"%ch+
                              " piece\nCoriander Powder=\t\t\t\t%d"%ch+ " spoon\nCumin Powder=\t\t\t\t%d"%ch+ " spoon\nGaram Masala=\t\t\t\t%d"%ch+
                              " spoon\nMeat Masala=\t\t\t\t%d"%ch+" spoon\nBiryani Masala=\t\t\t\t1 packet\nDahi Raita=\t\t\t\t%d"%(ch*2)+" cup")
                                txt.insert(END, "\n\n\n\t\tT H A N K   Y O U")
                                txt.pack()

                            ingrdnt()

                        person_label=Label(f1,text="PERSON ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                        person_label.grid(row=6,column=0,padx=10,pady=10,sticky="w")

                        myprsn=IntVar()
                        prsn_option=[1,2,3,4,5,6,7,8,9,10]
                        prsn_cmbx = ttk.Combobox(f1,value=prsn_option,font=("times new roman",14,"bold"),textvariable=myprsn)
                        prsn_cmbx.grid(row=6,column=0,sticky="e")

                        prsnbtn = Button(f5, bd=5, relief=GROOVE, text="SUBMIT", bg="cadetblue", fg="white",
                                                 width=10, font="arial 15 bold", command=prsnclck).grid(row=11, column=2, padx=15,
                                                                                                        pady=5, sticky=E)



                dishes_label=Label(f1,text="DISHES ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
                dishes_label.grid(row=4,column=0,padx=10,pady=10,sticky="w")

                mydish=StringVar()
                dishes_option=['Dahi Pakhala', 'Veg Biryani', 'Chicken Biryani', 'Mutton Biryani', 'Prawn Biryani']
                dishes_cmbx = ttk.Combobox(f1,value=dishes_option,font=("times new roman",14,"bold"),textvariable=mydish)
                dishes_cmbx.grid(row=4,column=0,sticky="e")

                dishbtn=ttk.Button(f1,text="NEXT",command=dishclck)
                dishbtn.grid(row=5,column=0,sticky="e")


        section_label=Label(f1,text="SECTION ",font=("times new roman",25,"bold"),bg=bg_clr, fg="yellow")
        section_label.grid(row=2,column=0,padx=10,pady=10,sticky="w")

        mysection=StringVar()
        sctn_option=['Basic Meals','Prime Dishes','Special Flavour']
        sctn_cmbx = ttk.Combobox(f1,value=sctn_option,font=("times new roman",14,"bold"),textvariable=mysection)
        sctn_cmbx.grid(row=2,column=0,sticky="e")

        sctn_btn = ttk.Button(f1, text="NEXT", command=secclck)
        sctn_btn.grid(row=3, column=0, sticky="e")

    startfun()


    clr_btn = Button(f5,bd=5,relief=GROOVE,text="CLEAR",bg="cadetblue",fg="white",padx=2,width=10,font="arial 15 bold",command=deleteall)\
        .grid(row=11,column=0,padx=15,pady=5,sticky=E)

deleteall()
root.mainloop()

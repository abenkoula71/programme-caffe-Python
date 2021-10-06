from tkinter import*
from tkinter import ttk
import sqlite3 
#---------------------------------------------------------------------------------------
bG="#fc7f03"
bg="#ffa500"
#---------------------------------------------------------------------------------------
#boisson chaud
btn1={'name':'CAPSULE  L`OR','prix_v':'120','bnf':'40','image':'1.png'}
btn2={'name':'CAPSULE'      ,'prix_v':'80' ,'bnf':'40','image':'2.png'}
btn3={'name':'MAXWELLE'     ,'prix_v':'50' ,'bnf':'30','image':'3.png'}
btn4={'name':'CAFE'         ,'prix_v':'40' ,'bnf':'20','image':'4.png'}
btn5={'name':'CAFE noisette','prix_v':'50' ,'bnf':'30','image':'5.png'}
btn6={'name':'t01 '         ,'prix_v':'50' ,'bnf':'30','image':'6.png'}
btn7={'name':'CAFE CREME '  ,'prix_v':'50' ,'bnf':'20','image':'7.png'}
btn8={'name':'CREME SEPARE' ,'prix_v':'70' ,'bnf':'30','image':'8.png'}
btn9={'name':'LAIT '        ,'prix_v':'40' ,'bnf':'20','image':'9.png'}
btn10={'name':'LAIT CHOCO'  ,'prix_v':'60' ,'bnf':'30','image':'10.png'}
btn11={'name':'TEA '        ,'prix_v':'40' ,'bnf':'20','image':'11.png'}
btn12={'name':'TEA LIPTON'  ,'prix_v':'50' ,'bnf':'25','image':'12.png'}
btn13={'name':' \t'         ,'prix_v':'\t' ,'bnf':'\t','image':'13.png'}
btn14={'name':' \t'         ,'prix_v':'\t' ,'bnf':'\t','image':'14.png'}
btn15={'name':' \t'         ,'prix_v':'\t' ,'bnf':'\t','image':'15.png'}
#---------------------------------------------------------------------------------------
#boisson nergetique
btn16={'name':'Red Star'    ,'prix_v':'70','bnf':'30','image':'16.png'}
btn17={'name':'TNT'         ,'prix_v':'70','bnf':'30','image':'17.png'}
btn18={'name':'Energie'     ,'prix_v':'80','bnf':'40','image':'18.png'}
btn19={'name':'Red Bull'    ,'prix_v':'290','bnf':'30','image':'19.png'}
btn20={'name':'Mozaia Parfum','prix_v':'50','bnf':'20','image':'20.png'}
btn21={'name':'Mozaia nature','prix_v':'40','bnf':'20','image':'21.png'}
btn22={'name':' Coca Centter','prix_v':'70','bnf':'20','image':'22.png'}
btn23={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'23.png'}
btn24={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'24.png'}
btn25={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'25.png'}
btn26={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'26.png'}
btn27={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'27.png'}
btn28={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'28.png'}
btn29={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'29.png'}
btn30={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'30.png'}
#---------------------------------------------------------------------------------------
#jus
btn31={'name':'Jus'         ,'prix_v':'70','bnf':'30','image':'31.png'}
btn32={'name':'Vita Jus'    ,'prix_v':'30','bnf':'10','image':'32.png'}
btn33={'name':'Eau PM'      ,'prix_v':'30','bnf':'15','image':'33.png'}
btn34={'name':'Eau GM'      ,'prix_v':'40','bnf':'15','image':'34.png'}
btn35={'name':'Tisane'      ,'prix_v':'40','bnf':'20','image':'35.png'}
btn36={'name':'Gingabir'    ,'prix_v':'40','bnf':'20','image':'36.png'}
btn37={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'37.png'}
btn38={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'38.png'}
btn39={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'39.png'}
btn40={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'40.png'}
btn41={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'41.png'}
btn42={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'42.png'}
btn43={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'43.png'}
btn44={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'44.png'}
btn45={'name':' \t'         ,'prix_v':'\t','bnf':'\t','image':'45.png'}
#---------------------------------------------------------------------------------------
#gateaux
btn46={'name':'Gateaux'     ,'prix_v':'80','bnf':'30','image':'46.png'}
btn47={'name':'Croissant'   ,'prix_v':'20','bnf':'10','image':'47.png'}
btn48={'name':'Madelene'    ,'prix_v':'50','bnf':'10','image':'48.png'}
btn49={'name':'donattes'    ,'prix_v':'50','bnf':'20','image':'49.png'}
btn50={'name':'Matlou3+N'   ,'prix_v':'130','bnf':'50','image':'50.png'}
btn51={'name':'Matlou3+Fromg','prix_v':'100','bnf':'40','image':'51.png'}
btn52={'name':'Matlou3+conf','prix_v':'100','bnf':'40','image':'52.png'}
btn53={'name':'Matlou3+F+T' ,'prix_v':'170','bnf':'70','image':'53.png'}
btn54={'name':'pizza'       ,'prix_v':'60','bnf':'30','image':'54.png'}
btn55={'name':'Kaoukaou'    ,'prix_v':'100','bnf':'50','image':'55.png'}
btn56={'name':'pistache'    ,'prix_v':'350','bnf':'100','image':'56.png'}
btn57={'name':'louz'        ,'prix_v':'300','bnf':'80','image':'57.png'}
btn58={'name':'bessboussa'  ,'prix_v':'50','bnf':'20','image':'58.png'}
btn59={'name':'millefeuille','prix_v':'50','bnf':'25','image':'59.png'}
btn60={'name':'Divers'      ,'prix_v':'10','bnf':'5','image':'60.png'}
#---------------------------------------------------------------------------------------
def btnclick (num):
    global operator
    if num != "":
        operator+=str("+")
        operator = operator + str (num) 
    text_Input . set(num)
#---------------------------------------------------------------------------------------
def bnfs (num):
    global bnif
    if num != "":
        bnif+=str("+")
        bnif = bnif + str (num)
#---------------------------------------------------------------------------------------
def affiche_name(p,n,b):
    bnfs(b)
    btnclick(p)
    conn=sqlite3.connect('c.db')
    cur=conn.cursor()
    cur.execute("insert into datac ( `name` , `prix` , `bnf` ) values(?,?,?)", ( n , p , b ))
    conn.commit()
    conn.close()

    conn=sqlite3.connect('c.db')
    cur=conn.cursor()
    select=cur.execute("select*from datac order by id desc")
    select=list(select)
    tree.insert('',END,values=select[0])
    conn.close()  
#---------------------------------------------------------------------------------------
def btncleardisplay():
    global operator
    global bnif
    operator=""
    bnif=""
    delete_old()
    tree.delete(*tree.get_children())
#---------------------------------------------------------------------------------------
def brnequalsinput():
    global operator
    global bnif
    global total_bnf
    global to
    sumup=str(eval(operator)) 
    operator=""
    s=str(eval(bnif)) 
    total_bnf+=str("+")
    total_bnf+=s
    to=str(eval(total_bnf))
    bnif=""
    t=time()
    # Go to data base
    total(sumup,s,t)
    text_Input.set(sumup)
    delete_old()

    return sumup    
#---------------------------------------------------------------------------------------
def time():
    import time
    mytime = time.localtime()
    resultTime=time.strftime("%d/%m/%Y ,%H:%M:%S",mytime)
    return resultTime
#---------------------------------------------------------------------------------------
def btnclick_name (name):
    global operator
    #boisson chaud
    if name== "boisson chaud":
        #button saf1
        
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo1,text=btn1['name']+"\n \n"+btn1['prix_v']+"DA",command=lambda:affiche_name(btn1['prix_v'],btn1['name'],btn1['bnf']),width=160,height=110,bg=bG).place(x=400,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo2,text=btn2['name']+"\n \n"+btn2['prix_v']+"DA",command=lambda:affiche_name(btn2['prix_v'],btn2['name'],btn2['bnf']),width=160,height=110,bg=bG).place(x=570,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo3,text=btn3['name']+"\n \n"+btn3['prix_v']+"DA",command=lambda:affiche_name(btn3['prix_v'],btn3['name'],btn3['bnf']),width=160,height=110,bg=bG).place(x=740,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo4,text=btn4['name']+"\n \n"+btn4['prix_v']+"DA",command=lambda:affiche_name(btn4['prix_v'],btn4['name'],btn4['bnf']),width=160,height=110,bg=bG).place(x=910,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),image="",text=btn5['name']+"\n \n"+btn5['prix_v']+"DA",command=lambda:affiche_name(btn5['prix_v'],btn5['name'],btn5['bnf']),width=12,height=4,bg=bG).place(x=1080,y=100)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),image="",text=btn6['name']+"\n \n"+btn6['prix_v']+"DA",command=lambda:affiche_name(btn6['prix_v'],btn6['name'],btn6['bnf']),width=12,height=4,bg=bG).place(x=400,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo7,text=btn7['name']+"\n \n"+btn7['prix_v']+"DA",command=lambda:affiche_name(btn7['prix_v'],btn7['name'],btn7['bnf']),width=160,height=110,bg=bG).place(x=570,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo8,text=btn8['name']+"\n \n"+btn8['prix_v']+"DA",command=lambda:affiche_name(btn8['prix_v'],btn8['name'],btn8['bnf']),width=160,height=110,bg=bG).place(x=740,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo9,text=btn9['name']+"\n \n"+btn9['prix_v']+"DA",command=lambda:affiche_name(btn9['prix_v'],btn9['name'],btn9['bnf']),width=160,height=110,bg=bG).place(x=910,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo10,text=btn10['name']+"\n \n"+btn10['prix_v']+"DA",command=lambda:affiche_name(btn10['prix_v'],btn10['name'],btn10['bnf']),width=160,height=110,bg=bG).place(x=1080,y=220)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo11,text=btn11['name']+"\n \n"+btn11['prix_v']+"DA",command=lambda:affiche_name(btn11['prix_v'],btn11['name'],btn11['bnf']),width=160,height=110,bg=bG).place(x=400,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),image=photo12,text=btn12['name']+"\n \n"+btn12['prix_v']+"DA",command=lambda:affiche_name(btn12['prix_v'],btn12['name'],btn12['bnf']),width=160,height=110,bg=bG).place(x=570,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),image="",text=btn13['name']+"\n \n"+btn13['prix_v']+"DA",command=lambda:affiche_name(btn13['prix_v'],btn13['name'],btn13['bnf']),width=12,height=4,bg=bG).place(x=740,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),image="",text=btn14['name']+"\n \n"+btn14['prix_v']+"DA",command=lambda:affiche_name(btn14['prix_v'],btn14['name'],btn14['bnf']),width=12,height=4,bg=bG).place(x=910,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),image="",text=btn15['name']+"\n \n"+btn15['prix_v']+"DA",command=lambda:affiche_name(btn15['prix_v'],btn15['name'],btn15['bnf']),width=12,height=4,bg=bG).place(x=1080,y=340)
    #boisson energetiques
    elif name== "boisson energetiques":
        
        #button saf1
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn16['name']+"\n \n"+btn16['prix_v']+"DA",command=lambda:affiche_name(btn16['prix_v'],btn16['name'],btn16['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn17['name']+"\n \n"+btn17['prix_v']+"DA",command=lambda:affiche_name(btn17['prix_v'],btn17['name'],btn17['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn18['name']+"\n \n"+btn18['prix_v']+"DA",command=lambda:affiche_name(btn18['prix_v'],btn18['name'],btn18['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn19['name']+"\n \n"+btn19['prix_v']+"DA",command=lambda:affiche_name(btn19['prix_v'],btn19['name'],btn19['bnf']),image=photo19,width=160,height=110,bg=bG).place(x=910,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn20['name']+"\n \n"+btn20['prix_v']+"DA",command=lambda:affiche_name(btn20['prix_v'],btn20['name'],btn20['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=100)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn21['name']+"\n \n"+btn21['prix_v']+"DA",command=lambda:affiche_name(btn21['prix_v'],btn21['name'],btn21['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn22['name']+"\n \n"+btn22['prix_v']+"DA",command=lambda:affiche_name(btn22['prix_v'],btn22['name'],btn22['bnf']),image=photo22,width=160,height=110,bg=bG).place(x=570,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn23['name']+"\n \n"+btn23['prix_v']+"DA",command=lambda:affiche_name(btn23['prix_v'],btn23['name'],btn23['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn24['name']+"\n \n"+btn24['prix_v']+"DA",command=lambda:affiche_name(btn24['prix_v'],btn24['name'],btn24['bnf']),image="",width=12,height=4,bg=bG).place(x=910,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn25['name']+"\n \n"+btn25['prix_v']+"DA",command=lambda:affiche_name(btn25['prix_v'],btn25['name'],btn25['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=220)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn26['name']+"\n \n"+btn26['prix_v']+"DA",command=lambda:affiche_name(btn26['prix_v'],btn26['name'],btn26['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn27['name']+"\n \n"+btn27['prix_v']+"DA",command=lambda:affiche_name(btn27['prix_v'],btn27['name'],btn27['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn28['name']+"\n \n"+btn28['prix_v']+"DA",command=lambda:affiche_name(btn28['prix_v'],btn28['name'],btn28['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn29['name']+"\n \n"+btn29['prix_v']+"DA",command=lambda:affiche_name(btn29['prix_v'],btn29['name'],btn29['bnf']),image="",width=12,height=4,bg=bG).place(x=910,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn30['name']+"\n \n"+btn30['prix_v']+"DA",command=lambda:affiche_name(btn30['prix_v'],btn30['name'],btn30['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=340)
    #jue
    elif name== "jus":
        
        #button saf1
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn31['name']+"\n \n"+btn31['prix_v']+"DA",command=lambda:affiche_name(btn31['prix_v'],btn31['name'],btn31['bnf']),image=photo31,width=160,height=110,bg=bG).place(x=400,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn32['name']+"\n \n"+btn32['prix_v']+"DA",command=lambda:affiche_name(btn32['prix_v'],btn32['name'],btn32['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn33['name']+"\n \n"+btn33['prix_v']+"DA",command=lambda:affiche_name(btn33['prix_v'],btn33['name'],btn33['bnf']),image=photo33,width=160,height=110,bg=bG).place(x=740,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn34['name']+"\n \n"+btn34['prix_v']+"DA",command=lambda:affiche_name(btn34['prix_v'],btn34['name'],btn34['bnf']),image=photo34,width=160,height=110,bg=bG).place(x=910,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn35['name']+"\n \n"+btn35['prix_v']+"DA",command=lambda:affiche_name(btn35['prix_v'],btn35['name'],btn35['bnf']),image=photo35,width=160,height=110,bg=bG).place(x=1080,y=100)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn36['name']+"\n \n"+btn36['prix_v']+"DA",command=lambda:affiche_name(btn36['prix_v'],btn36['name'],btn36['bnf']),image=photo36,width=160,height=110,bg=bG).place(x=400,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn37['name']+"\n \n"+btn37['prix_v']+"DA",command=lambda:affiche_name(btn37['prix_v'],btn37['name'],btn37['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn38['name']+"\n \n"+btn38['prix_v']+"DA",command=lambda:affiche_name(btn38['prix_v'],btn38['name'],btn38['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn39['name']+"\n \n"+btn39['prix_v']+"DA",command=lambda:affiche_name(btn39['prix_v'],btn39['name'],btn39['bnf']),image="",width=12,height=4,bg=bG).place(x=910,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn40['name']+"\n \n"+btn40['prix_v']+"DA",command=lambda:affiche_name(btn40['prix_v'],btn40['name'],btn40['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=220)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn41['name']+"\n \n"+btn41['prix_v']+"DA",command=lambda:affiche_name(btn41['prix_v'],btn41['name'],btn41['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn42['name']+"\n \n"+btn42['prix_v']+"DA",command=lambda:affiche_name(btn42['prix_v'],btn42['name'],btn42['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn43['name']+"\n \n"+btn43['prix_v']+"DA",command=lambda:affiche_name(btn43['prix_v'],btn43['name'],btn43['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn44['name']+"\n \n"+btn44['prix_v']+"DA",command=lambda:affiche_name(btn44['prix_v'],btn44['name'],btn44['bnf']),image="",width=12,height=4,bg=bG).place(x=910,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn45['name']+"\n \n"+btn45['prix_v']+"DA",command=lambda:affiche_name(btn45['prix_v'],btn45['name'],btn45['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=340)
    #gateaux
    elif name== "gateaux":
        
        #button saf1
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn46['name']+"\n \n"+btn46['prix_v']+"DA",command=lambda:affiche_name(btn46['prix_v'],btn46['name'],btn46['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn47['name']+"\n \n"+btn47['prix_v']+"DA",command=lambda:affiche_name(btn47['prix_v'],btn47['name'],btn47['bnf']),image=photo47,width=160,height=110,bg=bG).place(x=570,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn48['name']+"\n \n"+btn48['prix_v']+"DA",command=lambda:affiche_name(btn48['prix_v'],btn48['name'],btn48['bnf']),image=photo48,width=160,height=110,bg=bG).place(x=740,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn49['name']+"\n \n"+btn49['prix_v']+"DA",command=lambda:affiche_name(btn49['prix_v'],btn49['name'],btn49['bnf']),image=photo49,width=160,height=110,bg=bG).place(x=910,y=100)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn50['name']+"\n \n"+btn50['prix_v']+"DA",command=lambda:affiche_name(btn50['prix_v'],btn50['name'],btn50['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=100)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn51['name']+"\n \n"+btn51['prix_v']+"DA",command=lambda:affiche_name(btn51['prix_v'],btn51['name'],btn51['bnf']),image="",width=12,height=4,bg=bG).place(x=400,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn52['name']+"\n \n"+btn52['prix_v']+"DA",command=lambda:affiche_name(btn52['prix_v'],btn52['name'],btn52['bnf']),image="",width=12,height=4,bg=bG).place(x=570,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn53['name']+"\n \n"+btn53['prix_v']+"DA",command=lambda:affiche_name(btn53['prix_v'],btn53['name'],btn53['bnf']),image="",width=12,height=4,bg=bG).place(x=740,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn54['name']+"\n \n"+btn54['prix_v']+"DA",command=lambda:affiche_name(btn54['prix_v'],btn54['name'],btn54['bnf']),image=photo54,width=160,height=110,bg=bG).place(x=910,y=220)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn55['name']+"\n \n"+btn55['prix_v']+"DA",command=lambda:affiche_name(btn55['prix_v'],btn55['name'],btn55['bnf']),image=photo55,width=160,height=110,bg=bG).place(x=1080,y=220)

        #button saf2
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn56['name']+"\n \n"+btn56['prix_v']+"DA",command=lambda:affiche_name(btn56['prix_v'],btn56['name'],btn56['bnf']),image=photo56,width=160,height=110,bg=bG).place(x=400,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn57['name']+"\n \n"+btn57['prix_v']+"DA",command=lambda:affiche_name(btn57['prix_v'],btn57['name'],btn57['bnf']),image=photo57,width=160,height=110,bg=bG).place(x=570,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn58['name']+"\n \n"+btn58['prix_v']+"DA",command=lambda:affiche_name(btn58['prix_v'],btn58['name'],btn58['bnf']),image=photo58,width=160,height=110,bg=bG).place(x=740,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn59['name']+"\n \n"+btn59['prix_v']+"DA",command=lambda:affiche_name(btn59['prix_v'],btn59['name'],btn59['bnf']),image=photo59,width=160,height=110,bg=bG).place(x=910,y=340)
        Button(cal,fg="black",font=('arial',16,'bold'),text=btn60['name']+"\n \n"+btn60['prix_v']+"DA",command=lambda:affiche_name(btn60['prix_v'],btn60['name'],btn60['bnf']),image="",width=12,height=4,bg=bG).place(x=1080,y=340)
#---------------------------------------------------------------------------------------
def boss():
    global call
    ca = Toplevel(cal)
    ca.title("register")
    ca.geometry("300x250")
    Frame(ca,width=1500,height=1500,bg="#fc7f03").place(x=0,y=0)

    global umot
    global umot_b_entry
    umot = StringVar()
    Label(ca,text="mote passe :",font=(20),bg="#fc7f03").place(x=100,y=10)
    umot_b_entry=Entry(ca,textvariable=umot,font=(20))
    umot_b_entry.place(x=40,y=50)
    Label(ca,text=" ")
    Button(ca,text="ok",width=10,command=boss_mot).place(x=110,y=200)
#---------------------------------------------------------------------------------------
def total(total1,total2,time):
        
        db=sqlite3.connect("dat.db")
        cr = db.cursor()
        #ta3 li yjo 3andak
        cr.execute("create table if not exists dat (PRIX_V text,BNF text,time text)")
        cr.execute(f"insert into dat  ( PRIX_V , BNF , time  ) values('{total1} DA','{total2} DA','{time}')")
        db.commit()
        db.close()   
#---------------------------------------------------------------------------------------     
def bnf(total,date):
    db=sqlite3.connect("datat.db")
    cr = db.cursor()
    #ta3 li yjo 3andak
    cr.execute("insert into dat ( `bnf_total_j` ,`date` ) values(?,?)", ( total, date ))
    db.commit()
    db.close()
#---------------------------------------------------------------------------------------
def boss_mot():
    mot_b_info = umot.get()
    msg=mot_boss(mot_b_info)
    umot_b_entry.delete(0,END)
    Label (call,text=msg,fg="red",font=("calibri",15),bg="#1154f8").place(x=35,y=100)
#---------------------------------------------------------------------------------------
def mot_boss (motpasse):
    if motpasse == 'Harrag2021' :
        call = Toplevel(cal)
        call.title("register")
        call.geometry("300x250")
        Frame(call,width=1500,height=1500,bg=bG).place(x=0,y=0)
        Button(call,fg="black",font=(10),bg="#909930",text="data 1",command=boss_info1,width=20,height=3).place(x=35,y=10)
        Button(call,fg="black",font=(10),bg="#999930",text="data 2",command=boss_info2,width=20,height=3).place(x=35,y=120)
#---------------------------------------------------------------------------------------
def boss_info1 ():
    global call
    global t1
    call = Toplevel(cal)
    call.title("register")
    call.geometry("500x500")
    t1= ttk.Treeview(call,columns=(1,2,3),height = 5,show="headings")
    t1.place(width=500,height=400)

    t1.heading(1,text="prix")
    t1.heading(2,text="bnf")
    t1.heading(3,text="time")
    

    t1.column(1,width=80)
    t1.column(2,width=80)
    t1.column(3,width=150)

    import sqlite3
    conn=sqlite3.connect("dat.db")
    cur = conn.cursor()
    select = cur.execute("select*from dat")
    for row in select:
        t1.insert('',END,value=row)
    conn.close()
    Button(call,fg="black",font=('arial',15),text="cansel old",command=delete_old1,width=10).place(x=200,y=430)
#---------------------------------------------------------------------------------------
def boss_info2 ():
    global call
    call = Toplevel(cal)
    call.title("register")
    call.geometry("500x500")
    t2 = ttk.Treeview(call,columns=(1,2),height = 5,show="headings")
    t2.place(width=500,height=400)

    t2.heading(1,text="bnf_total_j")
    t2.heading(2,text="date")

    t2.column(1,width=200)
    t2.column(2,width=300)

    import sqlite3
    conn=sqlite3.connect("datat.db")
    cur = conn.cursor()
    select = cur.execute("select*from dat")
    for row in select:
        t2.insert('',END,value=row)
    conn.close()
    Button(call,fg="black",font=('arial',15),text="cansel old",command=delete_old2,width=10).place(x=200,y=430)
#---------------------------------------------------------------------------------------
def delete_customer ():
    idselect=tree.item(tree.selection())['values'][2]
    btnclick(-(tree.item(tree.selection())['values'][1]))
    bnfs(-(tree.item(tree.selection())['values'][3]))
    
    conn=sqlite3.connect('c.db')
    cur=conn.cursor()
    delete = cur.execute("delete from datac where id = {}".format(idselect))
    conn.commit()
    tree.delete(tree.selection())
#---------------------------------------------------------------------------------------
def delete_old ():
    i=0
    while(i<60):
        conn=sqlite3.connect('c.db')
        cur=conn.cursor()
        delete = cur.execute("delete from datac where id = {}".format(i))
        conn.commit()
        i+=1   
def delete_old1 ():
    i=0
    while(i<60):
        conn=sqlite3.connect('dat.db')
        cur=conn.cursor()
        cur.execute("delete from dat where id = {}".format(i))
        conn.commit()
        i+=1  
#---------------------------------------------------------------------------------------
def delete_old2 ():
    i=0
    while(i<60):
        conn=sqlite3.connect('datat.db')
        cur=conn.cursor()
        cur.execute("delete from dat where id = {}".format(i))
        conn.commit()
        i+=1  
#---------------------------------------------------------------------------------------
def next():

    delete_old()
    btncleardisplay()
    tree.delete(*tree.get_children())
#---------------------------------------------------------------------------------------
def date():
    import time
    mytime = time.localtime()
    resultTime=time.strftime("%d/%m/%Y",mytime)
    return resultTime
#---------------------------------------------------------------------------------------
def q():
    t=date()
    global to
    bnf(to,t)
    return quit()
#---------------------------------------------------------------------------------------
cal=Tk()
cal.title("caffee brown")
cal.geometry("1100x630")
#---------------------------------------------------------------------------------------
#les photo
#---------------------------------------------------------------------------------------
#boisson chaud
photo1= PhotoImage(file =btn1['image'])
photo2 = PhotoImage(file =btn2['image'])
photo3 = PhotoImage(file =btn3['image'])
photo4 = PhotoImage(file =btn4['image'])
#photo5 = PhotoImage(file =btn5['image'])
#photo6 = PhotoImage(file =btn6['image'])
photo7 = PhotoImage(file =btn7['image'])
photo8 = PhotoImage(file =btn8['image'])
photo9 = PhotoImage(file =btn9['image'])
photo10 = PhotoImage(file =btn10['image'])
photo11 = PhotoImage(file =btn11['image'])
photo12 = PhotoImage(file =btn12['image'])
#photo13 = PhotoImage(file =btn13['image'])
#photo14 = PhotoImage(file =btn14['image'])
#photo15 = PhotoImage(file =btn15['image'])
#---------------------------------------------------------------------------------------
#boisson nergetique
#photo16 = PhotoImage(file =btn16['image'])
#photo17 = PhotoImage(file =btn17['image'])
#photo18 = PhotoImage(file =btn18['image'])
photo19 = PhotoImage(file =btn19['image'])
#photo20 = PhotoImage(file =btn20['image'])
#photo21 = PhotoImage(file =btn21['image'])
photo22 = PhotoImage(file =btn22['image'])
#photo23 = PhotoImage(file =btn23['image'])
#photo24 = PhotoImage(file =btn24['image'])
#photo25 = PhotoImage(file =btn25['image'])
#photo26 = PhotoImage(file =btn26['image'])
#photo27 = PhotoImage(file =btn27['image'])
#photo28 = PhotoImage(file =btn28['image'])
#photo29 = PhotoImage(file =btn29['image'])
#photo30 = PhotoImage(file =btn30['image'])
#---------------------------------------------------------------------------------------
#jus
photo31 = PhotoImage(file =btn31['image'])
#photo32 = PhotoImage(file =btn32['image'])
photo33 = PhotoImage(file =btn33['image'])
photo34 = PhotoImage(file =btn34['image'])
photo35 = PhotoImage(file =btn35['image'])
photo36 = PhotoImage(file =btn36['image'])
#photo37 = PhotoImage(file =btn37['image'])
#photo38 = PhotoImage(file =btn38['image'])
#photo39 = PhotoImage(file =btn39['image'])
#photo40 = PhotoImage(file =btn40['image'])
#photo41 = PhotoImage(file =btn41['image'])
#photo42 = PhotoImage(file =btn42['image'])
#photo43 = PhotoImage(file =btn43['image'])
#photo44 = PhotoImage(file =btn44['image'])
#photo45 = PhotoImage(file =btn45['image'])
#---------------------------------------------------------------------------------------
#gateaux
#photo46 = PhotoImage(file =btn46['image'])
photo47 = PhotoImage(file =btn47['image'])
photo48 = PhotoImage(file =btn48['image'])
photo49 = PhotoImage(file =btn49['image'])
#photo50 = PhotoImage(file =btn50['image'])
#photo51 = PhotoImage(file =btn51['image'])
#photo52 = PhotoImage(file =btn52['image'])
#photo53 = PhotoImage(file =btn53['image'])
photo54 = PhotoImage(file =btn54['image'])
photo55 = PhotoImage(file =btn55['image'])
photo56 = PhotoImage(file =btn56['image'])
photo57 = PhotoImage(file =btn57['image'])
photo58 = PhotoImage(file =btn58['image'])
photo59 = PhotoImage(file =btn59['image'])
#photo60 = PhotoImage(file =btn60['image'])
#---------------------------------------------------------------------------------------
#disign
Frame(cal,width=1500,height=1500,bg="#010101").place(x=0,y=0)
#---------------------------------------------------------------------------------------
Button(cal,fg="black",font=('arial',16,'bold'),text="boisson\nchaud",width=8,height=2,command=lambda:btnclick_name("boisson chaud"),bg=bg).place(x=400,y=15)
Button(cal,fg="black",font=('arial',16,'bold'),text="boisson\nenergetiques",width=8,command=lambda:btnclick_name("boisson energetiques"),bg=bg).place(x=520,y=15)
Button(cal,fg="black",font=('arial',16,'bold'),text="JUS",width=8,height=2,command=lambda:btnclick_name("jus"),bg=bg).place(x=640,y=15)
Button(cal,fg="black",font=('arial',16,'bold'),text="GATEAUX",width=8,height=2,command=lambda:btnclick_name("gateaux"),bg=bg).place(x=760,y=15)
#---------------------------------------------------------------------------------------
#code for name fo salon
to=""
total_bnf=""
operator=""
bnif=""
bnf_j=""
text_Input=StringVar()
#---------------------------------------------------------------------------------------
Label(text="caffee brown",fg="white",bg = "#906030",font = ("calibri",30),width=13,height=1).place(x=1000,y=20)
# code for button of boss
#---------------------------------------------------------------------------------------
btn_for_bosse=Button(cal,fg="white",font=("calibri",10),bg="#906000",text="FOR BOSS",command=boss).place(x=10,y=10)
#---------------------------------------------------------------------------------------
cansle_old=Button(cal,fg="black",font=('arial',15),text="cansel old",command=btncleardisplay,width=10).place(x=10,y=520)
delete_one=Button(cal,fg="black",font=('arial',15),text="cansel",command=delete_customer,width=10).place(x=10,y=565)
sv=Button(cal,fg="black",font=('arial',15),text="sv",command=brnequalsinput,width=10).place(x=10,y=610)
#---------------------------------------------------------------------------------------
nextt=Button(cal,fg="black",font=('arial',15),text="NEXT",command=next,width=10).place(x=140,y=520)
vide=Button(cal,fg="black",font=('arial',15),text="\t",command="",width=10).place(x=140,y=565)
exit=Button(cal,fg="black",font=('arial',15),text="EXIT",command=q,width=10).place(x=140,y=610)
#---------------------------------------------------------------------------------------
Label(text="TOTAL:",font = ("calibri",40),bg="yellow").place(x=450,y=560)
txtDisplay=Entry(cal,font=('arial',30,'bold'),textvariable=text_Input,bd=20,insertwidth=4,justify="right").place(x=650,y=550)
Label(text="DA",font = ("calibri",40),bg="#303060",fg="white").place(x=1150,y=560)
#---------------------------------------------------------------------------------------
tree = ttk.Treeview(cal,columns=(1,2),height=5,show="headings")
tree.place(x=10,y=90,width=290,height=390)
#---------------------------------------------------------------------------------------
tree.heading(1,text="name")
tree.heading(2,text="prix")
#---------------------------------------------------------------------------------------
tree.column(1,width=130)
tree.column(2,width=50)
#---------------------------------------------------------------------------------------
cal.mainloop()
import random,sys,time,math,tkinter as tk
def det1():
        global b
        a.destroy()
        b=tk.Tk()
        b.geometry('750x800')
        b.title('Sign in')
        b.configure(bg='Yellow')
        l6=tk.Label(b,text='Welcome to Signup',font=('Verdana',20),bg='Yellow')
        l6.place(x=200,y=0)
        l7=tk.Label(b,text='Enter your name:',font=('Verdana',12),bg='Yellow')
        l7.place(x=0,y=40)
        l8=tk.Entry(width=30,font=('Verdana',12),textvariable='')
        l8.place(x=350,y=40)
        l9=tk.Label(b,text='Enter your email(gmail/yahoo/outlook):',font=('Verdana',12),bg='Yellow')
        l9.place(x=0,y=80)
        l10=tk.Entry(width=30,font=('Verdana',12),textvariable='')
        l10.place(x=350,y=80)
        l11=tk.Label(b,text='Enter your phone no :',font=('Verdana',12),bg='Yellow')
        l11.place(x=0,y=120)
        l12=tk.Entry(width=30,font=('Verdana',12),textvariable='')
        l12.place(x=350,y=120)
        l13=tk.Label(b,text='Enter a password in digits:',font=('Verdana',12),bg='Yellow')
        l13.place(x=0,y=160)
        l14=tk.Entry(width=30,font=('Verdana',12),show="*",textvariable='')
        l14.place(x=350,y=160)
        l15=tk.Label(b,text='Confirm the password:',font=('Verdana',12),bg='Yellow')
        l15.place(x=0,y=200)
        l16=tk.Entry(width=30,font=('Verdana',12),show="*",textvariable='')
        l16.place(x=350,y=200)
        l17=tk.Button(b,text='SUBMIT',font=('Verdana',16),bg='Red')
        l17.place(x=275,y=250)
        l17['command']=lambda:det2(l14.get(),l16.get(),l8.get(),l10.get(),l12.get())
        l20=tk.Button(b,text='   Back    ',font=('Verdana',16),command=lambda:intropg(b),bg='Red')
        l20.place(x=75,y=250)
        l5=tk.Button(b,text='  Exit    ',font=('Verdana',16),command=lambda:detd(b),bg=('Red'))
        l5.place(x=425,y=250)
def det2(x,y,ina,ie,ip):
        global curemail
        f21=open("C:\\Users\\vehrp\\Documents\\emsave.txt","r")
        rlines=f21.readlines()
        em2=('{}').format(ie)+"\n"
        if em2 not in rlines:
                if ina!='' and ie!='' and ip!='' and x!='' and y!='' and ip.isdigit()==True and len(str(ip))==10:
                        if '@gmail.com' in ie or '@yahoo.com' in ie or '@outlook.com'in ie:
                                if x==y:
                                        global c,newl
                                        em=('{}'+"\n").format(ie)
                                        curemail=em.rstrip("\n")
                                        f2.write(em)
                                        f2.close()
                                        s=("Email:'{}',Password:{}\n").format(ie,x)
                                        f.write(s)
                                        b.destroy()
                                        c=tk.Tk()
                                        c.geometry('300x400')
                                        c.title('Welcome to the Test')
                                        c.configure(bg='Gold')
                                        l18=tk.Button(c,text='Start the game',font=('Verdana',16),command=lambda:det5(c),bg='Orange')
                                        l18.place(x=75,y=50)
                                        l19=tk.Button(c,text='   Instruction    ',font=('Verdana',16),command=det3,bg='Orange')
                                        l19.place(x=75,y=100)
                                        l20=tk.Button(c,text='   Back    ',font=('Verdana',16),command=lambda:intropg(c),bg='Orange')
                                        l20.place(x=75,y=150)
                                        l5=tk.Button(c,text='  Exit    ',font=('Verdana',16),command=lambda:detd(c),bg=('Orange'))
                                        l5.place(x=75,y=200)
                                        f.close()
                                else:
                                        lu=tk.Label(b,text='Signup unsuccessful',font=('Verdana',16,'bold'),bg='Yellow')
                                        lu.place(x=325,y=300)
                                        lu1=tk.Label(b,text='Please Confirm password corectly',font=('Verdana',16,'bold'),bg='Yellow')
                                        lu1.place(x=250,y=345)
                        else:
                                lu=tk.Label(b,text=' Invalid Email ',font=('Verdana',16,'bold'),bg='Yellow')
                                lu.place(x=250,y=345)
                                lu=tk.Label(b,text='Signup unsuccessful',font=('Verdana',16,'bold'),bg='Yellow')
                                lu.place(x=250,y=300)
                else:
                        lu=tk.Label(b,text='Signup unsuccessful',font=('Verdana',16,'bold'),bg='Yellow')
                        lu.place(x=325,y=300)
                        lu=tk.Label(b,text='Please check mail (or)',font=('Verdana',16,'bold'),bg='Yellow')
                        lu.place(x=250,y=400)
                        lu=tk.Label(b,text='Phone number (or)',font=('Verdana',16,'bold'),bg='Yellow')
                        lu.place(x=250,y=450)
                        lu=tk.Label(b,text='Check whether everything is filled correctly',font=('Verdana',16,'bold'),bg='Yellow')
                        lu.place(x=150,y=500)
        else:
                lu=tk.Label(b,text='Email already exists, move to login',font=('Verdana',16,'bold'),bg='Yellow')
                lu.place(x=325,y=300)
def det3():
        global d
        d=tk.Tk()
        d.title('Instructions')
        d.geometry('1250x350')
        d.configure(bg='Gold')
        li1=tk.Label(d,text='Instructions',font=('Verdana',20),bg='Gold')
        li1.place(x=325,y=0)
        li2=tk.Label(d,text='1. A random sentence will be displayed on the screen when you start the game .',font=('Verdana',12),bg='Gold')
        li2.place(x=0,y=50)
        li3=tk.Label(d,text='2. Under the sentence , a dialog box will appear in which you must type the sentence above.',font=('Verdana',12),bg='Gold')
        li3.place(x=0,y=90)
        li4=tk.Label(d,text='3. When you finish and click on the submit button , your accuracy , wpm(words per minute)and the time you have taken will be displayed.',font=('Verdana',12),bg='Gold')
        li4.place(x=0,y=130)
        li5=tk.Label(d,text='4. After finishing you can either exit or reset the game again.',font=('Verdana',12),bg='Gold')
        li5.place(x=0,y=170)
        li5=tk.Label(d,text=' ALL THE BEST!!!!!',font=('Verdana',12),bg='Gold')
        li5.place(x=350,y=210)
        li6=tk.Button(d,text='Back',font=('Verdana',16),command=det4,bg='Red')
        li6.place(x=300,y=250)
        l5=tk.Button(d,text='  Exit    ',font=('Verdana',16),command=lambda:detd(d),bg=('Red'))
        l5.place(x=400,y=250)
def det4():
        d.destroy()
def det5(w):
        w.destroy()
        global e,t1
        e=tk.Tk()
        e.title('Test')
        e.geometry('1000x500')
        e.configure(bg='Orange')
        t1=time.time()
        k=det6()
        string=k
        ch=len(string.split())
        l20=tk.Label(e,text=k,font=('Verdana',16),bg='Yellow')
        l20.place(x=315,y=130)
        l21=tk.Entry(e,width=40,font=('Verdana',16))
        l21.place(x=200,y=250)
        l22=tk.Button(e,text='SUBMIT',command=lambda:det7(l21.get(),k),font=('Verdana',14),bg='Red')
        l22.place(x=750,y=250)
def det6():
        caps=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        lower=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        sym=['{','}','[',']',':',';','\"','\'','<','>','?']
        capsmax=26
        lowermax=26
        symmax=11
        seq=['1','2','3']
        k=1
        sent=''
        dlist=[]
        while k!=17:
                choice=random.choice(seq)
                if choice=='1':
                        dlist.append(caps[random.randint(0,capsmax-1)])
                if choice=='2':
                        dlist.append(lower[random.randint(0,lowermax-1)])
                if choice=='3':
                        dlist.append(sym[random.randint(0,symmax-1)])
                k+=1
        spacechoice=random.choice([3,4,5])
        for m in range(spacechoice):
                pos=random.randint(1,len(dlist)-1)
                dlist.insert(pos,',')
        for m in range(dlist.count(',')):
                n=dlist.index(',')
                dlist.insert(n,'')
                dlist.remove(',')
        for j in dlist:
                sent=sent+j
        return sent
def det7(u,q):
        f3=open("C:\\Users\\vehrp\\Documents\\bestattempt.txt","a")
        len1=len(q)
        len2=len(u)
        count=0
        if len2>len1:
                for y in range(len1):
                        if u[y]==q[y]:
                                count+=1
                if len2>len1:
                        count-=len2-len1
        else:
                for y in range(len2):
                        if u[y]==q[y]:
                                count+=1
        acc=(count/len1)*100
        t2=time.time()
        tt=round(t2-t1,2)
        cps=round(len2/tt,3)
        newl=[curemail]
        newl1=[acc,tt]
        newl.append(newl1)
        f3.write(str(newl)+"\n")
        l23=tk.Label(e,text="Accuracy = %s "%str(acc)+"%",font=('Verdana',12),bg='Orange')
        l23.place(x=100,y=350)
        l24=tk.Label(e,text="Time taken=%s"%str(tt)+"s",font=('Verdana',12),bg='Orange')
        l24.place(x=300,y=350)
        l25=tk.Label(e,text="Characters per sec=%s"%str(cps),font=('Verdana',12),bg='Orange')
        l25.place(x=500,y=350)
        l26=tk.Button(e,text=" Try again ",font=("Verdana",16),command=lambda:det8(e),bg="Blue",fg="Light Blue")
        l26.place(x=250,y=400)
        l27=tk.Button(e,text='  Exit    ',font=('Verdana',16),command=detd1,bg="Blue",fg="Light Blue")
        l27.place(x=500,y=400)
        l28=tk.Button(e,text=" Back ",font=('Verdana',15),command=lambda:getback(e),bg="Blue",fg="Light Blue")
        l28.place(x=400,y=400)
        f3.close()
def det8(e):
        return det5(e)
def det9(temp1,temp2,f,g):
        global curemail
        alist=("Email:'{}',Password:{}\n").format(temp1,temp2)
        lines=f.readlines()
        if alist in lines:
                global win
                win=tk.Tk()
                win.title('Login success')
                win.geometry('300x400')
                win.configure(bg='Gold')
                mail=('{}'+"\n").format(temp1)
                curemail=mail.rstrip("\n")
                l20=tk.Button(win,text='   My attempts    ',font=('Verdana',16),command=myattempts,bg='Orange')
                l20.place(x=50,y=150)
                l21=tk.Button(win,text='   Start game   ',font=('Verdana',16),command=lambda:det5(win),bg='Orange')
                l21.place(x=50,y=50)
                l19=tk.Button(win,text='   Instruction    ',font=('Verdana',16),command=det3,bg='Orange')
                l19.place(x=50,y=100)
                l20=tk.Button(win,text='   Back    ',font=('Verdana',16),command=lambda:intropg(win),bg='Orange')
                l20.place(x=50,y=250)
                l5=tk.Button(win,text='  Exit    ',font=('Verdana',16),command=lambda:detd(win),bg=('Orange'))
                l5.place(x=50,y=300)
                l6=tk.Button(win,text=' Your score   ',font=('Verdana',16),command=score,bg=('Orange'))
                l6.place(x=50,y=200)
                f.close()
                g.destroy()
        else:
                global m1
                g.destroy()
                m1=tk.Tk()
                m1.geometry('650x500')
                m1.title('Login error')
                m1.configure(bg='Yellow')
                lu=tk.Label(m1,text='Login unsuccessful',font=('Verdana',16,'bold'),bg='Yellow')
                lu.place(x=100,y=100)
                lu2=tk.Button(m1,text='Relogin',font=('Verdana',16),command=lambda:relogin(m1),bg='Red')
                lu2.place(x=100,y=200)
                l20=tk.Button(m1,text='   Back    ',font=('Verdana',16),command=lambda:intropg(m1),bg='Red')
                l20.place(x=225,y=200)
                l5=tk.Button(m1,text='  Exit   ',font=('Verdana',16),command=lambda:detd(m1),bg=('Red'))
                l5.place(x=350,y=200)
def det10(a):
        a.destroy()
        g=tk.Tk()
        g.geometry('650x500')
        g.title('Log in')
        g.configure(bg='Yellow')
        ll=tk.Label(g,text='Welcome to Login',font=('Verdana',20),bg='Yellow')
        ll.place(x=200,y=0)
        email_var=tk.StringVar(g)
        passwd_var=tk.StringVar(g)
        f=open("C:\\Users\\vehrp\\Documents\\signup.txt","r")
        l28=tk.Label(g,text='Enter your email(gmail/yahoo/outlook):',font=('Verdana',12),bg='Yellow')
        l28.place(x=0,y=80)
        l29=tk.Entry(width=25,font=('Verdana',12),textvariable=email_var)
        l29.place(x=350,y=80)
        l30=tk.Label(g,text='Enter a password in digits:',font=('Verdana',12),bg='Yellow')
        l30.place(x=0,y=160)
        l31=tk.Entry(width=25,font=('Verdana',12),show="*",textvariable=passwd_var)
        l31.place(x=350,y=160)
        l32=tk.Button(g,text='SUBMIT',font=('Verdana',16),bg='Red',command=lambda:det9(email_var.get(),passwd_var.get(),f,g))
        l32.place(x=225,y=250)
        l33=tk.Button(g,text='Back',font=('Verdana',16),bg='Red',command=lambda:intropg(g))
        l33.place(x=75,y=250)
        l5=tk.Button(g,text='  Exit    ',font=('Verdana',16),command=lambda:detd(g),bg=('Red'))
        l5.place(x=375,y=250)
def det11(k):
        global h
        k.destroy()
        h=tk.Tk()
        h.title('Second Test')
        h.geometry('1300x500')
        h.configure(bg='Orange')
        sent=[]
        s1='''The computer as we know it today had its beginning with a professor name Charles Babbage.'''
        sent.append(s1)
        s2='''He designed the Analytical Engine which became the basic framework of the computers.'''
        sent.append(s2)
        s3='''Since ancient times, simple manual devices like the abacus aided people in doing calculations.'''
        sent.append(s3)
        s4='''Early computers were only conceived as calculating devices.'''
        sent.append(s4)
        s5='''Conventionally, a modern computer consists of at least one processingelement, typically a CPU.'''
        sent.append(s5)
        s6='''An application, or application program, is a software program that runs on your computer.'''
        sent.append(s6)
        s7='''System software consists of programs that run in the background, enabling applications to run.'''
        sent.append(s7)
        s8='''Applications are said to run on top of the system software, since it is made of of "low-level" programs.'''
        sent.append(s8)
        s9='''Computers are used at homes for several purposes like online bill payment, watching movies, etc.'''
        sent.append(s9)
        s10='''Computers are used in hospitals to maintain a database of patients’ history, diagnosis, and such.'''
        sent.append(s10)
        s11='''Python was created by Guido van Rossum and first released in 1991.'''
        sent.append(s11)
        s12='''Python was created in the late 1980s as a successor to the ABC language.'''
        sent.append(s12)
        s13='''Java is a class-based, object-oriented programming language.'''
        sent.append(s13)
        s14='''Java was originally developed by James Gosling at Sun Microsystems.'''
        sent.append(s14)
        s15='''Hub is a small network device.'''
        sent.append(s15)
        s16='''There are a number of systems which enable you to create networks.'''
        sent.append(s16)
        s17=''' Point to Point topology is the simplest topology that connects two nodes with a common link.'''
        sent.append(s17)
        s18=''' It joins multiple computers together to form a single network segment.'''
        sent.append(s18)
        s19='''When the network of computer is confined to a small or localised area,it is known as LAN.'''
        sent.append(s19)
        s20='''The network of computers which is spread across the countries is known as a WAN.'''
        sent.append(s20)
        s21='''In star topology, the server is directly connected with each and every node in the network via a hub.'''
        sent.append(s21)
        s22='''Modem is a device that converts digital signal to analog signal and vice versa.'''
        sent.append(s22)
        s23='''The switch is a hardware device used to divide the network into smaller subnets or LAN segments.'''
        sent.append(s23)
        s24='''The repeater is a hardware device used in a network to amplify the weak signals.'''
        sent.append(s24)
        s25='''Gateway establishes an intelligent connection between a local network and external networks.'''
        sent.append(s25)
        s26='''HTTP is widely used for viewing information of a web page over Internet.'''
        sent.append(s26)
        s27='''A denial of service attack refers to an attempt to make computer resources unavailable to users.'''
        sent.append(s27)
        s28='''The user is provided with a login-id and password by which they is considered to be an authentic user.'''
        sent.append(s28)
        s29='''A hacker is someone who seeks and exploits weaknesses in a computer system or network.'''
        sent.append(s29)
        s30='''A Worm can self replicate itself in the files to accumulate any data.'''
        sent.append(s30)
        rsent=random.choice(sent)
        l36=tk.Label(h,text=rsent,font=('Verdana',16),bg='Gold')
        l36.place(x=50,y=50)
        l37=tk.Entry(h,width=80,font=('Verdana',16))
        l37.place(x=5,y=150)
        l38=tk.Button(h,text='SUBMIT',font=('Verdana',16),command=lambda:det12(l37.get(),rsent),bg='Red')
        l38.place(x=20,y=200)
        l39=tk.Button(h,text='Retry',font=('Verdana',16),command=lambda:det11(h),bg='Red')
        l39.place(x=170,y=200)
        l5=tk.Button(h,text='  Exit    ',font=('Verdana',16),command=lambda:detd(h),bg=('Red'))
        l5.place(x=320,y=200)
        l33=tk.Button(h,text='Back',font=('Verdana',16),bg='Red',command=lambda:intropg(h))
        l33.place(x=470,y=200)
def det12(y,rsent):
        len3=len(rsent)
        len4=len(y)
        counts=0
        for i in range(len4):
                if y[i]==rsent[i]:
                        counts+=1
        acc=(counts/len3)*100
        if acc<25:
                l39=tk.Label(h,text='You have to practice more ',font=('Verdana',16),bg='Gold')
                l39.place(x=50,y=300)
        if acc>=25 and acc<50:
                l40=tk.Label(h,text='You can perform better than this',font=('Verdana',16),bg='Gold')
                l40.place(x=50,y=300)
        if acc>=50 and acc<75:
                l41=tk.Label(h,text='Good,but you can improve more' ,font=('Verdana',16),bg='Gold')
                l41.place(x=50,y=300)
        if acc>=75 and acc<100:
                l42=tk.Label(h,text='Excellent,you are on your way to the top',font=('Verdana',16),bg='Gold')
                l42.place(x=50,y=300)
        if acc==100:
                l43=tk.Label(h,text='You are a perfectionist',font=('Verdana',16),bg='Gold')
                l43.place(x=50,y=300)
def relogin(g):
        det10(g)
def detd(r):
        r.destroy()
def detd1():
        e.destroy()
def myattempts():
        global ol
        win.destroy()
        ol=tk.Tk()
        ol.title('Login success')
        ol.geometry('1250x350')
        ol.configure(bg='Gold')
        f4=open("C:\\Users\\vehrp\\Documents\\bestattempt.txt","r")
        rlines=f4.readlines()
        tlst=[]
        p1=0
        for i in rlines:
                j=i.index(",")
                ml=i[2:j-1]
                if ml==curemail:
                        ind=i.index("]")
                        acclst=i[j+1:ind+1]
                        tlst.append(acclst)
                        p1=1
        aclst=[]
        timelst=[]
        for r in tlst:
                k2=(r.lstrip(" [")).rstrip("]")
                j=k2.split(",")
                for i in range(len(j)):
                        if i%2==0:
                                aclst.append(float(j[i]))
                        else:
                                timelst.append(float(j[i].lstrip(" ")))
        if p1:
                accstring=''
                for k1 in range(len(aclst)):
                        accstring+="["+str(aclst[k1])+","+str(timelst[k1])+"] "
                l7=tk.Label(ol,text="Accuracy,time:"+accstring,font=('Verdana',15),bg='Yellow')
                l7.place(x=25,y=100)
                l8=tk.Button(ol,text=" Back ",font=('Verdana',15),command=lambda:getback(ol),bg='Red')
                l8.place(x=100,y=150)
        else:
                accstring=" NO previous attempts "
                l7=tk.Label(ol,text=accstring,font=('Verdana',15),bg='Yellow')
                l7.place(x=100,y=100)
                l8=tk.Button(ol,text=" Back ",font=('Verdana',15),command=lambda:getback(ol),bg='Red')
                l8.place(x=100,y=150)
def getback(window):
        window.destroy()
        global win
        win=tk.Tk()
        win.title('Login success')
        win.geometry('300x400')
        win.configure(bg='Gold')
        l20=tk.Button(win,text='   My attempts    ',font=('Verdana',16),command=myattempts,bg='Orange')
        l20.place(x=50,y=150)
        l21=tk.Button(win,text='   Start game   ',font=('Verdana',16),command=lambda:det5(win),bg='Orange')
        l21.place(x=50,y=50)
        l19=tk.Button(win,text='   Instruction    ',font=('Verdana',16),command=det3,bg='Orange')
        l19.place(x=50,y=100)
        l20=tk.Button(win,text='   Back    ',font=('Verdana',16),command=lambda:intropg(win),bg='Orange')
        l20.place(x=50,y=250)
        l5=tk.Button(win,text='  Exit    ',font=('Verdana',16),command=lambda:detd(win),bg=('Orange'))
        l5.place(x=50,y=300)
        l6=tk.Button(win,text=' Your score   ',font=('Verdana',16),command=score,bg=('Orange'))
        l6.place(x=50,y=200)
def intropg(x):
        global a
        x.destroy()
        a=tk.Tk()
        a.geometry('650x500')
        a.title('Typing Speed Test')
        a.configure(bg='Yellow')
        l1=tk.Label(a,text='Welcome to Typing Speed Test',font=('Verdana',20),bg='Yellow')
        l1.place(x=100,y=0)
        l2=tk.Label(a,text='Choose any of the following options:',font=('Verdana',12),bg='Yellow')
        l2.place(x=0,y=40)
        l3=tk.Button(a,text='Sign up',font=('Verdana',16),command=det1,bg=('Light Blue'))
        l3.place(x=250,y=75)
        l4=tk.Button(a,text='  Login ',font=('Verdana',16),bg=('Light Blue'),command=lambda:det10(a))
        l4.place(x=250,y=135)
        l35=tk.Button(a,text='Practice',font=('Verdana',16),command=lambda:det11(a),bg=('Light Blue'))
        l35.place(x=250,y=195)
        l5=tk.Button(a,text='  Exit    ',font=('Verdana',16),command=lambda:detd(a),bg=('Light Blue'))
        l5.place(x=250,y=255)
def score():
        #since time taken and accuracy are inversely related avg. of acc./timetaken will give relative performance out of 1
        #this score multiplied by 10 gives score out of 1
        win.destroy()
        global nin
        nin=tk.Tk()
        nin.title('Your score')
        nin.geometry('1250x350')
        nin.configure(bg='Gold')
        f4=open("C:\\Users\\vehrp\\Documents\\bestattempt.txt","r")
        f4.seek(0,0)
        rlines=f4.readlines()
        tlst=[]
        p1=0
        for i in rlines:
                j=i.index(",")
                ml=i[2:j-1]
                if ml==curemail:
                        ind=i.index("]")
                        acclst=i[j+1:ind+1]
                        tlst.append(acclst)
                        p1=1
        aclst=[]
        timelst=[]
        for r in tlst:
                k2=(r.lstrip(" [")).rstrip("]")
                j=k2.split(",")
                for i in range(len(j)):
                        if i%2==0:
                                aclst.append(float(j[i]))
                        else:
                                timelst.append(float(j[i].lstrip(" ")))
        su=0
        n=0
        for i in range(len(aclst)):
                if int(aclst[i])>=30 or int(timelst[i])>=10:
                        su+=int(aclst[i])/int(timelst[i])
                        n+=1
        if n!=0:
                #accmax=100,timemax=12 seconds
                avg=su/8.33/n
                sc1=avg*10
                sc=round(sc1,2)
        else:
                sc="Your score is low,less than 3 on average"
        l1=tk.Label(nin,text=' SCORE out of 10 :' +str(sc)+" on average",font=('Verdana',12),bg='Yellow')
        l1.place(x=100,y=100)
        l5=tk.Button(nin,text='  Exit    ',font=('Verdana',16),command=lambda:detd(nin),bg=('Red'))
        l5.place(x=275,y=195)
        l20=tk.Button(nin,text='   Back    ',font=('Verdana',16),command=lambda:getback(nin),bg='Red')
        l20.place(x=150,y=195)
        f4.close()
userl=[]
f=open("C:\\Users\\vehrp\\Documents\\signup.txt","a")
f2=open("C:\\Users\\vehrp\\Documents\\emsave.txt","a")
a=tk.Tk()
a.geometry('650x500')
a.title('Typing Speed Test')
a.configure(bg='Yellow')
l1=tk.Label(a,text='Welcome to Typing Speed Test',font=('Verdana',20),bg='Yellow')
l1.place(x=100,y=0)
l2=tk.Label(a,text='Choose any of the following options:',font=('Verdana',12),bg='Yellow')
l2.place(x=0,y=40)
l3=tk.Button(a,text='Sign up',font=('Verdana',16),command=det1,bg=('Light Blue'))
l3.place(x=250,y=75)
l4=tk.Button(a,text='  Login ',font=('Verdana',16),bg=('Light Blue'),command=lambda:det10(a))
l4.place(x=250,y=135)
l35=tk.Button(a,text='Practice',font=('Verdana',16),command=lambda:det11(a),bg=('Light Blue'))
l35.place(x=250,y=195)
l5=tk.Button(a,text='  Exit    ',font=('Verdana',16),command=lambda:detd(a),bg=('Light Blue'))
l5.place(x=250,y=255)

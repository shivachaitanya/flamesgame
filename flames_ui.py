#! /usr/bin/python3

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Flames')
panedwindow = ttk.Panedwindow(root, orient = VERTICAL)
panedwindow.pack(fill = BOTH, expand = True)

frame1 = ttk.Frame(panedwindow,width = 300, height = 50, relief = SUNKEN)
frame2 = ttk.Frame(panedwindow,width = 300, height = 200, relief = SUNKEN)


panedwindow.add(frame1,weight = 1)
panedwindow.add(frame2, weight = 3)

titleLabel = ttk.Label(frame1,text = 'Flames Game')
titleLabel.config(justify = CENTER,background = 'yellow', foreground = 'black', font = ('Courier',14,'bold'))
titleLabel.pack()
root.resizable(False,False)


yourName = ttk.Label(frame2,text = "Your Name")
crushName = ttk.Label(frame2, text = "Your Crush Name")
yourNameEntry = ttk.Entry(frame2,width =20 )
yourCrushNameEntry = ttk.Entry(frame2,width = 20)
yourName.grid(row = 1, column = 2)
crushName.grid(row = 2,column = 2)
yourNameEntry.grid(row = 1, column =5)
yourCrushNameEntry.grid(row = 2, column = 5)


def output_window(person1,person2,relation,check):
    outputWindow = Toplevel(root)
    outputWindow.title("Your Result")
    wframe1 = ttk.Frame(outputWindow,width = 300, height = 100, relief = SUNKEN)
    if (check == 1 ):
        outputText = "Hi {},The relation between {} and you is {}".format(person1,person2,relation)
    elif(check == 2):
        outputText = "Hi {}, your name and your crush name {} has same characters,lucky fellows".format(person1,person2)
    else:
        outputText = "Hi, please enter your names, so we can play Flames game"
    outputLabel = ttk.Label(outputWindow,text = outputText)
    outputLabel.pack()
    outputLabel.config(background = "blue", foreground = "white", font = ("sans serif",16,"bold"))
    imageLabel = ttk.Label(outputWindow, text = " ")
    photoFile = "/home/chaitu/Documents/Python Practise/python prog/{}.gif".format(relation)
    print(photoFile)
    photo = PhotoImage(file = "/home/chaitu/Documents/Python Practise/python prog/{}.gif".format(relation))
    imageLabel.pic = photo
    imageLabel.config(image = imageLabel.pic)
    imageLabel.pack()
    outputWindow.resizable(False,False)

    
        
    return 0

def work_on():
    name1 = yourNameEntry.get()
    name2 = yourCrushNameEntry.get()
    listname1 = []
    listname2 = []

    #fetching charcters of names 
    for p in name1:
        listname1.append(p)
    for q in name2:
        listname2.append(q)
    length1 = len(listname1)
    length2 = len(listname2)
    if(length1!=0 and length2 !=0):
        i = 0
        checkCount = 0
        while( i< length1):
            flag = 0
            for j in range(0,length2):
                if( listname1[i] == listname2[j]):
                    listname2.pop(j)
                    listname2.append('dead') #tis append is to just maintain the constant lenght of listname2
                    flag = 1
                    break
            if(flag == 0):
                checkCount = checkCount + 1
            i = i + 1
            
        #removing the appended dead variable     
        while('dead' in listname2):
            listname2.remove('dead')

        checkCount =   checkCount+len(listname2)


        #we will get the total numbers
        flames = ['friends','lovers','ancestors','marriage','enemies','sisters']
        count = checkCount
        if(count != 0):
            adjustedNumber = count - 1
            maxBase = 6
            i = 0
            crossed = 0
            while(crossed < 5):
                count = 0
                while(count != adjustedNumber):
                    count = count + 1
                    i = (i+1)%maxBase
                flames.pop(i)
                maxBase = maxBase - 1
                crossed = crossed + 1
            print("the relation between you both is {}".format(flames[0]))
            output_window(name1,name2,flames[0],1)
            #if all characters cancel out, then we say it is an excpetion,
        else:
            print("this is an excpetion, your names cancelled out, LUCKY FELLOWS")
            output_window(name1,name2,"lucky",2)
            
    
    else:
        print("This game needs two people names")
        output_window(name1,name2,"name_please",0)
 
submitButton = ttk.Button(frame2,text = 'Submit', command = work_on)
submitButton.grid(row = 10, column = 5)
root.mainloop()


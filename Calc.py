from tkinter import *
import math
root = Tk()
root.title('Ksitij Calc')
root['bg'] = '#0073e6'
root.geometry('225x335')


to_find = ''


def show(event):
    global to_find
    to_find = e.get()
    operators = ('+','-','/','*')
    pos = 0
    l = []
    new_l = []
    found = False
    for j,i in enumerate(to_find):
        if i in operators:
            found = True
            l.append(float(to_find[pos:j]))
            l.append(i)
            pos = j+1
    if found:
        to_add = str()
        for j,i in enumerate(reversed(to_find)):
            if i in operators:
                break
            to_add += i
        l.append(float(to_add[::-1]))   
    m_found = False
    d_found = False
    for j ,i in enumerate(l):
        new_l.append(i)
        if m_found:
            aft_m = new_l.pop()
            m_sign = new_l.pop()
            before_m = new_l.pop()
            new_l.append(aft_m*before_m)
            m_found = False
        if d_found:
            aft_d = new_l.pop()
            d_sign = new_l.pop()
            before_d = new_l.pop()
            new_l.append(before_d/aft_d)
            d_found = False    
        if i == '*':
            m_found =True
        if i == '/':
            d_found = True
    ans = new_l[0]
    new_l = new_l[1:]
    for j , i in enumerate(new_l):
        if i== '+':
            ans+= new_l[j+1]
        elif i == '-':
            ans-= new_l[j+1]  
    print(ans)          
    if math.floor(ans)  == ans :
        e.delete(0, END)
        e.insert(0, int(ans))
    else :
        e.delete(0, END)
        e.insert(0, ans)
    
def del_(event):
    curr = e.index(INSERT)
    e.delete(curr - 1 , INSERT)
        
                                       
                                        
e = Entry(root , width = 0  )
e.grid(sticky = (W,E) , padx = 5 , pady = 5 )
e.focus()
e.bind('<Return>' , show)

display = Frame(root, width = 200 , height = 80 ,bg = 'black')
buttons = Frame(root,width = 200 , height = 500, bg = 'red')
display.grid(padx = 5 , pady = 10 ,sticky = (N,W,E,S))
buttons.grid(row = 1 , padx = 5 , pady = 5 ,sticky = (N,W,E,S) )

bdivide = Button(buttons , text = '/')
bdivide.grid(row = 1 , column = 1 , padx = 5 , pady = 5 )
bdivide.bind('<Button-1>' , lambda event: e.insert(INSERT , '/') )

bmultiply = Button(buttons , text = '*')
bmultiply.grid(row = 1 , column = 2 , padx = 5 , pady = 5 )
bmultiply.bind('<Button-1>' , lambda event: e.insert(INSERT , '*') )

bminus = Button(buttons , text = '-')
bminus.grid(row = 1 , column = 3 , padx = 5 , pady = 5  )
bminus.bind('<Button-1>' , lambda event: e.insert(INSERT , '-') )

bplus = Button(buttons , text = '+')
bplus.grid(row = 1 , column = 4 , padx = 5 , pady = 5  ) 
bplus.bind('<Button-1>' , lambda event: e.insert(INSERT , '+') )

b7 = Button(buttons , text = 7 )
b7.grid(row = 2 , column = 1 , padx = 5 , pady = 5  )
b7.bind('<Button-1>' , lambda event: e.insert(INSERT , '7') )

b8 = Button(buttons , text = 8 )
b8.grid(row = 2 , column = 2 , padx = 5 , pady = 5 )
b8.bind('<Button-1>' , lambda event: e.insert(INSERT , '8') )

b9 = Button(buttons , text = 9)
b9.grid(row = 2 , column = 3 , padx = 5 , pady = 5 )
b9.bind('<Button-1>' , lambda event: e.insert(INSERT , '9') )

b4 = Button(buttons , text = 4)
b4.grid(row = 3 , column = 1 , padx = 5 , pady = 5)
b4.bind('<Button-1>' , lambda event: e.insert(INSERT , '4') )

b5 = Button(buttons , text = 5)
b5.grid(row = 3 , column = 2 , padx = 5 , pady = 5 )
b5.bind('<Button-1>' , lambda event: e.insert(INSERT , '5') )

b6 = Button(buttons , text = 6)
b6.grid(row = 3 , column = 3 , padx = 5 , pady = 5 )
b6.bind('<Button-1>' , lambda event: e.insert(INSERT , '6') )

b1 = Button(buttons , text = 1)
b1.grid(row = 4 , column = 1 , padx = 5 , pady = 5 )
b1.bind('<Button-1>' , lambda event: e.insert(INSERT , '1') )

b2 = Button(buttons , text = 2) 
b2.grid(row = 4 , column = 2 , padx = 5 , pady = 5 )
b2.bind('<Button-1>' , lambda event: e.insert(INSERT , '2') )

b3 = Button(buttons , text = 3 )
b3.grid(row = 4 , column = 3 , padx = 5 , pady = 5 )
b3.bind('<Button-1>' , lambda event: e.insert(INSERT , '3') )

benter = Button(buttons , text = "=")
benter.grid(row = 2 , column = 4 , padx = 5 , pady = 5 , rowspan = 2 , sticky = (N , S) )
benter.bind('<Button-1>' , show)


b0 = Button(buttons , text = 0)
b0.grid(row = 5 , column = 1 , padx = 5 , pady = 5 , columnspan = 2 , sticky = (W ,E) )
b0.bind('<Button-1>' , lambda event: e.insert(INSERT , '0') )

bdec = Button(buttons , text = '.')
bdec.grid(row = 5 , column = 3 , padx = 5 , pady = 5  )
bdec.bind('<Button-1>' , lambda event: e.insert(INSERT , '.') )

bdelete = Button(buttons , text = 'D' )
bdelete.grid(row = 4 , column = 4 , padx = 5 , pady = 5 , rowspan = 2 , sticky = (N ,S))
bdelete.bind('<Button-1>' , del_ )

for child in buttons.winfo_children():
    child['width'] = 2
    child['height'] = 2
    print(child['text'])
        
benter['height'] = 5
bdelete['height'] = 5  
b0['width'] = 5

root.mainloop()
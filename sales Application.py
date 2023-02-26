from tkinter import * 
root=Tk()

root.title("Sales Application")
root.geometry("1000x1000")

month = ("January","February","March","April","May","June","July","August","September","October","November","December")
profits = (20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

months_lbl = Label(root)
months_lbl["text"]=month

profits_lbl = Label(root)
profits_lbl["text"]=profits

months_lbl.place(relx=0.5,rely=0.3,anchor=CENTER)
profits_lbl.place(relx=0.5,rely=0.4,anchor=CENTER)

def maxp():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    maxlbl["text"]="Maximum profit of "+str(max_profit)+" was recorded in the month of "+str(max_profit_month)
    
def minp():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    min_profit_month = month[min_profit_index]
    minlbl["text"]="Minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month)

maxprofit_btn = Button(root,text="Find Maximum Profit",command=maxp)
minprofit_btn = Button(root,text="Find Minimum Profit",command=minp)

maxprofit_btn.place(relx=0.5,rely=0.5,anchor=CENTER)
minprofit_btn.place(relx=0.5,rely=0.7,anchor=CENTER)

minlbl = Label(root)
maxlbl = Label(root)

maxlbl.place(relx=0.5,rely=0.6,anchor=CENTER)
minlbl.place(relx=0.5,rely=0.8,anchor=CENTER)

def maxp():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    max_profit_month = month[max_profit_index]
    maxlbl["text"]="Maximum profit of "+str(max_profit)+"was recorded in the month of "+str(max_profit_month)

root.mainloop()
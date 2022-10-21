from tkinter import*
root= Tk()
root.title("aSales Application")
root.geometry("400x400")
root.configure(background= "violet")


month=("January","Febuary","March","April","May","June","July","August","September","October","Novvember","December")

profit=(10000,10000,30000,50000,40000,40000,30000,30000,40000,90000,40000,50000)

month_label= Label(root)
month_label["text"]="Month:" + str(month)
month_label.place(relx= 0.5, rely=0.2, anchor= CENTER)

profit_label= Label(root)
profit_label["text"]="Profit:"+ str(profit)
profit_label.place(relx=0.5, rely=0.3, anchor=CENTER)


max_profitlabel=  Label(root)
max_profitlabel.place(relx=0.5, rely=0.5, anchor=CENTER)

min_profitlabel=  Label(root)
min_profitlabel.place(relx=0.5, rely=0.7, anchor=CENTER)

def maxProfit():
    max_profit= max(profit)
    max_profit_index= profit.index(max_profit)
    print(max_profit_index)
    max_profit_month= month[max_profit_index]
    print("the maximum profit of "+str(max_profit)+" was recorded in the month of "+str(max_profit_month))
    max_profitlabel["text"]="the maximum profit of "+str(max_profit)+"was recorded in the month of "+str(max_profit_month)

def minProfit():
    min_profit= min(profit)
    min_profit_index= profit.index(min_profit)
    print(min_profit_index)
    min_profit_month= month[min_profit_index]
    print("the minimum profit of "+str(min_profit)+" was recorded in the month of "+str(min_profit_month))
    min_profitlabel["text"]="the minimum profit of "+str(min_profit)+"was recorded in the month of "+str(min_profit_month)

btn1= Button(root, text= "Show Max Profitable Month", command= maxProfit)
btn1.place(relx=0.5, rely=0.4, anchor=CENTER)

btn1= Button(root, text= "Show Min Profitable Month", command= minProfit)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()
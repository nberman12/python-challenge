import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,"Budget_Data.csv")

output_file=os.path.join(dir_path,"Final_PyBank.txt")

date=[]
profit_loss=[]
net_change=[]
prev_row=[]
greatest=0
lowest=0

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)
    prev_row=next(csvreader)
    
    for row in csvreader:
        #Months
        date.append(row[0])
        months=int(len(date))+1
        #Total
        profit_loss.append(int(row[1]))
        total=sum(profit_loss)
        #Average Change
        net_change.append(int(row[1])-int(prev_row[1]))
        average_change=round(sum(net_change)/len(net_change),2)
        
        #Greatest Increase
        greatest_increase=max(net_change)
        greatest=net_change.index(greatest_increase)
        month_increase=date[greatest]

        #Greatest Loss
        greatest_loss=min(net_change)
        lowest=net_change.index(greatest_loss)
        month_loss=date[lowest]

        prev_row=row

print(f"Financial Analysis")
print("------------------------------------")
print(f"Total Months: {months}")        
print(f"Total: $ {total}")
print(f"Average Change: $ {average_change}")
print(f"Greatest Increase in Profits: {month_increase} ${greatest_increase} ")
print(f"Greatest Decrease in Profits: {month_loss} ${greatest_loss}")  

with open(output_file, "w") as txtfile:
    txtfile.write('Financial Analysis')
    txtfile.write('\n----------------------------------------')
    txtfile.write(f'\nTotal Months: {months}')
    txtfile.write(f'\nTotal: ${total}')
    txtfile.write(f'\nAverage Change: ${average_change}')
    txtfile.write(f'\nGreatest Increase in Profits: {month_increase} ${greatest_increase}')
    txtfile.write(f'\nGreatest Decrease in Profits:: {month_loss} ${greatest_loss}')

        




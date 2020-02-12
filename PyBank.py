import os
import csv

csvpath = os.path.join('..', 'Resources','budget_data.csv')
print(csvpath)

#open and read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvfile)
    
 
    # Declare variables 
    Total_months = []
    Profit_Loss = []
    Avg_changes = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
    
    # total number of months 
    for row in csvreader:
        Total_months.append(row[0])   
        Profit_Loss.append(int(row[1]))

    for i in range(1, len(Profit_Loss)):
        
        # Find average change between months
        Avg_changes.append(Profit_Loss[i] - Profit_Loss[i-1])
        
        # Find the average change
        Average_Changes = sum(Avg_changes) / len(Avg_changes)
        
        # find the greatest increase and date
        Greatest_Increase = max(Avg_changes)
        Greatest_Increase_Date = str(Months[Avg_changes.index(max(Avg_changes))])
        
        
        # find the greatest decrease and date
        Greatest_Decrease = min(Avg_changes)
        Greatest_Decrease_Date = str(Months[Avg_changes.index(min(Avg_changes))])    


# Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(Total_months))
print("Total : " +"$" +str(Profit_Loss))      
print("Average Change: " +"$"+ str(Avg_changes))
print("Greatest Increase :" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease :" + str(min[0])+" ($" + str(min[1])+")")
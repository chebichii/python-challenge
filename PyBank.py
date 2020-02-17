import os
import csv

csvpath = os.path.join('C:/Users/Cece Malachi/Desktop/PyBank_Resources_budget_data.csv')
outpath = os.path.join('C:/Users/Cece Malachi/Desktop/result/result.txt')
print(csvpath)

#open and read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    
    #specify delimiter
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
 
    # Declare variables 
    Total_months = []
    Profit_Loss = []
    Diff = []
    Greatest_Increase_Date = ""
    Greatest_Decrease_Date = ""
    
    
    # total number of months 
    for row in csvreader:
        Total_months.append(row[0])   
        Profit_Loss.append(row[1])
        Profit_Loss = [int(i) for i in Profit_Loss]
        total_change =0

    #print(Profit_Loss)
        #print (type(Profit_Loss))
    for i in range(len(Profit_Loss)-1):

        
        # Find average change between months
        diff=Profit_Loss[i+1] - Profit_Loss[i]
        total_change = total_change + diff
        
        # Find the average change
        Avg_Change = (total_change) / (len(Profit_Loss)-1)
        #Diff
    print(Diff)
        
        # find the greatest increase and date
    Greatest_Increase = max(Profit_Loss)
    Greatest_Increase_Date = str( Total_months[Profit_Loss.index(max(Profit_Loss))])
        
        
        # find the greatest decrease and date
    Greatest_Decrease = min(Profit_Loss)
    Greatest_Decrease_Date = str( Total_months[Profit_Loss.index(min(Profit_Loss))])  
     #file to write
      

with open(outpath, 'w') as writer:
          #delimiter
    writer.writelines("Financial Analysis")
    writer.writelines("---------------------------------------------\n")

    writer.writelines("Total Months: " + str(Total_months)+ "\n")

    writer.writelines("Total : $" + str(Profit_Loss) + "\n")

    writer.writelines("Average Change:" + "$" + str(Diff)+ "\n")

    writer.writelines("Greatest Increase:" + Greatest_Decrease_Date + " ($" + str(Greatest_Increase) + ")\n")

    writer.writelines("Greatest Decrease: " + Greatest_Decrease_Date + " ($" + str(Greatest_Decrease) + ")\n")
          


          


          
         
          


# Outputs
print("Financial Analysis")
print("------------------")
print("Total Months:", len(Total_months))
print("Total : $", sum(Profit_Loss))      
print("Average Change: $",round(Avg_Change))
print("Greatest Increase :" + Greatest_Increase_Date + " $" + str(Greatest_Increase))
print("Greatest Decrease :" + Greatest_Decrease_Date +" $" + str(Greatest_Decrease))
# Import modules
import os
import csv

#Determine path to retrieve and place
csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('analysis', 'analysis.txt')

total = 0
prof_loss = 0
total_months = 0
totalchange = 0
avgchange = 0
greatestincrease = 0
greatestdecrease = 0
profitchange = []
datechange = []
change_profloss =[]
dateincrease = ''
datedecrease = ''

with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csvheader = next(csvreader)
    print(f"csvheader: {csvheader}")
    
    for row in csvreader:

        prof_loss = int(row[1])
        total = total + prof_loss
        profitchange.append(prof_loss)
        datechange.append(row[0])
        total_months += 1

    for i in range(total_months - 1):
        change_profloss.append(profitchange[i+1]-profitchange[i])

    for i in range(len(change_profloss)):
        total_changes += change_profloss[i]
        total_changes.append(change_profloss[i] - change_profloss[i-1])   
        avgchange = totalchange / len(change_profloss)
    
    for i in range(len(change_profloss)):
        if change_profloss[i] > greatestincrease:
            greatestincrease = change_profloss[i]
            dateincrease = datechange[i+1]
        elif change_profloss[i] < greatestdecrease:
            greatestdecrease = change_profloss[i]
            datedecrease = datechange[i+1]


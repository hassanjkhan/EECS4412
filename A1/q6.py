import fileinput
import pandas as pd
import sys

transactions = sys.argv[1].split(",")
recommended = []
ID2NameFile = "ID2Name.csv"
itemNames = {}
print("transactions below:")
print(transactions)

def contains(transactions, Antecedents):
    for each in Antecedents:
        if each not in transactions:
            return False
    return True


for line in pd.read_csv(ID2NameFile,chunksize=1):
    pair = line.iloc[:, 1].to_string().split("    ")
    itemNames[pair[0]] = pair[1]

# open file in read mode
fileName = "walmart_rules.csv"
for line in pd.read_csv(fileName,chunksize=1):
    temp = line['Antecedent'].to_string().split("'")
    Antecedents = []
    for i in range(0,len(temp)):
        if(i%2!=0):
            Antecedents.append(temp[i])

    temp_Consequent = line['Consequent'].to_string().split("'")
    Consequent = []
    for i in range(0,len(temp_Consequent)):
        if(i%2!=0):
            Consequent.append(temp_Consequent[i])

    # check if every Antecedent is in transaction list
    # if yes then add the Consequent to recommended else do not add
    if (contains(transactions,Antecedents)):
        recommended.append(Consequent)

final_recommended = []
for each_list in recommended:
    for each in each_list:
        if each not in final_recommended:
            final_recommended.append(each)


recommended_named = []
for i in final_recommended:
    recommended_named.append(itemNames[i])
print(recommended_named)
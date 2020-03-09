import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(dir_path,"Election_Data.csv")

output_file=os.path.join(dir_path,"Final_PyPoll.txt")

total=0
candidate=[]
unique_candidate=[]
vote_count=[]
vote_percent=[]


with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvreader)

    for row in csvreader:
        #Total votes
        total=total+1

        #Candidate count
        candidate.append(row[2])
   
    #Loop through, find the count for each candidate 
    #and calc % of votes for each candidate
    for c in set(candidate):
        unique_candidate.append(c)
        v=candidate.count(c)
        vote_count.append(v)
        p=round((v/total)*100,2)
        vote_percent.append(p)
    
    #Identify the winner based on vote count adn index name based on count
    winner_count=max(vote_count)
    winner=unique_candidate[vote_count.index(winner_count)]

#Print results in terminal
print('Election Results')
print('--------------------------------')
print(f'Total Votes: {total}')
print('--------------------------------')
for i in range(len(unique_candidate)):
    print(f'{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
print('--------------------------------')
print(f'Winner: {winner}')
print('--------------------------------')

#Write results to text file
with open(output_file, "w") as txtfile:
    txtfile.write('Election Results')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nTotal Votes: {total}')
    txtfile.write('\n------------------------------------')
    for i in range (len(unique_candidate)):
        txtfile.write(f'\n{unique_candidate[i]}: {vote_percent[i]}% {vote_count[i]}')
    txtfile.write('\n------------------------------------')
    txtfile.write(f'\nWinner: {winner}')
    txtfile.write('\n------------------------------------')
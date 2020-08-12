# Python programming to analyze the election results
#
#
# Data we have to retrieve :
#  • Total number of votes cast
#  • A complete list of candidates who received votes
#  • Total number of votes each candidate received
#  • Percentage of votes each candidate won
#  • The winner of the election based on popular vote
#

# Add dependencies
import csv # Comma Separated Values
import os # access and open file

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variale to indirect ath to the file to write data
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results in read mode using the "with" method
with open(file_to_load, "r") as election_data:
    # Perform analysis
    print(election_data)
    # Read and analyze the data
    # Read the csv file using reader function
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    print(header)
    for row in file_reader:
        print(row[0])
        print(row[1])
        print(row[2])
        for i in range(len(row)):
            print(row[i])
        break



# Open the file using open() function in "w" mode to write using "with" method
with open(file_to_save, "w") as txt_file:
    txt_file.write("Hello World!!\n\n")
    txt_file.write("Counties in the Election\n")
    txt_file.write("__________________________\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")


 


# print(election_data)
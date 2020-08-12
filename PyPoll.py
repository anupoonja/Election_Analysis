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

# 1. Initialize total votes counter
total_votes = 0

# Initialize an empty list for Candidate options
candidate_options = []
# Declare empty dictionary to keep count of candidate votes
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results in read mode using the "with" method
with open(file_to_load, "r") as election_data:
    # Perform analysis
    # print(election_data)
    # Read and analyze the data
    # Read the csv file using reader function
    file_reader = csv.reader(election_data)
    header = next(file_reader)
    #print(header)
    for row in file_reader:
        # Calculate the total votes
        total_votes += 1
        # Get the candidate name
        candidate_name = row[2]

        # Check if the candidate name is already present in the candidate_options
        if candidate_name not in candidate_options:
            # Add the candidate name if not already present in the candidate_options
            candidate_options.append(candidate_name)
            # Track candidate votes
            candidate_votes[candidate_name] = 0
        
        # Add the votes to that candidate's vote count
        candidate_votes[candidate_name] += 1

# Open the file to save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #Write the Election results
    election_result = (
        f"\nElection Results\n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n"
    )
    print(election_result, end="")
    # Write the result to the txt file
    txt_file.write(election_result)

    # Find the winning candidate        
    for candidate_name in candidate_votes:
        # Retrieve the vote and determine percentage
        votes = candidate_votes[candidate_name]
        vote_percentage = votes/float(total_votes) * 100
        # Write each candidate, vote percentage and vote count
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
        )
        # Print each candidate, vote percentage and vote count to terminal
        print(candidate_results)
        # Print each candidate, vote percentage and vote count to file
        txt_file.write(candidate_results)
        
        # Determine winning vote count, percentage and candidate
        if votes > winning_count:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    # Print the winner candidate summary
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner : {winning_candidate}\n"
        f"Winning Vote Count : {winning_count:,}\n"
        f"Winning Percentage : {winning_percentage:.1f}\n"
        f"-------------------------------\n"
    )
    # Print the winning candidate summary to terminal
    print(winning_candidate_summary)
    # Write the winner summary to the file
    txt_file.write(winning_candidate_summary)

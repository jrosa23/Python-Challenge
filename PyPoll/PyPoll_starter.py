# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candidate_options = [] #List for candidate names
candidate_votes = {} #Dictionary to track votes per candidate

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
win_count = 0
win_percent = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets) #Xpert Learning Assistant
        print(".\n\n", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as text_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"\nElection Results\n\n"
        f"-------------------------\n\n"
        f"Total Votes: {total_votes}\n\n"
        f"-------------------------\n\n"
    )
    print(election_results, end="")

    # Write the total vote count to the text file
    text_file.write(election_results)

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate in candidate_votes:

        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percent = (votes / total_votes)*100

        # Update the winning candidate if this one has more votes
        if votes > win_count and vote_percent > win_percent:
            win_count = votes
            win_percent = vote_percent
            winning_candidate = candidate

        #Save each candidate's vote count and percentage
        candidate_results = (
            f"{candidate}: {vote_percent: .3f}% ({votes})\n\n"
        )
        print(candidate_results, end="")#print each candidate's vote count and percentage
        text_file.write(candidate_results)

    # Generate the winning candidate summary
    win_summary = (
        f"-------------------------\n\n"
        f"Winner: {winning_candidate}!\n\n"
        f"-------------------------\n\n"
    )
    print(win_summary)#print the winning candidate summary

    # Save the winning candidate summary to the text file
    text_file.write(win_summary)

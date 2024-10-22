# Python-Challenge


PyBank
---------------------------------------------------------------------------------------------
Start off by loading necessary modules and reading the csv_file later using the csv.reader functionality that I imported from the csv module, making note to skip the header row as to not cause initial problems when iterating through the rows of data. 

I then initialize a few variables to momentarily store placeholder data, that I will replace and fill as the iterator goes through the rows searching for my desired data. I also skip the first row of data in order to avoid appending it.

The for row in reader loop will go through each row and update the total_months, and total_net, and evaluate the changes if any from month to month, it then will compute and capture the greatest incerase and decrease through some comparative if statements. The Xpert Learning Assistant helped me in figuring out the precise logic for the if statements which didnt take too long but I was struggling to figure that out. 

After going through all the rows of data the results will get printed in the terminal as well as written to a text file named budget_analysis.txt.

PyPoll
--------------------------------------------------------------------------------------------
Begin by loading necessary modules and reading the csv_file later using the csv.reader, which was imported.

Then initialize some variables to be used through the iterator, and then open and begin to process the data making note to skip the header row. 

Once in the for loop, I asked the Xpert learning assistant for assistance on the loading indicator for large data sets, as I got stuck figuring that out. Once in the for loop we incrememnt the vote count for each row in the file, add new candidates to the list and track their vote counts in the dictionary. 

After iterating through all the rows I print the results and open a text file to save the output. I then enter a new for loop to search throught he candidates for the winning percentage and winning vote count, which then gets printed and saved to a text file named election_analysis.txt.

# Election Analysis

## Overview of Election Audit
A Colarado Board of Elections employee has requested below additional data to complete the election audit of a recent local congressional election.

* The voter turnout for each county
* The percentage of votes from each county out of the total count
* The county with the highest turnout

## Election-Data Analysis

### Candidate name

### County name

### Total vote count

  Total vote count is calculated by counting each votes while looping through all the rows in the election list using the formula
  ```  total_votes = total + 1  ```
  
### Candidate votes and percentage turnout

### County votes and percentage turnout

### Winner of the election

### County with largest turnout


## Election-Audit Results
The analysis of the election show that:
* **Total Votes** cast in the election : **"369,711"** 
* The **County Turnout** were:
  - Jefferson had **"10.5%"** of voter turnout and **"(38,885)"** number of votes
  - Denver had **"82.8%** of voter turnout and **"(306,055)"** number of votes
  - Arapahoe had **"6.7%"** of votes turnout and **"(24,801)"** number of votes 
* **Denver** had the largest number of votes with **"82.8%"** turnout
* The **Candidate Results** were:
  - Charles Casper Stockham received **"23.0%"** of the votes and **"(85,213)"** number of votes.
  - Diana DeGette received **"73.8%"** of the votes and **"(272,892)"** number of votes.
  - Raymon Anthony Doane received **"3.1%"** of the votes and **"(11,606)"** number of votes.  
* The **Winner** of the election was:
  - Candidate **Diana DeGette**, who received **"73.8%"** of the votes and **"(272,892)"** number of votes.
  
  Please find the output of the election audit :
  
  ![Election_result](analysis/command_line_output.png)
  
  ## Election-Audit Summary
  The python script written to analyse the data can be extended to analyze all the election results.
  Please find my business proposal on the changes that are needed to be able to analyze all other elections:
  * The script is capable of analyzing any election results, by modifying it to make the election result input file readable from user prompt.
  * The script is capable of handling any number of candidates and county names without any further changes, not limited to the current list of three candidates and counties.
  * The script can be modified to provide the winner or the popular candidate in each county.
  * The script can be modified to provide the breakdown of the votes and percentage of votes received by candidates in each county.
  

# science_paper_sum.py
Create an Excel sheet with selected chunks of scientific papers

## 1. Select the name of the topic you wanna read article about

For example, let's say I'm on a new project about the Default Mode Network in Alzheimer, I'd type "DMN_Alzheimer", this would create a Excel file with a column for title, date, authors, journal, methods, results, discussion and other. If the file already exists, then it will open it.

## 2. Select what you wanna do with it

Add new entry (0), modify entry (1), show the complete data (2), read a specific entry (3) or save data (4) or press ctrl + c to exit

#### Add new entry

The program will ask you to paste information about each part defined in the program. You can change this by changing the part of the code at line 17:

'''
self.columns = ["Title", "Authors", "Journal", "Date", "Methods",
                "Results", "Discussion", "Other"]
'''

Type 0 and press Enter
The program first ask you about the title, copy paste the title and press Enter
It then asks you if you want to add more in title. Type 0 and press Enter if not.

Follow the same procedure for the following columns until you get back to asking you about what to do next.
Then type 4 and press Enter to save the Dataframe onto the Excel document.

#### Modify entry

The program will ask you which index and column to modify. Copy paste the new value, press Enter. Then type 4 and press Enter to save it.



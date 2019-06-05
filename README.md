# science_paper_sum.py
Create an Excel sheet with selected chunks of scientific papers.

## Before running the program
You need to make sure Python 3 is installed as well as the module pandas. If not, activate python (open your terminal and type python or ipython) and type in:

'''
!pip install pandas
'''

Then you need to make sure you are in the working directory you wanna be in. The program will create an Excel document, if your Desktop is already busy, maybe you should create a new folder and run the script within the new folder.

You can do it this way:
'''
mkdir science_papers_sum    # create a new folder named "science_papers_sum"
cd science_papers_sum       # move into this directory
'''

Now you can download the script Science_paper_sum.py (on the top)
Put the script into your newly created folder "science_papers_sum".
Go back into your terminal with python or ipython activated and type 

'''
run Science_paper_sum.py
'''

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

The program will ask you which index and column to modify. Copy&paste the new value, press Enter. Then type 4 and press Enter to save it.

#### show the complete data

This option will print the Dataframe

#### read a specific entry

This option will allow you to read all entries of a specific index. You just have to specifiy the index.
If you write all instead of typing a number, the program will display all columns of all entries one by one.

#### save data

This option will save the Dataframe into the Excel document

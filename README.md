# Keep the summary of research papers
Create an Excel sheet with selected chunks of scientific papers.

## Before running the program
You need to make sure Python 3 is installed (<a href="http://jeremylefortbesnard.de/LearnPythonandML/">info here</a>) as well as the module pandas. If not, activate python (open your terminal and type python or ipython) and type in:
```
!pip install pandas
```

Then you need to make sure you are in the working directory you wanna be in. The program will create an Excel document, if your Desktop is already busy, maybe you should create a new folder and run the script within the new folder.

You can do it by typing in your terminal:
```
mkdir science_papers_sum    # create a new folder named "science_papers_sum"
cd science_papers_sum       # move into this directory
```
<p align="justify"> 
Now you can download the script Science_paper_sum.py (on the top)
Put the script into your newly created folder "science_papers_sum".
Go back into your terminal with python or ipython activated and type:
</p>

```
run sum_research_papers_keeper.py
```

## 1. Select the name of the topic you wanna read article about

For example, let's say I'm on a new project about the Default Mode Network in Alzheimer, I'd type "DMN_Alzheimer.xls" and press Enter. This action would create a empty dataframe with a column for title, date, authors, journal, methods, results, discussion and other,  and save it as an Excel file. If the file already exists, then it will open it.

## 2. Select what you wanna do with it

Add new entry (0), modify entry (1), show the complete data (2), read a specific entry (3) or save data (4) or press ctrl + c to exit.

### Add new entry

Type 0 and press Enter. The program will ask you to paste information about each part.

These parts are pre-defined in the script but you can change them by changing the part of the code at line 17:
```
self.columns = ["Title", "Authors", "Journal", "Date", "Methods",
                "Results", "Discussion", "Other"]
```
For example, to add a column named "sample size", type:
```
self.columns = ["Title", "Authors", "Journal", "Date", "Sample size", "Methods",
                "Results", "Discussion", "Other"]
```
<p align="justify"> 
The program first ask you about the title, copy paste the title and press Enter.
It then asks you if you want to add more in title. Type 0 and press Enter if not. Keep pasting stuff otherwise.
</p>
<p align="justify"> 
Follow the same procedure for the following columns until it gets back to asking you about what to do next.
Then type 4 and press Enter to save the Dataframe into the Excel document.
</p>

### Modify entry

The program will ask you which index and column to modify. Copy & paste the new value, press Enter. Then type 4 and press Enter to save it.

### Show the complete data

This option will print the Dataframe.

### Read a specific entry
<p align="justify"> 
This option will allow you to read what is in each column of a specific index. You just have to specifiy the index.
If you write *all* or anything else but a number, the program will display all columns of all entries one by one.
</p>

### Save data

This option will save the Dataframe into the Excel document.

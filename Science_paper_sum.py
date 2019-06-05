
import os
import pandas as pd
import glob
import time
from sys import platform

def clear_screen():
    if platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

class sum_paper_sheet:
    def __init__(self, path_df):
        self.path = path_df
        if os.path.exists(path_df):
            self.my_dataframe = pd.read_excel(path_df)
        else:
            df = pd.DataFrame(columns=["Title", "Authors",
                                    "Journal", "Date", "Sample size", "Methods",
                                    "Results", "Discussion", "Other"])
            df.to_excel(path_df, index=False)
            self.my_dataframe = pd.read_excel(path_df)

    def add_new_article(self):
        names = ["title" , "authors", "journal", "date", "sample_size", "methods", "results", "discussion", "other"]
        new_entry = []
        for name in names:
            txt = []
            clear_screen()
            print("type 0 and press enter to move on to the next entry")
            print(" " * 10)
            print(" *** ")
            inTxt = input("{} >".format(name))
            while inTxt != "0":
                txt.append(inTxt)
                inTxt = input("add more in {} >".format(name))
            print(" {} completed".format(name))
            txt = ''.join(txt)
            new_entry.append(txt)
        row_number = len(self.my_dataframe)
        self.my_dataframe.loc[row_number] = new_entry
        return self.my_dataframe
 
    
    def modify_entry(self):
        print(self.my_dataframe)
        row_number = int(input("Which index to modify?"))
        column = input("Which column to modify?")
        new_entry = input("new {} >".format(column))
        self.my_dataframe[column].loc[row_number] = new_entry
        return self.my_dataframe

    def print_df(self):
        print(self.my_dataframe)

    def save(self):
        self.my_dataframe.to_excel(self.path, index=False)
        print("***** DataFrame saved at {}*****".format(os.getcwd()))

def reading_of_the_day():
    existing_topic = glob.glob("*.xls")
    print("Existing topic (Dataframe): {}".format(existing_topic))
    chosen_topic = input("Select topic or create new one (with .xls)>")
    try_again = True
    while try_again == True:
        try:
            dic = sum_paper_sheet(chosen_topic)
            try_again = False
        except:
            print("I don't understand (maybe you forgot the .xls at the end of the file name)")
            chosen_topic = input("Select topic or create new one (with .xls)>")
    clear_screen()
    print("Dataframe chosen: {}".format(dic.print_df()))
    time.sleep(2)
    a = 0
    while a == 0:
        clear_screen()
        print("Add new entry (0), modify entry (1), show the data (2) or save data (3)? (press ctrl + c to exit)")
        choice = input(">")
        if choice == "0":
            clear_screen()
            dic.add_new_article()
        elif choice == "1":
            clear_screen()
            dic.modify_entry()
        elif choice == "2":
            clear_screen()
            dic.print_df()
        else:
            clear_screen()
            dic.save()

reading_of_the_day()

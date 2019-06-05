
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
        self.columns = ["Title", "Authors", "Journal", "Date", "Methods",
                       "Results", "Discussion", "Other"]
        if os.path.exists(self.path):
            self.my_dataframe = pd.read_excel(self.path)
        else:
            df = pd.DataFrame(columns=self.columns)
            df.to_excel(self.path, index=False)
            self.my_dataframe = pd.read_excel(self.path)

    def add_new_article(self):
        names = self.columns
        new_entry = []
        for name in names:
            txt = []
            clear_screen()
            print("type 0 and press enter to stop adding information")
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
        try:
            self.my_dataframe[column].loc[row_number] = new_entry
        except:
            print("Failed to modify entry (maybe the index or column is wrong?)")
        return self.my_dataframe

    def print_df(self):
        print(self.my_dataframe)
        
    def read_df(self):
        print(self.my_dataframe)
        print(" " * 150)
        print("*****")
        row_number = input("Which index to display? (Type all for iterating over the whole dataframe)")
        print(" " * 150)
        try:
            row_number = int(row_number)
            for column in self.columns:
                print("{} > ".format(column))
                entry = self.my_dataframe[column].loc[row_number]
                print(entry) 
                print(" " * 150)
                next = input(" ")
        except:
            for index in self.my_dataframe.index:
                print("-" * 10)
                print("index {} > ".format(index))
                print(" " * 10)
                for column in self.columns:
                    print("{} > ".format(column))
                    print(" " * 10)
                    entry = self.my_dataframe[column].loc[index]
                    print( entry)
                    print(" " * 150)
                    next = input(" ")

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
    a = 0
    while a == 0:
        print(" " * 150)
        print(" ***** ")
        print("Add new entry (0), modify entry (1), show the complete data (2),")
        print("read a specific entry (3) or save data (4)? (press ctrl + c to exit)")
        choice = input(">")
        print(" ***** ")
        print(" " * 150)
        if choice == "0":
            clear_screen()
            dic.add_new_article()
        elif choice == "1":
            clear_screen()
            dic.modify_entry()
        elif choice == "2":
            clear_screen()
            dic.print_df()
        elif choice == "3":
            clear_screen()
            dic.read_df() 
        else:
            clear_screen()
            dic.save()

reading_of_the_day()

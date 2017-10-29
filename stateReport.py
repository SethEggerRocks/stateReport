import tkinter as tk
from tkinter import filedialog
import openpyxl
import datetime
from tkinter import messagebox


now = datetime.datetime.now()
today = (str(now.month) + str(now.day) + str(now.year))

root = tk.Tk()
root.withdraw()

userFileName = today
helloPath3 = ("/Users/nichodeturbo/Desktop/Python_Code/" + "09" + str(now.month) + str(now.day))
helloFile3 = open(helloPath3, "w")
bigCount = 0

messagebox.showinfo("Choose File", "Choose File To Sift Through.")
file_path = filedialog.askopenfilename()
helloFile = open(file_path, "r")

messagebox.showinfo("Choose File", "Choose Spreadsheet Containing Identifiers.")
file_path2 = filedialog.askopenfilename()
helloFile2 = open(file_path2, "r")

state_wb = openpyxl.load_workbook(file_path2)    # This spreadsheet contains all the identifiers I need
state_sheet = state_wb.get_sheet_by_name("Sheet1")
state_otherThing = state_sheet.max_row

state_emptyList = []
state_asaList = []
state_completedList = []
state_arrestedList = []
state_dischargedList = []


def thisIsCool():                    # This is our function that opens a specific text file and then searches through it for Identifierss
    with open(file_path) as f:
        stateNumbers()
        for line in f:
            for i in state_emptyList:
                if str(i) != str(line[10:19]):
                    continue
                elif str(i) == str(line[10:19]):
                    print(line)
                    helloFile3.write(line)
                    break
                else:
                    break


def stateNumbers():
    for columnOfCellObjects in state_sheet["A1" : "A500"]:
        for cellObj in columnOfCellObjects:
            if cellObj.value != "":
                state_emptyList.append(cellObj.value)
    return(state_emptyList)


while True:                     # Now my state reporting has a choose file on top of it
    thisIsCool()                # which has some huge implications
    break
exit()                          # I want to make this program run for the python 2.7 version as well
                                # I need to see if the choose file method will work for choosing a folder
                                # And then concatenating it with a timestamp and a + ".txt" to write to a file path.

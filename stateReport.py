import tkinter as tk
from tkinter import filedialog
import openpyxl
import datetime

now = datetime.datetime.now()
today = (str(now.month) + str(now.day) + str(now.year))

root = tk.Tk()
root.withdraw()


          # "/Users/nichodeturbo/Desktop/dunno.txt"
userFileName = today
helloPath3 = ("/Users/nichodeturbo/Desktop/Python_Code/" + "09" + str(now.month) + str(now.day))
helloFile3 = open(helloPath3, "w")
bigCount = 0

file_path = filedialog.askopenfilename()
helloFile = open(file_path, "r")

file_path2 = filedialog.askopenfilename()
helloFile2 = open(file_path2, "r")


glc_wb = openpyxl.load_workbook(file_path2) # This spreadsheet contains all the identifiers I need
glc_sheet = glc_wb.get_sheet_by_name("Sheet1")                                              #to match against the larger .txt file ("allPeeps.txt")
glc_otherThing = glc_sheet.max_row

glc_emptyList = []
glc_asaList = []
glc_completedList = []
glc_arrestedList = []
glc_dischargedList = []



def thisIsCool():                    # This is our function that opens a specific text file and then searches through it for Identifierss
    with open(file_path) as f:
        glcNumbers()
        for line in f:
            for i in glc_emptyList:
                if str(i) != str(line[10:19]):
                    continue
                elif str(i) == str(line[10:19]):
                    print(line)
                    helloFile3.write(line)
                    break
                else:
                    break



def thisIsSweet():                    # This is our function that opens a specific text file and then searches through it for Identifierss
    with open(filePath) as f:
        for line in f:
            for i in myNames:
                if str(i) != str(line[10:19]):
                    continue
                elif str(i) == str(line[10:19]):
                    print(line)
                    helloFile.write(line)
                    break
                else:
                    break  # Doesn't even get used..


def glcNumbers():
    for columnOfCellObjects in glc_sheet["A1" : "A500"]:
        for cellObj in columnOfCellObjects:
            if cellObj.value != "":
                glc_emptyList.append(cellObj.value)
    return(glc_emptyList)

while True:                  # This allows for the thisIsSweet() to be called 1 time
    thisIsCool()
    break
exit()

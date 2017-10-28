import openpyxl


print("What is the name of the file you would like to create? \n")          # "/Users/nichodeturbo/Desktop/dunno.txt"
userFileName = input()
helloPath = ("/Users/nichodeturbo/Desktop/Python_Code/" + str(userFileName))
helloFile = open(helloPath, "w")                                            # This opens the text file to be written to.
bigCount = 0                                                                # We will use this for a starting place for our counter.


print("Enter the name of the file you would like to sift through.\n")       # /Users/nichodeturbo/Desktop/090117cs.txt (example path)
sift = input()
filePath = ("/Users/nichodeturbo/Desktop/Python_Code/" + str(sift))


glc_wb = openpyxl.load_workbook("/Users/nichodeturbo/Desktop/Python_Code/Identifiers.xlsx") # This spreadsheet contains all the identifiers I need
glc_sheet = glc_wb.get_sheet_by_name("Sheet1")                                              #to match against the larger .txt file ("allPeeps.txt")
glc_otherThing = glc_sheet.max_row


glc_emptyList = []
glc_asaList = []
glc_completedList = []
glc_arrestedList = []
glc_dischargedList = []


def glcNumbers():
    for columnOfCellObjects in glc_sheet["A1" : "A500"]:
        for cellObj in columnOfCellObjects:
            if cellObj.value != "":
                glc_emptyList.append(cellObj.value)
    return(glc_emptyList)


def thisIsCool():                    # This is our function that opens a specific text file and then searches through it for Identifierss
    with open(filePath) as f:
        glcNumbers()
        for line in f:
            for i in glc_emptyList:
                if str(i) != str(line[10:19]):
                    continue
                elif str(i) == str(line[10:19]):
                    print(line)
                    helloFile.write(line)
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




print("Press enter to start the program.")
identifier = input()

while bigCount <= 1:                  # This allows for the thisIsSweet() to be called 1 time
    if identifier == "n":                    # This allows for a way to exit the program once you have all of your data
        helloFile.close()
        exit()
    else:
        thisIsCool()                 # This begins the function which we pull lines from one file and write them to another
        break               # file, only if they contain the criteria designed for the function

        # I wish i could  sift through lines of text and only write the 9 characters after every other line of ********  (9 of them)
        # Then I could make it read the event report and place them in a list and then just call that and cut out the ssnFile completely

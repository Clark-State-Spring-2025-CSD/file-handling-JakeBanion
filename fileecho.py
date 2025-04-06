#Read in the echo.txt file and display it in the terminal using print()
#This is a guided practice. Either follow the video or your instructor in class.

curfile = open("echo.txt")
for curLine in curfile:
    print(curLine)
curfile.close()
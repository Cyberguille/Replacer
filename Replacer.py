import os

for filename in os.listdir(r"."):
    newname = filename.replace("%20"," ")
    newname = newname.replace("%28","(")
    newname = newname.replace("%29",")")
    newname = newname.replace("%3","-")
    newname = newname.replace("%5B","[")
    newname = newname.replace("%5D","]")
    newname = newname.replace("%5C%27","'")
    if newname != filename:
        os.rename(filename,newname)

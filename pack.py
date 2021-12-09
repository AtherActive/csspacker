import sys
import os

def Main():
    fullfile = ""
    try:
        path = sys.argv[1]
    except:
        print("ERROR : Please supply a valid folder to pull the CSS files from!")
        return

    if path.startswith('.'):
        path = os.getcwd()+path
    
    try:
        targetDir = sys.argv[2]
    except:
        print("WARN : Falling back to Working dir: Supplied dir was invalid.")
        targetDir = os.getcwd()

    try:
        targetName = sys.arv[3]
    except:
        print("WARN : Falling back to default name: No name was supplied")
        targetName = "build"
    files = os.listdir(path)
    for i in files:
        fullfile = fullfile + AppendFile(i,path,fullfile)

    writeFile(fullfile,targetDir,targetName)
    print("\nCOMPLETED : CSS written to "+targetDir+targetName+".css")

def AppendFile(filename, path, out):
    file = open(path+"/"+filename)
    fdata = file.read()
    return fdata

def writeFile(filedata,location,targetName):
    try:
        file = open((location+targetName+".css"), "x")
    except:
        file = open((location+targetName+".css"), "w")

    file.write(filedata)
    file.close()

Main()
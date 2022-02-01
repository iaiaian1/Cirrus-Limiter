import datetime
import os
import glob
import re
#import pickle

#Variables
username = os.environ['username']
limit = 4

#Get the time, and store the time of their builds.
currentTime = datetime.datetime.utcnow()
date = f"{currentTime.year}-{currentTime.month}-{currentTime.day}"
buildInfo = [username, currentTime.hour, currentTime.minute, 1]

#Function to insert their info
def insertInfo():
    with open(f"{date}.txt", "a") as info:
        info.write(','.join(str (e) for e in buildInfo)+"\n")

#Function to check
def check():
    with open(f"{date}.txt", "r") as dataArray:
        #Read each line and store it in an array
        for x in dataArray:
            dbData = x.strip().split(',')
            #Check username's occurence in db, store it in array
            if dbData[0] == username:
                userCount.append(dbData[0])

        #If name did not occur for $LIMIT or more times, let them build.
        if len(userCount) < limit:
            print('Limit OK')
            insertInfo()
            #Code here to proceed
        else:
            print('Limit REACHED')
            #Code here to terminate 

#Dispose of old dbtxt files
def clean():
    def delete():
        try:
            os.remove(file)
        except:
            print("Error while deleting file : ", file)

    if glob.glob("*.txt"):
        files = glob.glob("*.txt")
        for file in files:
            fileData = re.split('-|[.]',file)
            if int(fileData[0]) < currentTime.year:
                delete()
            if int(fileData[0]) == currentTime.year and int(fileData[1]) < currentTime.month:
                delete()

#Try codeblock
try:
    userCount = []
    #Create the dbfile for first time
    if(not os.path.isfile(f"{date}.txt")):
        #If not exist, create a file
        open(f"{date}.txt", "x")
        print('Just created. Let them build')

    check()
    clean()
except Exception as e:
    print (e)
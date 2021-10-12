import sys
import math
import os


"""
The trim function looks throguh the file and removes anything
that doesnt have to do with a song, ie any line that has "track"
in it.
It currently has no failsafe for when a song title has "track" in it.


"""

maintenanceMode = False

downOrUp = sys.argv[1]

def lineBreak(height,width):
    i = 0
    while i < height:
        j = 0;
        while j < width:
            print("_", end = "")
            j += 1;
        i += 1;
        print("")
    print("")
    print("")

def trim(txt):

    #fileLength = length of file
    f = open(txt, "r")
    fileLength = len(f.readlines())
    f.close()


    f = open(txt, "r")
    k = f.readlines()
    n = 0
    m = []

    #The while loop iterates through the file
    #and removes lines like "love this track"
    #or "user doesnt love this track"
    while n < fileLength:

        y = str.split(k[n])
        i = 0
        containsUseless = False

        while i < len(y):
            if y[i] == "track" or y == ['Buy'] and str.split(k[n+1]) == ['More']:
                containsUseless= True
            i += 1
        if containsUseless == False:
            m.append(y)
        n += 1
    f.close()
    return m; #Takes a text file, trims usesless,
    #Returns a list list

def moveToFile(txt):
    n = 0
    #k = input("What is name of file? ")
    k = trim(txt) #text file is here!!!!!!!
    f = open("secondfile.txt","w")

    while n < len(k):
        i = 0
        while i+1 <= len(k[n]):
            #print(k[n][i], end =' ')
            f.write(k[n][i]);
            f.write(" ")
            i += 1
        f.write("\n")
        #print('')
        n += 1

    f.close();
    print("")

def listList(k,interval,down):
    if down == False :
        i = 0
        m = []
        c = math.floor(len(k)/interval)*interval
        print(c)
        while i < c:
            j = 0;
            p = []
            while j < interval:
                p.append(k[j+i]);
                j += 1;
            m.append(p)
            i += interval;
        return m;
    else:
        i = 0
        m = []
        c = math.floor(len(k)/interval)*interval
        print(c)
        while i < c:
            j = 0;
            p = []
            while j < interval:
                p.append(k[c-1-(j+i)]);
                j += 1;
            m.append(p)
            i += interval;
        return m;

def songArtistForm(txt):

    f = open(txt, "r")
    fileLength = len(f.readlines())
    f.close()

    f = open(txt, "r")
    k = f.readlines()
    n = 0  # The current chunk of songs
    m = [] # The list that the songs will be sent to

    #Every song info is 5 chunks long.
    #Index 2 has the song name
    #Index 3 has the artist
    #Everything else can be more or less ignored.
    while n+3 <= fileLength:
        song = n + 2
        artist = n + 3
        y = str.split(k[song])
        m.append(y) #adds the song to the list
        z = str.split(k[artist])
        m.append(z) #adds the artist to the list
        n += 5
    #print(listList(k,5))
    f.close()

    return m;

def nestListSongs(txt,interval,down):
    f = open(txt, "r")
    fileLength = len(f.readlines())
    f.close()

    f = open(txt, "r")
    k = f.readlines()
    p = listList(k,interval,down);
    f.close();
    return p;


if maintenanceMode:
    lineBreak(3,25);

moveToFile("copyPasteFromLastFM.txt");

m = "secondfile.txt"

"""
if sys.argv[1]== "up":
    #print(nestListSongs(m,5,False))
else:
    #print(nestListSongs(m,5,True))
"""


if maintenanceMode:
    lineBreak(3,25);




k = songArtistForm(m)

## Formatting to file
if downOrUp != "down" and downOrUp != "up":
    print("Error")

elif downOrUp == "up":
    f = open("outputfile.txt","w")
    n = 0
    while n+1 <= len(k):
        c = 0
        if n%2 == 1:
            print("- ", end = '')
            f.write("- ")
        while c+1 <= len(k[n]):
            if maintenanceMode:
                print(k[n][c], end = ' ')
            f.write(k[n][c]);
            f.write(" ")
            c += 1
        if n%2 == 1:
            if maintenanceMode:
                print('')
            f.write("\n")
        n += 1
    f.close();
else:
    f = open("outputfile.txt","w")
    n = len(k)-1
    while n > -1:
        c = 0
        while c+1 <= len(k[n]):
            if maintenanceMode:
                print(k[n][c], end = ' ')
            f.write(k[n][c]);
            f.write(" ")
            c += 1
        if n%2 == 1:
            if maintenanceMode:
                print("- ", end = '')
            f.write("- ")
        if n%2 == 0:
            if maintenanceMode:
                print('')
            f.write("\n")
        n -= 1
    f.close();

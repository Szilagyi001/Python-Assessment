#Assesment program
#L.Silaghi
#17/03/2021

print ("Welcome to my Assessment program")
print('*********Liviu Silaghi**********')
input("\nPress Enter to run the program")

def readFile():
    #Import
    import csv

    input("Press Enter to read the files")

    #Opem file in read mode
    f=open("bkb.csv")
    csvFile=csv.reader(f)

    #Create empty arrays
    EventName=[]
    AdultParticipant=[]
    

    #Loop through each row in the file
    for row in csvFile:
        #Append each item to arrays
        EventName.append(row[0]) #colum A
        AdultParticipant.append(row[1]) #colom B

    #Close the file
    f.close()
    return EventName, AdultParticipant


#find the highest number
def findtheTopmark(AdultParticipant, EventName):
    #set the search value to 0
    topMark= AdultParticipant[0]
    topName=EventName[0]
    
    #loop for the lenght of array
    for counter in range(1,len(EventName)):
        #if bigger valu was found make it equals to counter
        if  AdultParticipant[counter] > topMark:
            topMark=AdultParticipant[counter]
            topName=EventName[counter]
    
    return topMark, topName


#display
def display(topMark, topName):
    #Print the result
    print("\nThe name of the event is",topName,"with the price of",topMark,"")
    f=open("Exam-TheResult.txt","w")
    input("\nPress Enter to save the file")
    #Write the result to the file
    f.write("The name of the event is " +topName+ " "" with the price of " +str(topMark)+".") 
    print("\nThe file has been written successfully")
    #Close the file
    f.close()                                                                               
    input("Press Enter to exit")


#run
EventName, AdultParticipant=readFile()
topMark, topName=findtheTopmark(AdultParticipant, EventName)

display(topMark, topName)





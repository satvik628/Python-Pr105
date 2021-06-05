# Python_Standard_Deviation 


# importing modules
import math
import csv


# reading .csv file by with open only & adding newLine as empty and taking .csv file as ' f '
with open('dataPy/data.csv',newline='') as f:
    reader=csv.reader(f)
    file_data=list(reader)
    data=file_data[0]


# creating  mean function to get mean of datas  
def mean(data):
    n=len(data)
    total=0
    
    for x in data:
        total+=int(x)
    
    mean=total/n
    print("The mean is : "+str(mean))
    return mean

    

# storing mean in m variable by getting mean using calling of mean function
m=mean(data)


# sq_list array to store data
sq_list=[]

# for looping i in data
for i in data:
    j=int(i)-m
    j=j**2
    sq_list.append(j)

# sum as 0
sum=0


# looping for in sq_list
for i in sq_list:
    sum=sum+i


# creating result variable for making result   
result=sum/ (len(data)-1)

# finding square root of result
stn_dev=math.sqrt(result)

# printing stn_dev
print("VALUE : "+str(stn_dev))

# Just trying '/' division by python
cal=284/4

# printing calculation
print(cal)







import os
import csv

us_state_abbrev = { 'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 
                    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
                    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
                    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
                    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS',
                    'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH',
                    'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC',
                    'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
                    'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN',
                    'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 
                    'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
                    }

coma = ","
empID = ""
firstName = ""
lastName = ""
dob = ""
ssn =""
state = ""
nl = "\n"

# Set path for file
csvpath = os.path.join("Hw3-Resources", "employee_data.csv")

# We create file for writing
f = open("new_employee_data.csv","w")

print ("Emp ID,First Name,Last Name,DOB,SSN,State")
f.write("Emp ID,First Name,Last Name,DOB,SSN,State"+nl)

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # loop through entire employee data file

    for row in csvreader:
        # No matter header
        if (row[0] == "Emp ID"):
            continue
        empID = row[0]
        nameList = row[1].split(" ")
        firstName = nameList[0] # We build the first name
        lastName = nameList[1] # We build the last name
        dob = row[2]
        dob = dob[5:10].replace("-","/",1)+"/"+dob[0:4] # We transform date(2010-12-20) - newDate(12/20/2010)
        ssn = row[3]
        ssn = "***-**-" + ssn[len(ssn)-4:len(ssn)]
        state = us_state_abbrev[row[4]]
        print(empID+coma+firstName+coma+lastName+coma+dob+coma+ssn+coma+state)
        f.write(empID+coma+firstName+coma+lastName+coma+dob+coma+ssn+coma+state+nl)

f.close()

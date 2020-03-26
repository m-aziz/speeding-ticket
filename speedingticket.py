#description: Determines for officer if ticket is given and if so, the amount.
#author: Aziz, Muhammad
#date: 9.20.2018

#function definitions
def fine(speed_mph,limit):
    fine = 50
    
    if speed_mph > 10 + limit:
        fine = fine + (10 * (speed_mph - (limit + 10)))
    if fine > 500:
        fine = 500
    return fine


def con_zone(fine):
    con_zone_start = int(input("Enter Zone Time Begin in 24 hour format: "))
    con_zone_end = int(input("Enter Zone Time End in 24 hour format: "))
    driver_stopped = int(input("Enter Stop Time in 24 Hour Format: "))

    #make adjustments
    if con_zone_start > con_zone_end:
        if driver_stopped < con_zone_end:
            driver_stopped += 2400
        con_zone_end = con_zone_end + 2400
        #checks for time
    if con_zone_start <= driver_stopped <= con_zone_end:
        fine = fine * 3
        if fine > 1500:
          fine = 1500 
    else:
        fine = fine * 2
        if fine > 1000:
           fine = 1000
    return fine
    
    

#Main program starts here

print("This program computes possible fines for motorists \nstopped on the Massachusetts Turnpike")

#variables collected
speed_mph = int(input("Enter Speed in MPH: "))
limit = int(input("Enter Speed Limit in MPH: "))

#testing if speed is over limit                  
if speed_mph > limit:
    fine = fine(speed_mph,limit)
    
    #asks if in conzone
    construction_zone = str(input("Is it a Construction Zone? Enter Y or N: "))
    construction_zone.lower()

    
    #since in con_zone, jumps into "con_zone" function
    if construction_zone == "y":
        con_zone = con_zone(fine)
        fine = con_zone + 50
        print("The fine is $",fine,"including a $50 donation to the head injury fund")

    else:
        fine = fine + 50
        print("The fine is $",fine,"including a $50 donation to the head injury fund")
        

else:
    print("No fine. Speed does not exceed Speed Limit")

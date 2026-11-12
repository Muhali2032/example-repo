# calculate user's total holiday cost

city_flight =input("Enter the city you are flying to(Port Elizabeth,George,East London,Cape Town) : ")
num_nights =int(input("Enter the number of nights you will stay: "))
rental_days =int(input("Enter the number of days which you will be hiring a Car : "))

def hotel_cost(num_nights):
    return num_nights* 2200


# calculate City Flight
def plane_cost(city_flight):
    if city_flight.upper()== "PORT ELIZABETH" :
        return 1600
    elif city_flight.upper()== "GEORGE" :
        return 1400
    elif city_flight.upper() == "EAST LONDON":
        return 1700
    elif city_flight.upper() == "CAPE TOWN":
        return 2300
    else :return 0

def car_rental(rental_days):
        return rental_days*600
def holiday_cost(num_nights,city_flight,rental_days):
    return(hotel_cost(num_nights)+plane_cost(city_flight)+ car_rental(rental_days))
# print details about the holiday
print("\n HOLIDAY DETAILS")
print("Destination :",city_flight)
print("Hotel Cost:R",hotel_cost(num_nights))
print("Plane Cost:R",plane_cost(city_flight))
print("Car Rental Cost :R ",car_rental(rental_days))
print("Total Holiday Cost:R",holiday_cost(num_nights,city_flight,rental_days))

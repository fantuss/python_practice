cars = 100
space_in_a_car = 4.0
drivers = 30 
passangers = 90

cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passanger_per_car = passangers / cars_driven

print "there are ", cars, "cars available"
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

#Returning additional info
car = make_car('Subaru', 'outback', color = 'blue', tow_package = True)
print(car)

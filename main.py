def calc_hustlescore(totalpoints = list(), months=1, frozen_months=0):
    points = 0
    for i in totalpoints:
        points += i
        lifetime = points/(months-frozen_months)
    monthsinyear = len(totalpoints)%12-frozen_months
    monthly = totalpoints[-1]/100
    yearly = totalpoints[-12:]/100*monthsinyear
    return monthly, yearly, lifetime


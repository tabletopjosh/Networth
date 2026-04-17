#def calc_hustlescore(totalpoints = list(), months=1, frozen_months=0):
def calc_hustlescore(totalpoints=None, months=1, frozen_months=0):
    if totalpoints is None:
        totalpoints = []

    # if months - frozen_months <= 0:
        # raise ValueError("months must be greater than frozen_months")

    points = sum(totalpoints)

    # Lifetime average
    lifetime = points / (months - frozen_months)

    # Monthly (last entry)
    monthly = totalpoints[-1] / 100 if totalpoints else 0

    # Yearly (last up to 12 months)
    last_12 = totalpoints[-12:]
    active_months = max(len(last_12) - frozen_months, 0)

    if active_months > 0:
        yearly = sum(last_12) / 100
    else:
        yearly = 0

    return monthly, yearly, lifetime
    
   # points = 0
    #yearly
    #for i in totalpoints:
     #   points += i
    #lifetime = points/(months-frozen_months)
    #if len(totalpoints)%12-frozen_months>0:
     #   monthsinyear = len(totalpoints)%12-frozen_months
      #  yearly = totalpoints[-12:]/100*monthsinyear

    #monthly = totalpoints[-1]/100
    #return monthly, yearly, lifetime


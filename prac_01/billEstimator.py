print("Electricity bill estimator")

cents = int(input("Each cents per kWh: "))
dailyUse = float(input("Each daily use per kWh: "))
billingDays = int(input("Each number of billing days: "))
estimatedBill = cents / 100 * dailyUse * billingDays

print("Estimated bill $ {:.2f}".format(estimatedBill))
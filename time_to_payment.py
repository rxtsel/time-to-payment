# Convert our hours, minutes and seconds to decimal hours
hours = 92
minutes = 35 / 60
seconds = 12 / 3600

# Sum all hours
total_hours = hours + minutes + seconds

print("Total Ours: ", total_hours.__round__(2))

# Rate per hour
rate_per_hour = 17

# Calculate total payment
total_payment = total_hours * rate_per_hour

print("Total: ", "${:,.2f}".format(total_payment))

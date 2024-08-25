# Only replace the values of hours, minutes and seconds and the rate_per_hour:
hours = 92
minutes = 35
seconds = 12

# Rate per hour
rate_per_hour = 17

# Convert minutes and seconds to decimal
minutes_to_decimal = minutes / 60
seconds_to_decimal = seconds / 3600

# Sum all hours
total_hours = hours + minutes_to_decimal + seconds_to_decimal
print("Total Ours: ", total_hours.__round__(2))

# Calculate total payment
total_payment = total_hours * rate_per_hour
print("Total: ", "${:,.2f}".format(total_payment))


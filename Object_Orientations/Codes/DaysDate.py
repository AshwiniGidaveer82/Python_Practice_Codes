from datetime import datetime
def daysDate(date1, date2):
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")

    return abs((d2 - d1).days)
print(daysDate("2019-06-26", "2019-07-26"))

# from datetime import datetime

# def days_between_dates(date1, date2):
#     # Convert strings to datetime objects
#     d1 = datetime.strptime(date1, "%Y-%m-%d")
#     d2 = datetime.strptime(date2, "%Y-%m-%d")
    
#     # Calculate the absolute difference in days
#     return abs((d2 - d1).days)

# # Example usage
# print(days_between_dates("2019-06-29", "2019-06-30"))  # Output: 1
# print(days_between_dates("2020-01-15", "2019-12-31"))  # Output: 15

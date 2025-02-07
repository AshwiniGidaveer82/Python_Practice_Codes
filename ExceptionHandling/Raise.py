def CheckAge(age):
    if (age < 18):
        raise ValueError("aGE MUST BE GREATER THAN 18")
    try:
        CheckAge(12)
    except ValueError as e:
        print("Error Message", e)

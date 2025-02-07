class PinError(Exception):
    pass
correctPin = 1212
pin = int(input("Enter 4 digit pin"))
try:
    if (pin == correctPin):
        print("Account unblocked")
    else:
        raise PinError("Entered pin is", pin)
except PinError as e:
    print("Incorrect pin", e)

 
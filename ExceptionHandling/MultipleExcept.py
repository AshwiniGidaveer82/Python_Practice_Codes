def disp(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Zero Division Error oddured and Handle")
    except NameError:
        print("Name error occurred and handle")
    except TypeError:
        print("Type Error occurred and handle")
    except:
        print("Some error occurred")


disp(10, 'kodnest')
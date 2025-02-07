def disp(a,b):
    try:
        print("Task Started")
    except:
        print("Some error Handled")
    else:
        print("Task Executed without any exception")
    finally:
        print("Task Ended")
disp(10,0)
disp(10,5)
disp(20,2)
import threading
import time

def background_task():
    print(threading.current_thread())
    while True:
        print("Background Task running....")
        time.sleep(1)

thread = threading.Thread(target = background_task, name="daemon")
thread.daemon = True
thread.start()
time.sleep(3)
print("Main Programs ends....")
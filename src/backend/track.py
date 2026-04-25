import time 



def start_tracking():
    start_time = time.time()
    while True:
        total = time.time() - start_time
        print(f"Screen Time: {total:.0f}")
        time.sleep(1)



start_tracking()
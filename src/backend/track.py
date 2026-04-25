import time
from datetime import datetime
import db

def start_tracking():
    db.init_db()
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    accumulated_time = db.get_screentime(today)
    print(f"--- Screen Time Tracker ---")
    print(f"Today: {today}")
    print(f"Already recorded: {accumulated_time} seconds")
    
    session_start_time = time.time()
    
    try:
        while True:
            elapsed_in_session = time.time() - session_start_time
            
            total_today = int(accumulated_time + elapsed_in_session)
            
            print(f"Current session: {elapsed_in_session:.0f}s | Total today: {total_today}s", end="\r")
            
            if int(elapsed_in_session) % 5 == 0:
                db.update_screentime(today, total_today)
            
            current_date = datetime.now().strftime("%Y-%m-%d")
            if current_date != today:
                print(f"\n[!] Day changed to {current_date}. Resetting session.")
                today = current_date
                accumulated_time = 0
                session_start_time = time.time()
                db.init_db()
                
            time.sleep(1)
            
    except KeyboardInterrupt:
        final_total = int(accumulated_time + (time.time() - session_start_time))
        db.update_screentime(today, final_total)
        print(f"\n[!] Session ended. Final total today: {final_total}s")

if __name__ == "__main__":
    start_tracking()
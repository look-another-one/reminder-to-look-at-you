from fastapi import FastAPI, HTTPException
import db

app = FastAPI()

@app.on_event("startup")
def startup_event():
    db.init_db()

@app.get("/")
def read_root():
    return {"status": "running", "message": "Screen Time Tracker API"}

@app.get("/screentime/{date}")
def get_daily_screentime(date: str):
    """
    Get screen time for a specific date (Format: YYYY-MM-DD)
    """
    try:
        from datetime import datetime
        datetime.strptime(date, "%Y-%m-%d")
        
        seconds = db.get_screentime(date)
        return {
            "date": date,
            "screentime_seconds": seconds,
            "screentime_formatted": f"{seconds // 3600}h {(seconds % 3600) // 60}m {seconds % 60}s"
        }
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid date format. Use YYYY-MM-DD")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


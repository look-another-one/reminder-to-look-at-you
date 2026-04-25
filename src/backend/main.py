import multiprocessing
import uvicorn
import api
import track
import db

def run_api():
    """Run the FastAPI server."""
    print("[*] Starting API server...")
    uvicorn.run(api.app, host="0.0.0.0", port=8000, log_level="info")

def run_tracker():
    """Run the screen time tracking loop."""
    print("[*] Starting screen time tracker...")
    track.start_tracking()

if __name__ == "__main__":
    # Initialize database before starting components
    db.init_db()
    
    # Create processes for API and Tracker
    api_process = multiprocessing.Process(target=run_api)
    tracker_process = multiprocessing.Process(target=run_tracker)

    try:
        # Start both processes
        api_process.start()
        tracker_process.start()

        print("\n--- All systems started ---")
        print("API: http://localhost:8000")
        print("Tracker: Monitoring session...")
        print("Press Ctrl+C to stop everything.\n")

        # Wait for processes to finish or be interrupted
        api_process.join()
        tracker_process.join()

    except KeyboardInterrupt:
        print("\n[!] Stopping all systems...")
        api_process.terminate()
        tracker_process.terminate()
        api_process.join()
        tracker_process.join()
        print("[!] Cleanup complete. Goodbye!")

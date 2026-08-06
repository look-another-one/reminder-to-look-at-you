import logging
from src.services.track_activity import TrackScreenTime

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(filename="logging.log", level=logging.DEBUG)
    logger.info("Program Started")
    start = TrackScreenTime()
    start.connect_to_window_manager()
    logger.info("Program Finished")

if __name__ == "__main__":
    main()
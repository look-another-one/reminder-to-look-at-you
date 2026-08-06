import subprocess
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

root = Path(__file__).resolve().parent.parent.parent

water_bottle = root / "assets" / "water_bottle.png"
alert = root / "assets" / "alert.png"


def send_notification(title:str, message:str, icon:str) -> None:
    """
    Sends a desktop notification using the libnotify lib
    """
    command = [
            "notify-send",
            title,
            message,
            "-i",
            icon
    ]
    try:
        subprocess.run(command)
        logger.debug("notification sended")
    except FileNotFoundError:
        logger.error("libnotify not found")
        raise ValueError("Error: The 'libnotify' lib is missing from this OS.")
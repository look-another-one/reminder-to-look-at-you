import asyncio
from desktop_notifier import DesktopNotifier, Icon
from pathlib import Path

project_root = Path(__file__).parent.parent  # give the location of folder

alert_icon = project_root / "assets" / "alert.png"
water_bottle = project_root / "assets" / "water_bottle.png"
notifier = DesktopNotifier()


def main() -> None:
    # Send a simple notification
    async def water_reminder():
        await notifier.send(
            title="Hello from Python!",
            message="This is a desktop notification.",
            icon=Icon(alert_icon),
        )

    asyncio.run(water_reminder())


# Run the async main function


main()


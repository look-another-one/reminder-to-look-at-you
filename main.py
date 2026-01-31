import asyncio
from desktop_notifier import DesktopNotifier, Icon, Button
from pathlib import Path
from time import ctime
import json


project_root = Path(__file__).parent  # give the location of folder

alert_icon = project_root / "assets" / "alert.png"
water_bottle = project_root / "assets" / "water_bottle.png"
json_file = project_root /"log" /"data.jsonl"
notifier = DesktopNotifier()


def writing_log(status:str):
    with open(json_file,"a") as data:
        json.dump({"Date": ctime(), "Reminder": "Drink Water","Status":status},data)
        data.write("\n")

# This Func gonna send a notification based on paramaters
async def send(title: str, message: str, icon: Path, reminder_interval: int, snooze_interval: int):
    sleep_duration = [reminder_interval]

    def on_ok():
        writing_log("Taken")
        sleep_duration[0] = reminder_interval

    def on_skip():
        writing_log("Skipped")
        sleep_duration[0] = reminder_interval

    def on_snooze():
        writing_log("Snoozed")
        sleep_duration[0] = snooze_interval

    while True:
        await notifier.send(
            title=title,
            message=message,
            icon=Icon(icon),
            buttons=[
                Button(title="Ok", on_pressed=on_ok),
                Button(title="skip", on_pressed=on_skip),
                Button(title="Snooze", on_pressed=on_snooze),
            ],
        )
        await asyncio.sleep(sleep_duration[0])
        # After a snooze, reset to the regular interval for the next cycle
        sleep_duration[0] = reminder_interval


if __name__ == "__main__":
    custom_remindtime = 3600  # 1 hour
    custom_snoozetime = 600   # 10 minutes

    print("""
----------------------------------
Reminder to look at you !
----------------------------------""")
    customize_yesno = input("Want to customize timings ? [y/n]: ")
    if customize_yesno.lower() == 'y':
        try:
            remind_input = input(f"Enter the reminder time in seconds (default: {custom_remindtime}): ")
            if remind_input:
                custom_remindtime = int(remind_input)

            snooze_input = input(f"Enter the snooze time in seconds (default: {custom_snoozetime}): ")
            if snooze_input:
                custom_snoozetime = int(snooze_input)
        except ValueError:
            print("Invalid input. Using default timings.")

    asyncio.run(
        send("There is Still Water in this world!", "Drink Water Sir!", water_bottle, custom_remindtime, custom_snoozetime)
    )

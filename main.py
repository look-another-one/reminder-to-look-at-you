import asyncio
from desktop_notifier import DesktopNotifier, Icon, Button
from pathlib import Path
from time import sleep, ctime
import json


project_root = Path(__file__).parent  # give the location of folder

alert_icon = project_root / "assets" / "alert.png"
water_bottle = project_root / "assets" / "water_bottle.png"
json_file = project_root /"log" /"data.jsonl"
notifier = DesktopNotifier()


def writing_log(taken:bool):
    with open(json_file,"a") as data:
        json.dump({"Date": ctime(), "Reminder": "Drink Water","Taken":taken},data)
        data.write("\n")
# This Func gonna send a notification based on paramaters
async def send(title: str, message: str, icon: Path):
    while True:
        await asyncio.sleep(3)
        await notifier.send(
            title=title,
            message=message,
            icon=Icon(icon),
            buttons=[
                Button(title="Ok", on_pressed=lambda: writing_log(True)),
                Button(title="skip", on_pressed=lambda: writing_log(False)),
            ],
        )


# print(project_root)
# print(ctime())

if __name__ == "__main__":
    asyncio.run(
        send("There is Still Water in this world!", "Drink Water Sir!", water_bottle)
    )


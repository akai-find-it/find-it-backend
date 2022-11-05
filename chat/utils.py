import requests


def send_notification(token, msg, user_name):
    url = "https://fcm.googleapis.com/fcm/send"
    data = {
        "to": token,
        "data": {
            "text": msg,
            "user_name": user_name,
        },
    }

    headers = {
        "Authorization": "key=AAAA1dlGh9k:APA91bH___L0oEEiZCmyTLUpyRY8aH8OWyJFEeP5km61lv4SqIMoOnvHSXyC9EyLODpyFu-H7lEvDdAAeLyQeJy_fDPI-nHJnhO1Kkw-XQAB9wPdffafoLQcFURvx65mabAC14lgsOGq"
    }
    x = requests.post(url, headers=headers, json=data)
    print(x.__dict__)


# send_notification(
#     "cyySE3OCRmmicBG6YRc3O7:APA91bGfEYoVGsAsU1vRiLzAuk5214q3EN_7sJqfyFrnZ0UncNZ_Zn_AemL3JXhawyxSlHskJVhWklL_eEHg1HyPUlHMCzEuaV3SHRnC54iOEi1TWySDpqxqcGU0Fo3rlqyAMjSLVfkZ",
#     "elo mordo",
# )


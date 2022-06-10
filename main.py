from webserver import keep_alive
import requests

channelID = 911854140320264252
headers = {
    "authorization":
    "OTgyNjU3MzQzNjU5NTk3OTA0.G57rzz.PKYS7GhCf4BmwBdzsTEPeY0aS6cCHhOaVM93SU"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})

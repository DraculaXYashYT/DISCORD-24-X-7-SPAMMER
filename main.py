from webserver import keep_alive
import requests

channelID = 911854140320264252 911855735493763083
headers = {
    "authorization":
    "OTgzNzcxNDY5MzgzMzQ0MTI4.GTzNvo.6sv10NRqpNmmG6rZspMzQtTWPlKPmlaxixqMbo"
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

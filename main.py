from webserver import keep_alive
import requests

channelID = 959892011618541588
headers = {
    "authorization":
    "ODYzMTg3NTk2NDY5NjAwMjg3.Yj9Jtg.xJ3RNfI2nVz32Zx_EnVkteNAqiE"
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

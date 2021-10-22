import requests


url = "https://discord.com/api/v8/applications/889509294536544266/commands"

# This is an example CHAT_INPUT or Slash Command, with a type of 1
json = {
    "name": "bothelp",
    "type": 1,
    "description": "Все команды",
    "options": [
        {
            "name": "animal",
            "description": "The type of animal",
            "type": 3,
            "required": True,
            "choices": [
                {
                    "name": "Dog",
                    "value": "animal_dog"
                },
                {
                    "name": "Cat",
                    "value": "animal_cat"
                },
                {
                    "name": "Penguin",
                    "value": "animal_penguin"
                }
            ]
        },
        {
            "name": "only_smol",
            "description": "Whether to show only baby animals",
            "type": 5,
            "required": False
        }
    ]
}

# For authorization, you can use either your bot token
headers = {
    "Authorization": "ODg5NTA5Mjk0NTM2NTQ0MjY2.YUiSFg.oVZ--7tu_qMuqx8XzycpI9hVkms"
}


r = requests.post(url, headers=headers, json=json)

Discord-Bot-1.0
================

## Overview
I built this project to learn how to work with the Discord API and external REST APIs using Python. The point of this project was to create a simple bot that listens to user commands with either a greeting or a random meme.

## Demo
<img width="1452" height="190" alt="image" src="https://github.com/user-attachments/assets/bf109c8e-d15c-4bb5-8f23-da9b68cd0d18" />

<img width="1457" height="622" alt="image" src="https://github.com/user-attachments/assets/8b1a4279-6792-4e7d-94dd-c57577569a97" />


Here's the bot responding to `$hello` and `$meme` in a live server.

## Setup

1. Clone the repo
```bash
   git clone https://github.com/seunseun66/Discord-Bot-1.0.git
   cd Discord-Bot-1.0
```

2. Install dependencies
```bash
   pip install discord.py requests python-dotenv
```

3. Create a Discord bot and get your token from the [Discord Developer Portal](https://discord.com/developers/applications)

4. Create a `.env` file in the project folder and add your token:
5. Run the bot
```bash
   python bot.py
```

## How it works
The bot first starts by connecting to Discord using the 'discord.py' library. Once it's connected it continuously listens for messages sent in the server. Whenever a new message is sent, the bot actively checks if the message comes from itself. This happens because it prevents the bot from responding to its own messages and creating an infinite response loop.

From there, the bot looks for supported commands:

- If a user enters "$hello" the bot responds with a greeting.
- If a user enters "$meme" the bot calls the get_meme() function.

The "get_meme()" function sends an HTTP GET request to the Meme API:

```python
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    return response.json()['url']
```

The API returns a JSON object with information about a random meme. The function extracts just the image URL and returns it, and the bot posts that URL directly into the Discord channel for users to view.

## Why I used this approach
The get_meme function helps keep the code organized instead of putting everything into one place. The function is responsible for getting the meme, while the rest of the bot handles the user commands. This makes it easier for me to update the bot or if I wanted to add more APIs.

I also used the discord event system because it lets the bot respond whenever a new message is sent. This helps prevent the bot from always checking for messages.

## What I learned
- Building applications with the Discord API
- Making HTTP requests to external APIs
- Event-driven programming
- Processing JSON responses

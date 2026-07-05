# Discord-Bot-1.0

# Overview

I built this project to learn how to work with the Discord API and external REST APIs using Python. The point of this project was to create a simple bot that listens to user commands with either a greeting or a random meme

# How it works

The bot first starts by connecting to Discord using the 'discord.py' library. Once it's connected its continuously listens for messages sent in the server. Whenever a new message is sent, the bot actively checks if the message comes from itself. This happens because it prevents the bot from responding to its own messages and creating an infinite response loop.

From there, the bot looks for supported commands:

-If a user enters "$hello" the bot responds with a greeting.

-If a user enters "$meme" the bot calls the get_meme() function.

The "get_meme()" Function sends an HTTP GET request to the Meme Api. The api then returns a JSON object having infromation about a random meme. The function only extracts the image URL and returns it, and then the bot posts that URL directly into the Discord channel for users to view.

# Why I used this approach

The get_meme function helps keep the code organized instead of putting everything into one place. The function is responsible for getting the meme, while the rest of the bot handles the user commands. This makes it easier for me to update the bot or if I wanted to add more APIs.

I also used the discord event systems because it lets the bot respond whenever a new message is sent. This helps prevent the bot from always checking for messages.

# What I learned

-Building applications with the Discord API

-Making HTTP requests to external APIs

-Event-driven programming

-Processing JSON responses

#

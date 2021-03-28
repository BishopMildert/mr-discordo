# mr-discordo

### A simple Discord bot.

#### Summary

A Discord bot that randomly replies with set phrases. More functionality can be added on top.

## Deploying:

- For the code to work locally you need a Discord [developer's account](https://discord.com/developers/).

- Install the required modules: `python3 -m pip install -U discord.py` and `python-dotenv`.

- Ensure that you have your Discord developer keys inside your `.env` file.

- To deploy the bot simply execute the `deploy.sh` or run `main.py` file within the repo's directory. Please note that the `deploy.sh` script has two different deployment methods, normal and background deployment. Check the file for more info.

#### Notes
- `core` contains additional functionalities for the bot, e.g reading for txt file and selecting random quote.

- `main` is used for connecting to Discord servers and executing Discord API functionalities.

#### References
 [tutorial](https://www.freecodecamp.org/news/create-a-discord-bot-with-python/)

[remote deploy](https://janakiev.com/blog/python-background/)
from os import environ

# To use manual values, change these
default_bot_token = ""
default_sudo_chat_id =  -1001335262387
default_owner_id = 1209574071

# Don't change these value
bot_token = environ.get("BOT_TOKEN", default_bot_token)
sudo_chat_id = int(environ.get("SUDO_CHAT_ID", default_sudo_chat_id))
owner_id = int(environ.get("OWNER_ID", default_owner_id))

import os

class Config(object):
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
	LD_DOMAIN = os.environ.get("LD_DOMAIN", "") # Without https:// or http://
	SECRET = os.environ.get("SECRET", "")
	ADMIN_IDS = os.environ.get("ADMIN_IDS", "") # ==> Enter Admin Chat IDs here !!
	PIC = os.environ.get("PIC", "")
	HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
	HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "")
	HEROKU_EMAIL = os.environ.get("HEROKU_EMAIL", "")
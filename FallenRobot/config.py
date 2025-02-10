class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 25395782
    API_HASH = "3c0f6066a07142d664690cfd34447450"

    CASH_API_KEY = "UHEHI3OQIOEBQ67A"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key
#new
    DATABASE_URL = "postgresql://neondb_owner:npg_0y9BdJIXatsK@ep-fragrant-moon-a8c4d82y-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
#old 
    #DATABASE_URL = "postgres://ndyctrmp:gW7_AJFZdV7w7mN48rNlSqiWm-W8l2Oj@john.db.elephantsql.com/ndyctrmp"
    
    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://nitinkumardhundhara:DARKXSIDE78@cluster0.wdive.mongodb.net/?retryWrites=true&w=majority"
    
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA/f051105a-1f86-4d69-95ae-92663bd7d058/anim=false,width=450/00059-3393265683.jpeg"

    SUPPORT_CHAT = "GenAnimeOfcChat"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7236820256:AAF3bDTr2cispwYXevolB4ReRlACLFwoTsE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "LS20TNCESP4C"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7086472788  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

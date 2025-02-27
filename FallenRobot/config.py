class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 22225430
    API_HASH = "4c5c28abd62233ef4b993fb972f83262"

    CASH_API_KEY = "UHEHI3OQIOEBQ67A"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key
#new
    DATABASE_URL = "postgresql://neondb_owner:npg_0y9BdJIXatsK@ep-fragrant-moon-a8c4d82y-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
#old 
    #DATABASE_URL = "postgres://ndyctrmp:gW7_AJFZdV7w7mN48rNlSqiWm-W8l2Oj@john.db.elephantsql.com/ndyctrmp"
    
    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://Mrdaxx123:Mrdaxx123@cluster0.q1da65h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    
    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://static.zerochan.net/Makima.full.3797768.png"

    SUPPORT_CHAT = "Anime_Nova_Chat_Group"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "8104462190:AAFejQ2wF5EfMfrZ8Zk3ndHZAsCtSlctex0"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "LS20TNCESP4C"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6039119180  # User id of your telegram account (Must be integer)

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

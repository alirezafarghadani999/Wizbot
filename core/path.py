class PATH:
    _DataBase = "./public/DataBase/"
    
    PATHS = {
        "User_DataBase": _DataBase + "User.db",
        "Channel_Database": _DataBase + "Channel.db", 
    }

    FOLDERTREE = {
        "public":{
            "DataBase"
            }
    }

    def __init__(self) -> None:
        pass
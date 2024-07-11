from core.path import PATH
from core.Database import Sqlite
import os

class Setup:

    def __init__(self) -> None:

        if self.is_first() :

            self.Udb = Sqlite(db_name=PATH.PATHS["User_DataBase"])
            self.CHdb = Sqlite(db_name=PATH.PATHS["Channel_Database"])
            self.FOLDERTREE = PATH.FOLDERTREE



    def __User_db_create(self):
        self.Udb.create_table(
            "users",{
                "id":"INTEGER PRIMARY KEY",
                "user_id":"INTEGER",
                "sub":"BOOLEAN",
                "sub_exp":"DATE"
            }
            )
        self.Udb.create_database(
            "user_channels",{
                "id":"INTEGER PRIMARY KEY",
                "owner_id":"INTEGER",
            }
        )

        self.Udb.create_database(
            "channels",{
                "id":"INTEGER",
                "topic":"TEXT",
                "AI_POST_GENERETOR":"BOOL",
            }
        )


    def _create_folder_tree(self):

        FOLDERTREE = self.FOLDERTREE
        
        def create_folders(FOLDERTREE,path=""):
            for FOLDER in FOLDERTREE:
                print(os.path.join(path,FOLDER))
                os.mkdir(os.path.join(path,FOLDER))
                try:
                    create_folders(FOLDERTREE[FOLDER],os.path.join(path,FOLDER))
                except:
                    pass



    def _check_file_tree(self):
        pass

    def is_first(self) -> bool :
        return False
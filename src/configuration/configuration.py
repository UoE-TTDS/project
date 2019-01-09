import configparser
import os

class Configuration:
    def __init__(self):
        self.__dataset_path = ''
        self.__metadata_database = ''
        self.__lyrics_database = ''

    @staticmethod
    def from_file(path):
        config = configparser.ConfigParser()
        config.read(path)
        if not config.sections():
            print(f'Config was not loaded correctly!! Check the path: {path}, currently reading from {os.getcwd()}')
        paths = config['Paths']
        c = Configuration()
        c.__dataset_path = paths['Dataset']
        c.__metadata_database = paths['MetadataDatabase']
        c.__lyrics_database = paths['LyricsDatabase']
        return c

    @property
    def dataset_path(self):
        return self.__dataset_path

    @property
    def metadata_database(self):
        return self.__metadata_database

    @property
    def lyrics_database(self):
        return self.__lyrics_database

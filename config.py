import os

class Config:
    '''
    The main configuration class for the application
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')


class ProdConfig(Config):
    '''
    Class that forms the subclass of the Config class and Debug-effective in the production environment

    Args:
        Config class
    '''
    pass


class DevConfig(Config):
    '''
    Class that is a subclass of the Config class and Debug-effective in the development phase/environment

    Args:
        Config class
    '''
    DEBUG=True


config_options={
    'development': DevConfig,
    'production': ProdConfig
}
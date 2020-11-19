class SystemConfig:

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
        'user': 'root',
        'password': 'tbctbctbc',
        'host': 'localhost',
        'db_name': 'fortune'
    })


Config = SystemConfig

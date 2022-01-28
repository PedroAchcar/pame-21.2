from app.sensive import Sensive as sv


class Config():
    DEBUG = sv.DEBUG
    SQLALCHEMY_DATABASE_URI = sv.SQLALCHEMY_DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = sv.SQLALCHEMY_TRACK_MODIFICATIONS
    JSON_SORT_KEYS = sv.JSON_SORT_KEYS

    MAIL_SERVER = sv.MAIL_SERVER
    MAIL_PORT = sv.MAIL_PORT
    MAIL_USERNAME = sv.MAIL_USERNAME
    MAIL_USE_TLS = sv.MAIL_USE_TLS
    MAIL_USE_SSL = sv.MAIL_USE_SSL

    MAIL_PASSWORD = sv.MAIL_PASSWORD

    JWT_SECRET_KEY = sv.JWT_SECRET_KEY
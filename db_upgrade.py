#!flask/bin/python
from migrate.versioning import api
from config import SQLALCHEMY_DATABASE_URI
from comfig import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI)
v = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_DATABASE_URI)
print('Current database version: ' + str(v))

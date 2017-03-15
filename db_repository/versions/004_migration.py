from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
article = Table('article', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR),
    Column('tags', VARCHAR),
    Column('bodyTxt', VARCHAR),
    Column('date', DATETIME),
    Column('user_id', INTEGER),
)

article = Table('article', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String),
    Column('tags', String),
    Column('bodytxt', String),
    Column('date', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['article'].columns['bodyTxt'].drop()
    post_meta.tables['article'].columns['bodytxt'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['article'].columns['bodyTxt'].create()
    post_meta.tables['article'].columns['bodytxt'].drop()

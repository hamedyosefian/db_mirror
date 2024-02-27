"""seed database table

Revision ID: ba247ffa6d5d
Revises: 79ce85f3f520
Create Date: 2024-02-27 10:00:08.111739

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.models.databases import Database

# revision identifiers, used by Alembic.
revision: str = 'ba247ffa6d5d'
down_revision: Union[str, None] = '79ce85f3f520'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(Database.__table__,
                   [
                       {
                           'id': 1,
                           'name': 'Mobedu Database',
                           'host': '192.168.0.20',
                           'port': 9001,
                           'username': 'postgres',
                           'password': 'RkIG6lXKVgBFaZDA5hgsCx5AY0RlKfCJio2VohgtWTsyusPAT02163aO16kbFhM2',
                           'database_name': 'mobedu',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },
                       {
                           'id': 2,
                           'name': 'Landing Exam Database',
                           'host': '192.168.0.20',
                           'port': 9002,
                           'username': 'postgres',
                           'password': 'oGbHTzygVGtksrNnLHyMTjkWdEQ1WIzAwfYPb8feFEVUYrxOM2hu8DqkXc5Z8QOT',
                           'database_name': 'mobexam',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },
                       {
                           'id': 3,
                           'name': 'Mobtakeran Automation Database',
                           'host': '192.168.0.20',
                           'port': 9003,
                           'username': 'postgres',
                           'password': 'nZeMeg9a7IdFu5PTX1D7mIG7qLnkdJUmf8u8XZJFVX0JkwlFA5748DGbrIfwh1zj',
                           'database_name': 'automob',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },

                       {
                           'id': 4,
                           'name': 'Register Exam Database',
                           'host': '192.168.0.20',
                           'port': 9004,
                           'username': 'postgres',
                           'password': 'mmnhaIyV2mKsqPg9L08HB7TRvgQe2uE1eVUKtEbJteoeMZ3e555iXJTRZNxjgyiX',
                           'database_name': 'regexam',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },
                       {
                           'id': 5,
                           'name': 'Tosifi Exam Database',
                           'host': '192.168.0.25',
                           'port': 9000,
                           'username': 'clt00ev2d000fa4n6cemo8ggf',
                           'password': 'phuVsa81CQSpQMIq7c7ZJnvq',
                           'database_name': 'exam',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },
                       {
                           'id': 6,
                           'name': 'Energy Database',
                           'host': '89.38.215.145',
                           'port': 9001,
                           'username': 'postgres',
                           'password': 'dbTlKU8kfvINuVKgmYFawk5QMIDVeeue0DSqHitoWgFNpDyiJBE0hxxaOj9Bqq78',
                           'database_name': 'ae_db',
                           'differential_backup_cron': '*/15 * * * *',
                           'full_backup_cron': '30 0 * * *',
                       },
                   ]
                   )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

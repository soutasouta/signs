"""empty message

Revision ID: b39a7256101b
Revises: 
Create Date: 2020-11-12 11:49:19.895926

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b39a7256101b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ID_UNIQUE', table_name='result')
    op.drop_table('result')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result',
    sa.Column('ID', mysql.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('f_result', mysql.VARCHAR(length=45), nullable=True),
    sa.PrimaryKeyConstraint('ID'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('ID_UNIQUE', 'result', ['ID'], unique=True)
    # ### end Alembic commands ###
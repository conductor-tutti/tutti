"""empty message

Revision ID: 34ffe21c48bc
Revises: 339c1e718dce
Create Date: 2014-08-29 01:26:52.415000

"""

# revision identifiers, used by Alembic.
revision = '34ffe21c48bc'
down_revision = '339c1e718dce'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('awards',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('musician_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['musician_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('musician_category')
    op.drop_table('musician_major')
    op.drop_table('musician')
    op.add_column('user', sa.Column('category', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('major', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('phrase', sa.String(length=255), nullable=True))
    op.drop_column('user', 'userid')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('userid', mysql.VARCHAR(length=15), nullable=True))
    op.drop_column('user', 'phrase')
    op.drop_column('user', 'major')
    op.drop_column('user', 'category')
    op.create_table('musician',
    sa.Column('category_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('major_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('phrase', mysql.VARCHAR(length=50), nullable=True),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('musician_major',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.create_table('musician_category',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('name', mysql.VARCHAR(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'utf8',
    mysql_engine=u'InnoDB'
    )
    op.drop_table('awards')
    ### end Alembic commands ###

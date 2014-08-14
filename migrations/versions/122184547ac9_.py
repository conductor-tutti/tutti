"""empty message

Revision ID: 122184547ac9
Revises: 206594167c34
Create Date: 2014-08-12 16:14:40.062000

"""

# revision identifiers, used by Alembic.
revision = '122184547ac9'
down_revision = '206594167c34'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('member')
    ### end Alembic commands ###

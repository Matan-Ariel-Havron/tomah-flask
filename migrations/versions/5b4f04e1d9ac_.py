"""empty message

Revision ID: 5b4f04e1d9ac
Revises: 7973b58c96d3
Create Date: 2020-06-11 12:03:42.643441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b4f04e1d9ac'
down_revision = '7973b58c96d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('site_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reference', sa.String(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('reference')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('site_data')
    # ### end Alembic commands ###

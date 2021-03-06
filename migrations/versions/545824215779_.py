"""empty message

Revision ID: 545824215779
Revises: edc596434b9d
Create Date: 2020-06-10 16:38:37.791196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '545824215779'
down_revision = 'edc596434b9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

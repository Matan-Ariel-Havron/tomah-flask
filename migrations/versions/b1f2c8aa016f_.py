"""empty message

Revision ID: b1f2c8aa016f
Revises: f8f9f2282944
Create Date: 2020-06-10 15:33:39.361632

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b1f2c8aa016f'
down_revision = 'f8f9f2282944'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'epx_answer',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('answer', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('answer', 'wil_answer',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('answer', 'wil_answer',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('answer', 'question_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('answer', 'epx_answer',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###

"""empty message

Revision ID: a956cb15eba0
Revises: fe9815fe4133
Create Date: 2020-07-13 15:06:39.318586

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a956cb15eba0'
down_revision = 'fe9815fe4133'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationship_object',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('slave', sa.Integer(), nullable=False),
    sa.Column('master', sa.Integer(), nullable=False),
    sa.Column('slave_description', sa.String(length=120), nullable=True),
    sa.Column('master_description', sa.String(length=120), nullable=True),
    sa.Column('relationship_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['master'], ['user.id'], ),
    sa.ForeignKeyConstraint(['slave'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id', 'slave', 'master')
    )
    op.drop_table('relationships')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('relationships',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slave', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('master', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('slave_description', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('master_description', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('relationship_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['master'], ['user.id'], name='relationships_master_fkey'),
    sa.ForeignKeyConstraint(['slave'], ['user.id'], name='relationships_slave_fkey'),
    sa.PrimaryKeyConstraint('id', 'slave', 'master', name='relationships_pkey')
    )
    op.drop_table('relationship_object')
    # ### end Alembic commands ###

"""custom_categories

Revision ID: 97dd03d6ec76
Revises: a6fbbe49d0bd
Create Date: 2016-07-30 11:47:46.826744

"""

# revision identifiers, used by Alembic.
revision = '97dd03d6ec76'
down_revision = 'a6fbbe49d0bd'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table(
        'user_categories',
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table(
        'alert_categories',
        sa.Column('alert_id', sa.Integer(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['alert_id'], ['alerts.id'], ),
        sa.ForeignKeyConstraint(['category_id'], ['categories.id'], )
    )
    op.alter_column(
        u'alerts', 'age', existing_type=sa.INTEGER(), nullable=False)
    op.drop_column(u'alerts', 'shelter')
    op.drop_column(u'alerts', 'food')
    op.drop_column(u'alerts', 'other')
    op.drop_column(u'alerts', 'clothes')
    op.drop_column(u'users', 'shelter')
    op.drop_column(u'users', 'food')
    op.drop_column(u'users', 'other')
    op.drop_column(u'users', 'clothes')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        u'users',
        sa.Column('clothes', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(
        u'users',
        sa.Column('other', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(
        u'users',
        sa.Column('food', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(
        u'users',
        sa.Column('shelter', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column(
        u'alerts',
        sa.Column('clothes', sa.BOOLEAN(), autoincrement=False, nullable=False)
    )
    op.add_column(
        u'alerts',
        sa.Column('other', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column(
        u'alerts',
        sa.Column('food', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.add_column(
        u'alerts',
        sa.Column('shelter', sa.BOOLEAN(), autoincrement=False, nullable=False)
    )
    op.alter_column(
        u'alerts', 'age', existing_type=sa.INTEGER(), nullable=True)
    op.drop_table('alert_categories')
    op.drop_table('user_categories')
    op.drop_table('categories')
    ### end Alembic commands ###

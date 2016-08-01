"""Creates schema

Revision ID: 868b58a77f8f
Revises: None
Create Date: 2016-08-01 13:06:10.016958

"""

# revision identifiers, used by Alembic.
revision = '868b58a77f8f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('mark',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('value', sa.SMALLINT(), nullable=True),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('value')
    )
    op.create_table('role',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=80), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('surname', sa.String(length=255), nullable=False),
        sa.Column('password', sa.String(length=255), nullable=True),
        sa.Column('active', sa.Boolean(), nullable=True),
        sa.Column('confirmed_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_table('category',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('friend',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('surname', sa.String(length=50), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('meal',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role_user',
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.create_table('participation',
        sa.Column('friend_id', sa.Integer(), nullable=False),
        sa.Column('meal_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['friend_id'], ['friend.id'], ),
        sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], ),
        sa.PrimaryKeyConstraint('friend_id', 'meal_id')
    )
    op.create_table('recipe',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('date', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('reference', sa.String(length=255), nullable=True),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('category_id', sa.Integer(), nullable=True),
        sa.Column('mark_id', sa.Integer(), nullable=True),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
        sa.ForeignKeyConstraint(['mark_id'], ['mark.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('cooking',
        sa.Column('recipe_id', sa.Integer(), nullable=False),
        sa.Column('meal_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['meal_id'], ['meal.id'], ),
        sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
        sa.PrimaryKeyConstraint('recipe_id', 'meal_id')
    )


def downgrade():
    op.drop_table('cooking')
    op.drop_table('recipe')
    op.drop_table('participation')
    op.drop_table('role_user')
    op.drop_table('meal')
    op.drop_table('friend')
    op.drop_table('category')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('mark')

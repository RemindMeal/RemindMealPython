"""empty message

Revision ID: 568116da84fc
Revises: 5a3cf7f71786
Create Date: 2015-08-22 10:49:52.337559

"""

# revision identifiers, used by Alembic.
revision = '568116da84fc'
down_revision = '5a3cf7f71786'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    ### end Alembic commands ###

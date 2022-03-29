"""auto votes

Revision ID: e21e35428c1c
Revises: 2824be0f38a4
Create Date: 2022-03-29 14:16:43.738263

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'e21e35428c1c'
down_revision = '2824be0f38a4'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id')
                    )


def downgrade():
    op.drop_table('votes')

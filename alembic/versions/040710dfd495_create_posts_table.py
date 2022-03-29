"""create posts table

Revision ID: 040710dfd495
Revises: 
Create Date: 2022-03-29 12:41:16.731398

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '040710dfd495'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("posts", sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False))


def downgrade():
    op.drop_table("posts")

"""add latest few columns to posts table

Revision ID: 2824be0f38a4
Revises: 747aa117b970
Create Date: 2022-03-29 14:11:47.071486

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2824be0f38a4'
down_revision = '747aa117b970'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, server_default="TRUE"))
    op.add_column("posts",
                  sa.Column("created_at", sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")))


def downgrade():
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")

"""add foreign-key to posts table

Revision ID: 747aa117b970
Revises: 1144f478b22a
Create Date: 2022-03-29 14:06:27.279564

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '747aa117b970'
down_revision = '1144f478b22a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", local_cols=["owner_id"],
                          remote_cols=["id"], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("posts_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")

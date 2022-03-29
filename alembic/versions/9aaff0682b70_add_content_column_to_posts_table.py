"""add content column to posts table

Revision ID: 9aaff0682b70
Revises: 040710dfd495
Create Date: 2022-03-29 12:50:19.809684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9aaff0682b70'
down_revision = '040710dfd495'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))


def downgrade():
    op.drop_column("posts", "content")

"""add users table

Revision ID: 1144f478b22a
Revises: 9aaff0682b70
Create Date: 2022-03-29 12:54:36.612314

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1144f478b22a'
down_revision = '9aaff0682b70'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users",
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text("now()"),
                              nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )


def downgrade():
    op.drop_table("users")

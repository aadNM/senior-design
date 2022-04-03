"""Add configuration values table.

Reason:
Add a table to store configuration values that might be modified during the
execution of the Rasa X server.

Revision ID: acd80348b093
Revises: 99e6a52a2eb7

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "acd80348b093"
down_revision = "d9d7b3d9cadd"
branch_labels = None
depends_on = None

TABLE_NAME = "configuration"


def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column("key", sa.String(255), nullable=False),
        sa.Column("value", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("key"),
    )


def downgrade():
    op.drop_table(TABLE_NAME)

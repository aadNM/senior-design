"""FIXED Remove is_unflagged field from Conversations

Reason:
We no longer track conversations which have been unflagged, as we don't use the data.

Revision ID: 8a260b1a797a
Revises: d5160f2d00b8

"""
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "8a260b1a797a"
down_revision = "d5160f2d00b8"
branch_labels = None
depends_on = None


def upgrade():
    # This is done because 0.25.0 release issue
    # Check the issue #1983
    if migration_utils.table_has_column("conversation_event", "is_unflagged"):
        migration_utils.drop_column("conversation_event", "is_unflagged")


def downgrade():
    migration_utils.create_column(
        "conversation_event", sa.Column("is_unflagged", sa.Boolean(), nullable=False)
    )

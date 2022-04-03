"""Add `in_training_data` column to `conversation_session` table.

Reason:
Whether conversations are in training data or not is determined based on the
conversations' constituent sessions. This migration adds a new column to store this
information.

Revision ID: 68a8a531a5ee
Revises: 37b34bf8df43

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "68a8a531a5ee"
down_revision = "37b34bf8df43"
branch_labels = None
depends_on = None

COLUMN_NAME = "in_training_data"
TABLE_NAME = "conversation_session"


def upgrade():
    migration_utils.create_column(
        TABLE_NAME, sa.Column(COLUMN_NAME, sa.Boolean(), default=True)
    )


def downgrade():
    migration_utils.drop_column(TABLE_NAME, COLUMN_NAME)

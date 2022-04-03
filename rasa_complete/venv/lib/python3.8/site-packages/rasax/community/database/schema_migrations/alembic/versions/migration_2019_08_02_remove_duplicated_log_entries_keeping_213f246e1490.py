"""Remove duplicated log entries keeping only most recent unique user messages.

Reason:
To avoid many entries of the same text in the database,
and to increase the log query speed, we need to delete all
rows with the same hash except the latest one.

Revision ID: 213f246e1490
Revises: 45546b047abe

"""

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "213f246e1490"
down_revision = "45546b047abe"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.delete_duplicate_rows("message_log", ["hash"])


def downgrade():
    pass

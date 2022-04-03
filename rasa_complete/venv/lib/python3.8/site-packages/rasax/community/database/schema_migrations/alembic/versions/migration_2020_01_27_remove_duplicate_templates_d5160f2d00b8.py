"""Remove duplicate responses.

Reason:
https://github.com/RasaHQ/rasa-x/issues/1808

Revision ID: d5160f2d00b8
Revises: 8893bba2a522

"""

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "d5160f2d00b8"
down_revision = "8893bba2a522"
branch_labels = None
depends_on = None

TABLE_NAME = "template"


def upgrade():
    migration_utils.delete_duplicate_rows(
        TABLE_NAME, ["project_id", "template", "text"]
    )


def downgrade():
    pass

"""Remove duplicate responses.

Reason:
Rasa X 0.25.0 made adding responses with the same text impossible.
The bug appeared again in 0.27.0, and this migration ensures
that responses that have been potentially added in the meantime are removed again.

Revision ID: b092b0fe590d
Revises: 73f46e0b7789

"""
import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "b092b0fe590d"
down_revision = "73f46e0b7789"
branch_labels = None
depends_on = None

TABLE_NAME = "template"


def upgrade():
    migration_utils.delete_duplicate_rows(
        TABLE_NAME, ["project_id", "template", "text"]
    )


def downgrade():
    pass

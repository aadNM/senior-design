"""Add column to `lookup_table` table which contains the number of elements in a table.

Reason:
Lookup tables can contain a lot of entries. Counting them every time could lead to a
performance problem.

Revision ID: 6fce9679db61
Revises: 35a1c7937594

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "6fce9679db61"
down_revision = "35a1c7937594"
branch_labels = None
depends_on = None

NEW_COLUMN = "number_of_elements"


def upgrade():
    migration_utils.create_column(
        "lookup_table", sa.Column(NEW_COLUMN, sa.Integer, nullable=True)
    )


def downgrade():
    migration_utils.drop_column("lookup_table", NEW_COLUMN)

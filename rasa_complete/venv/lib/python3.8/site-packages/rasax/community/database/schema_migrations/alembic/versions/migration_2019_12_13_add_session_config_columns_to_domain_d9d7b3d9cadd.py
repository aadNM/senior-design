"""Add `session_expiration_time` and `carry_over_slots_to_new_session` columns to table `domain`.

Reason:
The introduction of conversation sessions means the domain contains an additional
config section `session_config` whose values need to be stored.

Revision ID: d9d7b3d9cadd
Revises: 99e6a52a2eb7

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "d9d7b3d9cadd"
down_revision = "99e6a52a2eb7"
branch_labels = None
depends_on = None

TABLE_NAME = "domain"

# tuples of (column name, column type)
COLUMNS = [("session_expiration_time", sa.Float()), ("carry_over_slots", sa.Boolean())]


def upgrade():
    for column_name, column_type in COLUMNS:
        migration_utils.create_column(TABLE_NAME, sa.Column(column_name, column_type))


def downgrade():
    for column_name, _ in COLUMNS:
        migration_utils.drop_column(TABLE_NAME, column_name)

"""Addition of `is_default` and `description` columns to `user_role` table.

Reason:
The `user_role` table receives two additional columns: `description` and `is_default`.

Revision ID: 9d4a16758d6e
Revises: 2a216ed121dd

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "9d4a16758d6e"
down_revision = "2a216ed121dd"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.create_column(
        "user_role", sa.Column("description", sa.String(255), nullable=True)
    )
    migration_utils.create_column(
        "user_role", sa.Column("is_default", sa.Boolean, default=False)
    )


def downgrade():
    migration_utils.drop_column("user_role", "description")
    migration_utils.drop_column("user_role", "is_default")

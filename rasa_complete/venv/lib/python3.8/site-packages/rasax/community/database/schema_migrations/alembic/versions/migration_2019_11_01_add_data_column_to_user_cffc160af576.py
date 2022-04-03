"""Add data column to User

Reason:
Add a `data` column to `rasa_x_user`. This column can be used by Rasa X API
users to store arbitrary JSON data.

Revision ID: cffc160af576
Revises: 3b15f8e56784

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "cffc160af576"
down_revision = "a813c6c15a4c"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.create_column("rasa_x_user", sa.Column("data", sa.Text()))


def downgrade():
    migration_utils.drop_column("rasa_x_user", "data")

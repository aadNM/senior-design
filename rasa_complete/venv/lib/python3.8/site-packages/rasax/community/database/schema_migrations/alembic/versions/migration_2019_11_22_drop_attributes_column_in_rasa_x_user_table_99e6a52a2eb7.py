"""Drop 'attributes' column in 'rasa_x_user' table.

Reason:
The 'attributes' column was used to store user attributes. It is not needed for
authentication and can be removed.

Revision ID: 99e6a52a2eb7
Revises: 945ef2034d57

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "99e6a52a2eb7"
down_revision = "945ef2034d57"
branch_labels = None
depends_on = None

TABLE_NAME = "rasa_x_user"
COLUMN_NAME = "attributes"


def upgrade():
    migration_utils.drop_column(TABLE_NAME, COLUMN_NAME)


def downgrade():
    migration_utils.create_column(TABLE_NAME, sa.Column(COLUMN_NAME, sa.String(255)))

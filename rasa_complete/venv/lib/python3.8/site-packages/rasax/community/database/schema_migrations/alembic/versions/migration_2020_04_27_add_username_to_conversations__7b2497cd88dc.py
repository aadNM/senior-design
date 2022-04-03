"""Add `username` field to `conversation` table.

Reason:
We need to have information about who initiated the conversation
to make it possible for users to get their conversations. In order
to achieve that, we add a `username` column which is a foreign key
that refers to the primary key `username` in the `rasa_x_user` table.

Revision ID: 7b2497cd88dc
Revises: 425bd8f628db

"""
from alembic import op
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "7b2497cd88dc"
down_revision = "425bd8f628db"
branch_labels = None
depends_on = None

TABLE_NAME = "conversation"
CREATED_BY_COLUMN = "created_by"
FOREIGN_KEY_NAME = "fk_conversation_username"


def upgrade():
    if migration_utils.get_column(TABLE_NAME, CREATED_BY_COLUMN) is None:
        migration_utils.create_column(
            TABLE_NAME, sa.Column(CREATED_BY_COLUMN, sa.String(255), nullable=True)
        )

        with op.batch_alter_table(TABLE_NAME) as batch_op:
            batch_op.create_foreign_key(
                FOREIGN_KEY_NAME, "rasa_x_user", [CREATED_BY_COLUMN], ["username"]
            )


def downgrade():
    if migration_utils.get_column(TABLE_NAME, CREATED_BY_COLUMN) is not None:
        migration_utils.drop_column(TABLE_NAME, "username")

        with op.batch_alter_table(TABLE_NAME) as batch_op:  # type: op.BatchOperations
            batch_op.drop_constraint(FOREIGN_KEY_NAME)

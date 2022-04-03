"""Delete duplicate events and add unique constraint to `conversation_event` table.

Reason:
The Rasa CLI command `rasa export` publishes events to an event broker that may be
consumed by a Rasa X instance. In order to make sure events are not saved repeatedly,
for example through repeated calling of `rasa export`, we add a composite unique
constraint on the `conversation_id`, `timestamp` and `type_name` columns of the
`conversation_event` table.

Duplicate events with the same `conversation_id`, `timestamp` and `type_name`
columns are deleted.

Revision ID: 1a712f7b70e9
Revises: 0b35090e53cf

"""

from alembic import op

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.

revision = "1a712f7b70e9"
down_revision = "0b35090e53cf"
branch_labels = None
depends_on = None

TABLE_NAME = "conversation_event"
CONSTRAINT_NAME = "conversation_event_uq"


def upgrade():
    # delete duplicate rows
    rows_with_unique_constraint = ["conversation_id", "timestamp", "type_name"]

    message = (
        "This migration will remove duplicate events in the "
        "`conversation_event` table. These events likely are 'action_listen' events "
        "at the beginning of conversations, and can be safely removed."
    )
    migration_utils.delete_duplicate_rows(
        TABLE_NAME, rows_with_unique_constraint, message=message
    )

    # add composite UNIQUE constraint
    with op.batch_alter_table(TABLE_NAME) as batch_op:
        batch_op.create_unique_constraint(CONSTRAINT_NAME, rows_with_unique_constraint)


def downgrade():
    with op.batch_alter_table(TABLE_NAME) as batch_op:
        batch_op.drop_constraint(CONSTRAINT_NAME)

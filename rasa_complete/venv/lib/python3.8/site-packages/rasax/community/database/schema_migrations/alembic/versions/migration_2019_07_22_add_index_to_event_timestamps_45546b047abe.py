"""Add index to `timestamp` column in `conversation_event` table.

Reason:
We have to sort the events by their timestamp when retrieving them.
To make this fast, we need an index on the timestamp column.

Revision ID: 45546b047abe
Revises: 8b528d137850

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "45546b047abe"
down_revision = "8b528d137850"
branch_labels = None
depends_on = None


NEW_INDEX_NAME = "conv_event_timestamp_idx"


def upgrade():
    with op.batch_alter_table("conversation_event") as batch_op:
        batch_op.create_index(NEW_INDEX_NAME, ["timestamp"])


def downgrade():
    with op.batch_alter_table("conversation_event") as batch_op:
        batch_op.drop_index(NEW_INDEX_NAME)

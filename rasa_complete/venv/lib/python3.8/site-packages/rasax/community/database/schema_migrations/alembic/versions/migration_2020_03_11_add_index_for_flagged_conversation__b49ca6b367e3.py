"""Add index for flagged conversation events

Reason:
Filtering for conversations by flagged events without an index is _very_ slow,
the data is incredibly sparse.

Revision ID: b49ca6b367e3
Revises: 304e0754a200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b49ca6b367e3"
down_revision = "304e0754a200"
branch_labels = None
depends_on = None

CONVERSATION_EVENT = "conversation_event"
FLAGGED_EVENT_INDEX = "conversation_event_flag_index"


def upgrade():
    with op.batch_alter_table(CONVERSATION_EVENT) as batch_op:
        batch_op.create_index(
            FLAGGED_EVENT_INDEX,
            ["is_flagged"],
            postgresql_where=sa.text("is_flagged = TRUE"),
        )


def downgrade():
    op.drop_index(FLAGGED_EVENT_INDEX)

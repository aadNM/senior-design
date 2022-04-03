"""Indexes for faster NLU logs and training data queries.

Reason:
For faster queries on the conversation logs and the NLU training data, indexes
have to be added to the queried columns.

Revision ID: b4a9bd47b6e0
Revises: 1dfbf67d6ae2

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "b4a9bd47b6e0"
down_revision = "1dfbf67d6ae2"
branch_labels = None
depends_on = None


MESSAGE_LOG_INDEX_NAME = "message_log_idx_archived_text"
NLU_TRAINING_DATA_INDEX_NAME = "nlu_training_data_idx_hash"


def upgrade():
    try:
        with op.batch_alter_table("message_log") as batch_op:
            batch_op.create_index(MESSAGE_LOG_INDEX_NAME, ["archived", "text"])
    except Exception:
        # Some databases don't support `sa.Text()` columns as part of indexes. In that
        # case we simply skip creating the index.
        pass

    with op.batch_alter_table("nlu_training_data") as batch_op:
        batch_op.create_index("NLU_TRAINING_DATA_INDEX_NAME", ["hash"])


def downgrade():
    try:
        with op.batch_alter_table("message_log") as batch_op:
            batch_op.drop_index(MESSAGE_LOG_INDEX_NAME)
    except Exception:
        # This index might not exist for every database.
        pass

    with op.batch_alter_table("nlu_training_data") as batch_op:
        batch_op.drop_index(NLU_TRAINING_DATA_INDEX_NAME, ["hash"])

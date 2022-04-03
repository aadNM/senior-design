"""Add index to `conversation_id` column of table `conversation_event`.

Reason:
The PostgresSQL query analysis showed that queries are slow due to the
`conversation_id` field. Adding an index on this column should accelerate these
queries.

Revision ID: e3a3a2789e20
Revises: 2a216ed121dd

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "e3a3a2789e20"
down_revision = "9d4a16758d6e"
branch_labels = None
depends_on = None


NEW_INDEX_NAME = "conv_event_conv_id_idx"


def upgrade():
    with op.batch_alter_table("conversation_event") as batch_op:
        batch_op.create_index(NEW_INDEX_NAME, ["conversation_id"])


def downgrade():
    with op.batch_alter_table("conversation_event") as batch_op:
        batch_op.drop_index(NEW_INDEX_NAME)

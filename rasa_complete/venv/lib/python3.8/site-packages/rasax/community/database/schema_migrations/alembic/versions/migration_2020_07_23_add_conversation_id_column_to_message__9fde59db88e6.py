"""Add conversation_id column to message_log

Reason:
Add a `conversation_id` column to the `message_log` table so that we can
quickly access the conversation ID from the NLU inbox, without having to look
up the ID via the associated event ID (which would be slower).

Revision ID: 9fde59db88e6
Revises: 473b15141809

"""
from alembic import op
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "9fde59db88e6"
down_revision = "473b15141809"
branch_labels = None
depends_on = None

TABLE = "message_log"
COLUMN = "conversation_id"
FK_NAME = "fk_message_log_conv_id"


def upgrade():
    if not migration_utils.get_column(TABLE, COLUMN):
        with op.batch_alter_table(TABLE) as batch_op:
            batch_op.add_column(sa.Column(COLUMN, sa.String(255)))
            batch_op.create_foreign_key(
                FK_NAME, "conversation", [COLUMN], ["sender_id"]
            )


def downgrade():
    if migration_utils.get_column(TABLE, COLUMN):
        with op.batch_alter_table(TABLE) as batch_op:
            batch_op.drop_constraint(FK_NAME)
            batch_op.drop_column(COLUMN)

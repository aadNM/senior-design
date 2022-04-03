"""Add index for `created_by` foreign key.

Reason:
We are filtering on `created_by` in each conversation screen request,
so indexing `created_by` will speed up the query execution.

Revision ID: ac3fba1c2b86
Revises: 7b2497cd88dc

"""
from alembic import op
import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "ac3fba1c2b86"
down_revision = "7b2497cd88dc"
branch_labels = None
depends_on = None

TABLE_NAME = "conversation"
NEW_INDEX_NAME = "conversation_created_by_idx"


def upgrade():
    if not migration_utils.index_exists(TABLE_NAME, NEW_INDEX_NAME):
        with op.batch_alter_table(TABLE_NAME) as batch_op:
            batch_op.create_index(NEW_INDEX_NAME, ["created_by"])


def downgrade():
    if migration_utils.index_exists(NEW_INDEX_NAME, TABLE_NAME):
        with op.batch_alter_table(TABLE_NAME) as batch_op:
            batch_op.drop_index(NEW_INDEX_NAME)

"""Remove slot value index completely

Reason:
In migration 6738be716c3f, we created an index for the `slot_value` column of
`conversation_event`. A problem was reported where the migration failed on
PostgreSQL because some SlotSet events had very large values, and the default
index type (B-Tree) could not be applied to them. The migration was then
modified so that this index was no longer created. Then, migration 3fbc8790762e
was added, which 1) deleted the index in case it existed (this was the case for
users which were able to run the migration successfully) and 2) created a new
index, using GIN instead when running on PostgreSQL. However, in some cases the
GIN index creation failed. For that reason, this migration was added, which
directly removes the index for the `slot_value` field (only if it exists, which
it shouldn't for most users).

Revision ID: ef93223786ba
Revises: 3fbc8790762e

"""
from alembic import op

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "ef93223786ba"
down_revision = "3fbc8790762e"
branch_labels = None
depends_on = None

TABLE_NAME = "conversation_event"
INDEX_NAME = "conversation_slot_value_index"


def upgrade():
    # Remove the index, only if it's there
    if migration_utils.index_exists(TABLE_NAME, INDEX_NAME):
        with op.batch_alter_table(TABLE_NAME) as batch_op:
            batch_op.drop_index(INDEX_NAME)


def downgrade():
    pass

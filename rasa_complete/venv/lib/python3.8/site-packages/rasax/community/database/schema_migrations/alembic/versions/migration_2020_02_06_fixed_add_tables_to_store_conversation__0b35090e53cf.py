"""FIXED Add tables to store conversation tags.

Reason:
This migration adds new tables, "conversation_tag" and "conversation_to_tag_mapping"
which allows Rasa X to store arbitrary colored tags for conversations.

Revision ID: 0b35090e53cf
Revises: 8a260b1a797a

"""
from alembic import op
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "0b35090e53cf"
down_revision = "8a260b1a797a"
branch_labels = None
depends_on = None


CONVERSATION_TAG = "conversation_tag"

CONVERSATION_TO_TAG_MAPPING = "conversation_to_tag_mapping"
TAG_ID_INDEX = "cttm_tag_id_index"
CONVERSATION_ID_INDEX = "cttm_conversation_id_index"


def upgrade():
    # This is done because 0.25.0 release issue
    # Check the issue #1983
    if migration_utils.table_exists(CONVERSATION_TAG):
        return

    op.create_table(
        CONVERSATION_TAG,
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("value", sa.String(255), nullable=False, unique=True),
        # Limited to "6" here since it's a HEX color code
        sa.Column("color", sa.String(6), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )

    # add sequence for Oracle DB compatibility
    migration_utils.create_sequence(CONVERSATION_TAG)

    op.create_table(
        CONVERSATION_TO_TAG_MAPPING,
        sa.Column("tag_id", sa.Integer(), nullable=False),
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["tag_id"], [f"{CONVERSATION_TAG}.id"]),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.UniqueConstraint(
            "tag_id", "conversation_id", name="cttm_unique_tag_conversation"
        ),
    )

    # use shorter suffix for this sequence to fit the 30-char limit
    migration_utils.create_sequence(CONVERSATION_TO_TAG_MAPPING, suffix="seq")

    with op.batch_alter_table(CONVERSATION_TO_TAG_MAPPING) as batch_op:
        batch_op.create_index(TAG_ID_INDEX, ["tag_id"])
        batch_op.create_index(CONVERSATION_ID_INDEX, ["conversation_id"])


def downgrade():
    op.drop_table(CONVERSATION_TAG)

    with op.batch_alter_table(CONVERSATION_TO_TAG_MAPPING) as batch_op:
        batch_op.drop_index(TAG_ID_INDEX)
        batch_op.drop_index(CONVERSATION_ID_INDEX)
    op.drop_table(CONVERSATION_TO_TAG_MAPPING)

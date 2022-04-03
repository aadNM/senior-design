"""Add columns and indices for NLU/Core confidences

Reason:
Add additional columns for min/max NLU and Core confidences
Add indices for new columns to speed up search

Revision ID: 37b34bf8df43
Revises: b49ca6b367e3

"""
import json

from alembic import op
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "37b34bf8df43"
down_revision = "b49ca6b367e3"
branch_labels = None
depends_on = None


CONVERSATION = "conversation"
CONVERSATION_EVENT = "conversation_event"

MINIMUM_ACTION_CONFIDENCE = "minimum_action_confidence"
MAXIMUM_ACTION_CONFIDENCE = "maximum_action_confidence"
MINIMUM_INTENT_CONFIDENCE = "minimum_intent_confidence"
MAXIMUM_INTENT_CONFIDENCE = "maximum_intent_confidence"

MIN_ACTION_INDEX = "c_min_action_index"
MAX_ACTION_INDEX = "c_max_action_index"
MIN_INTENT_INDEX = "c_min_intent_index"
MAX_INTENT_INDEX = "c_max_intent_index"

COLUMNS = [
    (MAXIMUM_ACTION_CONFIDENCE, sa.Float()),
    (MINIMUM_INTENT_CONFIDENCE, sa.Float()),
    (MAXIMUM_INTENT_CONFIDENCE, sa.Float()),
]

INDEX_TO_COLUMN = [
    (MIN_INTENT_INDEX, MINIMUM_INTENT_CONFIDENCE),
    (MAX_INTENT_INDEX, MAXIMUM_INTENT_CONFIDENCE),
    (MIN_ACTION_INDEX, MINIMUM_ACTION_CONFIDENCE),
    (MAX_ACTION_INDEX, MAXIMUM_ACTION_CONFIDENCE),
]

BULK_SIZE = 500


def upgrade():
    for column_name, column_type in COLUMNS:
        migration_utils.create_column(CONVERSATION, sa.Column(column_name, column_type))

    with op.batch_alter_table(CONVERSATION) as batch_op:
        for index_name, column_name in INDEX_TO_COLUMN:
            batch_op.create_index(index_name, [column_name])

    extract_information_from_existing_data()


def extract_information_from_existing_data():
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    conversation_table = migration_utils.get_reflected_table(CONVERSATION, session)
    conversation_event_table = migration_utils.get_reflected_table(
        CONVERSATION_EVENT, session
    )

    for conversation in session.query(conversation_table).yield_per(BULK_SIZE):

        min_intent_confidence = 1.0
        max_intent_confidence = 0.0
        min_action_confidence = 1.0
        max_action_confidence = 0.0

        for row in (
            session.query(conversation_event_table)
            .filter(
                conversation_event_table.c.conversation_id == conversation.sender_id
            )
            .yield_per(BULK_SIZE)
        ):
            data = json.loads(row.data)

            if row.type_name == "user":
                confidence = (
                    data.get("parse_data", {}).get("intent", {}).get("confidence")
                )

                try:
                    confidence = float(confidence)
                except (ValueError, TypeError):
                    continue

                min_intent_confidence = min(min_intent_confidence, confidence)
                max_intent_confidence = max(max_intent_confidence, confidence)
            elif row.type_name == "action":
                confidence = data.get("confidence")

                try:
                    confidence = float(confidence)
                except (ValueError, TypeError):
                    continue

                min_action_confidence = min(min_action_confidence, confidence)
                max_action_confidence = max(max_action_confidence, confidence)

        if min_intent_confidence == 1.0:
            min_intent_confidence = None
        if max_intent_confidence == 0.0:
            max_intent_confidence = None
        if min_action_confidence == 1.0:
            min_action_confidence = None
        if max_action_confidence == 0.0:
            max_action_confidence = None

        query = (
            sa.update(conversation_table)
            .where(conversation_table.c.sender_id == conversation.sender_id)
            .values(
                minimum_intent_confidence=min_intent_confidence,
                maximum_intent_confidence=max_intent_confidence,
                minimum_action_confidence=min_action_confidence,
                maximum_action_confidence=max_action_confidence,
            )
        )
        session.execute(query)

    session.commit()


def downgrade():
    with op.batch_alter_table(CONVERSATION) as batch_op:
        for info in INDEX_TO_COLUMN:
            batch_op.drop_index(info[0])

    for column in COLUMNS:
        migration_utils.drop_column(CONVERSATION, column[0])

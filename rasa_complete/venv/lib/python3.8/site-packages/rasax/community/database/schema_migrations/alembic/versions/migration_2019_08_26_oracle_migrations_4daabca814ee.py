"""Oracle Migrations.

Reason:
Oracle is a particularly picky database which requires a couple of changes before
Rasa X can run with it. Changes we had to do:

- Databases like MySQL or Oracle require a certain length for `VARCHAR` types.
  This migration fixes the length for all `String` columns. This is already done
  in the initial migration because this would otherwise break the migrations for Oracle.
  However, all database systems should have the same types so this migration applies the
  changes to existing databases.
- Oracle does not support index names with a length > 32. Hence, we have to rename the
  chars to shorter names.
- Oracle does not support auto-incrementing keys. We have to use sequences to get this
  working in Oracle.

Revision ID: 4daabca814ee
Revises: 6fce9679db61

"""

from alembic import op
import sqlalchemy as sa
import logging
from typing import Dict, Text, Union, List

import rasax.community.database.schema_migrations.alembic.utils as migration_utils


logger = logging.getLogger(__name__)

# revision identifiers, used by Alembic.
revision = "4daabca814ee"
down_revision = "6fce9679db61"
branch_labels = None
depends_on = None

FIXED_SIZE_COLUMNS = "fixed"
VARIABLE_SIZED_COLUMNS = "variable"

COLUMN_NAME_KEY = "name"
COLUMN_SIZE_KEY = "size"

migrations: Dict[Text, Dict[Text, List[Union[Text, Dict[Text, Union[int, Text]]]]]] = {
    "analytics_cache": {
        FIXED_SIZE_COLUMNS: ["cache_key"],
        VARIABLE_SIZED_COLUMNS: ["result"],
    },
    "chat_tokens": {FIXED_SIZE_COLUMNS: ["bot_name", "description", "token"]},
    "conversation": {
        FIXED_SIZE_COLUMNS: ["sender_id", "latest_input_channel"],
        VARIABLE_SIZED_COLUMNS: ["evaluation"],
    },
    "password": {FIXED_SIZE_COLUMNS: ["password"]},
    "platform_feature": {FIXED_SIZE_COLUMNS: ["feature_name"]},
    "project": {
        FIXED_SIZE_COLUMNS: ["project_id", "team", "active_model", "handoff_url"],
        VARIABLE_SIZED_COLUMNS: ["config"],
    },
    "user_role": {FIXED_SIZE_COLUMNS: ["role", "description"]},
    "conversation_action_metadata": {FIXED_SIZE_COLUMNS: ["conversation_id", "action"]},
    "conversation_entity_metadata": {FIXED_SIZE_COLUMNS: ["conversation_id", "entity"]},
    "conversation_event": {
        FIXED_SIZE_COLUMNS: [
            "conversation_id",
            "type_name",
            "intent_name",
            "action_name",
            "policy",
        ],
        VARIABLE_SIZED_COLUMNS: ["data", "evaluation"],
    },
    "conversation_intent_metadata": {FIXED_SIZE_COLUMNS: ["conversation_id", "intent"]},
    "conversation_message_correction": {
        FIXED_SIZE_COLUMNS: ["conversation_id", "intent"]
    },
    "message_correction": {FIXED_SIZE_COLUMNS: ["conversation_id", "intent"]},
    "conversation_policy_metadata": {FIXED_SIZE_COLUMNS: ["conversation_id", "policy"]},
    "conversation_session": {FIXED_SIZE_COLUMNS: ["conversation_id"]},
    "conversation_statistic": {FIXED_SIZE_COLUMNS: ["project_id"]},
    "domain": {FIXED_SIZE_COLUMNS: ["project_id", "path"]},
    "entity_synonym": {
        FIXED_SIZE_COLUMNS: ["name", "synonym", "project_id", "filename"]
    },
    "environment": {FIXED_SIZE_COLUMNS: ["name", "project", "url", "token"]},
    "intent": {FIXED_SIZE_COLUMNS: ["name", "mapped_to", "project_id"]},
    "lookup_table": {
        FIXED_SIZE_COLUMNS: ["name", "filename", "project_id"],
        VARIABLE_SIZED_COLUMNS: ["elements"],
    },
    "model": {FIXED_SIZE_COLUMNS: ["hash", "name", "path", "project_id", "version"]},
    "permission": {FIXED_SIZE_COLUMNS: ["project", "role_id", "permission"]},
    "rasa_x_user": {
        FIXED_SIZE_COLUMNS: [
            "username",
            "name_id",
            "team",
            "project",
            "authentication_mechanism",
            "attributes",
            {COLUMN_NAME_KEY: "api_token", COLUMN_SIZE_KEY: 4000},
        ],
        VARIABLE_SIZED_COLUMNS: ["password_hash"],
    },
    "regex_feature": {
        FIXED_SIZE_COLUMNS: ["name", "filename", "project_id", "pattern"]
    },
    "user_goal": {FIXED_SIZE_COLUMNS: ["name", "project_id"]},
    "conversation_action_statistic": {FIXED_SIZE_COLUMNS: ["action", "project_id"]},
    "conversation_entity_statistic": {FIXED_SIZE_COLUMNS: ["entity", "project_id"]},
    "conversation_intent_statistic": {FIXED_SIZE_COLUMNS: ["intent", "project_id"]},
    "conversation_policy_statistic": {FIXED_SIZE_COLUMNS: ["policy", "project_id"]},
    "domain_action": {FIXED_SIZE_COLUMNS: ["action"]},
    "domain_entity": {FIXED_SIZE_COLUMNS: ["entity"]},
    "domain_intent": {
        FIXED_SIZE_COLUMNS: ["intent", "triggered_action"],
        VARIABLE_SIZED_COLUMNS: ["ignore_entities", "use_entities"],
    },
    "domain_slot": {FIXED_SIZE_COLUMNS: ["slot", "initial_value", "type", "values"]},
    "message_log": {
        FIXED_SIZE_COLUMNS: ["hash", "intent"],
        VARIABLE_SIZED_COLUMNS: ["intent_ranking", "entities", "text"],
    },
    "model_tag": {FIXED_SIZE_COLUMNS: ["tag"]},
    "nlu_evaluation": {
        FIXED_SIZE_COLUMNS: ["model_id"],
        VARIABLE_SIZED_COLUMNS: ["report"],
    },
    "nlu_training_data": {
        FIXED_SIZE_COLUMNS: [
            "hash",
            "intent",
            "annotator_id",
            "project_id",
            "filename",
        ],
        VARIABLE_SIZED_COLUMNS: ["text"],
    },
    "single_use_token": {
        FIXED_SIZE_COLUMNS: [
            {COLUMN_NAME_KEY: "token", COLUMN_SIZE_KEY: 4000},
            "username",
        ]
    },
    "story": {
        FIXED_SIZE_COLUMNS: ["name", "user", "filename"],
        VARIABLE_SIZED_COLUMNS: ["story"],
    },
    "template": {
        FIXED_SIZE_COLUMNS: ["template", "annotator_id", "project_id"],
        VARIABLE_SIZED_COLUMNS: ["content", "text"],
    },
    "temporary_intent_example": {FIXED_SIZE_COLUMNS: ["example_hash"]},
    "user_goal_intent": {FIXED_SIZE_COLUMNS: ["intent_name"]},
    "user_role_mapping": {FIXED_SIZE_COLUMNS: ["username", "role"]},
    "nlu_evaluation_prediction": {FIXED_SIZE_COLUMNS: ["text", "intent", "predicted"]},
    "nlu_training_data_entity": {FIXED_SIZE_COLUMNS: ["entity", "value", "extractor"]},
}


def upgrade():
    # Migrate string columns to Oracle compatible types
    for table_name, new_types in migrations.items():
        if migration_utils.table_exists(table_name):
            # Migrate columns which should get a fixed sized string type
            with op.batch_alter_table(table_name) as batch_op:
                logger.debug(
                    f"Start migrating fixed sized text columns for table "
                    f"'{table_name}'."
                )
                for column in new_types.get(FIXED_SIZE_COLUMNS, []):
                    if isinstance(column, str):
                        column_name = column
                        column_dict = {COLUMN_NAME_KEY: column}
                    else:
                        column_name = column[COLUMN_NAME_KEY]
                        column_dict = column

                    target_type = sa.String(column_dict.get(COLUMN_SIZE_KEY, 255))

                    # skip if the column type is already correct
                    if migration_utils.is_column_of_type(
                        table_name, column_name, type(target_type)
                    ):
                        logger.debug(
                            f"Skipping migration of column '{column_name}' of table "
                            f"'{table_name}'. The column is already of target type "
                            f"'{target_type}'."
                        )
                        continue

                    batch_op.alter_column(
                        column_dict[COLUMN_NAME_KEY],
                        type_=target_type,
                        existing_type=sa.String(),
                    )

            # Migrate columns which should get a variable sized string type
            logger.debug(
                f"Start migrating variable-length text columns for table "
                f"'{table_name}'."
            )
            modifications = []
            for column in new_types.get(VARIABLE_SIZED_COLUMNS, []):
                target_type = sa.Text()
                # skip if the column type is already correct
                if migration_utils.is_column_of_type(
                    table_name, column, type(target_type)
                ):
                    logger.debug(
                        f"Skipping migration of column '{column_name}' of table "
                        f"'{table_name}'. The column is already of target type "
                        f"'{target_type}'."
                    )
                    continue

                modifications.append(
                    migration_utils.ColumnTransformation(
                        column, [target_type], {"nullable": True}
                    )
                )

            migration_utils.modify_columns(table_name, modifications)

    # Rename indexes which have been too long
    migration_utils.rename_or_create_index(
        "conversation_event",
        "conversation_event_conversation_id_index",
        "conv_event_conv_id_idx",
        ["conversation_id"],
    )
    migration_utils.rename_or_create_index(
        "conversation_event",
        "conversation_event_timestamp_index",
        "conv_event_timestamp_idx",
        ["timestamp"],
    )

    # Rename wrong index name
    from rasax.community.database.schema_migrations.alembic.versions.migration_2019_07_05_indexes_for_logs_and_nlu_training_data_b4a9bd47b6e0 import (
        NLU_TRAINING_DATA_INDEX_NAME,
    )

    migration_utils.rename_or_create_index(
        "nlu_training_data",
        "NLU_TRAINING_DATA_INDEX_NAME",
        NLU_TRAINING_DATA_INDEX_NAME,
        ["hash"],
    )

    # Fix wrong index
    from rasax.community.database.schema_migrations.alembic.versions.migration_2019_07_22_add_index_to_event_timestamps_45546b047abe import (
        NEW_INDEX_NAME,
    )

    migration_utils.rename_or_create_index(
        "conversation_event", NEW_INDEX_NAME, NEW_INDEX_NAME, ["timestamp"]
    )

    # Create `Sequence`s which provide the auto-incrementing id for Oracle
    tables_with_sequences = [
        "conversation_event",
        "message_log",
        "template",
        "story",
        "nlu_training_data",
        "nlu_training_data_entity",
        "regex_feature",
        "lookup_table",
        "domain",
        "domain_action",
        "domain_intent",
        "domain_entity",
        "domain_slot",
        "intent",
        "temporary_intent_example",
        "user_goal",
        "model",
        "nlu_evaluation",
        "nlu_evaluation_prediction",
    ]
    for table in tables_with_sequences:
        migration_utils.create_sequence(table)


def downgrade():
    # don't downgrade these changes, they were updated in the initial migrations
    pass

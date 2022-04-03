"""Rename column `carry_over_slots_to_new_session` and index `nlu_train_data_ent_orig_val_idx`.

Reason:
The column `carry_over_slots` was originally named `carry_over_slots_to_new_session`.
This migration renames the column on databases that still have the longer column name.

In order to comply with Oracle 12c Enterprise Edition Release 12.1.0.2.0 requirements,
schema, table, and column names must be <= 30 characters.
https://docs.oracle.com/database/121/SQLRF/sql_elements008.htm#SQLRF51129

Revision ID: 8893bba2a522
Revises: acd80348b093

"""
from alembic import op
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "8893bba2a522"
down_revision = "22e9e6ea593c"
branch_labels = None
depends_on = None

TABLE_NAME = "domain"
OLD_COLUMN_NAME = "carry_over_slots_to_new_session"
NEW_COLUMN_NAME = "carry_over_slots"


def upgrade():
    # rename column
    if migration_utils.table_has_column(TABLE_NAME, OLD_COLUMN_NAME):
        with op.batch_alter_table(TABLE_NAME) as batch_op:
            batch_op.alter_column(OLD_COLUMN_NAME, new_column_name=NEW_COLUMN_NAME)

    # rename index
    migration_utils.rename_or_create_index(
        "nlu_training_data_entity",
        "nlu_train_data_ent_orig_val_idx",
        "nlu_train_dat_ent_orig_val_idx",
        ["original_value"],
    )


def downgrade():
    # don't downgrade the table name, since we changed it in the initial migrations
    pass

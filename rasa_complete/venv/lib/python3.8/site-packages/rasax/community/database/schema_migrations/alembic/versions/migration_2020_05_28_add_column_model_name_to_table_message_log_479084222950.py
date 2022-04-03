"""Add `model` column to table `message_log`.

Reason:
Message logs no longer reference a model by ID, as models can be deleted. Instead,
message logs now reference the model name of the active model at the time the log is
created or updated. To achieve this, a new column `model` is added to the
`message_log` table. The previous column `model_id` and foreign key constraint to the
`model` table are removed.

Existing message logs are associated with a dummy model named 'unavailable'.

Revision ID: 479084222950
Revises: eb2b98905e7e

"""
import sqlalchemy as sa
from alembic import op
from alembic.operations import BatchOperations

import rasax.community.database.schema_migrations.alembic.utils as migration_utils
import rasax.community.constants as constants

# revision identifiers, used by Alembic.
revision = "479084222950"
down_revision = "eb2b98905e7e"
branch_labels = None
depends_on = None

TABLE = "message_log"
MODEL_NAME_COLUMN = "model"

MODEL_ID_COLUMN = "model_id"
MODEL_ID_FOREIGN_KEY_NAME = "fk_model_id"


def upgrade():
    with op.batch_alter_table(TABLE) as batch_op:
        # delete old foreign key
        delete_model_foreign_key(batch_op)

        # we can safely drop the old column, as the previous `model_id` did not
        # reference the model that was actually used
        batch_op.drop_column(MODEL_ID_COLUMN)

        # create new column
        create_column(batch_op)


def delete_model_foreign_key(batch_op: BatchOperations) -> None:
    fk_name = migration_utils.get_foreign_key(
        TABLE, referred_table="model", constrained_column="model_id"
    )
    migration_utils.drop_constraint(fk_name, batch_op)


def create_column(batch_op: BatchOperations) -> None:
    batch_op.add_column(
        sa.Column(
            MODEL_NAME_COLUMN,
            sa.String(255),
            server_default=constants.UNAVAILABLE_MODEL_NAME,
        )
    )


def downgrade():
    with op.batch_alter_table(TABLE) as batch_op:
        # drop `model` column
        batch_op.drop_column(MODEL_NAME_COLUMN)

        # create the `model_id` column
        batch_op.add_column(sa.Column(MODEL_ID_COLUMN, sa.String(255)))

        # create the `model` FK constraint
        batch_op.create_foreign_key(
            MODEL_ID_FOREIGN_KEY_NAME, "model", [MODEL_ID_COLUMN], ["id"]
        )

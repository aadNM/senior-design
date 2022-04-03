"""Support for individually unfeaturized entities in domain.

Reason:
https://github.com/RasaHQ/rasa/pull/3655 adds the option to featurize entities
individually for each intent. This led to changes in the format of the intent
configuration which have to be reflected in the database.

Revision ID: 1dfbf67d6ae2
Revises: 59b7be3ad5fc

"""
from alembic import op
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "1dfbf67d6ae2"
down_revision = "59b7be3ad5fc"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("domain_intent") as batch_op:
        batch_op.add_column(sa.Column("ignore_entities", sa.Text(), nullable=True))

        # Change datatype of `use_entities` column from `Boolean` to `Text` since
        # we now store a JSON object in it.
        migration_utils.modify_columns(
            "domain_intent",
            [
                migration_utils.ColumnTransformation(
                    "use_entities",
                    new_column_kwargs={"type_": sa.Text(), "nullable": True},
                    modify_from_column_value=str,
                )
            ],
        )


def downgrade():
    with op.batch_alter_table("domain_intent") as batch_op:
        batch_op.drop_column("ignore_entities")
        # Change datatype of `use_entities` column from `Text` to `Boolean`.
        migration_utils.modify_columns(
            "domain_intent",
            [
                migration_utils.ColumnTransformation(
                    "use_entities",
                    new_column_kwargs={"type_": sa.String(), "nullable": True},
                    modify_from_column_value=lambda x: True if x else False,
                )
            ],
        )

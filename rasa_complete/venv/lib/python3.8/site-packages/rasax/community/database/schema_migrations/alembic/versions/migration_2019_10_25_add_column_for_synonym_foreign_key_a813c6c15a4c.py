"""Add a column to store the foreign key of a used synonym.

Reason:
In the training data screen you want to see which synonym is used by an entity.
For that we need a relationship from the entity to the used synonym.

Revision ID: a813c6c15a4c
Revises: a86c9fac00fa

"""
from alembic import op
import sqlalchemy as sa
from rasax.community.database.schema_migrations.alembic import utils as migration_utils


# revision identifiers, used by Alembic.
from sqlalchemy.orm import Session

revision = "a813c6c15a4c"
down_revision = "a86c9fac00fa"
branch_labels = None
depends_on = None


TABLE_NAME = "nlu_training_data_entity"
NEW_COLUMN_NAME = "entity_synonym_id"
FOREIGN_KEY_NAME = "fk_entity_synonym_id"


def upgrade():
    with op.batch_alter_table(TABLE_NAME) as batch_op:  # type: op.BatchOperations
        batch_op.add_column(sa.Column(NEW_COLUMN_NAME, sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            FOREIGN_KEY_NAME,
            "entity_synonym",
            [NEW_COLUMN_NAME],
            ["id"],
            ondelete="SET NULL",
        )

    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    set_synonym_references_for_old_mapped_values(session)


def set_synonym_references_for_old_mapped_values(session: Session) -> None:
    synonym_value_table = migration_utils.get_reflected_table(
        "entity_synonym_value", session
    )
    synonym_values = session.execute(synonym_value_table.select()).fetchall()

    entities_table = migration_utils.get_reflected_table(
        "nlu_training_data_entity", session
    )
    for synonym_value in synonym_values:
        update_query = (
            sa.update(entities_table)
            .where(entities_table.c.original_value == synonym_value.name)
            .values(entity_synonym_id=synonym_value.entity_synonym_id)
        )
        session.execute(update_query)
    session.commit()


def downgrade():
    with op.batch_alter_table(TABLE_NAME) as batch_op:  # type: op.BatchOperations
        batch_op.drop_column(NEW_COLUMN_NAME)
        batch_op.drop_constraint(FOREIGN_KEY_NAME)

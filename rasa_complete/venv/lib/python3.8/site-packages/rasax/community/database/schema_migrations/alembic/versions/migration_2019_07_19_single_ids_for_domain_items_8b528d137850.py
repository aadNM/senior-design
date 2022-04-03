"""Add single column id for domain objects such as actions, slots, etc.

Reason:
Currently the primary keys for these tables are composite keys of the associated domain
and the name of the object (e.g. the action name). If we don't want to use the domain
id in our API, we need single column primary keys to identify an object.

Revision ID: 8b528d137850
Revises: b4a9bd47b6e0

"""
import warnings

from alembic import op
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "8b528d137850"
down_revision = "b4a9bd47b6e0"
branch_labels = None
depends_on = None


def upgrade():
    # Filter warnings for inconsistent state of primary keys
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sa.exc.SAWarning)
        with op.batch_alter_table("domain_action") as batch_op:
            batch_op.alter_column("id", new_column_name="domain_id")
            batch_op.add_column(sa.Column("action_id", sa.Integer, primary_key=True))
            migration_utils.create_primary_key(
                batch_op, "domain_action", ["action_id"], "domain_action_pk"
            )
        with op.batch_alter_table("domain_intent") as batch_op:
            batch_op.alter_column("id", new_column_name="domain_id")
            batch_op.add_column(sa.Column("intent_id", sa.Integer, primary_key=True))
            migration_utils.create_primary_key(
                batch_op, "domain_intent", ["intent_id"], "domain_intent_pk"
            )
        with op.batch_alter_table("domain_entity") as batch_op:
            batch_op.alter_column("id", new_column_name="domain_id")
            batch_op.add_column(sa.Column("entity_id", sa.Integer, primary_key=True))
            migration_utils.create_primary_key(
                batch_op, "domain_entity", ["entity_id"], "domain_entity_pk"
            )
        with op.batch_alter_table("domain_slot") as batch_op:
            batch_op.alter_column("id", new_column_name="domain_id")
            batch_op.add_column(sa.Column("slot_id", sa.Integer, primary_key=True))
            migration_utils.create_primary_key(
                batch_op, "domain_slot", ["slot_id"], "domain_slot_pk"
            )


def downgrade():
    with op.batch_alter_table("domain_action") as batch_op:
        migration_utils.create_primary_key(
            batch_op, "domain_action", ["domain_id", "action"]
        )
        batch_op.drop_column("action_id")
        batch_op.alter_column("domain_id", new_column_name="id")

    with op.batch_alter_table("domain_intent") as batch_op:
        migration_utils.create_primary_key(
            batch_op, "domain_intent", ["domain_id", "intent"]
        )
        batch_op.drop_column("intent_id")
        batch_op.alter_column("domain_id", new_column_name="id")

    with op.batch_alter_table("domain_entity") as batch_op:
        migration_utils.create_primary_key(
            batch_op, "domain_entity", ["domain_id", "entity"]
        )
        batch_op.drop_column("entity_id")
        batch_op.alter_column("domain_id", new_column_name="id")

    with op.batch_alter_table("domain_slot") as batch_op:
        migration_utils.create_primary_key(
            batch_op, "domain_slot", ["domain_id", "slot"]
        )
        batch_op.drop_column("slot_id")
        batch_op.alter_column("domain_id", new_column_name="id")

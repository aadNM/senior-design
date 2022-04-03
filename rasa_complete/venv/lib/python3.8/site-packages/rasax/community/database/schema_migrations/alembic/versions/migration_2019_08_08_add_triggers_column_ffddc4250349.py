"""Add a column for `triggers` to the domain intents.

Reason:
When using the `MappingPolicy` users can define triggers for each intent which are
used to trigger certain actions. Rasa X has to store this information.

Revision ID: ffddc4250349
Revises: 213f246e1490

"""
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "ffddc4250349"
down_revision = "213f246e1490"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.create_column(
        "domain_intent", sa.Column("triggered_action", sa.String(255), nullable=True)
    )


def downgrade():
    migration_utils.drop_column("domain_intent", "triggered_action")

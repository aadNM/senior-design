"""Add `rasa_environment` column to `conversation_event` table.

Reason:
The Pika event consumer now consumes events from all environments. In order to keep
track of an event's origin we add a new column to the `conversation_event` table.

This new column `rasa_environment` stores the `app_id` message property of any incoming
RabbitMQ event.

Revision ID: a86c9fac00fa
Revises: 3b15f8e56784

"""

import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils
import rasax.community.constants as constants

# revision identifiers, used by Alembic.
revision = "a86c9fac00fa"
down_revision = "3b15f8e56784"
branch_labels = None
depends_on = None

TABLE_NAME = "conversation_event"
COLUMN_NAME = "rasa_environment"


def upgrade():
    migration_utils.create_column(
        TABLE_NAME,
        sa.Column(
            COLUMN_NAME,
            sa.String(255),
            server_default=constants.DEFAULT_RASA_ENVIRONMENT,
        ),
    )


def downgrade():
    migration_utils.drop_column(TABLE_NAME, COLUMN_NAME)

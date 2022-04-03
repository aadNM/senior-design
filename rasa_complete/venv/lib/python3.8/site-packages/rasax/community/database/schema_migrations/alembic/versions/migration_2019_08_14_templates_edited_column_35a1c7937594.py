"""Add `edited_since_last_training` column to `template` table.

Reason:
The user should be able to see which templates were edited since they trained the last
model. To do this fast, we add another column which indicates whether a template was
included in the latest model training.

Revision ID: 35a1c7937594
Revises: ffddc4250349

"""
import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "35a1c7937594"
down_revision = "ffddc4250349"
branch_labels = None
depends_on = None

NEW_COLUMN_NAME = "edited_since_last_training"


def upgrade():
    migration_utils.create_column(
        "template", sa.Column(NEW_COLUMN_NAME, sa.Boolean, default=True)
    )


def downgrade():
    migration_utils.drop_column("template", NEW_COLUMN_NAME)

"""Add `extractor` column to table `nlu_training_data_entity`.

Reason:
The `nlu_training_data_entity` table receives an additional column `extractor` which
holds the name of the module of the module that extracted the entity.

Revision ID: 59b7be3ad5fc
Revises: e3a3a2789e20

"""

import sqlalchemy as sa

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "59b7be3ad5fc"
down_revision = "e3a3a2789e20"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.create_column(
        "nlu_training_data_entity",
        sa.Column("extractor", sa.String(255), nullable=True),
    )


def downgrade():
    migration_utils.drop_column("nlu_training_data_entity", "extractor")

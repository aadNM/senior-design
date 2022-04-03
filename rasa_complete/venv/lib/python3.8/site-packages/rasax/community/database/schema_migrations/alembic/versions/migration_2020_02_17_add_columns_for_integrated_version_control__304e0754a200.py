"""Add columns for the updated Integrated Version Control features.

Reasons:
- When the target branch of a connected Git repository is protected, the UI should
  disable the button to push changes to the target branch directly. This information
  about the repository has to be stored.
- Rasa X should show which user annotated training data and hence was responsible
  that the state of Integrated Version Control switched to orange / red. We only need
  to store the first annotator and the time of the annotation.

Revision ID: 304e0754a200
Revises: 0b35090e53cf

"""

from alembic import op
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "304e0754a200"
down_revision = "6738be716c3f"
branch_labels = None
depends_on = None

TABLE_NAME = "git_repository"
TARGET_BRANCH_PROTECTED = "is_target_branch_protected"
FIRST_ANNOTATOR_ID = "first_annotator_id"
FIRST_ANNOTATED_AT = "first_annotated_at"

FOREIGN_KEY_NAME = "fk_git_annotator_username"


def upgrade():
    migration_utils.create_column(
        TABLE_NAME, sa.Column(TARGET_BRANCH_PROTECTED, sa.Boolean())
    )
    migration_utils.create_column(
        TABLE_NAME, sa.Column(FIRST_ANNOTATOR_ID, sa.String(255))
    )
    migration_utils.create_column(TABLE_NAME, sa.Column(FIRST_ANNOTATED_AT, sa.Float()))

    with op.batch_alter_table(TABLE_NAME) as batch_op:
        batch_op.create_foreign_key(
            FOREIGN_KEY_NAME, "rasa_x_user", [FIRST_ANNOTATOR_ID], ["username"]
        )


def downgrade():
    migration_utils.drop_column(TABLE_NAME, TARGET_BRANCH_PROTECTED)
    migration_utils.drop_column(TABLE_NAME, FIRST_ANNOTATOR_ID)
    migration_utils.drop_column(TABLE_NAME, FIRST_ANNOTATED_AT)

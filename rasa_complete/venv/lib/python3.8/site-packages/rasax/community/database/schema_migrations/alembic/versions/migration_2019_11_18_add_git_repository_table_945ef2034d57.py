"""Add `git_repository` table.

Reason:
As part of the developer workflow feature users can connect their Rasa X server to a
git repository. To do so, we have to store the credentials in the database.

Revision ID: 945ef2034d57
Revises: 3b15f8e56784

"""
from alembic import op
import sqlalchemy as sa
import rasax.community.database.schema_migrations.alembic.utils as migration_utils


# revision identifiers, used by Alembic.
revision = "945ef2034d57"
down_revision = "cffc160af576"
branch_labels = None
depends_on = None

TABLE_NAME = "git_repository"


def upgrade():
    op.create_table(
        TABLE_NAME,
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("repository_url", sa.Text(), nullable=False),
        sa.Column("ssh_key", sa.Text(), nullable=True),
        sa.Column("git_service", sa.String(255), nullable=True),
        sa.Column("git_service_access_token", sa.Text(), nullable=True),
        sa.Column("target_branch", sa.String(255), nullable=True),
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
    )

    migration_utils.create_sequence(TABLE_NAME)

    from rasax.community.services.user_service import ADMIN

    migration_utils.add_new_permission_to(ADMIN, "git.*")


def downgrade():
    op.drop_table(TABLE_NAME)

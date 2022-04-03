"""Add missing permissions for `tester` and `annotator` roles.

Reason:
Both `tester` and `annotator` cannot have conversations because
the currently active model needs to be fetched and both roles
don't have a permission to do that.

Revision ID: 425bd8f628db
Revises: 36fa577b374d

"""
import rasax.community.database.schema_migrations.alembic.utils as migration_utils
from rasax.community.services.user_service import TESTER, ANNOTATOR


# revision identifiers, used by Alembic.
revision = "425bd8f628db"
down_revision = "36fa577b374d"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.add_new_permission_to(ANNOTATOR, "models.view.*")
    migration_utils.add_new_permission_to(TESTER, "models.view.*")


def downgrade():
    migration_utils.delete_permission_from(ANNOTATOR, "models.view.*")
    migration_utils.delete_permission_from(TESTER, "models.view.*")

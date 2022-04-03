"""Add explicit domain.* permissions for the admin role

Reason:
Currently admin users (and only admin users) can edit the domain by default.
We want to gate more functionality (i.e. creating entities and intents) on that permission,
to separate it out from permission to annotate. As such, we need to move the permission
from a hard-coded assumption in `role_service.py` to an explicit yes/no in the database.

Revision ID: 3d91317b7460
66d1adeeec82

"""
import rasax.community.database.schema_migrations.alembic.utils as migration_utils
from rasax.community.services.user_service import ADMIN

# revision identifiers, used by Alembic.
revision = "3d91317b7460"
down_revision = "66d1adeeec82"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.add_new_permission_to(ADMIN, "domain.*")


def downgrade():
    migration_utils.delete_permission_from(ADMIN, "domain.*")

"""Add `conversations.view.metadata.get` permission to `annotator` role.

Reason:
Testers shouldn't have rights to get any conversations. That's the reason why the `metadata.get`
permission was excluded from `test_conversation.view` permission group. However, in order
to give annotators an access to conversations, we need to grant them this permission manually.

Revision ID: 473b15141809
Revises: 479084222950

"""
import rasax.community.database.schema_migrations.alembic.utils as migration_utils
from rasax.community.services.user_service import ANNOTATOR


# revision identifiers, used by Alembic.
revision = "473b15141809"
down_revision = "90b60aff4920"
branch_labels = None
depends_on = None


def upgrade():
    migration_utils.add_new_permission_to(ANNOTATOR, "conversations.view.metadata.get")


def downgrade():
    migration_utils.delete_permission_from(ANNOTATOR, "conversations.view.metadata.get")

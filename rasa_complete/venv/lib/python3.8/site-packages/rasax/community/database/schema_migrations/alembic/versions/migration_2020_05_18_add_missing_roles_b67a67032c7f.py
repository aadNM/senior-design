"""This migration comes from RBAC backport for `0.24.x`.
It is empty because all the permissions that are required for
role-based access control fixes were already added before.

Reason:
Alembic needs to know about this revision in order to
successfully upgrade from 0.24.9 to 0.28.4+.

Revision ID: b67a67032c7f
Revises: 8893bba2a522

"""

# revision identifiers, used by Alembic.
revision = "b67a67032c7f"
down_revision = "8893bba2a522"
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass

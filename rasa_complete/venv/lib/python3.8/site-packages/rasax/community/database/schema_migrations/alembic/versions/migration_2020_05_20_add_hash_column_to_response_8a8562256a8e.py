"""Add `hash` column and an index for it to `response` table.

Reason:
When adding a new response, we check if a response with the same content already exists.
Hashing the content, indexing the hash, and doing the query on the hash instead of the
content will be faster.

This migration also fixes the `content` column of existing responses. Previously, there
was a bug that allowed for the renaming of a response without adjusting the content.
This migration ensures that the `response_name` key in `content` matches the
`response_name` column.

Revision ID: 8a8562256a8e
Revises: 9e7a97234e85

"""
import json
import logging

from alembic import op
import sqlalchemy as sa

import rasax.community.utils.common as common_utils
import rasax.community.database.schema_migrations.alembic.utils as migration_utils
import rasax.community.constants as constants


# revision identifiers, used by Alembic.
revision = "8a8562256a8e"
down_revision = "9e7a97234e85"
branch_labels = None
depends_on = None

logger = logging.getLogger(__name__)

TABLE_NAME = "response"
COLUMN_NAME = "hash"
NEW_INDEX_NAME = "response_hash_index"

BULK_SIZE = 500


def upgrade():
    migration_utils.create_column(TABLE_NAME, sa.Column(COLUMN_NAME, sa.String(32)))

    with op.batch_alter_table(TABLE_NAME) as batch_op:
        batch_op.create_index(NEW_INDEX_NAME, [COLUMN_NAME])

    extract_and_fix_information_from_existing_data()

    migration_utils.delete_duplicate_rows(TABLE_NAME, ["project_id", COLUMN_NAME])


def extract_and_fix_information_from_existing_data() -> None:
    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)

    response_table = migration_utils.get_reflected_table(TABLE_NAME, session)

    logger.debug(
        "All responses will be loaded, adjusted and re-dumped. Depending on "
        "the number of responses in your database this might take a while."
    )

    for row in session.query(response_table).yield_per(BULK_SIZE):

        content = json.loads(row.content)
        response_name = row.response_name
        content[constants.RESPONSE_NAME_KEY] = response_name
        content.pop("template", None)

        content = json.dumps(content, sort_keys=True)

        query = (
            sa.update(response_table)
            .where(response_table.c.id == row.id)
            .values(content=content, hash=common_utils.get_text_hash(content))
        )
        session.execute(query)

    session.commit()


def downgrade():
    with op.batch_alter_table(TABLE_NAME) as batch_op:
        batch_op.drop_index(NEW_INDEX_NAME)

    migration_utils.drop_column(TABLE_NAME, COLUMN_NAME)

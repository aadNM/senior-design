"""Add unique ID to EntitySynonyms

Reason:
API consumers need to be able to identify and manipulate EntitySynonym objects.
Currently these objects don't have a unique ID, so this migration adds it. The
migration also separates entity synonym and their mapped values into two separate
tables, in order to avoid data duplication. Instead of storing each entity synonym
and one of its mapped values per row, now we store the entity synonyms one one table,
and the mapped values on a new table, with each mapped value having a FOREIGN KEY
that points to the entity synonym it refers to.


Based partly on: migration_2019_07_19_single_ids_for_domain_items_8b528d137850.py

Revision ID: d45a0bf21e89
Revises: 4daabca814ee

"""
import warnings

from alembic import op
import sqlalchemy as sa
import sqlalchemy.exc
from sqlalchemy.orm import Session


import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "d45a0bf21e89"
down_revision = "36c070bd6363"
branch_labels = None
depends_on = None

INDEX_NAME = "entity_synonym_value_idx_name"


def upgrade():
    # New schema:
    #
    #   EntitySynonym:
    #       Contains the reference values (i.e. what synonyms will be converted into
    #       when found in a message by the NLU functions). The string will be stored in
    #       column "name". (example: "New York")
    #
    #   EntitySynonymValue:
    #       Contains synonyms for values in EntitySynonym. The string value will be
    #       stored in column "name". (examples: "NYC", "NY")

    session = Session(bind=op.get_bind())

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=sqlalchemy.exc.SAWarning)
        # Add a unique ID to EntitySynonym
        with op.batch_alter_table("entity_synonym") as batch_op:
            batch_op.add_column(sa.Column("id", sa.Integer, primary_key=True))
            migration_utils.create_primary_key(
                batch_op, "entity_synonym", ["id"], "entity_synonym_pk"
            )

    # create sequence on this table to be used for the `id` column
    migration_utils.create_sequence("entity_synonym")

    # Create the new table for storing the entity synonym mapped values
    op.create_table(
        "entity_synonym_value",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("entity_synonym_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(
            ["entity_synonym_id"], ["entity_synonym.id"], ondelete="cascade"
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # create sequence for this new table
    migration_utils.create_sequence("entity_synonym_value")

    min_ids = set()
    synonym_value_table = migration_utils.get_reflected_table(
        "entity_synonym_value", session
    )

    for row in session.execute("select * from entity_synonym"):
        # Each reference value can be repeated various times in the table, so just
        # take the one with the smallest ID and treat that ID as the "real" one.
        min_id = session.scalar(
            "select min(id) from entity_synonym where synonym = :synonym",
            {"synonym": row["synonym"]},
        )
        min_ids.add(min_id)

        # Copy the synonyms previously stored in EntitySynonym over to
        # EntitySynonymValue
        insert_query = synonym_value_table.insert().values(
            entity_synonym_id=min_id, name=row["name"]
        )
        session.execute(insert_query)

    with op.batch_alter_table("entity_synonym") as batch_op:
        # Make column "name" have the reference value (currently, it's in
        # "synyonym"). The synonyms themselves have already been added to the
        # EntitySynonymValue table.
        batch_op.drop_column("name")
        batch_op.alter_column(
            "synonym",
            new_column_name="name",
            # The following arguments are required for MySQL
            existing_type=sa.String(),
            existing_server_default=None,
            existing_nullable=True,
        )

    # Now that the synonyms have been copied into EntitySynonymValue, and that the
    # EntitySynonym has been modified correctly, delete all repeated entries from it.
    synonym_table = migration_utils.get_reflected_table("entity_synonym", session)
    delete_query = synonym_table.delete().where(synonym_table.c.id.notin_(min_ids))
    session.execute(delete_query)

    with op.batch_alter_table("entity_synonym_value") as batch_op:
        batch_op.create_index(INDEX_NAME, ["name"])

    session.commit()


def downgrade():
    session = Session(bind=op.get_bind())

    with op.batch_alter_table("entity_synonym_value") as batch_op:
        batch_op.drop_index(INDEX_NAME)

    op.create_table(
        "entity_synonym_tmp",
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("synonym", sa.String(255), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("name", "synonym", "project_id"),
    )

    synonym_value_table = migration_utils.get_reflected_table(
        "entity_synonym_value", session
    )
    entity_synonym_values = session.execute(synonym_value_table.select()).fetchall()

    for entity_synonym_value in entity_synonym_values:
        session.execute(
            "insert into entity_synonym_tmp "
            "values (:name, :synonym, :project_id, :filename)",
            {
                "name": entity_synonym_value.name,
                "synonym": entity_synonym_value.entity_synonym.name,
                "project_id": entity_synonym_value.entity_synonym.project_id,
                "filename": entity_synonym_value.entity_synonym.filename,
            },
        )

    op.drop_table("entity_synonym_value")
    op.drop_table("entity_synonym")
    op.rename_table("entity_synonym_tmp", "entity_synonym")

    session.commit()

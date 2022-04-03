"""Initial migration

Reason:
It's recommended to keep the whole database layout in the migration. Hence, this runs
the initial setup of the database.

Revision ID: 2a216ed121dd
Revises:

"""
import sqlalchemy as sa
from alembic import op

import rasax.community.database.schema_migrations.alembic.utils as migration_utils

# revision identifiers, used by Alembic.
revision = "2a216ed121dd"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    if not migration_utils.table_has_column("environment", "db"):
        run_initial_migration()
    else:
        # Rasa 0.19.0 didn't include Alembic hence we only have to do one change
        drop_db_column()


def run_initial_migration():
    op.create_table(
        "analytics_cache",
        sa.Column("cache_key", sa.String(255), nullable=False),
        sa.Column("includes_platform_users", sa.Boolean(), nullable=False),
        sa.Column("timestamp", sa.Float(), nullable=True),
        sa.Column("result", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("cache_key", "includes_platform_users"),
    )
    op.create_table(
        "chat_tokens",
        sa.Column("token", sa.String(255), nullable=False),
        sa.Column("bot_name", sa.String(255), nullable=True),
        sa.Column("description", sa.String(255), nullable=True),
        sa.Column("expires", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("token"),
    )
    op.create_table(
        "conversation",
        sa.Column("sender_id", sa.String(255), nullable=False),
        sa.Column("number_user_messages", sa.Integer(), nullable=True),
        sa.Column("latest_input_channel", sa.String(255), nullable=True),
        sa.Column("latest_event_time", sa.Float(), nullable=True),
        sa.Column("in_training_data", sa.Boolean(), nullable=True),
        sa.Column("minimum_action_confidence", sa.Float(), nullable=True),
        sa.Column("evaluation", sa.Text(), nullable=True),
        sa.Column("interactive", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("sender_id"),
    )
    op.create_table(
        "password",
        sa.Column("password", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("password"),
    )
    op.create_table(
        "platform_feature",
        sa.Column("feature_name", sa.String(255), nullable=False),
        sa.Column("enabled", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("feature_name"),
    )
    op.create_table(
        "project",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("team", sa.String(255), nullable=False),
        sa.Column("active_model", sa.String(255), nullable=True),
        sa.Column("config", sa.Text(), nullable=True),
        sa.Column("handoff_url", sa.String(255), nullable=True),
        sa.PrimaryKeyConstraint("project_id"),
    )
    op.create_table(
        "user_role",
        sa.Column("role", sa.String(255), nullable=False),
        sa.PrimaryKeyConstraint("role"),
    )
    op.create_table(
        "conversation_action_metadata",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("action", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "action"),
    )
    op.create_table(
        "conversation_entity_metadata",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("entity", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "entity"),
    )
    op.create_table(
        "conversation_event",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("type_name", sa.String(255), nullable=False),
        sa.Column("timestamp", sa.Float(), nullable=False),
        sa.Column("intent_name", sa.String(255), nullable=True),
        sa.Column("action_name", sa.String(255), nullable=True),
        sa.Column("policy", sa.String(255), nullable=True),
        sa.Column("is_flagged", sa.Boolean(), nullable=False),
        sa.Column("is_unflagged", sa.Boolean(), nullable=False),
        sa.Column("data", sa.Text(), nullable=True),
        sa.Column("evaluation", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "conversation_intent_metadata",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("intent", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "intent"),
    )
    op.create_table(
        "message_correction",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("message_timestamp", sa.Float(), nullable=False),
        sa.Column("intent", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "message_timestamp"),
    )
    op.create_table(
        "conversation_policy_metadata",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("policy", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "policy"),
    )
    op.create_table(
        "conversation_session",
        sa.Column("conversation_id", sa.String(255), nullable=False),
        sa.Column("session_id", sa.Integer(), nullable=False),
        sa.Column("session_start", sa.Float(), nullable=True),
        sa.Column("session_length", sa.Float(), nullable=True),
        sa.Column("latest_event_time", sa.Float(), nullable=True),
        sa.Column("user_messages", sa.Integer(), nullable=True),
        sa.Column("bot_messages", sa.Integer(), nullable=True),
        sa.Column("is_new_user", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["conversation_id"], ["conversation.sender_id"]),
        sa.PrimaryKeyConstraint("conversation_id", "session_id"),
    )
    op.create_table(
        "conversation_statistic",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("total_user_messages", sa.Integer(), nullable=True),
        sa.Column("total_bot_messages", sa.Integer(), nullable=True),
        sa.Column("latest_event_timestamp", sa.Float(), nullable=True),
        sa.Column("latest_event_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("project_id"),
    )
    op.create_table(
        "domain",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("store_entities_as_slots", sa.Boolean(), nullable=True),
        sa.Column("path", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "entity_synonym",
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("synonym", sa.String(255), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("name", "synonym", "project_id"),
    )
    op.create_table(
        "environment",
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("project", sa.String(255), nullable=False),
        sa.Column("url", sa.String(255), nullable=False),
        sa.Column("token", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("name", "project"),
    )
    op.create_table(
        "intent",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("mapped_to", sa.String(255), nullable=True),
        sa.Column("is_temporary", sa.Boolean(), nullable=True),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "lookup_table",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("elements", sa.Text(), nullable=True),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "model",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("hash", sa.String(255), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("path", sa.String(255), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("version", sa.String(20), nullable=True),
        sa.Column("trained_at", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("path"),
    )
    op.create_table(
        "permission",
        sa.Column("project", sa.String(255), nullable=False),
        sa.Column("role_id", sa.String(255), nullable=False),
        sa.Column("permission", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["project"], ["project.project_id"]),
        sa.ForeignKeyConstraint(["role_id"], ["user_role.role"]),
        sa.PrimaryKeyConstraint("project", "role_id", "permission"),
    )
    op.create_table(
        "rasa_x_user",
        sa.Column("username", sa.String(255), nullable=False),
        sa.Column("name_id", sa.String(255), nullable=True),
        sa.Column("password_hash", sa.Text(), nullable=True),
        sa.Column("team", sa.String(255), nullable=False),
        sa.Column("api_token", sa.String(4000), nullable=False),
        sa.Column("project", sa.String(255), nullable=True),
        sa.Column("username_is_assigned", sa.Boolean(), nullable=True),
        sa.Column("authentication_mechanism", sa.String(255), nullable=True),
        sa.Column("attributes", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("username"),
    )
    op.create_table(
        "regex_feature",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("pattern", sa.String(255), nullable=True),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_goal",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "conversation_action_statistic",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("action", sa.String(255), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["conversation_statistic.project_id"]),
        sa.PrimaryKeyConstraint("project_id", "action"),
    )
    op.create_table(
        "conversation_entity_statistic",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("entity", sa.String(255), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["conversation_statistic.project_id"]),
        sa.PrimaryKeyConstraint("project_id", "entity"),
    )
    op.create_table(
        "conversation_intent_statistic",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("intent", sa.String(255), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["conversation_statistic.project_id"]),
        sa.PrimaryKeyConstraint("project_id", "intent"),
    )
    op.create_table(
        "conversation_policy_statistic",
        sa.Column("project_id", sa.String(255), nullable=False),
        sa.Column("policy", sa.String(255), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["project_id"], ["conversation_statistic.project_id"]),
        sa.PrimaryKeyConstraint("project_id", "policy"),
    )
    op.create_table(
        "domain_action",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("action", sa.String(255), nullable=False),
        sa.Column("is_form", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["domain.id"]),
        sa.PrimaryKeyConstraint("id", "action"),
    )
    op.create_table(
        "domain_entity",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("entity", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["id"], ["domain.id"]),
        sa.PrimaryKeyConstraint("id", "entity"),
    )
    op.create_table(
        "domain_intent",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("intent", sa.String(255), nullable=False),
        sa.Column("use_entities", sa.Boolean(), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["domain.id"]),
        sa.PrimaryKeyConstraint("id", "intent"),
    )
    op.create_table(
        "domain_slot",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("slot", sa.String(255), nullable=False),
        sa.Column("auto_fill", sa.Boolean(), nullable=True),
        sa.Column("initial_value", sa.String(255), nullable=True),
        sa.Column("type", sa.String(255), nullable=True),
        sa.Column("values", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["id"], ["domain.id"]),
        sa.PrimaryKeyConstraint("id", "slot"),
    )

    op.create_table(
        "message_log",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("hash", sa.String(255), nullable=True),
        sa.Column("model_id", sa.Integer(), nullable=True),
        sa.Column("archived", sa.Boolean(), nullable=True),
        sa.Column("time", sa.Float(), nullable=True),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("intent", sa.String(255), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.Column("intent_ranking", sa.Text(), nullable=True),
        sa.Column("entities", sa.Text(), nullable=True),
        sa.Column("event_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["event_id"], ["conversation_event.id"]),
        sa.ForeignKeyConstraint(["model_id"], ["model.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "model_tag",
        sa.Column("model_id", sa.Integer(), nullable=False),
        sa.Column("tag", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["model_id"], ["model.id"]),
        sa.PrimaryKeyConstraint("model_id", "tag"),
    )
    op.create_table(
        "nlu_evaluation",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("model_id", sa.String(255), nullable=True),
        sa.Column("report", sa.Text(), nullable=True),
        sa.Column("precision", sa.Float(), nullable=True),
        sa.Column("f1", sa.Float(), nullable=True),
        sa.Column("accuracy", sa.Float(), nullable=True),
        sa.Column("timestamp", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["model_id"], ["model.name"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "nlu_training_data",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("hash", sa.String(255), nullable=True),
        sa.Column("text", sa.Text(), nullable=True),
        sa.Column("intent", sa.String(255), nullable=True),
        sa.Column("annotator_id", sa.String(255), nullable=True),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("annotated_at", sa.Float(), nullable=True),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["annotator_id"], ["rasa_x_user.username"]),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "single_use_token",
        sa.Column("token", sa.String(4000), nullable=False),
        sa.Column("expires", sa.Float(), nullable=True),
        sa.Column("username", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["username"], ["rasa_x_user.username"]),
        sa.PrimaryKeyConstraint("token"),
    )
    op.create_table(
        "story",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(255), nullable=True),
        sa.Column("story", sa.Text(), nullable=True),
        sa.Column("user", sa.String(255), nullable=True),
        sa.Column("annotated_at", sa.Float(), nullable=True),
        sa.Column("filename", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["user"], ["rasa_x_user.username"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "template",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("template", sa.String(255), nullable=False),
        sa.Column("text", sa.String(255), nullable=True),
        sa.Column("content", sa.Text(), nullable=True),
        sa.Column("annotator_id", sa.String(255), nullable=True),
        sa.Column("annotated_at", sa.Float(), nullable=True),
        sa.Column("project_id", sa.String(255), nullable=True),
        sa.Column("domain_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["annotator_id"], ["rasa_x_user.username"]),
        sa.ForeignKeyConstraint(["domain_id"], ["domain.id"]),
        sa.ForeignKeyConstraint(["project_id"], ["project.project_id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "temporary_intent_example",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("intent_id", sa.Integer(), nullable=True),
        sa.Column("example_hash", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["intent_id"], ["intent.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "user_goal_intent",
        sa.Column("user_goal_id", sa.Integer(), nullable=False),
        sa.Column("intent_name", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["user_goal_id"], ["user_goal.id"]),
        sa.PrimaryKeyConstraint("user_goal_id", "intent_name"),
    )
    op.create_table(
        "user_role_mapping",
        sa.Column("username", sa.String(255), nullable=True),
        sa.Column("role", sa.String(255), nullable=True),
        sa.ForeignKeyConstraint(["role"], ["user_role.role"]),
        sa.ForeignKeyConstraint(["username"], ["rasa_x_user.username"]),
    )
    op.create_table(
        "nlu_evaluation_prediction",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("evaluation_id", sa.Integer(), nullable=True),
        sa.Column("text", sa.String(255), nullable=True),
        sa.Column("intent", sa.String(255), nullable=True),
        sa.Column("predicted", sa.String(255), nullable=True),
        sa.Column("confidence", sa.Float(), nullable=True),
        sa.ForeignKeyConstraint(["evaluation_id"], ["nlu_evaluation.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "nlu_training_data_entity",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("example_id", sa.Integer(), nullable=True),
        sa.Column("entity", sa.String(255), nullable=True),
        sa.Column("value", sa.String(255), nullable=True),
        sa.Column("start", sa.Integer(), nullable=True),
        sa.Column("end", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["example_id"], ["nlu_training_data.id"]),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("nlu_training_data_entity")
    op.drop_table("nlu_evaluation_prediction")
    op.drop_table("user_role_mapping")
    op.drop_table("user_goal_intent")
    op.drop_table("temporary_intent_example")
    op.drop_table("template")
    op.drop_table("story")
    op.drop_table("single_use_token")
    op.drop_table("nlu_training_data")
    op.drop_table("nlu_evaluation")
    op.drop_table("model_tag")
    op.drop_table("message_log")
    op.drop_table("domain_slot")
    op.drop_table("domain_intent")
    op.drop_table("domain_entity")
    op.drop_table("domain_action")
    op.drop_table("conversation_policy_statistic")
    op.drop_table("conversation_intent_statistic")
    op.drop_table("conversation_entity_statistic")
    op.drop_table("conversation_action_statistic")
    op.drop_table("user_goal")
    op.drop_table("regex_feature")
    op.drop_table("rasa_x_user")
    op.drop_table("permission")
    op.drop_table("model")
    op.drop_table("lookup_table")
    op.drop_table("intent")
    op.drop_table("environment")
    op.drop_table("entity_synonym")
    op.drop_table("domain")
    op.drop_table("conversation_statistic")
    op.drop_table("conversation_session")
    op.drop_table("conversation_policy_metadata")
    op.drop_table("conversation_message_correction")
    op.drop_table("conversation_intent_metadata")
    op.drop_table("conversation_event")
    op.drop_table("conversation_entity_metadata")
    op.drop_table("conversation_action_metadata")
    op.drop_table("user_role")
    op.drop_table("project")
    op.drop_table("platform_feature")
    op.drop_table("password")
    op.drop_table("conversation")
    op.drop_table("chat_tokens")
    op.drop_table("analytics_cache")


def drop_db_column():
    with op.batch_alter_table("environment") as batch_op:
        batch_op.drop_column("db")

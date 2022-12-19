"""Initial revision

Revision ID: f35e1eca70f7
Revises:
Create Date: 2022-12-18 19:24:37.714021

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "f35e1eca70f7"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "plugin_testapi_reviews",
        sa.Column("id", sa.Text(), nullable=False),
        sa.Column("created", sa.DateTime(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("plugin_testapi_reviews_pkey")),
    )
    op.create_index(op.f("plugin_testapi_reviews_id_idx"), "plugin_testapi_reviews", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("plugin_testapi_reviews_id_idx"), table_name="plugin_testapi_reviews")
    op.drop_table("plugin_testapi_reviews")
    # ### end Alembic commands ###
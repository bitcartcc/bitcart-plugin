"""add name

Revision ID: 32974039eb89
Revises: f35e1eca70f7
Create Date: 2022-12-18 19:51:20.619707

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "32974039eb89"
down_revision = "f35e1eca70f7"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("plugin_testapi_reviews", sa.Column("name", sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("plugin_testapi_reviews", "name")
    # ### end Alembic commands ###
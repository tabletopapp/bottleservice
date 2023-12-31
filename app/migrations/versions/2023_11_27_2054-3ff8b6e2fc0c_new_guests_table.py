"""new guests table

Revision ID: 3ff8b6e2fc0c
Revises: 8fac9d046a90
Create Date: 2023-11-27 20:54:30.730562

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3ff8b6e2fc0c"
down_revision: Union[str, None] = "8fac9d046a90"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "guests",
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
            name=op.f("fk_guests_user_id_users"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_guests")),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("guests")
    # ### end Alembic commands ###

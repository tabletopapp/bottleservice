"""changed clubs table

Revision ID: 220202f601e2
Revises: eadf9df5b92d
Create Date: 2023-11-27 14:40:02.878240

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "220202f601e2"
down_revision: Union[str, None] = "eadf9df5b92d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("clubs", sa.Column("address_line_1", sa.String(), nullable=False))
    op.add_column("clubs", sa.Column("address_line_2", sa.String(), nullable=True))
    op.add_column("clubs", sa.Column("city", sa.String(), nullable=False))
    op.add_column("clubs", sa.Column("state", sa.String(), nullable=False))
    op.add_column("clubs", sa.Column("zip_code", sa.String(), nullable=False))
    op.drop_column("clubs", "address")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "clubs",
        sa.Column("address", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("clubs", "zip_code")
    op.drop_column("clubs", "state")
    op.drop_column("clubs", "city")
    op.drop_column("clubs", "address_line_2")
    op.drop_column("clubs", "address_line_1")
    # ### end Alembic commands ###

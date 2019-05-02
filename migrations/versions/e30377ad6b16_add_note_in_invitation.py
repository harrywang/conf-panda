"""add note in invitation

Revision ID: e30377ad6b16
Revises: cc8a04bf1a9e
Create Date: 2017-02-09 11:09:41.605674

"""

# revision identifiers, used by Alembic.
revision = 'e30377ad6b16'
down_revision = 'cc8a04bf1a9e'

from alembic import op
import sqlalchemy as sa
from app.utils.customDataType import NestedMutableJson as JsonObject


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('note', JsonObject, nullable=True))

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('invitations', schema=None) as batch_op:
        batch_op.drop_column('note')

    ### end Alembic commands ###

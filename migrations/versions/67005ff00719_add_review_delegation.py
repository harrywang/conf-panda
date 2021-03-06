"""add review delegation

Revision ID: 67005ff00719
Revises: 0c24adbbb3d8
Create Date: 2017-03-07 18:55:44.980373

"""

# revision identifiers, used by Alembic.
revision = '67005ff00719'
down_revision = '0c24adbbb3d8'

from alembic import op
import sqlalchemy as sa
from app.utils.customDataType import NestedMutableJson as JsonObject


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('delegate_reviewers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('email_content', JsonObject, nullable=True),
    sa.Column('delegator_id', sa.Integer(), nullable=True),
    sa.Column('delegatee_id', sa.Integer(), nullable=True),
    sa.Column('paper_id', sa.Integer(), nullable=True),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['delegatee_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['delegator_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['paper_id'], ['papers.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('delegate_reviewers', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_delegate_reviewers_delegator_id'), ['delegator_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_delegate_reviewers_paper_id'), ['paper_id'], unique=False)

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('delegate_reviewers', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_delegate_reviewers_paper_id'))
        batch_op.drop_index(batch_op.f('ix_delegate_reviewers_delegator_id'))

    op.drop_table('delegate_reviewers')
    ### end Alembic commands ###

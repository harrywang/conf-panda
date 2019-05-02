"""empty message

Revision ID: 8dfaef9946ac
Revises: 54288858e30f
Create Date: 2018-03-06 15:09:50.056586

"""

# revision identifiers, used by Alembic.
revision = '8dfaef9946ac'
down_revision = '54288858e30f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review_actions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('review_id', sa.Integer(), nullable=True),
    sa.Column('commenter_id', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('action', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['commenter_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['review_id'], ['reviews.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('review_actions', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_review_actions_timestamp'), ['timestamp'], unique=False)

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review_actions', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_review_actions_timestamp'))

    op.drop_table('review_actions')
    ### end Alembic commands ###
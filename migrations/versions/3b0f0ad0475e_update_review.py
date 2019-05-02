"""update review

Revision ID: 3b0f0ad0475e
Revises: 41d66b4678f2
Create Date: 2016-07-08 11:38:32.262592

"""

# revision identifiers, used by Alembic.
revision = '3b0f0ad0475e'
down_revision = '41d66b4678f2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('custom_question_answer', sa.PickleType(), nullable=True))
        batch_op.add_column(sa.Column('update_timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_reviews_update_timestamp'), ['update_timestamp'], unique=False)
        batch_op.drop_column('review_answer')

    with op.batch_alter_table('conferences', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_deadline', sa.Date(), nullable=True))


    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_answer', sa.BLOB(), nullable=True))
        batch_op.drop_index(batch_op.f('ix_reviews_update_timestamp'))
        batch_op.drop_column('update_timestamp')
        batch_op.drop_column('custom_question_answer')

    with op.batch_alter_table('conferences', schema=None) as batch_op:
        batch_op.drop_column('review_deadline')

    ### end Alembic commands ###

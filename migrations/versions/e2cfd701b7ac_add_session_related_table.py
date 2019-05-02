"""add session related table

Revision ID: e2cfd701b7ac
Revises: f56664fc32ae
Create Date: 2017-07-19 20:36:23.111519

"""

# revision identifiers, used by Alembic.
revision = 'e2cfd701b7ac'
down_revision = 'f56664fc32ae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper_session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('paper_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paper_id'], ['papers.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('paper_session', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_paper_session_paper_id'), ['paper_id'], unique=False)
        batch_op.create_index(batch_op.f('ix_paper_session_session_id'), ['session_id'], unique=False)
    op.create_table('discussant_paper_session',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('paper_session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paper_session_id'], ['paper_session.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paper_session', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_paper_session_session_id'))
        batch_op.drop_index(batch_op.f('ix_paper_session_paper_id'))

    op.drop_table('paper_session')
    op.drop_table('discussant_paper_session')
    ### end Alembic commands ###
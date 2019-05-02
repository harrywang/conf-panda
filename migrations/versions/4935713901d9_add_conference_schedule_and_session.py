"""add conference schedule and session

Revision ID: 4935713901d9
Revises: 4dd4a1538dc5
Create Date: 2017-07-04 19:54:18.949746

"""

# revision identifiers, used by Alembic.
revision = '4935713901d9'
down_revision = '4dd4a1538dc5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('conference_schedules',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conference_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conference_id'], ['conferences.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sessions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conference_schedule_id', sa.Integer(), nullable=True),
    sa.Column('venue', sa.String(length=128), nullable=True),
    sa.Column('type', sa.String(length=128), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['conference_schedule_id'], ['conference_schedules.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('discussant_session',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('speaker_session',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('moderator_session',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    op.create_table('paper_session',
    sa.Column('paper_id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['paper_id'], ['papers.id'], ),
    sa.ForeignKeyConstraint(['session_id'], ['sessions.id'], )
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('speaker_session')
    op.drop_table('sessions')
    op.drop_table('paper_session')
    op.drop_table('moderator_session')
    op.drop_table('discussant_session')
    op.drop_table('conference_schedules')
    ### end Alembic commands ###

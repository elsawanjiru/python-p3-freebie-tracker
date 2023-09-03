from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=False),
        sa.Column('value', sa.Integer(), nullable=False),
        sa.Column('dev_id', sa.Integer(), sa.ForeignKey('dev.id'), nullable=False),
        sa.Column('company_id', sa.Integer(), sa.ForeignKey('company.id'), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('freebies')

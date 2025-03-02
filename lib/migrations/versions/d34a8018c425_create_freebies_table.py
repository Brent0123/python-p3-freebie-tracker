"""create freebies table

Revision ID: <your_revision_id>
Revises: 5f72c58bf48c
Create Date: <your_timestamp>

"""
from alembic import op
import sqlalchemy as sa

# Revision identifiers, used by Alembic.
revision = '<your_revision_id>'  # This will be auto-filled by Alembic
down_revision = '5f72c58bf48c'  # Matches the previous migration ID
branch_labels = None
depends_on = None

def upgrade() -> None:
    # Create the freebies table with necessary columns and foreign keys
    op.create_table('freebies',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('item_name', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('company_id', sa.Integer(), nullable=True),
        sa.Column('dev_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['company_id'], ['companies.id'], name='fk_freebies_company_id_companies'),
        sa.ForeignKeyConstraint(['dev_id'], ['devs.id'], name='fk_freebies_dev_id_devs'),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade() -> None:
    # Drop the freebies table if we need to rollback
    op.drop_table('freebies')
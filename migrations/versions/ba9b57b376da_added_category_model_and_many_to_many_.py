"""Added Category model and many-to-many relationship with Recipe

Revision ID: ba9b57b376da
Revises: a3e56301faf9
Create Date: 2025-03-23 11:21:35.742195

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ba9b57b376da"
down_revision = "a3e56301faf9"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "category",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "recipe_categories",
        sa.Column("recipe_id", sa.Integer(), nullable=False),
        sa.Column("category_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["category_id"],
            ["category.id"],
        ),
        sa.ForeignKeyConstraint(
            ["recipe_id"],
            ["recipe.id"],
        ),
        sa.PrimaryKeyConstraint("recipe_id", "category_id"),
    )
    with op.batch_alter_table("recipe", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_recipe_cuisine"), ["cuisine"], unique=False
        )
        batch_op.create_index(batch_op.f("ix_recipe_title"), ["title"], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("recipe", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_recipe_title"))
        batch_op.drop_index(batch_op.f("ix_recipe_cuisine"))

    op.drop_table("recipe_categories")
    op.drop_table("category")
    # ### end Alembic commands ###

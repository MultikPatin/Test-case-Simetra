from sqlalchemy.orm import Mapped, declarative_base, mapped_column


class Base:
    """Class for base model with standard fields for all models."""

    id: Mapped[int] = mapped_column(primary_key=True)


Base = declarative_base(cls=Base)

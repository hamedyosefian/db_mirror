from typing import TYPE_CHECKING

from sqlalchemy.orm import mapped_column, Mapped, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.backup import BackupTarget


class Database(Base):
    __tablename__ = "databases"

    id: Mapped[int] = mapped_column(primary_key=True)
    # id: Mapped[int] = mapped_column(primary_key=True,index=True)
    name: Mapped[str] = mapped_column(unique=True)
    host: Mapped[str]
    port: Mapped[int]
    username: Mapped[str]
    password: Mapped[str]
    database_name: Mapped[str]

    backup_targets: Mapped[list["BackupTarget"]] = relationship(back_populates="database")

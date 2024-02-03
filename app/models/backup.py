from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.models.databases import Database


class BackupTarget(Base):
    __tablename__ = "backup_targets"

    id: Mapped[int] = mapped_column(primary_key=True)

    database_id: Mapped[int] = mapped_column(ForeignKey("databases.id"))
    database: Mapped["Database"] = relationship(back_populates="backup_targets")

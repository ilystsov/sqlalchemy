from uuid import UUID

from sqlalchemy import Uuid, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from seminar_materials.app.models.base import BaseModel


class WorkerModel(BaseModel):
    """БД модель для работника."""

    __tablename__ = "workers"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    worker_class: Mapped[str] = mapped_column(String(20), nullable=False)


class DepartmentModel(BaseModel):
    """БД модель для департамента."""

    __tablename__ = "departments"

    uuid: Mapped[UUID] = mapped_column(Uuid(), primary_key=True, unique=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=False)
    zip_code: Mapped[str] = mapped_column(String(10))


class DepartmentWorkerModel(BaseModel):
    """БД модель для должности работника."""

    __tablename__ = "department_worker"

    worker_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("workers.uuid", ondelete="CASCADE"), primary_key=True)
    department_id: Mapped[UUID] = mapped_column(Uuid(), ForeignKey("departments.uuid", ondelete="CASCADE"),
                                                primary_key=True)
    job_title: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"DepartmentWorker: worker_id={self.worker_id}, " \
               f"department_id={self.department_id}, job_title={self.job_title}"

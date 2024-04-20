from sqlalchemy import select, text
from sqlalchemy.orm import Session

from seminar_materials.app.config import ENGINE
from seminar_materials.app.models import WorkerModel, DepartmentModel, DepartmentWorkerModel

if __name__ == '__main__':
    with Session(ENGINE) as session:
        # Вариант 1.1
        worker = session.get(WorkerModel, '6aa2bb37-bcfb-480c-b439-35589e59830e')
        department = session.get(DepartmentModel, '2d60fc2f-1336-429e-a434-467de0b0c6fb')
        print(worker.name, department.name)

        worker_job_title = session.get_one(DepartmentWorkerModel, (worker.uuid, department.uuid))
        print(worker_job_title)

        # Вариант 1.2
        stmt = select(WorkerModel).where(WorkerModel.uuid == '6aa2bb37-bcfb-480c-b439-35589e59830e')

        print([w.name for w in session.scalars(stmt)])

        # Вариант 2

        print(session.query(WorkerModel).where(WorkerModel.uuid == '14634735-acdf-4824-b536-a45cd51ad697').one().name)

        # Вариант 3

        query = text("SELECT w.name from seminar.workers w where w.uuid = '6aa2bb37-bcfb-480c-b439-35589e59830e'")

        print(session.execute(query).all())


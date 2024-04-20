import uuid

from sqlalchemy.orm import Session

from seminar_materials.app.config import ENGINE
from seminar_materials.app.models import WorkerModel, DepartmentModel, DepartmentWorkerModel

if __name__ == '__main__':
    with Session(ENGINE) as session:
        worker_sss = WorkerModel(
            uuid=uuid.uuid4(),
            name="John Wick",
            email='i.love.dogs@yahoo.com',
            worker_class="SSS",
        )

        worker_d = WorkerModel(
            uuid=uuid.uuid4(),
            name="Patrick",
            email='mmmgggbbb@yahoo.com',
            worker_class="D",
        )

        department_weaponry = DepartmentModel(
            uuid=uuid.uuid4(),
            name="Advanced Weaponry Dep.",
            address='The Hell, 8 circle',
            zip_code="666",
        )

        department_main = DepartmentModel(
            uuid=uuid.uuid4(),
            name="Lethal Company Main",
            address='Old Earth, Maniac str. 42',
            zip_code="777-666",
        )

        session.add_all([worker_sss, worker_d, department_weaponry, department_main])

        session.commit()

        john_wick_workplace = DepartmentWorkerModel(
            worker_id=worker_sss.uuid,
            department_id=department_weaponry.uuid,
            job_title="Killer",
        )

        patrick_workplace_1 = DepartmentWorkerModel(
            worker_id=worker_d.uuid,
            department_id=department_weaponry.uuid,
            job_title="Cleaner",
        )

        patrick_workplace_2 = DepartmentWorkerModel(
            worker_id=worker_d.uuid,
            department_id=department_main.uuid,
            job_title="Cleaner",
        )

        session.add_all([john_wick_workplace, patrick_workplace_1, patrick_workplace_2])

        session.commit()



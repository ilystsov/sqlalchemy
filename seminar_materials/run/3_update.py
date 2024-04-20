from sqlalchemy.orm import Session

from seminar_materials.app.config import ENGINE
from seminar_materials.app.models import WorkerModel, DepartmentModel, DepartmentWorkerModel

if __name__ == '__main__':

    with Session(ENGINE) as session:
        worker = session.get(WorkerModel, '6aa2bb37-bcfb-480c-b439-35589e59830e')
        department = session.get(DepartmentModel, '2d60fc2f-1336-429e-a434-467de0b0c6fb')

        worker_job_title = session.get_one(DepartmentWorkerModel, (worker.uuid, department.uuid))

        worker_job_title.job_title = "Domosed"

        session.commit()
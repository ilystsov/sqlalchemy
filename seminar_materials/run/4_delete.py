from sqlalchemy.orm import Session

from seminar_materials.app.config import ENGINE
from seminar_materials.app.models import WorkerModel

if __name__ == '__main__':
    with Session(ENGINE) as session:
        worker = session.get(WorkerModel, '6aa2bb37-bcfb-480c-b439-35589e59830e')

        session.delete(worker)

        session.commit()
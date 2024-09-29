from fastapi import FastAPI
import uvicorn

from version import __version__
from config.database import get_db, check_db, engine, Base

from models.specialty import Specialty

from routers.offers import offers_router

app = FastAPI(
    title='Legal Roster API',
    description='API for Legal Roster',
    terms_of_service='https://legalroster.com/terms/',
    version=__version__,
    contact={
        'name': 'Xulio Legal Roster',
        'email': 'a22julioaa@iessanclemente.net',
    },
    license_info={
        'name': 'MIT',
        'url': 'https://legalroster.com/license/',
    },
)

@app.get(
        '/',
        summary='Check the API Database',
        description='Returns the status of the database',
        tags=['Check'],
)
def check_database():
    """
    Check the database status
    FIXME: This should be removed in production
    """
    return check_db()

app.include_router(offers_router)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    uvicorn.run(app='run:app', host='0.0.0.0', port=8999, reload=True)

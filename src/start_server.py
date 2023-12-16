from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from server.database.db_manager import base_manager
from server.users.routers import router as users_routers
from server.settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH

app = FastAPI()
app.include_router(users_routers, prefix='/users')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base('scripts/tables.sql', 'scripts/primary_data.sql')
    uvicorn.run(app='start_server:app', host='127.0.0.1', port=8123, reload=True)

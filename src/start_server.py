from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse
from server.users.routers import router as users_routers

app = FastAPI()
app.include_router(users_routers, prefix='/users')


@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    uvicorn.run(app='start_server:app', host='127.0.0.1', port=8123, reload=True)

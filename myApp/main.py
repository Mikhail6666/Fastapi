from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_versioning import VersionedFastAPI
from fastapi.staticfiles import StaticFiles

from myApp.users.router import router_users, router_auth
from myApp.pages.router import router as router_pages
from myApp.images.router import router as router_images

app = FastAPI(
    title="Тест",
    version="0.1.0",
    root_path="/api",
)

app = VersionedFastAPI(app,
                       version_format='{major}',
                       prefix_format='/api/v{major}',
                       # lifespan=lifespan,
                       )

app.mount("/static", StaticFiles(directory="myApp/static"), "static")

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_pages)
app.include_router(router_images)

origins = [
    # 3000 - порт, на котором работает фронтенд на React.js
    "http://localhost:3000",
    "*"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin", "Authorization"],
)




@app.get("/")
def get_hello():
    return "Добро пожаловать на сайт"

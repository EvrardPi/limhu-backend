from ninja import NinjaAPI
from article.views import router as article_router

api = NinjaAPI()

api.add_router("articles/", article_router)

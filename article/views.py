from django.db.transaction import atomic
from ninja import Router
from ninja.responses import Response

from article.models import Article
from article.schemas import ArticleResponseSchema, ArticleCreationSchema

router = Router()


@router.get('/', response={200: list[ArticleResponseSchema]}, tags=["Articles"])
def get_articles(request):
    return Article.objects.all()


@router.post('/', response={201: None}, tags=["Articles"])
@atomic()
def create_articles(request, data: ArticleCreationSchema):
    created_article = Article()
    created_article.title = data.title
    created_article.content = data.content
    created_article.save()

    return Response(status=201, data={})

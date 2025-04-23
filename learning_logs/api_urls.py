from rest_framework.routers import DefaultRouter
from .views import TopicViewSet, EntryViewSet, NoticiaViewSet

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'entries', EntryViewSet)
router.register(r'noticias', NoticiaViewSet)

urlpatterns = router.urls

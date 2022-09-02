from rest_framework.routers import DefaultRouter
from .apiviews import ClassViewSet, StudentViewSet

router = DefaultRouter()

router.register(r"class", ClassViewSet, basename="class")
router.register(r"student", StudentViewSet, basename="student")

urlpatterns = router.urls

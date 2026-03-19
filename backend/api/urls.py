from rest_framework.routers import DefaultRouter
from .views import WeightViewSet, RoutineRecordViewSet,RoutineViewSet

router = DefaultRouter()
router.register(r'weights',WeightViewSet)
router.register(r'routine',RoutineViewSet)
router.register(r'record',RoutineRecordViewSet)
urlpatterns = router.urls

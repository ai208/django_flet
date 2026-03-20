from rest_framework.routers import DefaultRouter
from .views import WeightViewSet, RoutineRecordViewSet,RoutineViewSet

router = DefaultRouter()
router.register(r'weights',WeightViewSet)
router.register(r'routines',RoutineViewSet)
router.register(r'routinerecords',RoutineRecordViewSet)
urlpatterns = router.urls

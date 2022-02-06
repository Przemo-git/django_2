from .views import ApertamentViewSet
#from .views import ApartmentDetailSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'apartments', ApertamentViewSet)
#router.register(r'apartments', ApartmentDetailSet)
urlpatterns = router.urls
from django.urls import include, path
from rest_framework import routers
from . import views

'''
/branches?bank_name&city --> list of branches
/branches/:ifsc --> branch details
'''
router = routers.DefaultRouter()
router.register('branches', views.BranchesViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]

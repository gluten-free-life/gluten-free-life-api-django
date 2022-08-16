from foodapi.viewsets import EmployeeViewset
from foodapi.viewsets import FoodViewset
from foodapi.viewsets import UserViewset
from foodapi.viewsets import WishlistViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('foods', FoodViewset)
router.register('users', UserViewset)
router.register('wishlists', WishlistViewset)


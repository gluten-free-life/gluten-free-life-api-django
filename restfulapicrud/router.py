from foodapi.viewsets import EmployeeViewset
from foodapi.viewsets import FoodViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', EmployeeViewset)
router.register('foods', FoodViewset)


from rest_framework import routers
# from crud.rental import views as myapp_views
from rental.views import FriendViewset, BorrowedViewset,BelongingViewset
router = routers.DefaultRouter()
router.register(r'friends', FriendViewset)
router.register(r'belongings', BelongingViewset)
router.register(r'borrowings', BorrowedViewset)
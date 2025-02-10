from rest_framework import permissions



class IsAuthenticatedAdmin(permissions.BasePermission):
    """
    Yalnız login olmuş və is_employee=True olan istifadəçilərə icazə ver.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return request.user.is_employee
    

class IsAuthenticatedBuyer(permissions.BasePermission):
    """
    Yalnız login olmuş və is_employee=True olan istifadəçilərə icazə ver.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        return not request.user.is_employee
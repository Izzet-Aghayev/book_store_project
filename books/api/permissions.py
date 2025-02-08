from rest_framework import permissions



class IsAuthenticatedAdmin(permissions.BasePermission):
    """
    Yalnız login olmuş və is_employee=True olan istifadəçilərə icazə ver.
    """

    def has_permission(self, request, view):
        # Əgər istifadəçi login olmamışsa, icazə verilmir
        if not request.user or not request.user.is_authenticated:
            return False

        # Əgər istifadəçi login olub və admin (is_employee=True) -dirsə, icazə verilir
        return request.user.is_employee
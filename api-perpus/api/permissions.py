from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.request import Request


class ReadOnlyOrAuthenticated(BasePermission):
    """
    Permission class yang memungkinkan akses read-only untuk semua orang,
    tetapi memerlukan autentikasi untuk operasi tulis.
    """
    
    def has_permission(self, request: Request, view) -> bool:
        # Izinkan semua metode GET, HEAD, OPTIONS (read-only)
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Untuk metode lain (POST, PUT, PATCH, DELETE), perlu autentikasi
        return request.user and request.user.is_authenticated


class LoanPermission(BasePermission):
    """
    Permission class khusus untuk operasi peminjaman yang selalu memerlukan autentikasi.
    """
    
    def has_permission(self, request: Request, view) -> bool:
        # Semua operasi pada loan memerlukan autentikasi
        return request.user and request.user.is_authenticated


class ReservePermission(BasePermission):
    """
    Permission class khusus untuk operasi reservasi yang selalu memerlukan autentikasi.
    """
    
    def has_permission(self, request: Request, view) -> bool:
        # Semua operasi pada reservasi memerlukan autentikasi
        return request.user and request.user.is_authenticated


class FinePermission(BasePermission):
    """
    Permission class khusus untuk operasi denda yang selalu memerlukan autentikasi.
    """
    
    def has_permission(self, request: Request, view) -> bool:
        # Semua operasi pada denda memerlukan autentikasi
        return request.user and request.user.is_authenticated
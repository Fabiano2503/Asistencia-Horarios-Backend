# app/api/v1/routes/__init__.py
from .dashboard import router as dashboard_router
# Los demás los iremos agregando después
__all__ = ["dashboard_router"]
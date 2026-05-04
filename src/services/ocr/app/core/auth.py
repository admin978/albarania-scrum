import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.config import settings

bearer_scheme = HTTPBearer()


class AuthContext:
    __slots__ = ("user_id", "empresa_id", "rol")

    def __init__(self, user_id: str, empresa_id: str, rol: str) -> None:
        self.user_id = user_id
        self.empresa_id = empresa_id
        self.rol = rol


def verify_jwt(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
) -> AuthContext:
    try:
        payload = jwt.decode(
            credentials.credentials,
            settings.jwt_secret,
            algorithms=["HS256"],
        )
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {exc}",
        ) from exc

    user_id = payload.get("user_id") or payload.get("sub")
    empresa_id = payload.get("empresa_id")
    rol = payload.get("rol")

    if not user_id or not empresa_id or not rol:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing user_id/empresa_id/rol",
        )

    return AuthContext(user_id=str(user_id), empresa_id=str(empresa_id), rol=str(rol))


def require_role(*allowed: str):
    def _checker(ctx: AuthContext = Depends(verify_jwt)) -> AuthContext:
        if ctx.rol not in allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Role '{ctx.rol}' not allowed",
            )
        return ctx

    return _checker

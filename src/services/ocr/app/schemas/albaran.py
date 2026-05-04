from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, field_validator

VALID_UNIDADES: frozenset[str] = frozenset({"ud", "kg", "m", "l", "h", "pack"})


class LineaAlbaran(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    descripcion: str
    cantidad: Decimal = Field(ge=0)
    unidad: str
    precio_unitario: Decimal = Field(ge=0)
    subtotal: Decimal = Field(ge=0)

    @field_validator("unidad", mode="before")
    @classmethod
    def coerce_unidad(cls, value: object) -> str:
        if not isinstance(value, str):
            return "ud"
        normalized = value.strip().lower()
        aliases = {"unidad": "ud", "unidades": "ud", "uds": "ud", "kgs": "kg", "litro": "l", "litros": "l", "metro": "m", "metros": "m", "hora": "h", "horas": "h"}
        normalized = aliases.get(normalized, normalized)
        if normalized not in VALID_UNIDADES:
            return "ud"
        return normalized


Confianza = Annotated[float, Field(ge=0.0, le=1.0)]


class AlbaranExtraido(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    es_albaran: bool
    confianza_extraccion: Confianza
    numero_documento: str | None = None
    fecha: date | None = None
    proveedor_nombre: str | None = None
    proveedor_cif: str | None = None
    base_imponible: Decimal = Field(default=Decimal("0"), ge=0)
    iva_total: Decimal = Field(default=Decimal("0"), ge=0)
    importe_total: Decimal = Field(default=Decimal("0"), ge=0)
    lineas: list[LineaAlbaran] = Field(default_factory=list)
    observaciones: str | None = None

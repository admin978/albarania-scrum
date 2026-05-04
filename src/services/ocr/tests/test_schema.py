from decimal import Decimal

import pytest
from pydantic import ValidationError

from app.schemas.albaran import AlbaranExtraido, LineaAlbaran, VALID_UNIDADES


def test_albaran_valid_fixture() -> None:
    payload = {
        "es_albaran": True,
        "confianza_extraccion": 0.92,
        "numero_documento": "ALB-2026-001",
        "fecha": "2026-04-15",
        "proveedor_nombre": "Suministros García SL",
        "proveedor_cif": "B12345678",
        "base_imponible": "100.00",
        "iva_total": "21.00",
        "importe_total": "121.00",
        "lineas": [
            {
                "descripcion": "Detergente industrial",
                "cantidad": "5",
                "unidad": "L",
                "precio_unitario": "15",
                "subtotal": "75",
            },
            {
                "descripcion": "Bayetas",
                "cantidad": "10",
                "unidad": "unidades",
                "precio_unitario": "2.5",
                "subtotal": "25",
            },
        ],
        "observaciones": None,
    }

    albaran = AlbaranExtraido.model_validate(payload)

    assert albaran.es_albaran is True
    assert albaran.importe_total == Decimal("121.00")
    assert len(albaran.lineas) == 2
    assert albaran.lineas[0].unidad == "l"
    assert albaran.lineas[1].unidad == "ud"


def test_albaran_rejects_negative_total() -> None:
    with pytest.raises(ValidationError):
        AlbaranExtraido.model_validate(
            {
                "es_albaran": True,
                "confianza_extraccion": 0.5,
                "importe_total": "-10",
            }
        )


def test_albaran_rejects_confianza_out_of_range() -> None:
    with pytest.raises(ValidationError):
        AlbaranExtraido.model_validate(
            {
                "es_albaran": True,
                "confianza_extraccion": 1.5,
            }
        )


def test_linea_unknown_unit_falls_back_to_ud() -> None:
    linea = LineaAlbaran.model_validate(
        {"descripcion": "X", "cantidad": "1", "unidad": "barril", "precio_unitario": "1", "subtotal": "1"}
    )
    assert linea.unidad == "ud"


def test_valid_unidades_set() -> None:
    assert VALID_UNIDADES == {"ud", "kg", "m", "l", "h", "pack"}

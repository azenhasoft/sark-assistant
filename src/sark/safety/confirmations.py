"""Aqui defino quando uma ação precisa da confirmação do usuário."""

from enum import Enum


class ActionRisk(str, Enum):
    READ_ONLY = "read_only"
    WRITE = "write"
    EXTERNAL = "external"
    DESTRUCTIVE = "destructive"


def requires_confirmation(risk: ActionRisk) -> bool:
    """Eu peço confirmação quando a ação altera dados ou afeta algo externo."""
    return risk is not ActionRisk.READ_ONLY

"""
Generated by qenerate plugin=pydantic_v1. DO NOT MODIFY MANUALLY!
"""
from collections.abc import Callable  # noqa: F401 # pylint: disable=W0611
from datetime import datetime  # noqa: F401 # pylint: disable=W0611
from enum import Enum  # noqa: F401 # pylint: disable=W0611
from typing import (  # noqa: F401 # pylint: disable=W0611
    Any,
    Optional,
    Union,
)

from pydantic import (  # noqa: F401 # pylint: disable=W0611
    BaseModel,
    Extra,
    Field,
    Json,
)


class ConfiguredBaseModel(BaseModel):
    class Config:
        smart_union=True
        extra=Extra.forbid


class SLODocumentSLOSLOParametersV1(ConfiguredBaseModel):
    window: str = Field(..., alias="window")


class SLODocumentSLOV1(ConfiguredBaseModel):
    name: str = Field(..., alias="name")
    sli_type: str = Field(..., alias="SLIType")
    slo_details: str = Field(..., alias="SLODetails")
    slo_target: float = Field(..., alias="SLOTarget")
    slo_target_unit: str = Field(..., alias="SLOTargetUnit")
    sli_specification: str = Field(..., alias="SLISpecification")
    slo_parameters: SLODocumentSLOSLOParametersV1 = Field(..., alias="SLOParameters")


class SLODocuments(ConfiguredBaseModel):
    labels: Optional[Json] = Field(..., alias="labels")
    slos: Optional[list[SLODocumentSLOV1]] = Field(..., alias="slos")
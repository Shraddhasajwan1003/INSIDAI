"""Schemas for InsidAI Engineering CV Pipeline."""

from insidai.schemas.canonical_schema import (
    SCHEMA_VERSION,
    Point2D,
    BBox,
    ProvenanceSource,
    TextObservation,
    TableObservation,
    LineSegmentObservation,
    EngineeringEntity,
    DimensionObservation,
    Relationship,
    DocumentMetadata,
    CanonicalEngineeringDocument,
)
from insidai.schemas.cad_schema import (
    CADLayer,
    CADLine,
    CADArc,
    CADPolyline,
    CADText,
    CADDimension,
    CADBlockReference,
    CADDrawingVectorPackage,
)

__all__ = [
    "SCHEMA_VERSION",
    "Point2D",
    "BBox",
    "ProvenanceSource",
    "TextObservation",
    "TableObservation",
    "LineSegmentObservation",
    "EngineeringEntity",
    "DimensionObservation",
    "Relationship",
    "DocumentMetadata",
    "CanonicalEngineeringDocument",
    "CADLayer",
    "CADLine",
    "CADArc",
    "CADPolyline",
    "CADText",
    "CADDimension",
    "CADBlockReference",
    "CADDrawingVectorPackage",
]

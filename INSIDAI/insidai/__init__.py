"""
InsidAI Computer Vision & Engineering Drawing Subsystem.
Modular document understanding, fine-grained symbol detection, geometry extraction,
multi-modal fusion, and graph synthesis for engineering drawings.
"""

from insidai.pipeline import InsidAIPipeline
from insidai.schemas.canonical_schema import (
    CanonicalEngineeringDocument,
    EngineeringEntity,
    LineSegmentObservation,
    TextObservation,
    TableObservation,
    DimensionObservation,
    Relationship,
    SCHEMA_VERSION,
)
from insidai.graph.engineering_graph import EngineeringGraph
from insidai.llm_interface.prompt_builder import LLMEvidenceInterface

__all__ = [
    "InsidAIPipeline",
    "CanonicalEngineeringDocument",
    "EngineeringEntity",
    "LineSegmentObservation",
    "TextObservation",
    "TableObservation",
    "DimensionObservation",
    "Relationship",
    "SCHEMA_VERSION",
    "EngineeringGraph",
    "LLMEvidenceInterface",
]

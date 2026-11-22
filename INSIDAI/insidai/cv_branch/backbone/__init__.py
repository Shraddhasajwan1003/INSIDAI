"""Visual backbone modules."""

from insidai.cv_branch.backbone.base import BaseVisualBackbone
from insidai.cv_branch.backbone.dinov3 import DINOv3Backbone

__all__ = ["BaseVisualBackbone", "DINOv3Backbone"]

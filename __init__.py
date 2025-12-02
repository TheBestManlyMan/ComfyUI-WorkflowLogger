from .workflow_logger import WorkflowLoggerNode
from .image_sampler import ImageBatchSampler

NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode,
    "ImageBatchSampler": ImageBatchSampler
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger",
    "ImageBatchSampler": "Image Batch Sampler"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

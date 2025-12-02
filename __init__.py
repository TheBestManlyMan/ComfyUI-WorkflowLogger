from .workflow_logger import WorkflowLoggerNode
from .image_sampler import ImageBatchSampler
from .string_to_boolean import StringToBoolean

NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode,
    "ImageBatchSampler": ImageBatchSampler,
    "StringToBoolean": StringToBoolean
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger",
    "ImageBatchSampler": "Image Batch Sampler",
    "StringToBoolean": "String to Boolean"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

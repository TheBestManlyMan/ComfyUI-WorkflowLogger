from .workflow_logger import WorkflowLoggerNode

NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

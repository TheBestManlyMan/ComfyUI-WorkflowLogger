"""
ComfyUI-WorkflowLogger: Custom nodes for logging workflow data to CSV files
"""

from .workflow_logger import WorkflowLoggerNode
from .csv_reader import CSVReaderNode
from .csv_browser import CSVBrowserNode


# Node registration mapping
NODE_CLASS_MAPPINGS = {
    "WorkflowLogger": WorkflowLoggerNode,
    "CSVReader": CSVReaderNode,
    "CSVBrowser": CSVBrowserNode
}

# Display name mapping
NODE_DISPLAY_NAME_MAPPINGS = {
    "WorkflowLogger": "Workflow Logger",
    "CSVReader": "CSV Reader",
    "CSVBrowser": "CSV Browser"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

"""
Simple test script for the Workflow Logger node
Run this to verify the node works before installing in ComfyUI
"""

import sys
import os

# Add the current directory to path so we can import the node
sys.path.insert(0, os.path.dirname(__file__))

from __init__ import WorkflowLoggerNode

def test_node():
    """Test the workflow logger node"""
    print("Testing Workflow Logger Node...")
    print("-" * 50)
    
    # Create node instance
    node = WorkflowLoggerNode()
    
    # Test data (similar to your CSV example)
    test_cases = [
        {
            "id": "1_21_02",
            "prompt": "a woman in a grey coat holding a brown bag walking, only her lower body is visible",
            "prompt1": "on a green screen background",
            "prompt_neg": "moving mouth, talking, speaking, singing, lips moving, expression_talking",
            "csv_filename": "test_output.csv",
            "shift": "",
            "seed": ""
        },
        {
            "id": "1_21_03",
            "prompt": "a woman with red hair and a black hat, wearing a grey coat holding a brown bag walking",
            "prompt1": "on a green screen background",
            "prompt_neg": "moving mouth, talking, speaking, singing, lips moving, expression_talking",
            "csv_filename": "test_output.csv",
            "shift": "",
            "seed": "12345"
        }
    ]
    
    # Run tests
    for i, test_data in enumerate(test_cases, 1):
        print(f"\nTest case {i}:")
        print(f"  ID: {test_data['id']}")
        result = node.log_to_csv(**test_data)
        print(f"  Result: {result[0]}")
    
    print("\n" + "-" * 50)
    print("Test complete! Check the 'output' folder for test_output.csv")
    
    # Try to read and display the CSV
    csv_path = os.path.join(os.path.dirname(__file__), "output", "test_output.csv")
    if os.path.exists(csv_path):
        print("\nGenerated CSV content:")
        print("-" * 50)
        with open(csv_path, 'r', encoding='utf-8-sig') as f:
            print(f.read())

if __name__ == "__main__":
    test_node()

"""
Buffer Utility for Pipeline Stages

This module defines a flexible buffer class used to pass data
between CPU pipeline stages, allowing both key-based and attribute-based access.
"""

class PipelineBuffer(dict):
    def __getattr__(self, name):
        return self.get(name)

    def __setattr__(self, name, value):
        self[name] = value

    def __setitem__(self, name, value):
        super().__setitem__(name, value)
        self.__dict__[name] = value

    def __delattr__(self, name):
        self.__delitem__(name)

    def __delitem__(self, name):
        super().__delitem__(name)
        self.__dict__.pop(name, None)

# Example usage for different pipeline stages:
# fetch_decode = PipelineBuffer()   # Between Fetch and Decode
# decode_execute = PipelineBuffer() # Between Decode and Execute
# execute_memory = PipelineBuffer() # Between Execute and Memory
# memory_writeback = PipelineBuffer() # Between Memory and Writeback


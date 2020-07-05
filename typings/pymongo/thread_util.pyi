"""
This type stub file was generated by pyright.
"""

from typing import Any, Optional

"""Utilities for multi-threading support."""
class Semaphore:
    def __init__(self, value=...):
        ...
    
    def acquire(self, blocking: bool = ..., timeout: Optional[Any] = ...):
        ...
    
    __enter__ = ...
    def release(self):
        ...
    
    def __exit__(self, t, v, tb):
        ...
    
    @property
    def counter(self):
        ...
    


class BoundedSemaphore(Semaphore):
    """Semaphore that checks that # releases is <= # acquires"""
    def __init__(self, value=...):
        ...
    
    def release(self):
        ...
    


class DummySemaphore(object):
    def __init__(self, value: Optional[Any] = ...):
        ...
    
    def acquire(self, blocking: bool = ..., timeout: Optional[Any] = ...):
        ...
    
    def release(self):
        ...
    


class MaxWaitersBoundedSemaphore(object):
    def __init__(self, semaphore_class, value=..., max_waiters=...):
        self.waiter_semaphore = ...
        self.semaphore = ...
    
    def acquire(self, blocking: bool = ..., timeout: Optional[Any] = ...):
        ...
    
    def __getattr__(self, name):
        ...
    


class MaxWaitersBoundedSemaphoreThread(MaxWaitersBoundedSemaphore):
    def __init__(self, value=..., max_waiters=...):
        ...
    


def create_semaphore(max_size, max_waiters):
    ...

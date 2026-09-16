"""Animus: an AI that learns to move.

This package wraps the compiled C++ physics core (`_animus_core`) with a
Python learning layer (RL training) and voice I/O.
"""

from ._animus_core import Body  # noqa: F401

__all__ = ["Body"]
__version__ = "0.1.0"

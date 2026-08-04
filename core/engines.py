"""Register the macOS Dictation speech engine with Talon."""

from talon import speech_system
from talon.engines.macsf import MacSFEngine

engine = MacSFEngine()
speech_system.add_engine(engine)

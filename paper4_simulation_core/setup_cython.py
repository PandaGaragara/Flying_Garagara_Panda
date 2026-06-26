# -*- coding: utf-8 -*-
"""
================================================================================
          PANDA GMC-AUTOPILOT: CROSS-PLATFORM HARDENING BUILD SCRIPT
================================================================================
Description:
    Standard setuptools configuration script. Compiles Python source files 
    into platform-native, optimized binary files (.so on Linux/macOS, .pyd on 
    Windows). Ensures fast, microsecond-level matrix evaluations.
================================================================================
"""

import sys
import subprocess

# Self-Bootstrapping: Automatically detect and install Cython dependency
try:
    from setuptools import setup, Extension
    from Cython.Build import cythonize
except ImportError:
    print("[SYSTEM] Cython compiler not found. Initiating dynamic environment preparation...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Cython"])
        from setuptools import setup, Extension
        from Cython.Build import cythonize
        print("[SYSTEM] Dynamic environment preparation complete. Resuming compilation.")
    except Exception as e:
        print(f"[FATAL] Failed to install Cython automatically. Reason: {e}")
        print("[FATAL] Please run 'pip install Cython' manually before executing this script.")
        sys.exit(1)

extensions = [
    Extension(
        "gmc_secured_middleware",
        sources=["gmc_secured_middleware.py"]
    )
]

setup(
    name="GMC Secured Autopilot Kernel",
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            'language_level': "3",
            'boundscheck': False,       # Disables array bound checking for speed
            'wraparound': False         # Disables negative index wrapping
        }
    )
)

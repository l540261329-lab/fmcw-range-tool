"""fmcw-range: FMCW 毫米波雷达距离/分辨率计算小工具。"""

from .core import (
    SPEED_OF_LIGHT,
    beat_to_range,
    range_resolution,
    doppler_to_velocity,
    dbm_to_watt,
    ghz_to_hz,
    mhz_to_hz,
)

__all__ = [
    "SPEED_OF_LIGHT",
    "beat_to_range",
    "range_resolution",
    "doppler_to_velocity",
    "dbm_to_watt",
    "ghz_to_hz",
    "mhz_to_hz",
]

__version__ = "0.1.0"

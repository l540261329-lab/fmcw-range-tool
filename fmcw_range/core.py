"""FMCW 雷达基础公式。

只依赖 Python 标准库，便于在任何环境中直接运行。
"""

SPEED_OF_LIGHT = 299792458.0  # 光速，单位 m/s


def ghz_to_hz(ghz: float) -> float:
    """GHz 转 Hz。"""
    return ghz * 1e9


def mhz_to_hz(mhz: float) -> float:
    """MHz 转 Hz。"""
    return mhz * 1e6


def beat_to_range(beat_hz: float, bandwidth_hz: float, chirp_time_s: float) -> float:
    """由拍频估算目标距离，单位：米。

    FMCW 雷达中，目标距离 R 与拍频 f_b 的关系为：
        R = c * f_b * T_chirp / (2 * B)
    其中 c 为光速，B 为扫频带宽，T_chirp 为单个啁啾持续时间。
    """
    if bandwidth_hz <= 0:
        raise ValueError("bandwidth_hz 必须为正数")
    if chirp_time_s <= 0:
        raise ValueError("chirp_time_s 必须为正数")
    return SPEED_OF_LIGHT * beat_hz * chirp_time_s / (2.0 * bandwidth_hz)


def range_resolution(bandwidth_hz: float) -> float:
    """距离分辨率，单位：米。公式：ΔR = c / (2B)，带宽越大分辨率越高。"""
    if bandwidth_hz <= 0:
        raise ValueError("bandwidth_hz 必须为正数")
    return SPEED_OF_LIGHT / (2.0 * bandwidth_hz)


def doppler_to_velocity(doppler_hz: float, carrier_freq_hz: float) -> float:
    """由多普勒频移估算径向速度，单位：米/秒。公式：v = λ * f_d / 2。"""
    if carrier_freq_hz <= 0:
        raise ValueError("carrier_freq_hz 必须为正数")
    wavelength = SPEED_OF_LIGHT / carrier_freq_hz
    return wavelength * doppler_hz / 2.0


def dbm_to_watt(dbm: float) -> float:
    """dBm 转瓦特。"""
    return 1e-3 * (10.0 ** (dbm / 10.0))

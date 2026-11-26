"""最小可运行示例：python example.py"""

from fmcw_range import beat_to_range, ghz_to_hz, mhz_to_hz, range_resolution

B = ghz_to_hz(4.0)       # 扫频带宽 4 GHz
T = 1e-3                 # 啁啾时长 1 ms
f_beat = mhz_to_hz(2.0)  # 拍频 2 MHz

print(f"带宽 {B / 1e9:.1f} GHz，啁啾时长 {T * 1e3:.1f} ms")
print(f"距离分辨率：{range_resolution(B):.4f} m")
print(f"拍频 {f_beat / 1e6:.1f} MHz → 目标距离：{beat_to_range(f_beat, B, T):.2f} m")

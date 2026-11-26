# FMCW Range Tool

一个用于 **FMCW 毫米波雷达**基础距离计算的极简 Python 工具：由拍频估算目标距离、计算距离分辨率，并提供多普勒测速与 dBm 换算。纯标准库实现，零第三方依赖。

> 这是一个用于练习「从零上传一个开源项目」的示例仓库。上传前请把文中的占位内容替换成你自己的。

## 特性

- 由拍频（beat frequency）计算目标距离
- 由扫频带宽计算距离分辨率
- 由多普勒频移估算径向速度
- dBm / W 功率换算
- 零依赖、带单元测试

## 安装

```bash
git clone https://github.com/<lyh>/fmcw-range-tool.git
cd fmcw-range-tool
```

无需安装第三方包，Python 3.8+ 即可运行。

## 快速开始

```python
from fmcw_range import beat_to_range, range_resolution, ghz_to_hz, mhz_to_hz

B = ghz_to_hz(4.0)       # 扫频带宽 4 GHz
T = 1e-3                 # 啁啾时长 1 ms
f_beat = mhz_to_hz(2.0)  # 拍频 2 MHz

print(range_resolution(B))          # 0.037474057...
print(beat_to_range(f_beat, B, T))  # 74.948...
```

也可以直接运行示例：

```bash
python example.py
```

## API

| 函数 | 说明 | 公式 |
| --- | --- | --- |
| `beat_to_range(beat_hz, bandwidth_hz, chirp_time_s)` | 拍频 → 距离（m） | `R = c·f_b·T / (2B)` |
| `range_resolution(bandwidth_hz)` | 距离分辨率（m） | `ΔR = c / (2B)` |
| `doppler_to_velocity(doppler_hz, carrier_freq_hz)` | 多普勒 → 速度（m/s） | `v = λ·f_d / 2` |
| `dbm_to_watt(dbm)` | dBm → W | `P = 10^(dBm/10) / 1000` |

## 测试

```bash
python -m unittest discover -s tests -v
```

## 许可证

[MIT](lyh) © 2026 lyh

---


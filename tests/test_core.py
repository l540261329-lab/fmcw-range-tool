"""core 模块的单元测试。运行：python -m unittest discover -s tests -v"""

import unittest

from fmcw_range.core import (
    beat_to_range,
    dbm_to_watt,
    doppler_to_velocity,
    ghz_to_hz,
    mhz_to_hz,
    range_resolution,
)


class TestFMCWCore(unittest.TestCase):
    def test_beat_to_range(self):
        # B=1GHz, T=1ms, f_beat=1MHz
        # R = 299792458 * 1e6 * 1e-3 / (2e9) ≈ 149.896229 m
        self.assertAlmostEqual(beat_to_range(mhz_to_hz(1), ghz_to_hz(1), 1e-3), 149.896229, places=6)

    def test_range_resolution(self):
        # B=1GHz => 0.149896229 m；B=4GHz => 0.037474057 m
        self.assertAlmostEqual(range_resolution(ghz_to_hz(1)), 0.149896229, places=6)
        self.assertAlmostEqual(range_resolution(ghz_to_hz(4)), 0.037474057, places=6)

    def test_doppler_to_velocity(self):
        # 77GHz 载频，1kHz 多普勒 => (299792458/77e9)*1000/2 ≈ 1.946704273 m/s
        self.assertAlmostEqual(doppler_to_velocity(1000, ghz_to_hz(77)), 1.946704273, places=6)

    def test_dbm_to_watt(self):
        self.assertAlmostEqual(dbm_to_watt(0), 0.001, places=9)
        self.assertAlmostEqual(dbm_to_watt(30), 1.0, places=9)

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            range_resolution(0)
        with self.assertRaises(ValueError):
            beat_to_range(1e6, 0, 1e-3)
        with self.assertRaises(ValueError):
            beat_to_range(1e6, 1e9, -1)


if __name__ == "__main__":
    unittest.main()

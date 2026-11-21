import pytest
import math
from render import texture_atlas_padding as mod

CASES = [
    ("pad", 'm.pad_size(16, 2) == 20'),
    ("align", 'm.block_align(10, 4) == 12'),
    ("inset", 'm.uv_inset(0.5, 4) == approx(0.375)'),
    ("shift", 'm.offset_shift((0.1, 0.2), (0.5, 0.5)) == approx((0.6, 0.7))'),
    ("levels", 'm.mip_levels(16) == 5'),
    ("aniso", 'm.aniso_clamp(16, 8) == 8'),
    ("rotate", 'm.rotate_uv((0.2, 0.3), 1) == approx((0.7, 0.2))'),
    ("format", 'm.format_for(True) == "bc7"'),
    ("aspect", 'm.aspect_size(200, 100, 50) == (50, 25)'),
    ("handle", 'm.handle_valid(1, 1) is True'),
    ("page", 'm.page_for(5, 4) == 1'),
    ("sample", 'm.sample_uv(0.5, 0.5, 64, 64) == (32.0, 32.0)'),
    ("key", 'm.atlas_key(3, 2) == "3:2"'),
    ("pot", 'm.is_power_of_two(64) is True'),
    ("area", 'm.subrect_area(4, 5) == 20')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})

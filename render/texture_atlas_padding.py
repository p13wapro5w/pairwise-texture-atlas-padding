import math

def pad_size(size, levels):
    """分级留边。"""
    raise NotImplementedError("TODO: pad_size")

def block_align(size, block):
    """压缩块对齐。"""
    raise NotImplementedError("TODO: block_align")

def uv_inset(u, size):
    """UV 内缩。"""
    raise NotImplementedError("TODO: uv_inset")

def offset_shift(uv, offset):
    """偏移同步。"""
    raise NotImplementedError("TODO: offset_shift")

def mip_levels(size):
    """mip 层数。"""
    raise NotImplementedError("TODO: mip_levels")

def aniso_clamp(aniso, size):
    """各向异性限制。"""
    raise NotImplementedError("TODO: aniso_clamp")

def rotate_uv(uv, quarter):
    """旋转 UV。"""
    raise NotImplementedError("TODO: rotate_uv")

def format_for(has_alpha):
    """格式选择。"""
    raise NotImplementedError("TODO: format_for")

def aspect_size(width, height, max_side):
    """等比缩放。"""
    raise NotImplementedError("TODO: aspect_size")

def handle_valid(old, new):
    """句柄校验。"""
    raise NotImplementedError("TODO: handle_valid")

def page_for(offset, page):
    """换页。"""
    raise NotImplementedError("TODO: page_for")

def sample_uv(u, v, width, height):
    """子图采样。"""
    raise NotImplementedError("TODO: sample_uv")

def atlas_key(seed, index):
    """图集键。"""
    raise NotImplementedError("TODO: atlas_key")

def is_power_of_two(value):
    """2 的幂。"""
    raise NotImplementedError("TODO: is_power_of_two")

def subrect_area(width, height):
    """子图面积。"""
    raise NotImplementedError("TODO: subrect_area")

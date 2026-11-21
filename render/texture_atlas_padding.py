import math

def pad_size(size, levels):
    """分级留边：每个 mip 层级两侧各留 1 像素 padding。"""
    return size + 2 * levels

def block_align(size, block):
    """压缩块对齐：向上取整到块尺寸的整数倍。"""
    return ((size + block - 1) // block) * block

def uv_inset(u, size):
    """UV 内缩半像素，避免边界插值跨到邻居。"""
    return u - 0.5 / size

def offset_shift(uv, offset):
    """偏移同步：重打包后 UV 加上新的偏移。"""
    return (uv[0] + offset[0], uv[1] + offset[1])

def mip_levels(size):
    """mip 层数：floor(log2(size)) + 1。"""
    return int(math.log2(size)) + 1

def aniso_clamp(aniso, size):
    """各向异性限制：不超过子图尺寸，防止长轴采样落到邻居。"""
    return min(aniso, size)

def rotate_uv(uv, quarter):
    """旋转 UV：quarter 个 90 度顺时针。"""
    u, v = uv
    for _ in range(quarter % 4):
        u, v = 1.0 - v, u
    return (u, v)

def format_for(has_alpha):
    """格式选择：带 alpha 用 bc7，不透明用 bc1。"""
    return "bc7" if has_alpha else "bc1"

def aspect_size(width, height, max_side):
    """等比缩放：最长边限制为 max_side，保持宽高比。"""
    scale = max_side / max(width, height)
    return (round(width * scale), round(height * scale))

def handle_valid(old, new):
    """句柄校验：扩容后旧句柄是否仍有效。"""
    return old == new

def page_for(offset, page):
    """换页：偏移落在第几页。"""
    return offset // page

def sample_uv(u, v, width, height):
    """子图采样：UV 映射到纹素坐标。"""
    return (u * width, v * height)

def atlas_key(seed, index):
    """图集键。"""
    return f"{seed}:{index}"

def is_power_of_two(value):
    """2 的幂。"""
    return value > 0 and (value & (value - 1)) == 0

def subrect_area(width, height):
    """子图面积。"""
    return width * height

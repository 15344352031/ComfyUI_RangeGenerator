"""
范围数列生成器节点定义
"""

class RangeGenerator:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "range_start": ("INT", {"default": 0, "min": -10000, "max": 10000, "step": 1}),
                "range_end": ("INT", {"default": 10, "min": -10000, "max": 10000, "step": 1}),
                "step": ("INT", {"default": 1, "min": 1, "max": 1000, "step": 1}),
                "allow_reverse": ("BOOLEAN", {"default": True}),
                "prefix": ("STRING", {"default": ""}),
                "suffix": ("STRING", {"default": ""}),
                "global_prefix": ("STRING", {"default": ""}),
                "global_suffix": ("STRING", {"default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("range_string",)
    FUNCTION = "generate_range"
    CATEGORY = "RangeGenerator"
    
    def generate_range(self, range_start, range_end, step, allow_reverse, prefix, suffix, global_prefix, global_suffix):
        try:
            # 确保输入是整数
            range_start = int(range_start)
            range_end = int(range_end)
            step = int(step)
            
            # 处理步长为0的情况
            if step <= 0:
                step = 1
            
            # 生成范围数列
            if range_end < range_start:
                if allow_reverse:
                    # 支持逆向生成数列
                    numbers = list(range(range_start, range_end - 1, -step))
                    # 应用前缀和后缀到每个数字
                    formatted_numbers = [f"{prefix}{i}{suffix}" for i in numbers]
                    # 应用总体前缀和后缀
                    range_string = f"{global_prefix}{', '.join(formatted_numbers)}{global_suffix}"
                else:
                    range_string = ""
            else:
                numbers = list(range(range_start, range_end + 1, step))
                # 应用前缀和后缀到每个数字
                formatted_numbers = [f"{prefix}{i}{suffix}" for i in numbers]
                # 应用总体前缀和后缀
                range_string = f"{global_prefix}{', '.join(formatted_numbers)}{global_suffix}"
            
            return (range_string,)
        except Exception:
            return ("",)

# 节点映射
NODE_CLASS_MAPPINGS = {
    "RangeGenerator": RangeGenerator
}

# 节点显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "RangeGenerator": "范围数列生成器"
} 
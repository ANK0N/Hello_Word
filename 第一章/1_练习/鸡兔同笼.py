
def calculate_chicken_and_rabbit(total_heads, total_legs):
    rabbit_count = (total_legs - 2 * total_heads) / 2
    chicken_count = total_heads - rabbit_count
    if chicken_count >= 0 and rabbit_count >= 0 and (chicken_count + rabbit_count) == total_heads:
        return f"坤的数量：{int(chicken_count)}，兔子的数量：{int(rabbit_count)}"
    else:
        return "参数不合理"
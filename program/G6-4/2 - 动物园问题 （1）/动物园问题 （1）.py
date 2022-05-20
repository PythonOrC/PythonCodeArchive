visit = {"猴子", "狮子", "老虎", "大象", "长颈鹿", "鳄鱼", "猎豹", "斑马"}
plans = {
    "A": {"大象", "狒狒", "鳄鱼", "海豚", "蜘蛛"},
    "B": {"老虎", "猎豹", "猩猩"},
    "C": {"猴子", "狮子", "老鹰", "长颈鹿"},
    "D": {"河马", "长臂猿", "老鹰", "斑马", "灰熊"},
    "E": {"猎豹", "斑马", "灰熊"},
}
best = set()
for plan, animal in plans.items():
    target = visit & animal
    if len(target) > len(best):
        best = target
        best_plan = plan
print(best_plan, visit - best)

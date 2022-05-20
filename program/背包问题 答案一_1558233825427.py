# 制定规则: 从价值最大的开始装
# 找目标数
target = 175
# 种类  制定规则后按照规则进行排序,方便下面的for循环进行对比
name = ["D", "B", "F", "E", "C", "G", "A"]
# 重量
weight = [50, 30, 10, 40, 35, 30, 30, 10]
# 价值
value = [50, 40, 40, 35, 30, 30, 10]
# 结果
number = [0, 0, 0, 0, 0, 0, 0]


total_value = 0
# 循环,从最大价值的物品开始找
for i in range(7):
    # 判断,当前背包内容大于等于物品重量
    if target >= weight[i]:
        # 取整, 算出当前物品价值可以找的最大数量(此时物品已经是从价值最大开始排序)
        number[i] = number[i] + target // weight[i]
        # 算出当前背包剩余容量
        target = target - weight[i] * number[i]
        # 计算总价值
        total_value = total_value + value[i]*number[i]


print("背包总价值为:", total_value)
print("背包剩余容量为:", target, "Kg")
for i in range(7):
    print(name[i], "物品数量为:", number[i], "个")
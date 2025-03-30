import torch

# 创建两个张量
a = torch.tensor([1, 2, 3])  # 形状为 (3,)
b = torch.tensor([[4, 5, 6], [7, 8, 9]])  # 形状为 (2, 3)

# 执行加法操作
c = a + b

print("a 的形状:", a.shape)
print("b 的形状:", b.shape)
print("c 的形状:", c.shape)
print("c 的值:\n", c)
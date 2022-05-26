import torch

x = torch.Tensor([5, 3])
y = torch.Tensor([2, 1])

print(x * y)

x = torch.zeros([2, 5])

print(x)

x.shape
torch.Size([2, 5])

y = torch.rand([2, 5])
print(y)

#flatten tensor before passing it into neural network
y = y.view([1, 10])
print(y)
import torch
import time

torch_curr = time.time()
for x in range(100000):
    y = torch.FloatTensor([[2,2],[2,2]])
    z = torch.FloatTensor([[1,1],[1,1]])
    res = y.add(z)
print('torch time: ', time.time() - torch_curr)

import syft as sy
hook = sy.TorchHook()
syft_curr = time.time()
for x in range(100000):
    y = sy.FloatTensor([[2,2],[2,2]])
    z = sy.FloatTensor([[1,1],[1,1]])
    res = y.add(z)
print('syft time: ', time.time() - syft_curr)

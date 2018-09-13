## Test environments
OriginalEnv:
- Ubuntu 16.04
- i7 processor (6-core)
- torch 0.3.0 (iirc)
UpdatedEnv:
- Mac OS X High Sierra 10.13.6
- i7 processor (4-core)
- torch 0.3.1

## Original test case:
```python
for x in range(100000):
    y = torch.FloatTensor([[2,2],[2,2]])
    z = torch.FloatTensor([[1,1],[1,1]])
    res = y.add(z)
```

##### Native PyTorch (OriginalEnv):
```
CPU times: user 1.3 s, sys: 25.7 ms, total: 1.33 s
Wall time: 1.32 s
```

##### Native PyTorch (UpdatedEnv):
```
Wall time: 0.4715731143951416 s
```

##### Original Hooks (OriginalEnv):
```
CPU times: user 2.21 s, sys: 567 ms, total: 2.78 s
Wall time: 2.31 s
```

## PySyft code:
```python
for x in range(100000):
    y = sy.FloatTensor([[2,2],[2,2]])
    z = sy.FloatTensor([[1,1],[1,1]])
    res = y.add(z)
```

##### New PySyft Hooks (UpdatedEnv):
```
Wall time: 12.89029598236084 s
```

## Conclusions
- PySyft to PyTorch speed ratio for UpdatedEnv is about 12.89 / 0.4716 which is 27.33x
- Assuming we could run this on OriginalEnv and it would translate similarly, the current PySyft code would require 27.33 * 1.32 s ~= 36.08 s.
- This means that, under these assumptions and running in OriginalEnv, we have the following approximate results for 100k iterated `FloatTensor.add` operations:
  - Native PyTorch:      1.32 s
  - Original Hooks:      2.31 s (1.75x)
  - New PySyft Hooks:  36.08 s (27.33x)

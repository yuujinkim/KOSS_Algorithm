# 순열 라이브러리
리스트에서 n개를 골라 __순서를 고려해__ 나열
### permutations(리스트, n)
```
import itertools as it
for tmp in it.permutations([1,2,3,4], 3):
    print(tmp)
```

---

# 조합 라이브러리
리스트에서 n개를 골라 __순서를 고려하지 않고__ 나열
### combinations(리스트, n)
```
import itertools as it
for tmp in it.combinations([1,2,3,4], 3):
    print(tmp)
```

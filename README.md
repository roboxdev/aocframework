##AoC Framework

Helper class that aims to reduce your boilerplate code when solving adventofcode.com challenges.

Does following:
* fetch puzzle input
* save puzzle input to file
* splitlines() your puzzle input
* run tests

####Usage example
```python
from aocframework import AoCFramework


class Day(AoCFramework):
    test_cases = (
        ('abcde fghij', 1),
        ('abcde xyz ecdab', 0),
        ('a ab abc abd abf abj', 1),
        ('iiii oiii ooii oooi oooo', 1),
        ('oiii ioii iioi iiio', 0),
    )

    def go(self):
        counter = 0
        for line in self.linesplitted:
            p = [''.join(sorted(v)) for v in line.split()]
            if len(p) == len(set(p)):
                counter += 1
        return counter


Day()
```
Output
```
 puzzle input
***
[Test OK] abcde fghij: 1
[Test OK] abcde xyz ecdab: 0
[Test OK] a ab abc abd abf abj: 1
[Test OK] iiii oiii ooii oooi oooo: 1
[Test OK] oiii ioii iioi iiio: 0
Answer: 231

```

Please note, code heavily depends on folder structure. It should look like this
```
aoc2015/
...
aoc2017/
    d1/
    d2/
    ...
    d12/
        foo1.py
        foo2.py
session_token

```
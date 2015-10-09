# README
####Everything is written in Python 2.7.
------------------

### Question 1: Anagram
Program Usage:

```
$anagram/> python main.py --help
```

Example:

```
$anagram/> python main.py incredible
decline rib
dirl in ce be
```

Run Sample Test:

```
$anagram/> python tests.py
SUCCESS
```

First output string will be two words anagram.
Second output string will be most words anagram.

##### Known Issues:
Program takes a long time for long words. (14+ letters.)

### Question 2: Tail
Program Usage:

```
$tail/> python main.py --help
```

Example:

```
$tail/> python main.py -n 5 ../anagram/words.txt
zythem
Zythia
zythum
Zyzomys
Zyzzogeton
```

Run Sample Test:

```
$tail/> python tests.py
```
No output means all tests passed.
# Git Bisect Example

* Initiate the git bisect as
```sh
$ git bisect start
```

* Indicate the commit where the code was working fine, and where the bug is noticed. This can be done using git bisect good and git bisect bad as follow -
```sh
$ git bisect good ed81cd1878b4d75b0eb9ec15af63c5449d7822e6
$ git bisect bad 0a1e7cd830489d594b74d5c5a0cb66fadeb88370
```

* Now tell the git bisect to run test to check if the commit is good/bad.
```sh
$ git bisect run python test.py 
```



Sunils-MacBook-Pro:git_bisect Sunny$ git bisect start
Already on 'master'
Your branch is up-to-date with 'origin/master'.
Sunils-MacBook-Pro:git_bisect Sunny$ git bisect good ed81cd1878b4d75b0eb9ec15af63c5449d7822e6
Sunils-MacBook-Pro:git_bisect Sunny$ git bisect bad 0a1e7cd830489d594b74d5c5a0cb66fadeb88370
Bisecting: 3 revisions left to test after this (roughly 2 steps)
[4702e7379a56a81e048e55cfe7c80697bbf16204] added sub function
Sunils-MacBook-Pro:git_bisect Sunny$ git bisect run python test.py 
running python test.py
Traceback (most recent call last):
  File "test.py", line 16, in <module>
    from main import Add, Sub
  File "/Users/Sunny/prv/github/git_bisect/main.py", line 23
    return a - b
               ^
IndentationError: unindent does not match any outer indentation level
Bisecting: 1 revision left to test after this (roughly 1 step)
[df8a1e970a6b9e7ba48e643b755f3bc7d7c237ec] added sub function
running python test.py
Traceback (most recent call last):
  File "test.py", line 16, in <module>
    from main import Add
  File "/Users/Sunny/prv/github/git_bisect/main.py", line 23
    return a - b
               ^
IndentationError: unindent does not match any outer indentation level
Bisecting: 0 revisions left to test after this (roughly 0 steps)
[b3848e7a2a44e66196bfedb3e9ee7d605c1df570] return sub of a, b
running python test.py
Traceback (most recent call last):
  File "test.py", line 16, in <module>
    from main import Add
  File "/Users/Sunny/prv/github/git_bisect/main.py", line 23
    return a - b
               ^
IndentationError: unindent does not match any outer indentation level
b3848e7a2a44e66196bfedb3e9ee7d605c1df570 is the first bad commit
commit b3848e7a2a44e66196bfedb3e9ee7d605c1df570
Author: Sunil <sunhick@gmail.com>
Date:   Thu Sep 1 16:50:26 2016 -0600

    return sub of a, b

:100644 100644 500dd1b467260e7078d67a24836ee0f05b3393bd f0a394220ed0148a69ee584e33ac8a31e52e3c98 M	main.py
bisect run success
Sunils-MacBook-Pro:git_bisect Sunny$ 

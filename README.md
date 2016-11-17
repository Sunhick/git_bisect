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

```sh
output:
$ git bisect run python test.py
...

b3848e7a2a44e66196bfedb3e9ee7d605c1df570 is the first bad commit
$
```

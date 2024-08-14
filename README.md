# cou
CLI utility that counts lines of code within files, analyzes directories containing code, and provides a concise summary.

## Usage
`cou path [options]`


Options:
- `[path]`, required, should contain at least one dir/file, if there are more than one, paths should be separated by spaces like `cou path1 path2 path3`.
- `[-l, --list]`, list of files with lines of code count. Default state: false.
- `[-s, --statistic]`, shows statistic: total num of dirs and files, all languages that used, lines per language. Default state: false.
- `[-e, --exclude]`, counts lines of code, excluding selected files/dirs (space-separated, at least one file/dir). Default state: none.


To Do:
- exclude hidden dirs (like .git, .venv) from files search
- add [-t, -tree] option (shows project tree with number of lines of code)



## Examples

```python
# walk through all files in current directory, count lines of code in files with code 
# and shows total number of lines of code

# input
cou .

# output
Processing files: 100%|█████████████████████████████| 760/760 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 237158 lines of code.
```

```python
# walk through all files in './bar' and './baz' directories, count lines of code in files with code 
# and shows total number of lines of code

# input
cou bar baz

# output
Processing files: 100%|█████████████████████████████| 760/760 [00:00<00:00, 5591.07file/s]
Paths "/users/foo/projects/bar", "/users/foo/projects/baz" contains 237158 lines of code.
```

```python
# shows list of files with number of code in it

# input
cou . -l

# output
Processing files: 100%|█████████████████████████████| 760/760 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 237158 lines of code.

File "/users/foo/projects/bar/main.py" contain 5409 lines of code;
File "/users/foo/projects/bar/utils.py" contain 809 lines of code;
...
```

```python
# analyze current directory and show statistic

# input
cou . -s

# output
Processing files: 100%|█████████████████████████████| 760/760 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 237158 lines of code.
Directories: 17, files with code: 760.
Languages: 
    Python  81%, 192.097 lines;
    C       17%,  40.316 lines;
    Go       2%,   4.743 lines;

```

```python
# shows total number of lines of code in current directory, excluding './bar' dir and './baz/setup.py' file

# input
cou . -e bar baz/setup.py

# output
Processing files: 100%|█████████████████████████████| 743/743 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 212090 lines of code.
...
```

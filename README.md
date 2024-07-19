# cou
CLI utility that counts lines of code within files, analyzes directories containing code, and provides a concise summary.  
  
Cou count lines quite fast, for example: 30.000 files and 10.000.000 lines of code it count for 5 seconds. 
Regular pet-projects cou count for less than 1 second.

## Usage:
`cou path [options]`


Options:
- [-l, --list], list of files with lines of code count.
- [-s, --statistic], shows statistic: total num of lines of code, total num of dirs and files, all languages that
                     used, lines per language.
- [-e, --exclude], counts lines of code, excluding selected files/dirs (space-separated, at least one file/dir).
- [-m, --multy], count lines of code in chosen files/dirs (space-separated, at least one file/dir).


To Do:
- exclude from files search hidden dirs like .git, .venv
- add [-t, -tree] option ([-t, --tree], shows project tree with number of lines of code)



## Examples

```commandline
# walk through all files in current directory, count lines of code in files with code 
# and shows total number of lines of code

# input
cou .

# output
Processing files: 100%|█████████████████████████████| 760/760 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 237158 lines of code.
```

```commandline
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

```commandline
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

```commandline
# shows total number of lines of code in current directory, excluding './bar' dir and './baz/setup.py' file

# input
cou . -e bar baz/setup.py

# output
Processing files: 100%|█████████████████████████████| 743/743 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 212090 lines of code.
...
```

```commandline
# shows total number of lines of code in './bar' and './baz' directories

# input
cou . -m bar baz

# output
Processing files: 100%|█████████████████████████████| 209/209 [00:00<00:00, 5591.07file/s]
Path "/users/foo/projects" contains 12318 lines of code.
...
```

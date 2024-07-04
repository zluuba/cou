# cou
CLI utility that counts lines of code within files, analyzes directories containing code, and provides a concise summary.

## Usage:
`cou path/to/file/or/dir [options]`


Options:
- [-e, --exclude] + [list,of,paths], counts lines of code, excluding selected files/dirs.
- [-l, --list], list of files with lines of code count
- [-s, --statistic], shows statistic like: total num of lines of code, total num of dirs and files, all languages that
                     used, lines per language.
- [-t, --tree], shows project tree with number of lines of code


Possible options:
- [-m, --multy] + [list,of,paths], count lines of code in chosen files/dirs


To Do:
- exclude from files search hidden dirs like .git, .venv


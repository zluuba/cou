# cou
CLI utility that counts lines of code within files, analyzes directories containing code, and provides a concise summary.

## Usage:
`cou [options]`


options:
- h - help
- p - path
- c - comments
- e - empty lines
- f - files
- l - specify programming language (file extension or full name - in every case (lower, upper)) 
      to count files only with that lang (ex.: rc,py | rust,python | C,JavaScript)
- r - in range (ex.: 10,1000)
- s - search for


### Main
- `cou -h` - print help man
- `cou .` - counting in curr directory.
- `cou -p /full/path/` - counting lines in all files in full/rel path.
- `cou -p /full/path/to/file.py` - counting lines in file in full/rel path.
- `cou -c` - counting without comments.
- `cou -e` - count without empty lines.
- `cou -ce` - counting without comments and empty lines.
- `cou -f` - counting files with code (files with .py extension).
- `cou -fe` - counting files with code, exclude empty files (with 0 lines).
- `cou -l {lang1,lang2}` - counting files with code in specified languages (file extension or language full name)
- `cou -fr {start_num,finish_num}` - counting files with code where lines count from {start_num} to {finish_num} (not included).

or did `cou files [options]`


### Code
- `cou code -h` - print help man
- `cou code -fs "keyword"` - scan curr dir to files that contain keyword, print number of files with keyword.
- `cou code -fs "keyword" -full` - scan curr dir to files that contain keyword, print number of lines with keyword and table with file path/name and line when this word are was find.

### Directory Analizer
- `cou analyze .` - analyze files, show short reference in table: files count, files with code (add diff languages), code lines count in total, lines per file, etc.


## Usage
```ch
# count lines of code without comments and empty lines in all files with code in current directory
cou .

# count lines of code with comments and empty lines in file on path "path/to/file.py"
cou path/to/file.py -ce
```
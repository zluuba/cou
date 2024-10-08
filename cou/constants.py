BASIC_OFFSET = 3

EXTENSIONS = {
    'Python': ['.py'],
    'C': ['.c', '.h'],
    'C++': ['.cpp', '.cc', '.cxx', '.hpp', '.hh', '.hxx', '.h++'],
    'C#': ['.cs'],
    'Java': ['.java'],
    'JavaScript': ['.js', '.jsx'],
    'TypeScript': ['.ts', '.tsx'],
    'HTML': ['.html', '.htm'],
    'CSS': ['.css'],
    'Ruby': ['.rb'],
    'PHP': ['.php'],
    'Go': ['.go'],
    'Rust': ['.rs'],
    'Swift': ['.swift'],
    'Kotlin': ['.kt', '.kts'],
    'Objective-C': ['.m', '.mm'],
    'Shell': ['.sh', '.bash'],
    'Perl': ['.pl', '.pm'],
    'R': ['.r', '.R'],
    'Lua': ['.lua'],
    'Scala': ['.scala'],
    'Haskell': ['.hs'],
    'Erlang': ['.erl', '.hrl'],
    'Elixir': ['.ex', '.exs'],
    'Dart': ['.dart'],
    'MATLAB': ['.m'],
    'Julia': ['.jl'],
    'Assembly': ['.asm', '.s', '.S'],
    'Fortran': ['.f', '.for', '.f90'],
    'COBOL': ['.cob', '.cbl'],
    'Pascal': ['.pas'],
    'Visual Basic': ['.vb'],
    'SQL': ['.sql'],
    'Markdown': ['.md'],
    'YAML': ['.yaml', '.yml'],
    'JSON': ['.json'],
    'XML': ['.xml'],
    'Dockerfile': ['Dockerfile'],
    'Makefile': ['Makefile'],
    'TOML': ['.toml'],
    'INI': ['.ini'],
    'VHDL': ['.vhdl', '.vhd'],
    'Verilog': ['.v', '.vh', '.sv'],
    'OCaml': ['.ml', '.mli'],
    'Prolog': ['.pl'],
    'Scheme': ['.scm'],
    'Lisp': ['.lisp', '.lsp'],
}

ALLOWED_EXTENSIONS = set(ext for exts in EXTENSIONS.values() for ext in exts)

Python 3.14.2 (v3.14.2:df793163d58, Dec  5 2025, 12:18:06) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>> from pathlib import Path
>>> print(Path.cwd())
/Users/suzanneberger/Documents
>>> basename = "bergerbits.json"
>>> jsonfile = Path.cwd() / basename
>>> jsonfile
PosixPath('/Users/suzanneberger/Documents/bergerbits.json')
>>> thisdir = "/Users/suzanneberger/Documents/teaching"
>>> this_path = Path(thisdir)
>>> this_path.is_dir()
True
>>> Path(jsonfile).is_file()
False
>>> thisfile = this_path / "deozdenny.json"
>>> Path(thisfile).is_file()
True

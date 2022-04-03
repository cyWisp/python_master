# mv_all
Recursive firectory copy tool...

Will recursively copy the directory specified in the first argument to all
the children within the directory specified in the second.

Usage (python/python3): python mv_all.py [source_dir] [target_dir]
Usage (executable): ./mv_all.exe [source_dir] [target_dir]

Currently does not have any error checking implemented- will crash if target dirs
already exist.


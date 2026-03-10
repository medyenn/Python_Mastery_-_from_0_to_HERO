#!/usr/bin/env python3

# We're going to try to install a package using the pip PM
# from our terminal by the command : pip install cowsay

import cowsay  # package
import sys  # module

if len(sys.argv) == 2:
    cowsay.cow("Hello, " + sys.argv[1])
    cowsay.trex(sys.argv[1] + " is the STRONGEST future data scientist !")

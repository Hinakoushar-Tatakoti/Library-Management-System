#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "Library-Management-System"
version= "1.0"

authors = [Author("Hinakoushar Tatakoti","Hinakoushar.Tatakoti@outlook.com")]
license = "None"
default_task = "publish"


@init
def set_properties(project):
    project.set_property("coverage_break_build", False) # default is True



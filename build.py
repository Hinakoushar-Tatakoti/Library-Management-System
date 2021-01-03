from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("pypi:pybuilder_pytest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")


name = "Library-Management-System"
version = "1.0"

summary = "Library-Management-System"
url = "https://github.com/Hinakoushar-Tatakoti/Library-Management-System.git"


authors = [Author("Hinakoushar Tatakoti", "Hinakoushar.Tatakoti@outlook.com")]
license = "Beuth University Berlin"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("mockito")

@init
def set_properties(project):
    pass
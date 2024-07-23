name = "blosc"

version = "1.17.2.hh.1.0.0"

authors = [
    "Blosc",
]

description = """High performance compressor optimized for binary data"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_BLOSC_ROOT = "{root}"
    env.BLOSC_ROOT = "{root}"
    env.BLOSC_LOCATION = "{root}"
    env.BLOSC_INCLUDE_DIR = "{root}/include"
    env.BLOSC_LIBRARY_DIR = "{root}/lib"

    env.LD_LIBRARY_PATH.append("{root}/lib")
    env.PKG_CONFIG_PATH.append("{root}/lib/pkgconfig")


uuid = "repository.c-blosc"

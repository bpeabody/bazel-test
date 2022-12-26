# Overview

The purpose of this repo is to serve as both a proof of concept of a
bazel-based Python build system and a draft proposal for structuring a monorepo
using Bazel.  Note that I've structured it for now with the idea that
cross-language dependencies are not allowed but that could be changed.

# Features

The system has many useful aspects, including:

* builds are fast and minimal
    * when building a specific package, only its dependencies are built
    * when building anything it only rebuilds things that need to be rebuilt
    * this includes external dependencies
* tests are fast and minimal
    * similar to builds, and it will not rerun tests that don't need to be
      re-run
* dependencies must be explicitly specified -- even though all projects are in
  the repo, `import` will work only when the dependencies are explicitly
  specified
* deployments are minimal

# Trying it Out

First, you need to install bazel (`brew install bazel` on a mac).  Next,
initialize the bazel submodule

```
$ git submodule update --init
```

Then cd to the root of the python projects:

```
cd src/python
```

Sample commands:

```
# run the apps

bazel run //app_1
bazel run //app_2

# run individual tests

bazel test //lib_y:test_num_some
bazel test //lib_x:test_x_util

# build everything

bazel build //...

# test everything

bazel test //...

```

# Repo Structure

`src` -- where all authored source lives

`src/python` -- Where python source lives; every "project" is a directory in
this folder.  More structure could be added, e.g. `src/python/apps` for
applications/services and `src/python/lib` for libraries.

`src/python/external` -- where requirements files live

`tools/rules_python` -- submodule for the Bazel rules repo


# Bazel Files

`src/python/WORKSPACE.bazel` -- global configuration
`$project/BUILD.bazel` -- project files

# Example projects:

`lib_x` -- a library with no dependencies
`lib_y` -- a library that uses `numpy`
`app_1` -- an application that uses `lib_x` and `argparse`
`app_2` -- an application that uses `lib_y`

# Contributing

## Issues

You can find our open issues in the project's
[issue tracker](https://github.com/vizzuhq/ipyvizzu/issues). Please let us know
if you find any issues or have any feature requests there.

## Contributing

If you want to contribute to the project, your help is very welcome. Just fork
the project, make your changes and send us a pull request. You can find the
detailed description of how to do this in
[Github's guide to contributing to projects](https://docs.github.com/en/get-started/quickstart/contributing-to-projects).

## CI-CD

### Development environment

For contributing to the project, it is recommended to use `Python` `3.10` as the
primary programming language for most parts of the source code. However, a
specific portion of the codebase is written in `JavaScript`. If you plan to
contribute to this `JavaScript` part or the documentation, you will need
`Node.js`, preferably version `18`.

The following steps demonstrate how to set up the development environment on an
`Ubuntu` `22.04` operating system. However, the process can be adapted for other
operating systems as well.

To start using the `ipyvizzu` development environment, you need to create a
virtual environment and install `pdm` within it.

```sh
python3.10 -m venv ".venv"
source .venv/bin/activate
pip install pdm==2.8.0
```

Once set up, you can utilize the pre-defined `pdm` scripts. For example, you can
initialize the entire development environment using the command `pdm run init`,
or specific parts like `init_src_py`, `init_src`, `init_docs`, or `init_tools`.

```sh
pdm run init
```

**Note:** For all available `pdm` scripts, run `pdm run --list`.

The development requirements are installed based on the `pdm.lock` and
`package-lock.json` files. To update the development requirements, you can use
the command `pdm run lock`.

For better development practices, you can set up `pre-commit` and `pre-push`
hooks in your local `Git` repository. The `pre-commit` hook will format the code
automatically, and the `pre-push` hook will run the CI steps before pushing your
changes.

```sh
pre-commit install --hook-type pre-commit --hook-type pre-push -c ./tools/ci/.pre-commit-ubuntu.yaml
```

**Note:** The provided `.pre-commit-ubuntu.yaml` configuration file is tailored
for `Ubuntu` `22.04`. If you intend to use another operating system, you may
need to create a custom configuration file suitable for that environment.

### CI

The CI pipeline includes code formatting checks, code analysis, typing
validation, and unit tests for the `ipyvizzu` project.

To run the entire CI pipeline, execute the following `pdm` script:

```sh
pdm run ci
```

However, if you want to run the CI steps on specific parts of the project, you
can use the following scripts: `ci_src_py`, `ci_src`, `ci_docs`, or `ci_tools`.

#### Formatting

You can check the code's formatting using the `format` script:

```sh
pdm run format
```

If you need to fix any formatting issues, you can use the `fix_format` script:

```sh
pdm run fix_format
```

If you wish to format specific parts of the project, you can use the following
scripts: `format_src_py`, `format_src`, `format_docs`, `format_tools`, or
`fix_format_src_py`, `fix_format_src`, `fix_format_docs`, `fix_format_tools`.

#### Code analyses

To perform code analyses, you can use the `lint` script:

```sh
pdm run lint
```

If you need to run code analyses for specific parts of the project, you can
utilize the following scripts: `lint_src_py`, `lint_src`, `lint_docs`, or
`lint_tools`.

#### Typing

For type checking, you can use the `type` script:

```sh
pdm run type
```

If you want to check specific parts of the project, you can use the following
scripts: `type_src` or `type_tools`.

#### Testing

The project is tested using the `unittest` testing framework and `tox`. To run
the tests, you can use the `test` script:

```sh
pdm run test
```

### Documentation

**Note:** The preset, static, animated, and analytical operation examples are
generated from the [vizzu-lib](https://github.com/vizzuhq/vizzu-lib) repository.
If you wish to build them as well, run the following command before building the
site.

```sh
git clone --depth 1 https://github.com/vizzuhq/vizzu-lib.git
```

To build the documentation, you can use the `docs_build` script:

```sh
pdm run docs_build
```

You can read the online version at [ipyvizzu.com](https://ipyvizzu.vizzuhq.com).

### Release

`ipyvizzu` is distributed on [pypi](https://pypi.org/project/ipyvizzu).
**Note:** You need to be an administrator to release the project.

To release `ipyvizzu`, follow the steps below:

- Increase the version number in `__version__.py`. The version bump should be in
  a separate commit.

- Generate the release notes and publish the new release on
  [Releases](https://github.com/vizzuhq/ipyvizzu/releases).

**Note:** Publishing a new release will automatically trigger the `release`
workflow, which builds, checks, and uploads the `ipyvizzu` package to
[pypi](https://pypi.org/project/ipyvizzu).

Before making a release, you can build and check the package using the
`pkg_release` script:

```sh
pdm run pkg_release
```

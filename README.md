[![codecov.io](https://codecov.io/github/sbellem/example-python/coverage.svg?branch=master)](https://codecov.io/github/sbellem/example-python?branch=master)


Python Example
=======
| [https://codecov.io/][1] | [@codecov][2] | [hello@codecov.io][3] |
| ------------------------ | ------------- | --------------------- |

> Example of how to integrate with [Codecov.io][1] for your **awesome** Python project!

## See this repo's [Coverage Reports][4]


## Usage

```sh
pip install codecov
codecov --token=<repo token>
```

## Using `tox`?
Codecov can be ran from inside your `tox.ini` please make sure you pass all the necessary environment variables through:

```
[testenv]
passenv = CI TRAVIS_BUILD_ID TRAVIS TRAVIS_BRANCH TRAVIS_JOB_NUMBER TRAVIS_PULL_REQUEST TRAVIS_JOB_ID TRAVIS_REPO_SLUG TRAVIS_COMMIT
deps = codecov>=1.4.0
commands = codecov -e TOXENV
```
> See all the environment variable for other CI providers [here](https://github.com/codecov/codecov-python/blob/master/codecov/__init__.py#L260-L430). Note the `-e TOXENV` is used to distinquish builds in Codecov UI [example](https://codecov.io/gh/pyca/cryptography?ref=99c45f19be196cb45bf8de8ea105fcb4619ab504&build=7312.1).

## Private repositories
Please provide your private repository token (found at Codecov) to upload reports.

```
export CODECOV_TOKEN=:token
codecov
# or
codecov -t :token
```

# Some example CI providers

### [![travis-org](https://avatars2.githubusercontent.com/u/639823?v=2&s=50)](https://travis-ci.org) Travis CI
> Append to your `.travis.yml`

```yml
install:
    pip install codecov
after_success:
    codecov
```

> Note: No need to include a repository token for **public** repos on Travis


### [![circleci](https://avatars0.githubusercontent.com/u/1231870?v=2&s=50)](https://circleci.com/) [Circle CI](https://circleci.com/).
> Append to your `circle.yml` file

```yml
test:
    post:
        - pip install codecov && codecov
```
> Note: No need to include a repository token for **public** repos on CircleCI




[1]: https://codecov.io/
[2]: https://twitter.com/codecov
[3]: mailto:hello@codecov.io
[4]: https://codecov.io/github/codecov/example-python

# 🌀 blue-plugin

🌀 `blue-plugin` is a git template for an 🚀 [`awesome-bash-cli`](https://github.com/kamangir/awesome-bash-cli) (`abcli`) plugin, to build [things like these](https://github.com/kamangir?tab=repositories), that out-of-the-box support,

- a git repo with actions.
- [pytest](https://docs.pytest.org/).
- [pylint](https://pypi.org/project/pylint/).
- a python package.
- [pypi](https://pypi.org/).
- a bash interface.
- bash testing.

## installation

```bash
pip install blue-plugin
```

## creating a blue-plugin

1️⃣ create a new repository from [this template](https://github.com/kamangir/blue-plugin),

2️⃣ complete `<repo-name>` and `<plugin-name>` and run,

```bash
@git clone <repo-name> cd

@plugins transform <repo-name>

@init
<plugin-name> help
```

---

[![PyPI version](https://img.shields.io/pypi/v/blue-plugin.svg)](https://pypi.org/project/blue-plugin/)

To use on [AWS SageMaker](https://aws.amazon.com/sagemaker/) replace `<plugin-name>` with the name of the plugin and follow [these instructions](https://github.com/kamangir/notebooks-and-scripts/blob/main/SageMaker.md).

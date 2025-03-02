# mujoco-stubs
Mujoco Python Stubs for Code Completion

Once installed, your IDE will provide full code completion for MuJoCo's Python API.

## Installation

Clone the repository and install it in editable mode:

```bash
git clone https://github.com/I-am-Future/mujoco-stubs.git
cd mujoco-stubs
pip install -e .
```

## Bonus: Generating (updating) `.pyi` files if needed

The script `mujoco-gen_mujoco_stubs.py` automatically generates MuJoCo `.pyi` stub files. If you need to update the stubs / do some modifications, you can run this script with:

```bash
python gen_mujoco_stubs.py
```

**NOTE:** If `stubgen` is missing, install `mypy` to enable stub generation:

```bash
pip install mypy
```

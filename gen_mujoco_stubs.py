import os
import shutil
import site
import subprocess

force_regen = True


current_dir = os.getcwd()
stubs_dir = os.path.join(current_dir, "stubs")

modules = [
    "mujoco._callbacks",
    "mujoco._constants",
    "mujoco._enums",
    "mujoco._errors",
    "mujoco._functions",
    "mujoco._render",
    "mujoco._specs",
    "mujoco._structs",
    "mujoco.gl_context",
    "mujoco.renderer",
]

# 1. Generate stub files
if force_regen or not os.path.exists(stubs_dir):
    print("Generating stub files...")
    for module in modules:
        subprocess.run(["stubgen", "-m", module, "-o", stubs_dir, "--include-docstrings"], check=True)

    # 2. Make __init__.py files
    init_pyi_path = os.path.join(stubs_dir, "mujoco", "__init__.pyi")
    print("Creating __init__.pyi...")

    merged_content = """\"\"\" My generated .pyi file for MuJoCo \"\"\"\n\n"""

    for module in modules:
        module_pyi_path = os.path.join(stubs_dir, "mujoco", f"{module.split('.')[-1]}.pyi")
        if os.path.exists(module_pyi_path):
            with open(module_pyi_path, "r", encoding="utf-8") as f:
                merged_content += f"\n# --- {module} ---\n" + f.read()

    with open(init_pyi_path, "w", encoding="utf-8") as f:
        f.write(merged_content)

print(f"Stub files successfully generated at {init_pyi_path}!")

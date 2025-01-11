import os
import shutil
from pathlib import Path


def restore_structure():
    # 获取项目根目录
    root = Path(__file__).parent

    # 创建必要的目录
    directories = [
        "app",
        "app/static",
        "app/static/css",
        "app/static/js",
        "app/templates",
        "app/utils",
    ]

    for dir_path in directories:
        os.makedirs(str(root / dir_path), exist_ok=True)

    # 移动文件到正确的位置
    file_moves = [
        ("static/css/style.css", "app/static/css/style.css"),
        ("static/js/app.js", "app/static/js/main.js"),
        ("templates/base.html", "app/templates/base.html"),
        ("templates/index.html", "app/templates/index.html"),
        ("index.py", "app/routes.py"),
    ]

    for src, dst in file_moves:
        src_path = root / src
        dst_path = root / dst
        if src_path.exists():
            print(f"Moving {src} to {dst}")
            shutil.copy2(str(src_path), str(dst_path))
            os.remove(str(src_path))

    # 删除不需要的目录
    cleanup_dirs = ["static", "templates"]
    for dir_path in cleanup_dirs:
        dir_full_path = root / dir_path
        if dir_full_path.exists():
            print(f"Removing directory {dir_path}")
            shutil.rmtree(str(dir_full_path))

    print("Project structure restored!")


if __name__ == "__main__":
    restore_structure()

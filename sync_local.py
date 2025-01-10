import os
import shutil
from pathlib import Path


def sync_files():
    # 定义源文件路径（app目录）
    LOCAL_PATH = Path(__file__).parent / "app"

    # 定义目标文件路径（当前项目目录）
    PROJECT_PATH = Path(__file__).parent

    # 需要同步的文件映射
    files_to_sync = {
        # 静态文件
        "static/css/style.css": "static/css/style.css",
        "static/js/main.js": "static/js/app.js",
        # 模板文件
        "templates/base.html": "templates/base.html",
        "templates/index.html": "templates/index.html",
        # Python 文件
        "routes.py": "index.py",  # 注意这里做了文件名映射
        "__init__.py": "app.py",  # 添加应用初始化文件
    }

    # 确保目录存在
    for path in ["static/css", "static/js", "templates"]:
        os.makedirs(str(PROJECT_PATH / path), exist_ok=True)

    # 同步文件
    for src, dst in files_to_sync.items():
        src_path = LOCAL_PATH / src
        dst_path = PROJECT_PATH / dst

        if src_path.exists():
            print(f"Syncing {src} to {dst}")
            shutil.copy2(str(src_path), str(dst_path))
        else:
            print(f"Warning: Source file {src} not found at {src_path}")

    print("Sync completed!")


if __name__ == "__main__":
    # 执行同步
    sync_files()

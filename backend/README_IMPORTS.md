# 后端项目路径引用规范指南

本对应项目的后端代码 (`backend/`) 制定了统一的文件引用和路径导入规范，旨在确保项目在开发环境 (`fastapi dev`) 和生产环境中均能稳定运行，并提供良好的 IDE 支持。

## 1. 核心原则

**本项目将 `backend` 目录视为 Python 包的根目录 (Root Package)。**

所有导入语句都应基于 `backend` 目录作为顶级命名空间，或者相对于当前文件的位置。

### 推荐的引用方式

*   **绝对导入 (Absolute Imports)**: 推荐用于跨模块引用。从根目录 (`backend`) 下的子包开始引用。
    *   ✅ `from core.database import Base`
    *   ✅ `from model.qaLeaderboard import QALeaderboard`
    *   ✅ `from dao.qa_leaderboard_dao import get_all_sorted_by_score`
*   **相对导入 (Relative Imports)**: 仅建议在同一包（文件夹）内部使用，以保持模块的独立性。
    *   ✅ `from . import utils` (在同一目录下的引用)

### 需要避免的反模式

*   ❌ **绝对路径硬编码**: 不要使用 `sys.path.append('E:/...')` 这样的硬编码路径。这会导致代码无法在其他机器上运行。
*   ❌ **错误的顶层引用**: 避免使用 `from backend.core import ...`，除非你明确知道父目录在 `sys.path` 中。由于我们在 `backend` 目录下运行程序，直接使用 `from core import ...` 更加通用且符合 `fastapi dev` 的运行机制。
*   ❌ **混合使用 `sys.path` 修改**: 尽量不要在业务代码中手动修改 `sys.path`。

## 2. 常见引用方式对比

| 特性 | 绝对导入 (`from core.db import ...`) | 相对导入 (`from ..core.db import ...`) | 系统路径修改 (`sys.path.append`) |
| :--- | :--- | :--- | :--- |
| **清晰度** | ⭐⭐⭐ 高 (路径明确) | ⭐⭐ 中 (依赖当前文件位置) | ⭐ 低 (隐式依赖，难以追踪) |
| **重构难度** | ⭐⭐ 中 (移动文件需修改路径) | ⭐⭐⭐ 低 (包内移动通常无需修改) | ⭐ 困难 (容易导致意外错误) |
| **IDE 支持** | ⭐⭐⭐ 完美支持 | ⭐⭐⭐ 完美支持 | ⭐ 较差 (IDE 可能无法识别) |
| **运行环境** | 需根目录在 `PYTHONPATH` 中 | 需作为模块运行 (`python -m`) | 依赖运行时动态修改 |
| **本项目推荐** | **✅ 首选** | **⭕ 仅限包内** | **❌ 禁止** |

## 3. 目录结构与 `__init__.py`

为了让 Python 将目录识别为包，我们在所有子目录下添加了 `__init__.py` 文件：

```text
backend/
├── __init__.py      (可选，视 backend 是否被作为包导入而定)
├── main.py          (入口文件)
├── core/
│   ├── __init__.py  (✅ 已添加)
│   └── database.py
├── dao/
│   ├── __init__.py  (✅ 已添加)
│   └── ...
├── model/
│   ├── __init__.py  (✅ 已添加)
│   └── ...
└── router/
    ├── __init__.py  (✅ 已添加)
    └── ...
```

## 4. 运行方式说明

### 开发环境 (`fastapi dev`)

在 `backend` 目录下运行：
```bash
# 确保当前目录是 backend
cd e:\研究生\中医Benchmark\AcupunctureEval\backend

# 运行
fastapi dev main.py
```
此时，`backend` 目录会被自动添加到 `PYTHONPATH`，因此 `from core...` 等导入语句可以正常工作。

### 脚本运行 (如 `test.py`, `init_db.py`)

直接在 `backend` 目录下运行：
```bash
python test.py
python init_db.py
```
Python 会自动将当前脚本所在的目录 (`backend`) 添加到 `sys.path`，因此绝对导入依然有效。

## 5. 特殊情况处理

如果必须在项目根目录 (`AcupunctureEval/`) 运行后端脚本，建议使用模块方式运行，以保持路径一致性：

```bash
# 在 AcupunctureEval/ 目录下
python -m backend.test
```
(注意：这需要代码中支持 `backend` 前缀的导入，或者统一使用相对导入。但在本项目中，我们约定**总是进入 `backend` 目录**来运行后端相关命令，以简化配置。)

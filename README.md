# ✈️ AirDashboard

一个基于 **Python + Pygame + C** 开发的航空仪表盘，使用`uv`进行项目管理依赖

AirDashBoard 提供简洁直观的界面，支持速度，高度，角度，油量，转速查看

## ✨ 功能特性

### 当前功能

- ✅ 查看基础信息

### 技术栈 🛠️

| 技术 | 用途 |
| --- | --- |
| C | 底层核心逻辑（数值映射、动画插值、报警判断） |
| Python | 程序入口与整体调度 |
| Pygame | GUI 框架 |
| uv | 项目与依赖管理 |

## 🚀 安装运行
```bash
1. 克隆项目
git clone https://github.com/xunmouren/AirDashboard.git
cd AirDashboard

2. 安装 uv
# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

3. 创建虚拟环境并安装依赖
#本项目使用uv管理 Python 环境和依赖
uv sync

4. 运行程序
uv run main.py
```

## 🔮 后续开发计划
- [ ] 深色模式
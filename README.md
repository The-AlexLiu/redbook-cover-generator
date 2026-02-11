# 小红书封面生成器 (Redbook Title Generator)

一个简单高效的工具，用于生成“网飞风格”的小红书封面图。支持自定义标题和日期，一键生成 1242x1656 高清大图。
<img width="1512" height="790" alt="PixPin_2026-02-11_15-27-39" src="https://github.com/user-attachments/assets/67e6d09c-adb1-463f-b772-83827f9b7ce1" />


## 功能特点

- **高清输出**：自动生成 1242x1656 像素的完美尺寸图片。
- **Web 界面**：提供友好的可视化操作界面（基于 Flask + Tailwind CSS）。
- **自动化脚本**：支持命令行批量生成，自带 macOS 自动预览功能。
- **高度还原**：精准复刻网飞风格排版，支持超大字号冲击力。

## 快速开始

### 1. 安装依赖

需要 Python 3.8+ 环境。

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 启动 Web 界面（推荐）

运行以下命令启动网页版工具：

```bash
python3 server.py
# 然后在浏览器访问 http://127.0.0.1:5001
```

在网页中输入标题和日期，点击“立即生成封面”即可。

### 3. 命令行使用

如果你喜欢使用终端，也可以直接运行脚本：

```bash
python3 generate_image.py --title "你的标题" --date "你的日期"
```

## 项目结构

- `server.py`: Web 服务器入口
- `generate_image.py`: 核心图像生成逻辑（Playwright）
- `ui/index.html`: 前端界面源码
- `index.html`: 图片渲染模板
- `style.css`: 样式定义
- `Background.jpg`: 背景素材

## 常见问题

- **端口占用**：默认使用 5001 端口。如果启动失败，请检查端口是否被占用或修改 `server.py`。
- **图片未居中**：生成器经过校准，确保文字在视觉重心。如需调整，可修改 `style.css` 中的 `margin-top`。

---

Enjoy! 🚀

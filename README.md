# NeuraBox_app

一个基于 PyQt6 和 PyTorch 的本地神经网络应用程序。

## 项目结构

```bash
NeuraBox_app/
├── presentation/           # 表现层
│   └── views/             # 视图层
│       ├── ui/            # Qt Designer UI 文件
│       │   └── main_window.ui
│       └── main_window.py
│
├── business/              # 业务逻辑层
│   ├── controllers/       # 控制器
│   │   └── main_controller.py
│   └── services/         # 业务服务
│       └── model_service.py
│
├── data/                  # 数据层
│   ├── models/           # 神经网络模型
│   │   └── neural_net.py
│   ├── repositories/     # 数据访问
│   └── storage/         # 数据存储
│       ├── datasets/    # 训练数据
│       └── weights/     # 模型权重
│
├── main.py               # 程序入口
├── requirements.txt      # 项目依赖
└── git_push.bat         # Git 自动提交脚本
```

## 项目架构说明

### 表现层 (Presentation Layer)
- `views/`: 包含所有的界面视图文件
  - `ui/`: 存放 Qt Designer 创建的 UI 文件
  - `main_window.py`: UI 控制逻辑

### 业务逻辑层 (Business Layer)
- `controllers/`: 控制器，处理用户交互和业务流程
- `services/`: 业务服务，实现核心业务逻辑

### 数据层 (Data Layer)
- `models/`: 神经网络模型定义和实现
- `repositories/`: 数据访问和持久化
- `storage/`: 数据存储，包括数据集和模型权重

## 技术栈
- Python 3.8+
- PyQt6 - GUI 框架
- PyTorch - 深度学习框架
- NumPy - 数据处理
- Pandas - 数据分析

## 开发环境设置
1. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

## 项目运行
```bash
python main.py
```

## UI 开发
使用 Qt Designer 编辑 `presentation/views/ui/*.ui` 文件来设计界面。

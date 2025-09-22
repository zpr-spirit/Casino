# CSMAR 智能财经报告分析平台 API (新版本)

基于FastAPI构建的智能财经分析后端服务，采用现代化的项目结构和设计模式。

## 🏗️ 项目结构

```
royal_flush/
├── app/                              # 应用主目录
│   ├── __init__.py
│   ├── main.py                       # 主应用文件
│   ├── api/                          # API层
│   │   ├── __init__.py
│   │   └── v1/                       # API v1版本
│   │       ├── __init__.py
│   │       └── endpoints/            # API端点
│   │           ├── __init__.py
│   │           ├── stocks.py         # 股票分析端点
│   │           ├── quantitative.py   # 量化分析端点
│   │           ├── health.py         # 健康检查端点
│   │           └── depends/          # 依赖注入
│   │               ├── __init__.py
│   │               └── common.py
│   ├── core/                         # 核心模块
│   │   ├── __init__.py
│   │   ├── config.py                 # 配置管理
│   │   └── security.py               # 安全相关
│   ├── models/                       # 数据模型
│   │   ├── __init__.py
│   │   ├── schemas/                  # 数据模式
│   │   │   ├── __init__.py
│   │   │   ├── common.py             # 通用模式
│   │   │   ├── stock.py              # 股票相关模式
│   │   │   └── quantitative.py       # 量化分析模式
│   │   └── entities/                 # 实体模型
│   │       ├── __init__.py
│   │       ├── stock.py              # 股票实体
│   │       └── quantitative.py       # 量化分析实体
│   ├── services/                     # 服务层
│   │   ├── __init__.py
│   │   ├── stock/                    # 股票分析服务
│   │   │   ├── __init__.py
│   │   │   └── analysis.py
│   │   └── quantitative/             # 量化分析服务
│   │       ├── __init__.py
│   │       └── analysis.py
│   └── utils/                        # 工具模块
│       ├── __init__.py
│       ├── logger.py                 # 日志工具
│       └── helpers.py                # 辅助函数
├── tests/                            # 测试目录
│   ├── unit/                         # 单元测试
│   └── integration/                  # 集成测试
├── docs/                             # 文档目录
├── scripts/                          # 脚本目录
├── main.py                           # 启动入口
├── start_new.py                      # 新版本启动脚本
├── test_new_api.py                   # 新版本测试脚本
├── requirements.txt                  # 项目依赖
└── README_NEW.md                     # 新版本说明文档
```

## 🚀 快速开始

### 1. 安装依赖

```bash
cd /home/ryanzhangadmin/quant/Casino/royal_flush
pip install -r requirements.txt
```

### 2. 启动服务

```bash
# 方式1: 使用新版本启动脚本
python start_new.py

# 方式2: 直接运行main.py
python main.py

# 方式3: 使用uvicorn
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

### 3. 访问服务

- **API文档**: http://localhost:8000/docs
- **ReDoc文档**: http://localhost:8000/redoc
- **健康检查**: http://localhost:8000/health
- **API信息**: http://localhost:8000/

## 📚 API接口

### 股票分析接口

#### 1. 分析单只股票
```http
POST /api/v1/stocks/analyze
Content-Type: application/json

{
    "stock_code": "000001",
    "market": "a_stock",
    "analysis_type": "basic"
}
```

#### 2. 搜索股票
```http
GET /api/v1/stocks/search?query=平安&market=a_stock&limit=10
```

#### 3. 获取市场股票列表
```http
GET /api/v1/stocks/market/a_stock/list
```

### 量化分析接口

#### 1. 运行量化分析
```http
POST /api/v1/quantitative/analyze
Content-Type: application/json

{
    "strategy_name": "momentum_strategy",
    "parameters": {},
    "start_date": "2023-01-01",
    "end_date": "2023-12-31",
    "initial_capital": 100000.0
}
```

#### 2. 获取可用策略
```http
GET /api/v1/quantitative/strategies
```

#### 3. 获取策略信息
```http
GET /api/v1/quantitative/strategies/momentum_strategy
```

### 健康检查接口

#### 1. 系统健康检查
```http
GET /api/v1/health/
```

#### 2. API信息
```http
GET /api/v1/health/info
```

## 🏛️ 架构设计

### 分层架构
- **API层** (`app/api/`): 处理HTTP请求和响应
- **服务层** (`app/services/`): 业务逻辑处理
- **模型层** (`app/models/`): 数据模型定义
- **核心层** (`app/core/`): 配置和安全
- **工具层** (`app/utils/`): 通用工具函数

### 设计模式
- **依赖注入**: 使用FastAPI的Depends进行依赖管理
- **分层架构**: 清晰的层次分离，便于维护和测试
- **配置管理**: 使用Pydantic Settings进行配置管理
- **日志记录**: 统一的日志记录和管理
- **异常处理**: 全局异常处理机制

## 🔧 配置说明

### 环境变量
创建 `.env` 文件来覆盖默认配置：

```env
# 应用配置
APP_NAME=CSMAR API
DEBUG=true
HOST=0.0.0.0
PORT=8000

# 日志配置
LOG_LEVEL=INFO

# 安全配置
SECRET_KEY=your-secret-key-here

# 外部API配置
STOCK_DATA_API_URL=https://api.example.com
STOCK_DATA_API_KEY=your-api-key
```

### 配置类
所有配置都在 `app/core/config.py` 中定义，支持环境变量覆盖。

## 🧪 测试

### 运行测试
```bash
# 运行新版本API测试
python test_new_api.py

# 运行单元测试（待实现）
pytest tests/unit/

# 运行集成测试（待实现）
pytest tests/integration/
```

## 📝 开发指南

### 添加新的API端点
1. 在 `app/api/v1/endpoints/` 中创建新的端点文件
2. 在 `app/main.py` 中注册路由
3. 添加相应的数据模型和服务

### 添加新的服务
1. 在 `app/services/` 中创建新的服务模块
2. 实现相应的业务逻辑
3. 在API端点中使用依赖注入

### 添加新的数据模型
1. 在 `app/models/schemas/` 中定义请求/响应模型
2. 在 `app/models/entities/` 中定义实体模型
3. 在服务中使用这些模型

## 🔍 监控和日志

### 日志记录
- 使用 `app/utils/logger.py` 进行日志记录
- 支持控制台和文件输出
- 可配置日志级别

### 健康检查
- 提供多个健康检查端点
- 监控各个服务的状态
- 支持详细的系统信息

## 🚀 部署

### Docker部署（待实现）
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### 生产环境配置
- 设置 `DEBUG=false`
- 配置适当的日志级别
- 设置安全密钥
- 配置数据库连接

## 📈 性能优化

### 异步处理
- 使用FastAPI的异步特性
- 数据库操作异步化
- 外部API调用异步化

### 缓存策略
- Redis缓存（待实现）
- 内存缓存
- 查询结果缓存

## 🔒 安全特性

### 认证和授权
- JWT令牌认证
- 密码加密
- 权限控制

### 数据验证
- Pydantic模型验证
- 输入参数验证
- 输出数据验证

## 📞 支持

如有问题或建议，请通过以下方式联系：
- 创建Issue
- 发送邮件
- 提交Pull Request

## 📄 许可证

本项目采用MIT许可证，详见LICENSE文件。

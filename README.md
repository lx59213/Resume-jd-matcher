# 简历JD匹配器

一个帮助求职者快速匹配职位JD的工具。

## 功能特点

- 支持PDF简历解析
- 智能匹配职位要求
- 生成匹配度分析
- 提供改进建议

## 技术栈

- 后端：Flask
- 前端：Vue 3 + Element Plus
- AI：DeepSeek API

## 本地开发

1. 克隆项目
```bash
git clone https://github.com/yourusername/Resume-jd-matcher.git
cd Resume-jd-matcher
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 设置环境变量
```bash
cp .env.example .env
# 编辑 .env 文件，添加必要的配置
```

4. 运行项目
```bash
python run.py
```

## 部署

项目支持 Vercel 部署，只需要：

1. Fork 本仓库
2. 在 Vercel 中导入项目
3. 设置环境变量
4. 完成部署

## 文档

- [Element Plus CDN 使用指南](docs/element-plus-cdn.md)

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT 
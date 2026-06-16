# 🤖 Windows 自动化助手系统 - Auto Helper

一套完整的、开箱即用的 Windows 自动化系统。无需编程基础，一键启动！

## 🎯 功能特性

- 📁 **文件自动整理** - 按类型自动分类和整理文件
- 💾 **自动备份系统** - 定时自动备份重要文件
- ⏰ **定时任务执行** - 按设定时间自动执行任务
- 📊 **系统监控** - 实时监控 CPU、内存、磁盘使用情况
- 🔔 **系统通知** - 任务完成/异常时自动通知
- 📝 **日志记录** - 详细记录所有操作日志
- 🚀 **一键启动** - 双击运行，无需任何配置

## 📋 快速开始

### 1️⃣ 安装依赖（第一次使用）

双击运行 `install.bat` 文件，自动安装所需的 Python 库。

或者在命令行运行：
```bash
pip install -r requirements.txt
```

### 2️⃣ 配置任务

编辑 `config.yaml` 文件，配置您想要自动化的任务。

### 3️⃣ 启动程序

双击 `run.bat` 文件启动自动化系统。

## 📁 文件说明

```
auto-helper/
├── run.bat                 # 🚀 一键启动脚本（双击运行）
├── install.bat             # 📦 安装依赖脚本
├── main.py                 # 🎯 主程序
├── config.yaml             # ⚙️ 配置文件（在这里设置任务）
├── requirements.txt        # 📚 Python依赖列表
├── tasks/
│   ├── file_organizer.py   # 📁 文件整理器
│   ├── backup_system.py    # 💾 备份系统
│   ├── task_scheduler.py   # ⏰ 任务调度器
│   └── system_monitor.py   # 📊 系统监控
├── logs/                   # 📝 日志文件夹（自动创建）
└── backups/                # 💾 备份文件夹（自动创建）
```

## 🔧 配置说明

### 文件整理任务示例
```yaml
tasks:
  - name: "整理下载文件夹"
    type: "organize_files"
    source: "C:/Users/YourUsername/Downloads"
    enabled: true
    schedule: "08:00"  # 每天早上8点执行
```

### 定时备份任务示例
```yaml
tasks:
  - name: "备份文档"
    type: "backup"
    source: "C:/Users/YourUsername/Documents"
    destination: "D:/Backups"
    enabled: true
    schedule: "22:00"  # 每天晚上10点执行
```

### 系统监控任务示例
```yaml
tasks:
  - name: "监控系统"
    type: "monitor"
    enabled: true
    check_interval: 300  # 每5分钟检查一次
    alert_cpu: 80        # CPU超过80%时告警
    alert_memory: 85     # 内存超过85%时告警
```

## ⏰ 支持的时间格式

- `08:00` - 每天早上8点
- `14:30` - 每天下午2点30分
- `*/5` - 每5分钟
- `0 0 * * 1` - 每周一午夜（Cron格式）

## 📝 查看日志

所有操作都会记录在 `logs/` 文件夹中：
- `main.log` - 主程序日志
- `tasks.log` - 任务执行日志
- `errors.log` - 错误日志

## 🆘 常见问题

### Q: 双击 run.bat 没反应？
A: 右键选择"以管理员身份运行"

### Q: 如何停止程序？
A: 在运行窗口按 Ctrl+C

### Q: 如何修改任务？
A: 编辑 config.yaml 文件，程序会自动重新加载配置

### Q: 备份文件去哪了？
A: 查看 backups/ 文件夹

## 🔐 安全提示

- 备份很重要！定期检查备份文件
- 谨慎配置文件删除操作
- 定期查看日志了解程序运行状态

## 📞 需要帮助？

遇到问题时：
1. 查看 logs/ 文件夹中的错误日志
2. 检查 config.yaml 配置是否正确
3. 确保有足够的磁盘空间和权限

---

**祝您使用愉快！** 🎉

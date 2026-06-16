#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Windows 自动化助手系统 - 主程序
Auto Helper System - Main Program
"""

import os
import sys
import time
import logging
import yaml
import schedule
import threading
from pathlib import Path
from datetime import datetime

# 导入任务模块
from tasks.file_organizer import FileOrganizer
from tasks.backup_system import BackupSystem
from tasks.task_scheduler import TaskScheduler
from tasks.system_monitor import SystemMonitor

# 配置日志
def setup_logging():
    """设置日志系统"""
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "main.log", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

logger = setup_logging()

class AutoHelper:
    """自动化助手主类"""
    
    def __init__(self, config_file="config.yaml"):
        """初始化自动助手"""
        self.config_file = config_file
        self.config = None
        self.scheduler = schedule.Scheduler()
        self.running = True
        
        logger.info("=" * 60)
        logger.info("🤖 Windows 自动化助手系统启动")
        logger.info("=" * 60)
        
        self.load_config()
        self.initialize_tasks()
    
    def load_config(self):
        """加载配置文件"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                self.config = yaml.safe_load(f)
            logger.info(f"✅ 配置文件加载成功: {self.config_file}")
        except FileNotFoundError:
            logger.error(f"❌ 配置文件不存在: {self.config_file}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"❌ 配置文件加载失败: {e}")
            sys.exit(1)
    
    def initialize_tasks(self):
        """初始化所有任务"""
        tasks = self.config.get('tasks', [])
        logger.info(f"📋 发现 {len(tasks)} 个任务")
        
        for task in tasks:
            if not task.get('enabled', False):
                logger.info(f"⏭️  跳过禁用的任务: {task['name']}")
                continue
            
            task_type = task.get('type')
            task_name = task.get('name')
            schedule_time = task.get('schedule')
            
            if task_type == 'organize_files':
                self.scheduler.every().day.at(schedule_time).do(
                    self.run_file_organizer, task
                )
                logger.info(f"✅ 已注册任务: {task_name} (每天 {schedule_time})")
            
            elif task_type == 'backup':
                self.scheduler.every().day.at(schedule_time).do(
                    self.run_backup, task
                )
                logger.info(f"✅ 已注册任务: {task_name} (每天 {schedule_time})")
            
            elif task_type == 'monitor':
                interval = task.get('check_interval', 300)
                self.scheduler.every(interval).seconds.do(
                    self.run_monitor, task
                )
                logger.info(f"✅ 已注册任务: {task_name} (每 {interval} 秒)")
            
            elif task_type == 'cleanup':
                self.scheduler.every().day.at(schedule_time).do(
                    self.run_cleanup, task
                )
                logger.info(f"✅ 已注册任务: {task_name} (每天 {schedule_time})")
            
            elif task_type == 'execute_command':
                self.scheduler.every().day.at(schedule_time).do(
                    self.run_command, task
                )
                logger.info(f"✅ 已注册任务: {task_name} (每天 {schedule_time})")
    
    def run_file_organizer(self, task):
        """运行文件整理器"""
        try:
            logger.info(f"▶️  开始执行: {task['name']}")
            organizer = FileOrganizer(task)
            organizer.organize()
            logger.info(f"✅ 完成: {task['name']}")
            self.notify(f"✅ {task['name']} 完成", True)
        except Exception as e:
            logger.error(f"❌ {task['name']} 出错: {e}")
            self.notify(f"❌ {task['name']} 失败: {e}", False)
    
    def run_backup(self, task):
        """运行备份系统"""
        try:
            logger.info(f"▶️  开始执行: {task['name']}")
            backup = BackupSystem(task)
            backup.backup()
            logger.info(f"✅ 完成: {task['name']}")
            self.notify(f"✅ {task['name']} 完成", True)
        except Exception as e:
            logger.error(f"❌ {task['name']} 出错: {e}")
            self.notify(f"❌ {task['name']} 失败: {e}", False)
    
    def run_monitor(self, task):
        """运行系统监控"""
        try:
            monitor = SystemMonitor(task)
            monitor.check()
        except Exception as e:
            logger.error(f"❌ 监控出错: {e}")
    
    def run_cleanup(self, task):
        """运行清理任务"""
        try:
            logger.info(f"▶️  开始执行: {task['name']}")
            # TODO: 实现清理逻辑
            logger.info(f"✅ 完成: {task['name']}")
            self.notify(f"✅ {task['name']} 完成", True)
        except Exception as e:
            logger.error(f"❌ {task['name']} 出错: {e}")
    
    def run_command(self, task):
        """运行命令"""
        try:
            logger.info(f"▶️  开始执行: {task['name']}")
            command = task.get('command')
            os.system(command)
            logger.info(f"✅ 完成: {task['name']}")
            self.notify(f"✅ {task['name']} 完成", True)
        except Exception as e:
            logger.error(f"❌ {task['name']} 出错: {e}")
    
    def notify(self, message, success=True):
        """发送通知"""
        try:
            from win10toast import ToastNotifier
            toaster = ToastNotifier()
            toaster.show_toast(
                "自动化助手",
                message,
                duration=5,
                threaded=True
            )
        except:
            pass
    
    def run_scheduler(self):
        """运行调度器"""
        logger.info("🚀 调度器启动，等待任务执行...")
        logger.info("按 Ctrl+C 停止程序\n")
        
        while self.running:
            try:
                self.scheduler.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                logger.info("\n⏹️  正在停止程序...")
                self.running = False
            except Exception as e:
                logger.error(f"❌ 调度器错误: {e}")
                time.sleep(1)
    
    def run(self):
        """启动助手"""
        try:
            self.run_scheduler()
        except KeyboardInterrupt:
            logger.info("\n⏹️  程序已停止")
        finally:
            logger.info("=" * 60)
            logger.info("自动化助手已关闭")
            logger.info("=" * 60)

def main():
    """主函数"""
    helper = AutoHelper()
    helper.run()

if __name__ == "__main__":
    main()

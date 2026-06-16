#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
任务调度器模块
Task Scheduler Module
"""

import logging
import schedule
from datetime import datetime

logger = logging.getLogger(__name__)

class TaskScheduler:
    """任务调度器类"""
    
    def __init__(self):
        """初始化任务调度器"""
        self.scheduler = schedule.Scheduler()
        self.tasks = []
        logger.info("任务调度器已初始化")
    
    def add_task(self, name, func, schedule_time):
        """添加任务"""
        try:
            self.scheduler.every().day.at(schedule_time).do(func)
            self.tasks.append({
                'name': name,
                'schedule_time': schedule_time,
                'created_at': datetime.now()
            })
            logger.info(f"✓ 已添加任务: {name} (每天 {schedule_time})")
        except Exception as e:
            logger.error(f"✗ 添加任务失败 {name}: {e}")
    
    def get_tasks(self):
        """获取所有任务"""
        return self.tasks
    
    def run_pending(self):
        """运行待执行的任务"""
        self.scheduler.run_pending()

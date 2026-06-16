#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统监控模块
System Monitor Module
"""

import logging
import psutil

logger = logging.getLogger(__name__)

class SystemMonitor:
    """系统监控类"""
    
    def __init__(self, config):
        """初始化系统监控"""
        self.config = config
        self.alert_cpu = config.get('alert_cpu', 80)
        self.alert_memory = config.get('alert_memory', 85)
        self.alert_disk = config.get('alert_disk', 90)
        self.log_stats = config.get('log_stats', True)
    
    def check(self):
        """检查系统状态"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            memory_percent = psutil.virtual_memory().percent
            disk_percent = psutil.disk_usage('/').percent
            
            if self.log_stats:
                logger.debug(f"系统状态 - CPU: {cpu_percent}%, 内存: {memory_percent}%, 磁盘: {disk_percent}%")
            
            self.check_alerts(cpu_percent, memory_percent, disk_percent)
        
        except Exception as e:
            logger.error(f"✗ 监控失败: {e}")
    
    def check_alerts(self, cpu_percent, memory_percent, disk_percent):
        """检查告警阈值"""
        alerts = []
        
        if cpu_percent > self.alert_cpu:
            alerts.append(f"⚠️  CPU使用率过高: {cpu_percent}%")
        
        if memory_percent > self.alert_memory:
            alerts.append(f"⚠️  内存使用率过高: {memory_percent}%")
        
        if disk_percent > self.alert_disk:
            alerts.append(f"⚠️  磁盘使用率过高: {disk_percent}%")
        
        for alert in alerts:
            logger.warning(alert)

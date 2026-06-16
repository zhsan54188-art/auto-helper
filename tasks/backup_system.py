#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
备份系统模块
Backup System Module
"""

import os
import shutil
import zipfile
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class BackupSystem:
    """备份系统类"""
    
    def __init__(self, config):
        """初始化备份系统"""
        self.config = config
        self.source = config.get('source')
        self.destination = config.get('destination')
        self.compress = config.get('compress', True)
        self.skip_patterns = config.get('skip_patterns', [])
        self.backup_size = 0
    
    def backup(self):
        """执行备份"""
        if not os.path.exists(self.source):
            logger.error(f"源文件夹不存在: {self.source}")
            return
        
        logger.info(f"开始备份: {self.source} -> {self.destination}")
        
        os.makedirs(self.destination, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if self.compress:
            self.backup_as_zip(timestamp)
        else:
            self.backup_as_folder(timestamp)
        
        logger.info(f"备份完成，大小: {self.backup_size / (1024*1024):.2f} MB")
    
    def backup_as_zip(self, timestamp):
        """备份为压缩文件"""
        try:
            source_name = os.path.basename(self.source.rstrip('\\').rstrip('/'))
            backup_file = os.path.join(
                self.destination, 
                f"{source_name}_{timestamp}.zip"
            )
            
            logger.info(f"创建压缩备份: {backup_file}")
            
            with zipfile.ZipFile(backup_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for root, dirs, files in os.walk(self.source):
                    for file in files:
                        if self.should_skip(file):
                            continue
                        
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, self.source)
                        
                        zipf.write(file_path, arcname)
                        self.backup_size += os.path.getsize(file_path)
            
            logger.info(f"✓ 备份文件已创建: {backup_file}")
        
        except Exception as e:
            logger.error(f"✗ 备份失败: {e}")
    
    def backup_as_folder(self, timestamp):
        """备份为文件夹"""
        try:
            source_name = os.path.basename(self.source.rstrip('\\').rstrip('/'))
            backup_dir = os.path.join(
                self.destination, 
                f"{source_name}_{timestamp}"
            )
            
            os.makedirs(backup_dir, exist_ok=True)
            
            logger.info(f"创建文件夹备份: {backup_dir}")
            
            for item in os.listdir(self.source):
                if self.should_skip(item):
                    continue
                
                src_path = os.path.join(self.source, item)
                dst_path = os.path.join(backup_dir, item)
                
                if os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path)
                else:
                    shutil.copy2(src_path, dst_path)
                    self.backup_size += os.path.getsize(src_path)
            
            logger.info(f"✓ 备份文件夹已创建: {backup_dir}")
        
        except Exception as e:
            logger.error(f"✗ 备份失败: {e}")
    
    def should_skip(self, filename):
        """检查是否应该跳过该文件"""
        from fnmatch import fnmatch
        
        for pattern in self.skip_patterns:
            if fnmatch(filename.lower(), pattern.lower()):
                return True
        return False

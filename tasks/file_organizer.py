#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
文件整理器模块
File Organizer Module
"""

import os
import shutil
import logging
from pathlib import Path
from datetime import datetime

logger = logging.getLogger(__name__)

class FileOrganizer:
    """文件整理器类"""
    
    def __init__(self, config):
        """初始化文件整理器"""
        self.config = config
        self.source = config.get('source')
        self.organize_by = config.get('organize_by', 'extension')
        self.rules = config.get('rules', [])
        self.moved_count = 0
    
    def organize(self):
        """执行文件整理"""
        if not os.path.exists(self.source):
            logger.error(f"源文件夹不存在: {self.source}")
            return
        
        logger.info(f"开始整理文件夹: {self.source}")
        
        files = os.listdir(self.source)
        logger.info(f"找到 {len(files)} 个文件/文件夹")
        
        for item in files:
            full_path = os.path.join(self.source, item)
            
            if os.path.isdir(full_path):
                continue
            
            target_folder = self.get_target_folder(item)
            
            if target_folder:
                self.move_file(full_path, item, target_folder)
        
        logger.info(f"文件整理完成，共移动 {self.moved_count} 个文件")
    
    def get_target_folder(self, filename):
        """根据文件名获取目标文件夹"""
        # 检查自定义规则
        for rule in self.rules:
            pattern = rule.get('pattern', '')
            folder = rule.get('folder', '')
            
            if self.match_pattern(filename, pattern):
                return folder
        
        # 按扩展名分类
        if self.organize_by == 'extension':
            ext = Path(filename).suffix.lower()
            if ext:
                return ext[1:]  # 移除点号
        
        return None
    
    def match_pattern(self, filename, pattern):
        """检查文件是否匹配模式"""
        from fnmatch import fnmatch
        
        patterns = pattern.split('|')
        for p in patterns:
            if fnmatch(filename.lower(), p.lower()):
                return True
        return False
    
    def move_file(self, full_path, filename, target_folder):
        """移动文件到目标文件夹"""
        try:
            target_dir = os.path.join(self.source, target_folder)
            os.makedirs(target_dir, exist_ok=True)
            
            target_path = os.path.join(target_dir, filename)
            
            # 如果文件已存在，生成新名字
            if os.path.exists(target_path):
                name, ext = os.path.splitext(filename)
                target_path = os.path.join(
                    target_dir, 
                    f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{ext}"
                )
            
            shutil.move(full_path, target_path)
            logger.info(f"✓ 已移动: {filename} -> {target_folder}/")
            self.moved_count += 1
        
        except Exception as e:
            logger.error(f"✗ 移动失败 {filename}: {e}")

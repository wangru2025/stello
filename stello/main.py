"""
Stello 主程序入口
"""

import sys
from pathlib import Path
from .build.build_site import SiteBuilder


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法: python -m stello.main <配置文件>")
        print("\n示例: python -m stello.main examples/config.dsl")
        sys.exit(1)
    
    config_path = Path(sys.argv[1])
    
    if not config_path.exists():
        print(f"错误: 配置文件不存在: {config_path}")
        sys.exit(1)
    
    print(f"正在构建网站...")
    print(f"配置文件: {config_path}")
    print()
    
    # 创建构建器并执行构建
    builder = SiteBuilder(config_path)
    success = builder.build()
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

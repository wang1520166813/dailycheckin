import json
import os
import sys

def main():
    # 从环境变量获取 Cookie
    cookie = os.environ.get('ALYUN_DRIVE_COOKIES', '')
    
    if not cookie:
        print("Error: ALYUN_DRIVE_COOKIES environment variable is not set or empty!")
        sys.exit(1)
    
    # 阿里云盘配置键名通常是 ALYUN_DRIVE 或 ALIYUN_DRIVE
    # 根据 dailycheckin 项目结构，模块名为 aliyun，所以键名应为 ALIYUN
    config = {
        "ALIYUN": [
            {
                "cookie": cookie,
                "checkin": True
            }
        ]
    }
    
    # 写入 config.json
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print("Aliyun Drive config.json created successfully!")
    # 打印前 100 个字符用于调试
    print(f"Config content preview: {str(config)[:100]}...")

if __name__ == "__main__":
    main()

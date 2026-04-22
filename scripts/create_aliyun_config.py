import json
import os
import sys

def main():
    # 从环境变量获取 refresh_token
    refresh_token = os.environ.get('ALYUN_REFRESH_TOKEN', '')
    
    if not refresh_token:
        print("Error: ALYUN_REFRESH_TOKEN environment variable is not set or empty!")
        sys.exit(1)
    
    # 阿里云盘配置需要 refresh_token
    config = {
        "ALIYUN": [
            {
                "refresh_token": refresh_token
            }
        ]
    }
    
    # 写入 config.json
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print("Aliyun Drive config.json created successfully!")
    print(f"Config content preview: {str(config)[:100]}...")

if __name__ == "__main__":
    main()

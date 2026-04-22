import json
import os
import sys

def main():
    # 从环境变量获取 Cookie
    cookie = os.environ.get('BAIDU_TIEBA_COOKIES', '')
    
    if not cookie:
        print("Error: BAIDU_TIEBA_COOKIES environment variable is not set or empty!")
        sys.exit(1)
    
    config = {
        "BAIDU": [
            {
                "cookie": cookie,
                "checkin": True
            }
        ]
    }
    
    # 写入 config.json
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)
    
    print("Tieba config.json created successfully!")
    # 为了调试，打印前 100 个字符（不打印完整 Cookie 以防泄露，实际运行中可调整）
    print(f"Config content preview: {str(config)[:100]}...")

if __name__ == "__main__":
    main()

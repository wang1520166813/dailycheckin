import json
import os
import sys

def main():
    # 从环境变量获取 Cookie
    cookie = os.environ.get('KGQQ_COOKIES', '')

    if not cookie:
        print("Error: KGQQ_COOKIES environment variable is not set or empty!")
        sys.exit(1)

    config = {
        "KGQQ": [
            {
                "cookie": cookie
            }
        ]
    }

    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print("KGQQ config.json created successfully!")
    print(f"Config content preview: {str(config)[:100]}...")

if __name__ == "__main__":
    main()

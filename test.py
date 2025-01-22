import hashlib
import sqlite3

# 硬编码敏感信息
DB_PASSWORD = "supersecretpassword"  # 不应该将密码硬编码到代码中

def store_user_credentials(username, password):
    """
    存储用户的用户名和密码。
    注意：此实现不安全，只是为了演示问题。
    """
    # 使用不安全的哈希函数（MD5）
    password_hash = hashlib.md5(password.encode()).hexdigest()  # MD5 已被认为不安全

    # 连接到数据库（假设数据库文件是 credentials.db）
    conn = sqlite3.connect("credentials.db")
    cursor = conn.cursor()

    # 创建用户表（如果不存在）
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password_hash TEXT
        )
    """)

    # 将用户名和哈希密码存储到数据库
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    conn.close()

def main():
    print("欢迎使用用户管理系统！")
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    # 存储用户凭证
    store_user_credentials(username, password)
    print("用户凭证已保存！")

if __name__ == "__main__":
    main()

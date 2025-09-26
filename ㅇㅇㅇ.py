import hashlib

# 희소 메모리 (dictionary)
memory = {}

# 값 쓰기
def set_mem(x, y, value):
    memory[(x, y)] = value

# 값 읽기
def get_mem(x, y):
    return memory.get((x, y), 0)

# SHA-256 해시 계산
def sha256_hex(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# 타겟 문자열 및 해시
TARGET_STRING = "42"
TARGET_HASH = sha256_hex(TARGET_STRING)
print(f"[+] Target string: '{TARGET_STRING}'")
print(f"[+] Target SHA-256: {TARGET_HASH}")

# 엄청 큰 메모리에서 브루트포스
def brute_force_large_memory(x_limit=1000000, y_limit=1000000):
    counter = 0
    for x in range(x_limit):
        for y in range(y_limit):
            set_mem(x, y, counter)
            candidate = str(counter)
            h = sha256_hex(candidate)
            if h == TARGET_HASH:
                print(f"[✔] Match found at ({x},{y}): {candidate}")
                return
            counter += 1
    print("[×] No match found.")

# 실행
if __name__ == "__main__":
    brute_force_large_memory(x_limit=1024, y_limit=1024)  # 여긴 원하는 만큼 키울 수 있음

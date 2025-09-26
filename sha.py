import hashlib

# 2차원 메모리 정의
MEM_SIZE_X = 256
MEM_SIZE_Y = 256

# 메모리 초기화 (2D 배열)
memory = [[0 for _ in range(MEM_SIZE_Y)] for _ in range(MEM_SIZE_X)]

# 메모리에 값 쓰기
def set_mem(x, y, value):
    if 0 <= x < MEM_SIZE_X and 0 <= y < MEM_SIZE_Y:
        memory[x][y] = value

# 메모리에서 값 읽기
def get_mem(x, y):
    if 0 <= x < MEM_SIZE_X and 0 <= y < MEM_SIZE_Y:
        return memory[x][y]
    return 0

# SHA-256 해시 계산
def sha256_hex(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

# 타겟 해시 설정 (예: 문자열 "42"의 해시)
TARGET_STRING = "42"
TARGET_HASH = sha256_hex(TARGET_STRING)
print(f"[+] Target string: '{TARGET_STRING}'")
print(f"[+] Target SHA-256: {TARGET_HASH}")

# 메모리 초기화 (모든 셀에 숫자값 채우기: 예, 0~(256x256))
def initialize_memory():
    counter = 0
    for x in range(MEM_SIZE_X):
        for y in range(MEM_SIZE_Y):
            set_mem(x, y, counter)
            counter += 1

# 해시 역산 시도
def brute_force_hash():
    for x in range(MEM_SIZE_X):
        for y in range(MEM_SIZE_Y):
            val = get_mem(x, y)
            s = str(val)  # 문자열 변환
            h = sha256_hex(s)
            if h == TARGET_HASH:
                print(f"[✔] Match found at ({x},{y}): {s}")
                return
    print("[×] No match found.")

# 실행
if __name__ == "__main__":
    initialize_memory()
    brute_force_hash()

# Weather Fetcher

โครงการนี้เป็นสคริปต์ Python สำหรับดึงข้อมูลสภาพอากาศของหลายเมืองจาก Open-Meteo API โดยใช้ 3 วิธี:
- **Synchronous (วิ่งทีละคำขอ ช้าที่สุด)**
- **Threading (ใช้หลายเธรด เร็วขึ้น)**
- **Asyncio + Aiohttp (ใช้ async API เร็วที่สุด)**

## 🔧 การติดตั้ง

ก่อนใช้งาน ให้ติดตั้งไลบรารีที่จำเป็นโดยใช้คำสั่ง:

```sh
pip install requests aiohttp
```

## 🚀 วิธีใช้งาน

### 1️⃣ **Synchronous (ช้าแต่เข้าใจง่าย)**
```sh
python synchronous.py
```

### 2️⃣ **Threading (เร็วขึ้นโดยใช้หลายเธรด)**
```sh
python threading.py
```

### 3️⃣ **Asyncio + Aiohttp (เร็วสุด ใช้ async API)**
```sh
python asyncio_fetch.py
```

## 📊 ผลการทดสอบความเร็ว
| วิธี | เวลา (วินาที) |
|------|-------------|
| **Synchronous** | ~5-10 วินาที |
| **Threading** | ~2-5 วินาที |
| **Asyncio** | ~1-2 วินาที |

## 📌 หมายเหตุ
- `synchronous.py` ใช้ `requests`
- `threading.py` ใช้ `concurrent.futures.ThreadPoolExecutor`
- `asyncio_fetch.py` ใช้ `asyncio` + `aiohttp`

## ✨ ผู้พัฒนา
- **Your Name**
- GitHub: [your_github](https://github.com/your_github)

## 📜 License
โปรเจกต์นี้ใช้ MIT License

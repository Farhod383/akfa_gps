# 🌍 GPS Tracker Django Project

Bu loyiha **real vaqtda agentlarning joylashuvini kuzatish** uchun Django asosida qurilgan.  
Frontend — Leaflet xarita, backend — Django REST API.  
Agentlar koordinatalarini `/api/update_location/` endpoint orqali yuboradi,  
brauzer esa `/api/get_positions/` orqali ularni xaritada ko‘rsatadi.

---

## 🚀 Deploy qilish (Render orqali)

### 1️⃣ GitHub’ga loyihani joylash
PyCharm terminalida:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main

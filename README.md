# FastAPI Image Upload Service with Nginx (Windows)

A simple and production-oriented image upload service built using FastAPI and Uvicorn, with Nginx acting as a reverse proxy and static file server.  
The application supports uploading images per user and stores them on a local Windows system.

---

## Features

- Image upload API using FastAPI
- User-wise directory structure for uploaded images
- Images served directly via Nginx
- Reverse proxy configuration for FastAPI
- Windows-friendly setup
- Suitable for local development and self-hosted environments

---

## Tech Stack

- Python 3.9+
- FastAPI
- Uvicorn
- Nginx (Windows)

---

## Project Structure

```
image-upload-app/
├── main.py
├── requirements.txt
└── nginx/
    └── nginx.conf
```

---

## Upload Directory

All uploaded images are stored at:

```
E:\upload
```

Each user has a dedicated folder:

```
E:\upload\<user_id>\
```

---

## API Endpoint

### Upload Image

**Endpoint**
```
POST /upload-image
```

**Request Type**
```
multipart/form-data
```

**Form Fields**

| Field   | Type   | Required | Description            |
|-------- |--------|----------|------------------------|
| user_id | string | Yes      | Unique user identifier |
| file    | file   | Yes      | Image file             |

**Allowed File Types**

- jpg
- jpeg
- png
- gif
- webp

**Sample Response**

```json
{
  "message": "Image uploaded successfully",
  "filename": "uuid.jpg",
  "url": "http://localhost/uploads/user123/uuid.jpg"
}
```

---

## Setup Instructions (Windows)

### Clone Repository

```bash
git clone https://github.com/<your-username>/image-upload-app.git
cd image-upload-app
```

---

### Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run FastAPI

```bash
uvicorn main:app --host 127.0.0.1 --port 8000
```

Access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Nginx Configuration

1. Install Nginx for Windows from https://nginx.org
2. Copy `nginx/nginx.conf` to:

```
C:\nginx\conf\nginx.conf
```

3. Start or reload Nginx:

```bash
nginx.exe -s reload
```

---

## Access Uploaded Images

```
http://localhost/uploads/<user_id>/<filename>
```

---

## Security Considerations

- Extension-based file validation
- Auto-created user directories
- Recommended additions for production:
  - Authentication (JWT or API key)
  - File size limits
  - Image content validation
  - Disable directory listing

---

## License

MIT License



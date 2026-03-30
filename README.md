# Gemini Avatar | XYZ Rainbow

![Gemini Avatar](frontend/Makima.webp)

An interactive animated avatar application with personality, featuring multiple expressions, idle animations, and a chat interface. Now with **One UI Glassmorphism** design and full **i18n** support.

---
#xyz-rainbow #xyz-rainbowtechnology #rainbowtechnology.xyz #rainbow.xyz #rainbow@rainbowtechnology.xyz
---

## 🚀 New Features (v1.1.0)

- **One UI Glassmorphism**: A modern, translucent interface inspired by Samsung's One UI. Controls are minimal and appear on hover.
- **Internationalization (i18n)**: Support for multiple languages (Spanish and English included). Easily add more in `backend/i18n.json`.
- **Global Configuration**: Centralized settings in `backend/config.json` (language, idle times, ports, etc.).
- **Spanish Comments**: All code documentation and comments are now in Spanish.
- **XYZ Rainbow Branding**: Official project signatures and ASCII art.

## 📁 Project Structure

```
gemini-avatar/
├── backend/
│   ├── app.py              # Backend Flask (lógica principal e i18n)
│   ├── i18n.json           # Diccionario de traducciones
│   ├── config.json         # Configuración global de la app
│   └── command.txt         # Archivo de comandos temporales
├── frontend/
│   ├── index.html          # Interfaz principal del avatar
│   ├── style.css           # Estilos One UI Glassmorphism
│   ├── script.js           # Lógica del frontend
│   └── avatar/             # Vídeos de las expresiones
├── run.py                  # Punto de entrada (PyWebView + Flask)
└── requirements.txt        # Dependencias de Python
```

## 🛠 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/xyz-rainbow/gemini-avatar.git
   cd gemini-avatar
   ```

2. **Create a virtual environment (Recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux/macOS
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Start the application
```bash
python run.py
```

### Configuration
Edit `backend/config.json` to change:
- `language`: "es" or "en".
- `inactivity_delay`: Seconds before idle mode starts.
- `long_idle_interval`: Seconds between major expression changes.

### Adding Translations
Edit `backend/i18n.json` to add new phrases or languages.

## 📡 API Endpoints

- `GET /api/state`: Returns the current avatar state.
- `POST /api/chat`: Send a message and get a response sequence.
  ```json
  {"message": "hola"}
  ```
- `POST /api/update_from_gui`: Update expression and subtitle manually.

## 🎨 Aesthetic
The new **One UI Glass** theme features:
- **Translucent backgrounds**: Using `backdrop-filter: blur()`.
- **Rounded corners**: 24px-28px radius for a soft, modern look.
- **Auto-hide controls**: Window controls appear only when hovering over the application.

## 📄 License
This project is open source under XYZ Rainbow Technology guidelines.

---
**Developed with ❤️ by XYZ Rainbow Technology**

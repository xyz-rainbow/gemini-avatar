# <img src="logo.svg" width="40" height="40" valign="middle"> Gemini Avatar | Makima

An interactive, AI-powered desktop avatar with **Ollama** integration, **Glassmorphism** UI, and **VHS** retro effects.  
*Un avatar de escritorio interactivo potenciado por IA con integración de **Ollama**, interfaz **Glassmorphism** y efectos retro **VHS**.*

---
#xyz-rainbow #xyz-rainbowtechnology #rainbowtechnology.xyz #rainbow.xyz
---

## 🌟 Features / Características

### 🇬🇧 English
- **Ollama AI Integration**: Local LLM chat processing with emotion detection.
- **Glassmorphism UI**: Modern, translucent interface inspired by Samsung's One UI.
- **Internal Thoughts**: Real-time visualization of the AI's analytical process in cyan.
- **Clean Crossout Transitions**: Smooth video transitions without flickering.
- **VHS Retro Effect**: Authentic analog noise and scanlines.
- **Full i18n Support**: Toggle between English and Spanish instantly.
- **Custom Persona**: Set the avatar's personality via System Prompt.

### 🇪🇸 Español
- **Integración con Ollama**: Procesamiento de chat local con detección de emociones.
- **Interfaz Glassmorphism**: Diseño moderno y translúcido inspirado en One UI.
- **Pensamientos Internos**: Visualización en tiempo real del razonamiento de la IA.
- **Transiciones Crossout**: Cambios de vídeo fluidos sin parpadeos.
- **Efecto Retro VHS**: Ruido analógico y líneas de escaneo auténticas.
- **Soporte i18n Completo**: Cambia entre Inglés y Español al instante.
- **Personalidad Personalizada**: Configura el comportamiento mediante System Prompt.

## 🛠 Installation / Instalación

1. **Clone & Setup / Clonar y Configurar**
   ```bash
   git clone https://github.com/xyz-rainbow/gemini-avatar.git
   cd gemini-avatar
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Ollama Setup / Configurar Ollama**
   Ensure Ollama is running locally at `http://localhost:11434`.
   *Asegúrate de que Ollama esté corriendo localmente.*

3. **Run / Ejecutar**
   ```bash
   python run.py
   ```
   *Or use the alias / O usa el alias:* `makima`

## 📁 Project Structure / Estructura del Proyecto

- `backend/`: Flask server, Ollama logic, and i18n config.
- `frontend/`: HTML/CSS/JS files with Glassmorphism styles.
- `frontend/avatar/`: WebM video assets for expressions.
- `config.json`: Persistent application settings.
- `logo.svg`: Official project branding.

## ⚙️ Configuration / Configuración

Access the **Settings Panel** (⚙️ icon) to adjust:
- **Language**: English / Spanish.
- **Model**: Select from your local Ollama models.
- **Thought Mode**: None, Short, Deep, or Creative.
- **Transitions**: Style (Fade/Crossout) and Duration.
- **Persona**: Define how Makima speaks and thinks.

---
**Developed with ❤️ by [XYZ Rainbow Technology](https://rainbowtechnology.xyz)**

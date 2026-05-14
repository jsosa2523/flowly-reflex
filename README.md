Landing Page con Reflex
Landing page moderna para un SaaS de gestión de equipos, construida con reflex


## Cómo ejecutar

```bash
git clone https://github.com/jsosa2523/flowly-reflex.git
cd flowly-reflex
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Inicializar el proyecto Reflex

```bash
reflex init
```

### Ejecutar en modo desarrollo

```bash
reflex run
```

Abre [http://localhost:3000](http://localhost:3000) en tu navegador.

---

## Decisiones de diseño

- **Tipografía**: Syne (display, 800w) + DM Sans (body) — contraste entre fuente geométrica y humanista
- **Paleta**: Violeta primario (`violet`) + verde acento (`green`) sobre gris neutro — transmite modernidad sin ser genérico
- **Layout hero**: Grid 1→2 columnas (responsive). Mockup del dashboard da contexto visual inmediato
- **Componentes Reflex usados**: `rx.container`, `rx.flex`, `rx.grid`, `rx.vstack`, `rx.hstack`, `rx.box`, `rx.text`, `rx.heading`, `rx.button`, `rx.link`, `rx.icon`, `rx.separator`, `rx.cond`, `rx.desktop_only`

## Despliegue con Reflex Hosting

```bash
reflex login
reflex deploy
```

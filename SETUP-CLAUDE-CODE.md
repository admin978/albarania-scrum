# Instrucciones de Setup — Claude Code + GitHub + MCPs

## 1. Crear el repo en GitHub

```bash
cd /ruta/a/tu/workspace
mkdir albarania-scrum && cd albarania-scrum
git init
# Copia aquí todos los archivos generados (CLAUDE.md, README.md, docs/)
git add .
git commit -m "feat: estructura inicial del proyecto AlbaranIA Scrum"
gh repo create albarania-scrum --public --source=. --push
```

> Si no tienes `gh` CLI: `sudo apt install gh` o `brew install gh`, luego `gh auth login`.

## 2. Invitar a tus compañeros al repo

```bash
gh repo invite USUARIO_GITHUB --permission write
```

O desde GitHub → Settings → Collaborators → Add people.

## 3. Configurar MCPs en Claude Code

Edita tu config global de Claude Code:

```bash
# Abrir config global
claude config
# O editar directamente:
nano ~/.claude/settings.json
```

Añade los MCPs que quieras conectar. Ejemplo de config:

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_TU_TOKEN_AQUI"
      }
    },
    "slack": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-slack"],
      "env": {
        "SLACK_BOT_TOKEN": "xoxb-TU_TOKEN_AQUI"
      }
    },
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-server-google-drive"],
      "env": {
        "GOOGLE_CLIENT_ID": "...",
        "GOOGLE_CLIENT_SECRET": "...",
        "GOOGLE_REDIRECT_URI": "..."
      }
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/ruta/a/albarania-scrum"]
    }
  }
}
```

## 4. MCPs recomendados para esta práctica

| MCP | Para qué lo usas | Prioridad |
|-----|-------------------|-----------|
| GitHub | Crear issues, PRs, gestionar el repo | Alta |
| Slack | Enviar updates al canal #scrum | Media |
| Filesystem | Leer/escribir archivos del proyecto | Alta |
| Google Drive | Compartir docs con el grupo | Baja |

## 5. Flujo de trabajo con Claude Code

```bash
# Entrar al proyecto
cd albarania-scrum
claude

# Ejemplos de lo que puedes pedirle:
# "Crea las issues en GitHub para cada historia del Sprint 1"
# "Envía un resumen de la Daily 2 al canal #scrum de Slack"
# "Genera el mockup del panel principal en HTML"
# "Escribe el informe LaTeX con toda la documentación del sprint"
```

## 6. Generar el informe LaTeX desde Claude Code

```bash
claude "Lee todos los docs/ y genera el informe LaTeX final en docs/informe/main.tex siguiendo el formato del enunciado (máx 6 páginas)"
```

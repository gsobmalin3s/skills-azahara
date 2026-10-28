# skills-azahara

Skills de Claude preparadas para Azahara (LIN3S) que automatizan artefactos del **SWIN · Estrategia de Demanda** (metodología ORIA de LIN3S). Cada skill implementa uno o varios artefactos del documento de procedimiento y entrega su resultado en Excel, que es la capa de dato del SWIN (en producción, Google Sheets).

| Skill | Artefactos SWIN | Qué hace | Entregable |
|---|---|---|---|
| [`auditoria-redes-sociales`](skills/auditoria-redes-sociales/SKILL.md) | 1.4 · Auditoría de activos (redes) · 1.5 / 3.1 (redes de la competencia) | Descubre todas las redes de una marca, navega los perfiles y saca, post a post, formato, tipo de contenido, likes, comentarios, vistas y engagement. Aplica el Estándar de auditoría (rol → ¿cumple la función?) y la síntesis D/F | Excel: Resumen · Publicaciones · Formatos · Tipos de contenido · Comparativa · Insights · Pendientes · Metodología |
| [`analisis-sector-competencia`](skills/analisis-sector-competencia/SKILL.md) | 1.5 · Sector y competencia · 3.1 · Benchmark, Retos y Oportunidades | Tendencias del sector con fuentes, set competitivo (sugerir → validar → investigar), ficha por competidor, comparativa, posicionamiento, oportunidades/amenazas. En modo benchmark: cómo resuelven otros nuestros retos, Mapa de Retos y Mapa de Oportunidades | Excel con hojas fijas (ver `references/hojas_excel.md`) |

## Instalación

- **Claude (claude.ai / app de escritorio):** sube el archivo de [`dist/`](dist/) (`.skill`) en *Ajustes → Capacidades → Skills*.
- **Claude Code:** copia la carpeta de la skill en `~/.claude/skills/` (o en `.claude/skills/` del proyecto).

Las skills se activan solas cuando pides algo como "audítame las redes de X" o "análisis de competencia de X".

## Requisitos

- **Navegador** para la auditoría de redes: Claude in Chrome con sesión iniciada en Instagram, LinkedIn y Facebook (recomendado). Sin sesión funciona, pero Instagram solo enseña ~12 publicaciones y sin vistas de reels.
- **Búsqueda web** para el análisis de sector.
- **Python 3 + `openpyxl`** para generar los Excel.


## Regenerar los `.skill`

Tras cambiar una skill, vuelve a empaquetarla con el `package_skill` de la skill-creator de Anthropic, o comprime la carpeta de la skill en un zip con extensión `.skill`.

## Pendiente

- Probar la auditoría de redes con sesión iniciada en Chrome (comentarios, vistas de reels, LinkedIn).
- Probar el modo benchmark (3.1) con objetivos SMART y retos reales.
- Siguientes skills candidatas: `auditoria-web` (vista estratégica), `extraer-documentacion-cliente` (1.1–1.2), `procesar-taller` (2.2 / 3.3), `objetivos-smart` (2.3), `pool-iniciativas-roadmap` (4.2–4.3).

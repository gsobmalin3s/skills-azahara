---
name: auditoria-redes-sociales
description: Audita las redes sociales de una marca (cliente nuevo, competidor o referente) navegando sus perfiles y entrega un Excel con todas sus redes, los formatos y tipos de contenido que usa en cada una, medias de likes, comentarios y visualizaciones, engagement rate, frecuencia, detalle post a post, comparativa con competidores e insights. Úsala siempre que alguien pida "auditar las redes de X", "sácame las métricas de redes de esta marca", "tabla/excel de redes sociales del cliente", "benchmark de redes de la competencia", "qué publica X en Instagram/TikTok/LinkedIn", o cuando entre un cliente nuevo y haya que montar su foto de partida en redes, aunque no diga literalmente "auditoría".
---

# Auditoría de redes sociales

Una consultora de LIN3S recibe un cliente (p. ej. Serrats) y necesita, en minutos y no en horas, la foto completa de su presencia social: qué redes tiene, qué tipo de publicaciones hace en cada una y en qué formato, cuánto interactúa su audiencia y qué se puede sacar de ahí. Esta skill hace ese trabajo de campo navegando los perfiles y lo entrega en un **Excel**, con un resumen breve en el chat.

Implementa la parte de redes del SWIN · Estrategia de Demanda (método ORIA, Fase 1 *Where You Are*):

- **Modo cliente → artefacto 1.4 Auditoría de activos.** Una ficha por cuenta con la rejilla de redes: tono, seguidores y evolución, frecuencia, formatos, mercados, audiencias, engagement (rate medio y por formato), interacciones, comentarios y estado de la cuenta.
- **Modo competencia → artefacto 1.5 Sector y competencia** (y benchmark de 3.1). Misma rejilla, aplicada a cada competidor o referente, con comparativa y espacios de oportunidad/amenaza.

En ambos modos se aplica el **Estándar de auditoría** del SWIN: por cada cuenta auditada, (1) enfoque/rol que debería cumplir respecto a los objetivos, (2) URL, (3) análisis comentado, (4) ¿cumple la función? Sí / Parcialmente / No + razón. Lo que hace que esto sea una auditoría y no un listado de métricas es ese contraste entre lo que la cuenta *debería* hacer y lo que *hace*.

El Excel es la capa de dato del SWIN (en producción, Google Sheets): fuente de verdad del dato, no la presentación al cliente.

## Herramientas y requisitos

**Navegador.** Claude in Chrome (`mcp__claude-in-chrome__*`) con el usuario **logueado en Instagram, LinkedIn y Facebook** es lo recomendado: con sesión se ven ~30 publicaciones por perfil, las visualizaciones de los reels, los comentarios y las métricas de los posts de LinkedIn y Facebook. Sin sesión (navegador integrado) la skill funciona igual, pero Instagram solo enseña ~12 publicaciones sin vistas de reels, y LinkedIn/Facebook casi solo el número de seguidores. Al empezar, comprueba si hay sesión; si no la hay, avísalo en una línea y sigue.

**Excel.** Python con `openpyxl` (el script `scripts/generar_excel.py` lo usa).

Reglas de navegación, porque es la cuenta personal de quien usa la skill:
- Solo mirar. No dar like, seguir, comentar, guardar ni aceptar nada. Si una red pide iniciar sesión, pide al usuario que la inicie él; nunca escribas credenciales.
- Declina cookies no esenciales.
- Prefiere leer los datos que la página incrusta (ver atajos en `references/redes.md`) o `get_page_text` / `find`; captura de pantalla solo cuando no haya otra forma.

## Flujo

### 1. Identificar la marca y descubrir sus redes

Parte del nombre o la web que te den. Localiza las redes oficiales en este orden: enlaces del pie o cabecera de la web oficial → búsqueda "<marca> instagram", "<marca> tiktok", etc. → enlaces cruzados desde un perfil ya confirmado (bio de Instagram, "Acerca de" de YouTube).

La web no siempre enlaza todas las redes (en la prueba con conserveras, ninguna enlazaba TikTok), así que comprueba también los handles probables directamente en cada red. Un handle que coincide con el nombre no prueba nada: `@donbocarte` en TikTok resultó ser una persona. Da un perfil por bueno solo si el nombre, la bio o el enlace coinciden con la marca; si no, no lo incluyas.

Cubre todas las que existan: Instagram, TikTok, Facebook, LinkedIn, YouTube, X, Pinterest, y otras si son relevantes para el sector. Si la marca tiene cuentas por país o línea de producto (p. ej. `@marca_es`, `@marca_mx`), inclúyelas como filas separadas.

Antes de recoger métricas, enseña la lista de perfiles encontrados (red · handle · URL · por qué crees que es oficial) y continúa salvo que el usuario corrija algo. Un perfil equivocado invalida todo el Excel, por eso conviene confirmarlo pronto. Descarta cuentas de fans, distribuidores o agregadores.

**Rol de cada cuenta.** Junto a la lista, propón el enfoque de cada red: qué papel debería jugar respecto a los objetivos de demanda. Si el usuario ha dado objetivos o hipótesis (del briefing, 1.1–1.2), úsalos; si no, parte del rol por defecto del SWIN y dilo: los perfiles sociales sirven a **notoriedad, comunidad y tono de marca, y captación en la parte alta del funnel** (áreas Comunidad · Marca). Ajusta por red cuando tenga sentido (LinkedIn → marca corporativa / empleadora / B2B; YouTube → contenido de consideración; TikTok → alcance en público joven). Ese rol es contra lo que se juzga después si la cuenta "cumple".

**Modo competencia.** Si piden competidores sin dar la lista, sigue el flujo del SWIN *sugerir → validar → investigar*: propón 3–5 competidores directos (marca, por qué y qué referencia representa: líder en notoriedad, referente de contenido, rival local…), marca el origen ("sugerido por IA"), espera la validación y solo entonces audita. No cuelas distribuidores, marketplaces ni agregadores como competidores.

### 2. Recoger datos de cada perfil

Lee `references/redes.md`: dónde está cada dato en cada red, atajos para sacarlo rápido y trampas habituales (colaboraciones, fijados, sorteos, vistas promocionadas).

**Nivel perfil**: seguidores, seguidos, nº total de publicaciones, bio, enlace de la bio, verificado, idioma(s), fecha de la última publicación.

**Nivel publicación** (la muestra): las últimas 30 publicaciones o las de los últimos 90 días, lo que sea menor. Si la cuenta publica muy poco, toma las 12 últimas aunque sean más antiguas y dilo. De cada una: fecha, formato, likes/reacciones, comentarios, visualizaciones, compartidos y guardados (si son visibles), tema en 3–5 palabras, si es colaboración, URL.

**Tipo de contenido.** Clasifica cada publicación también por lo que cuenta (receta, producto, origen/proceso, historia de marca, serie propia, colaboración con creador, alianza con marca, sorteo, promoción, educativo, efeméride, corporativo, evento, UGC). Las definiciones y pistas están en `references/tipos_contenido.md`. El formato dice *cómo* publica la marca; el tipo dice *qué estrategia de contenidos* tiene, que es lo que más interesa al consultor.

Marca los posts fijados (`"fijado": true`): se listan pero no entran en las medias.

Ve guardando lo recogido en un JSON de trabajo (estructura en el docstring de `scripts/generar_excel.py`) **mientras navegas**, no al final, y guárdalo en una carpeta que no se borre (la del proyecto o la que indique el usuario): si la sesión se corta, lo recogido no se pierde.

### 3. Leer los comentarios

Si hay sesión, en las 3–5 publicaciones con más interacción de cada red lee los comentarios visibles: temas recurrentes, sentimiento dominante (positivo / neutro / negativo), preguntas frecuentes del público, y si la marca responde. Parafrasea; no copies comentarios con nombre de usuario. Sin sesión, anótalo como pendiente.

### 4. Analizar

Para ver las cifras mientras analizas:

```bash
python3 scripts/calcular_metricas.py datos_<marca>.json
```

Con eso, completa en el JSON los campos de juicio de cada red (`tono`, `estado`, `rol`, `valoracion`, `cumple`, `cumple_razon`) y los de síntesis a nivel raíz (`insights`, `fortalezas`, `debilidades`, `urgentes`, `optimizacion`, `hipotesis`, `oportunidades`, `amenazas`, `limitaciones`). Qué poner en cada uno:

- **Valoración** en la escala del SWIN: fuerte / medio / débil / inexistente (la marca no tiene esa red y es relevante para su sector) / sin datos (existe pero no se pudo ver).
- **¿Cumple la función?**: Sí / Parcialmente / No + razón en una frase, contrastando lo medido con el rol.
- **Insights** (5–8): lo que un consultor contaría al cliente, cada uno apoyado en un dato y con su implicación. Mira especialmente qué tipos de contenido y formatos rinden mejor en cada red, y si la marca publica lo que mejor le funciona. Separa dato de interpretación.
- **Síntesis D/F** (como la pide el SWIN en 1.4): top 3 fortalezas-palanca, top 3 debilidades críticas, cuentas urgentes vs. de optimización progresiva, hipótesis a validar con el cliente.
- **Modo competencia**: compara siempre también el **contenido propio** (sin colaboraciones ni sorteos), porque ahí se ve el trabajo de cada marca y no el de los creadores que contrata; añade oportunidades y amenazas para el cliente (input para la diferenciación de la Fase 3). En el JSON, cada entrada de `redes` lleva su `"marca"`.
- **Limitaciones**: qué no se pudo ver y por qué, y qué acceso lo completaría (sesión, export de Meta Business Suite, Metricool…). Audiencias demográficas, alcance e impresiones nunca son públicos. En el SWIN son pendientes no bloqueantes: se apuntan y se sigue.

### 5. Entregar el Excel

```bash
python3 scripts/generar_excel.py datos_<marca>.json "Auditoria_redes_<Marca>_<AAAA-MM-DD>.xlsx"
```

Genera estas hojas:

| Hoja | Contenido |
|---|---|
| Resumen | Una columna por red, una fila por métrica: seguidores, frecuencia, formato y tipo principal, % colaboraciones, medias y medianas, engagement rate total y del contenido propio, tono, estado, rol, valoración, ¿cumple? |
| Publicaciones | Detalle post a post con filtros: fecha, día, formato, tipo, colaboración, tema, likes, comentarios, vistas, compartidos, guardados, ER, URL |
| Formatos | Por red y formato: nº, %, medias y ER. En verde, lo que mejor rinde en cada red |
| Tipos de contenido | Igual, por tipo de contenido |
| Comparativa | Solo con varias marcas: una fila por marca y red |
| Insights | Insights, D/F, urgentes vs. progresivas, oportunidades, amenazas, hipótesis |
| Pendientes | Limitaciones y accesos que faltan |
| Metodología | Qué es cada métrica (incluido el engagement rate) y de dónde sale cada dato |

Guárdalo en la carpeta de trabajo del usuario (o donde pida) y entrégaselo. En el chat, además, da un resumen corto: perfiles auditados, 3–5 insights principales y qué ha quedado pendiente. El detalle va en el Excel, no lo repitas entero en el chat.

## Criterios de calidad

- Nunca inventes una cifra. Si un dato no es visible, déjalo vacío ("sin datos") y explica por qué en Pendientes. Un Excel con huecos honestos vale más que uno completo con estimaciones disfrazadas.
- Las cifras redondeadas que muestran las redes ("12,4 mil", "1,2M") se registran como número aproximado (12400) y se indica en Pendientes.
- Fecha todo: la auditoría es una foto de un día concreto.
- El **engagement rate** se calcula siempre igual para poder comparar entre marcas y auditorías: (likes + comentarios) / seguidores, por publicación, promediado. Lo hace el script; no lo calcules a mano.
- **Fuente de cada dato** (trazabilidad SWIN): cifras = observadas en el perfil público en la fecha de la auditoría; tono, estado, valoración e insights = análisis IA; exports o datos que aporte el usuario = aportado por cliente.
- Tono y estado son juicios: descríbelos en pocas palabras apoyados en algo observable ("activa: publica 4/semana, responde comentarios").

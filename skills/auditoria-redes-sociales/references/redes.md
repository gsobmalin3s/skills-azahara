# Dónde está cada dato en cada red

## Atajos probados (más rápidos que abrir post a post)

Leer las cifras de los datos que la propia página incrusta suele ser más rápido y fiable que leer la pantalla. Usa `javascript_tool` en la pestaña de la red (mismo origen) con `fetch(url).then(r => r.text())`:

- **Instagram**: cada post (`/p/<id>/`, `/reel/<id>/`) trae en `<meta property="og:description">` un texto del tipo "275 likes, 14 comments - <cuenta> el October 15, 2026: \"<caption>\"". Ahí tienes likes, comentarios, fecha, autor y pie. Sin sesión solo se ven los ~12 primeros posts del perfil, y las vistas de los reels no aparecen. Los seguidores exactos están en la `meta[name=description]` del perfil.
- **TikTok**: el perfil y cada vídeo traen el JSON `<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__">`. En el perfil, `webapp.user-detail.userInfo.stats` (seguidores, likes totales, nº de vídeos). En cada vídeo, `webapp.video-detail.itemInfo.itemStruct` (createTime, stats: playCount, diggCount, commentCount, shareCount, collectCount, isPinnedItem). La rejilla del perfil tarda unos segundos en cargar.
- **YouTube**: `ytInitialData` en el HTML de `/@canal/videos` (suscriptores y nº de vídeos en el header, IDs de los vídeos). En cada `/watch?v=<id>`: `"viewCount"`, `"publishDate"` y `"likeCount"`. Antes sale un muro de consentimiento: "Rechazar todo".
- **Facebook**: sin sesión, la `meta[name=description]` de la página da los seguidores y se ve la última publicación con sus reacciones. Más allá hace falta sesión.
- **LinkedIn**: la página pública de empresa muestra seguidores, empleados, sector y las últimas ~10 actualizaciones con fecha relativa, pero sin reacciones. Para las métricas de los posts hace falta sesión.
- **Pinterest**: el HTML del perfil trae `"follower_count"`, `"pin_count"`, `"board_count"` y `"last_pin_save_time"`.

## Cosas que confunden

- **Colaboraciones**: en la rejilla de Instagram aparecen posts de otras cuentas (creadores, restaurantes) publicados como colaboración. Cuentan como contenido de la marca, pero márcalos aparte ("reel colab", "post colab"): suelen rendir mucho más y mezclarlos infla las medias del contenido propio.
- **Fijados**: un post con fecha muy anterior al resto, o que rompe el orden cronológico al principio de la rejilla, está fijado. Exclúyelo de las medias.
- **Sorteos**: disparan los comentarios (la mecánica es "comenta y menciona"). Sepáralos como formato propio y no los uses para hablar del engagement "normal".
- **Vistas muy altas con pocos likes** (p. ej. 145.000 vistas y 77 likes): casi siempre es contenido promocionado. Señálalo como hipótesis, no como dato.
- **0 comentarios en todos los posts**: puede que los comentarios estén desactivados. Compruébalo antes de concluir que no hay conversación.

Qué se puede ver públicamente y dónde. Las interfaces cambian: si algo no está donde dice aquí, búscalo en la página y no lo des por inexistente sin mirar.

## Instagram (instagram.com/<handle>)
- **Perfil**: seguidores, seguidos y nº de publicaciones en la cabecera. Bio, enlace y verificado debajo.
- **Rejilla**: al pasar el ratón por un post aparecen likes y comentarios (necesita captura o `find`). Los reels muestran visualizaciones en la pestaña Reels.
- **Post individual** (`/p/<id>` o `/reel/<id>`): fecha, likes ("y X personas más"), comentarios, pie de foto, colaboradores ("<marca> y <otra>"), etiqueta "Colaboración pagada".
- **Formatos**: imagen, carrusel (icono de varias hojas), reel (icono de clapper), vídeo. Las stories no son auditables a posteriori; anota solo si hay destacados y sus temas.
- **Límites**: la marca puede ocultar los likes ("oculto"). Sin sesión, Instagram corta a los pocos scrolls.

## TikTok (tiktok.com/@<handle>)
- **Perfil**: seguidores, siguiendo, "Me gusta" totales, bio y enlace.
- **Rejilla**: visualizaciones de cada vídeo sobre la miniatura. Los fijados llevan la etiqueta "Fijado".
- **Vídeo**: likes, comentarios, guardados, compartidos y fecha (a veces relativa, como "hace 3 d"; conviértela a fecha).
- **Formatos**: vídeo, carrusel de fotos, directo (si hay replay).

## Facebook (facebook.com/<página>)
- **Página**: seguidores y "Me gusta" de la página. La categoría está en Información.
- **Publicaciones**: reacciones totales, comentarios, compartidos y fecha. Los reels muestran reproducciones.
- **Formatos**: texto, foto, álbum, vídeo, reel, enlace, evento.
- **Límites**: sin sesión casi no muestra nada. Muchas marcas tienen la página abandonada; mira la fecha de la última publicación.

## LinkedIn (linkedin.com/company/<slug>)
- **Página**: seguidores, nº de empleados en LinkedIn, sector y sede.
- **Publicaciones** (pestaña Publicaciones): reacciones, comentarios, compartidos y fecha relativa.
- **Formatos**: texto, imagen, carrusel/documento, vídeo, artículo, encuesta, evento.
- **Límites**: necesita sesión. Las fechas son relativas ("2 sem"); apunta la fecha aproximada.

## YouTube (youtube.com/@<handle>)
- **Canal**: suscriptores, nº de vídeos, fecha de alta y vistas totales (en "Más información").
- **Pestañas Vídeos y Shorts**: visualizaciones y fecha relativa por vídeo.
- **Vídeo**: likes, comentarios, duración y fecha exacta.
- **Formatos**: vídeo largo, short, directo.

## X (x.com/<handle>)
- **Perfil**: seguidores, siguiendo y fecha de alta.
- **Posts**: respuestas, reposts, likes, visualizaciones y fecha.
- **Límites**: sin sesión casi no se ve el timeline.

## Pinterest (pinterest.com/<handle>)
- **Perfil**: seguidores y visualizaciones mensuales.
- **Pines y tableros**: guardados por pin (no siempre visibles). Tableros y temas.

## Otras
Spotify/podcast, Twitch, Threads, WhatsApp Channels, etc.: incluir si existen y son relevantes para el sector, con lo que sea visible.

---
name: analisis-sector-competencia
description: Analiza el sector y la competencia de una marca y entrega un Excel con tendencias y motores de demanda del sector (con fuentes), set competitivo, ficha por competidor (posicionamiento, propuesta de valor, gama y precio, canales, tono, presencia digital), tabla comparativa y espacios de oportunidad y amenaza; o, en fase de benchmark, cómo resuelven competidores y referentes los retos del cliente con Mapa de Retos ("¿Cómo podríamos…?") y Mapa de Oportunidades. Úsala siempre que pidan "análisis de competencia", "análisis del sector", "quiénes son los competidores de X", "benchmark", "cómo se posiciona la competencia", "mapa de retos/oportunidades", o cuando entre un cliente nuevo y haya que situarlo en su mercado, aunque no lo digan con esas palabras.
---

# Análisis de sector y competencia

Una consultora de LIN3S necesita situar al cliente en su mercado: hacia dónde va el sector, quién compite con él por la atención y la compra, cómo se posiciona cada uno y dónde hay hueco. Esta skill hace la investigación con fuentes reales y la entrega en un **Excel** (capa de dato del SWIN; en producción, Google Sheets), con un resumen corto en el chat.

Implementa dos artefactos del SWIN · Estrategia de Demanda (método ORIA). Elige el modo según lo que haya:

| Modo | Artefacto | Cuándo | Necesita |
|---|---|---|---|
| **Contexto** | 1.5 · Sector y competencia (Fase 1, *Where You Are*) | Cliente nuevo; primera toma de contacto con el mercado | Marca y, si lo hay, sector, mercado geográfico, objetivos o hipótesis |
| **Benchmark** | 3.1 · Benchmark, Retos y Oportunidades (Fase 3, *What's Stopping You*) | Ya hay objetivos SMART, Main Challenge y retos | Objetivos/retos (2.3–2.4); idealmente el análisis de 1.5 y la auditoría 1.4 |

Si piden "benchmark" pero no hay objetivos ni retos, haz el modo contexto y explica que el benchmark del SWIN se orienta a retos y necesita esos inputs. Si hay dudas sobre el modo, pregunta.

## Principios (vienen del SWIN y son lo que da valor al análisis)

- **Investigar de verdad.** Busca en la web y en fuentes públicas (webs de las marcas, prensa sectorial, asociaciones, informes, registros mercantiles, tiendas). Nunca respondas "información no disponible" sobre algo que es mercado abierto: búscalo.
- **Cada afirmación con su fuente.** Toda cifra o hecho lleva fuente (URL o documento) y fecha. Lo no verificable se marca como **estimación** o **hipótesis**, nunca como dato. No afirmes cuotas de mercado ni cifras sin fuente.
- **Foco en demanda.** No es un análisis de producto: interesa cómo compite el sector por la atención y la conversión (canales, mensajes, precio, distribución, comunidad).
- **El set competitivo no se cierra solo.** Flujo *sugerir → validar → investigar*: propones, el usuario (o el cliente) valida y puede añadir, y solo entonces investigas a fondo. Marca el origen de cada marca: *sugerido por IA* / *aportado por cliente* / *aportado por LIN3S*.
- **Nada de agregadores.** Distribuidores, marketplaces, directorios o comparadores no son competidores (salvo que el cliente compita realmente con ellos, p. ej. marca blanca).
- **Rankings.** Si piden un ranking o una categoría, da un top 5 por categoría, sin agrupar.
- **Distinguir dato de interpretación** y señalar qué conviene validar con investigación primaria (entrevistas, encuestas, datos del cliente).

## Modo contexto (1.5)

### 1. Encuadre
Con lo que te den (y una búsqueda rápida si hace falta), fija: sector y subcategoría, mercado geográfico, segmento de precio del cliente, canales de venta (retail, online, horeca, export) y, si los hay, objetivos o hipótesis. Dilo en dos líneas antes de seguir: todo lo que viene depende de este encuadre.

### 2. Set competitivo
Propón 4–6 marcas: competidores **directos** (mismo segmento y público), y si aporta, 1–2 **indirectos** (otro segmento que roba la misma ocasión de consumo) y 1–2 **referentes** (marcas que hacen algo especialmente bien). Para cada una: por qué entra y qué **referencia** representa respecto al cliente (líder en notoriedad, rival local, referente de contenido, competidor en precio…). Explica también qué has dejado fuera y por qué. **Espera la validación** antes de investigar.

### 3. Tendencias del sector
4–6 tendencias o motores de demanda, cada una con: qué está pasando, evidencia (cifra o hecho) con fuente y fecha, e implicación para el cliente. Prioriza fuentes sectoriales (asociaciones, estudios de consumo, prensa especializada) sobre blogs genéricos.

### 4. Ficha por competidor
Lee `references/ficha_competidor.md` (campos y dónde buscar cada uno). Si puedes lanzar subagentes, investiga **una marca por subagente en paralelo** (cliente incluido, para compararlo con la misma vara), pasándoles los campos de la ficha y lo que ya sepas (p. ej. datos de redes); mientras, tú investigas las tendencias. Revisa lo que devuelvan: si dos fuentes no cuadran, dilo en la ficha en vez de elegir una en silencio.

**Precios comparables.** Normaliza siempre a **€/100 g de peso neto** del mismo producto de referencia (p. ej. bonito en aceite de oliva), y fíjate en *cómo* se vende: por unidad o solo por cajas, pedido mínimo, umbral de envío gratis. Esa fricción de compra es tan reveladora como el precio. Por cada marca: datos básicos, posicionamiento y propuesta de valor (con sus propias palabras, citando la web), gama y precio de referencia, canales de venta, canales de comunicación (todas las URLs), tono y mensajes, presencia digital, y el veredicto del **Estándar de auditoría** del SWIN: ¿cumple la referencia por la que se le audita? Sí / Parcialmente / No + razón.

**Presencia en redes:** si la skill `auditoria-redes-sociales` está disponible, úsala en su modo competencia para las métricas de redes y trae a esta ficha el resumen (seguidores, frecuencia, formato y tipo principal, engagement, estado). Si no lo está, recoge al menos seguidores, actividad reciente y tono por red, siguiendo la rejilla básica del SWIN (tono, seguidores, frecuencia, formatos, mercados, audiencias, engagement, interacciones, comentarios → comentario del estado de la cuenta).

### 5. Síntesis
- **Comparativa**: una fila por marca (cliente incluido) con las dimensiones clave, para leer de un vistazo dónde está cada uno.
- **Mapa de posicionamiento**: sitúa a cada marca en dos ejes relevantes para el sector (p. ej. precio × tradición/innovación) y dilo en texto; los ejes se eligen según lo que diferencia de verdad a las marcas.
- **Oportunidades y amenazas** para el cliente (3–5 de cada), cada una apoyada en evidencia de las fichas o tendencias. Es el input de mercado para la diferenciación de la Fase 3.
- **Qué validar**: hipótesis que solo se confirman con investigación primaria o con datos del cliente.

## Modo benchmark (3.1)

El SWIN es explícito: **no repitas el perfilado de competidores** (eso es 1.5). Aquí el foco es *cómo resuelven otros nuestros objetivos y retos*.

1. **Referencias.** Set de 3–5 competidores directos (de 1.5) + 2–3 **referentes externos**: marcas de fuera del sector que resuelven muy bien alguno de los retos. Por cada una: origen (competidor de 1.5 / referente externo / aportada por el cliente), reto u objetivo con el que se relaciona y todos sus canales (web, redes, blog, newsletter…). Valida el set con el usuario.
2. **Benchmark reto a reto** (no competidor a competidor): por cada objetivo SMART y reto, quién lo resuelve bien y **cómo**: mecanismo o táctica concreta, canal donde se observa, evidencia con fuente, y qué podemos aprender o aplicar. Si un canal es la clave de ese "cómo", analízalo con la profundidad del Estándar de auditoría.
3. **Cruce con la auditoría 1.4**: si existe, señala discrepancias (lo que el benchmark revela que contradice o actualiza lo visto en la auditoría de activos).
4. **Mapa de Retos**: cada reto trazado a su objetivo y reformulado como **"¿Cómo podríamos…?"**, con evidencia y prioridad por impacto. En los de mayor impacto o causa raíz poco clara, aplica **5 Whys** (opcional): Problema → ¿Por qué? → … → causa raíz (3–5 iteraciones), para no tratar síntomas.
5. **Mapa de Oportunidades**: por cada "¿Cómo podríamos…?", ideas o caminos formulados **en gerundio** ("Creando…", "Aprovechando…"), sin filtrar, clasificados por **accesibilidad** e **impacto** (alto/medio/bajo). Un reto es un obstáculo; una oportunidad es una idea de solución: no los confundas. Las oportunidades no son iniciativas dimensionadas (eso es la Fase 4).

## Entregar el Excel

Escribe un JSON con las hojas (estructura en el docstring de `scripts/generar_excel.py`) y genera el archivo:

```bash
python3 scripts/generar_excel.py analisis_<marca>.json "Analisis_sector_competencia_<Marca>_<AAAA-MM-DD>.xlsx"
```

Las hojas y sus columnas exactas están en `references/hojas_excel.md`; síguelas para que todos los análisis de LIN3S tengan la misma forma y se puedan comparar y volcar al SWIN. Guarda el JSON y el Excel en una carpeta que no se borre (la del proyecto o la que diga el usuario) e ir guardando el JSON mientras investigas, no al final.

En el chat, resumen corto: encuadre, set analizado, 3–5 hallazgos principales, oportunidades/amenazas clave y qué queda por validar. El detalle va en el Excel.

## Criterios de calidad

- Cada fila con dato lleva **fuente** (URL) y **fecha de consulta**. La hoja Fuentes las recoge todas.
- **Etiqueta de origen** (trazabilidad SWIN): *dato público* (con fuente) / *análisis IA* / *aportado por cliente* / *aportado por LIN3S*.
- Si un dato no aparece tras buscarlo, escribe "no encontrado" y dónde se buscó: eso también es información.
- Precios: con fecha, formato y canal (p. ej. "lata 120 g, tienda online, 27/10/2026"), porque cambian.
- Prefiere menos tendencias y fichas bien fundamentadas a muchas genéricas que valdrían para cualquier sector.

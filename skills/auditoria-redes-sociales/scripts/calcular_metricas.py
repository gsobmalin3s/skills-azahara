"""Calcula las métricas de la auditoría de redes a partir del JSON de trabajo.

Uso:
    python3 calcular_metricas.py datos_marca.json

Estructura del JSON (los campos que no se vean se dejan en null):

{
  "marca": "Serrats",
  "fecha_auditoria": "2026-10-21",
  "redes": [
    {
      "red": "Instagram",
      "handle": "@serrats",
      "url": "https://www.instagram.com/serrats/",
      "seguidores": 12400,
      "publicaciones": [
        {
          "fecha": "2026-10-18",
          "formato": "reel",
          "likes": 312,
          "comentarios": 14,
          "vistas": 8900,
          "compartidos": null,
          "guardados": null,
          "fijado": false,
          "tema": "receta bonito",
          "url": "https://www.instagram.com/reel/..."
        }
      ]
    }
  ]
}

Imprime en Markdown las métricas por red y por formato y el top 3 de publicaciones.
ER = (likes + comentarios) / seguidores, por publicación, en %.
"""

import json
import sys
from collections import defaultdict
from datetime import date
from statistics import mean, median

DIAS = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]


def valores(posts, campo):
    return [p[campo] for p in posts if p.get(campo) is not None]


def fmt(n, dec=0):
    if n is None:
        return "sin datos"
    s = f"{n:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def media(posts, campo):
    v = valores(posts, campo)
    return mean(v) if v else None


def mediana(posts, campo):
    v = valores(posts, campo)
    return median(v) if v else None


def er(posts, seguidores):
    if not seguidores:
        return None
    tasas = [
        ((p.get("likes") or 0) + (p.get("comentarios") or 0)) / seguidores * 100
        for p in posts
        if p.get("likes") is not None or p.get("comentarios") is not None
    ]
    return mean(tasas) if tasas else None


def interacciones(p):
    return (p.get("likes") or 0) + (p.get("comentarios") or 0)


def frecuencia_semanal(posts):
    fechas = sorted(date.fromisoformat(p["fecha"]) for p in posts if p.get("fecha"))
    if len(fechas) < 2:
        return None
    dias = (fechas[-1] - fechas[0]).days or 1
    return len(fechas) / dias * 7


def informe(datos):
    out = [f"# {datos.get('marca', '')} · auditoría {datos.get('fecha_auditoria', '')}", ""]
    for red in datos["redes"]:
        todos = red.get("publicaciones", [])
        posts = [p for p in todos if not p.get("fijado")]
        seg = red.get("seguidores")
        fechas = sorted(p["fecha"] for p in posts if p.get("fecha"))
        out.append(f"## {red['red']} · {red.get('handle', '')}")
        out.append(f"- Seguidores: {fmt(seg)}")
        out.append(
            f"- Muestra: {len(posts)} publicaciones"
            + (f" ({fechas[0]} → {fechas[-1]})" if fechas else "")
            + (f", {len(todos) - len(posts)} fijada(s) excluida(s)" if len(todos) > len(posts) else "")
        )
        out.append(f"- Última publicación: {fechas[-1] if fechas else 'sin datos'}")
        out.append(f"- Publicaciones/semana: {fmt(frecuencia_semanal(posts), 1)}")
        for campo in ("likes", "comentarios", "vistas", "compartidos", "guardados"):
            if valores(posts, campo):
                out.append(
                    f"- {campo.capitalize()}: media {fmt(media(posts, campo))} · mediana {fmt(mediana(posts, campo))}"
                )
        tasa = er(posts, seg)
        out.append(f"- Engagement rate: {fmt(tasa, 2) + ' %' if tasa is not None else 'sin datos'}")

        por_formato = defaultdict(list)
        for p in posts:
            por_formato[p.get("formato") or "sin datos"].append(p)
        out += ["", "| Formato | Nº | % | Media likes | Media coment. | Media vistas | ER % |", "|---|---|---|---|---|---|---|"]
        for f, ps in sorted(por_formato.items(), key=lambda kv: -len(kv[1])):
            out.append(
                f"| {f} | {len(ps)} | {fmt(len(ps) / len(posts) * 100)} | {fmt(media(ps, 'likes'))} | "
                f"{fmt(media(ps, 'comentarios'))} | {fmt(media(ps, 'vistas'))} | {fmt(er(ps, seg), 2)} |"
            )

        por_dia = defaultdict(list)
        for p in posts:
            if p.get("fecha") and (p.get("likes") is not None or p.get("comentarios") is not None):
                por_dia[date.fromisoformat(p["fecha"]).weekday()].append(interacciones(p))
        # Con menos de 3 publicaciones por día el "mejor día" es ruido: no se reporta.
        por_dia = {d: v for d, v in por_dia.items() if len(v) >= 3}
        if por_dia:
            mejor = max(por_dia, key=lambda d: mean(por_dia[d]))
            out += ["", f"Mejor día (media de interacciones): {DIAS[mejor]} ({len(por_dia[mejor])} publicaciones)"]

        top = sorted(posts, key=lambda p: (interacciones(p), p.get("vistas") or 0), reverse=True)[:3]
        out += ["", "Top 3:"]
        for p in top:
            out.append(
                f"- {p.get('fecha')} · {p.get('formato')} · {p.get('tema', '')} · "
                f"{fmt(p.get('likes'))} likes · {fmt(p.get('comentarios'))} coment. · "
                f"{fmt(p.get('vistas'))} vistas · {p.get('url', '')}"
            )
        out.append("")
    return "\n".join(out)


if __name__ == "__main__":
    with open(sys.argv[1], encoding="utf-8") as fh:
        print(informe(json.load(fh)))

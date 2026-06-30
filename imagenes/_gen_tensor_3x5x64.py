"""Genera imagenes/tensor_3x5x64.png (figura del tensor (batch, seq_len, embed_dim)).

Se exporta como imagen estática porque el backend inline de Quarto guarda con
bbox_inches='tight', y ese recorte ignora el texto 3D de matplotlib, cortando las
etiquetas que quedan fuera del cubo. Ejecutar con el Python del proyecto:

    .venv/Scripts/python.exe imagenes/_gen_tensor_3x5x64.py
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

AZUL, NARANJA = "#1381B0", "#FF961C"


def cuboide(ax, origin, size, fc, ec=AZUL, alpha=0.9, lw=1.0):
    ox, oy, oz = origin
    dx, dy, dz = size
    x = [ox, ox + dx]; y = [oy, oy + dy]; z = [oz, oz + dz]
    V = np.array([[x[0], y[0], z[0]], [x[1], y[0], z[0]], [x[1], y[1], z[0]], [x[0], y[1], z[0]],
                  [x[0], y[0], z[1]], [x[1], y[0], z[1]], [x[1], y[1], z[1]], [x[0], y[1], z[1]]])
    faces = [[V[0], V[1], V[2], V[3]], [V[4], V[5], V[6], V[7]], [V[0], V[1], V[5], V[4]],
             [V[2], V[3], V[7], V[6]], [V[1], V[2], V[6], V[5]], [V[0], V[3], V[7], V[4]]]
    ax.add_collection3d(Poly3DCollection(faces, facecolors=fc, edgecolors=ec, linewidths=lw, alpha=alpha))


fig = plt.figure(figsize=(8.0, 4.2))
ax = fig.add_subplot(111, projection="3d")
L, W, t, gap = 8.0, 5.0, 0.55, 0.7
top = lambda z0: z0 + t + 0.02
for i in range(3):                                   # 3 láminas = batch
    z0 = i * (t + gap)
    cuboide(ax, (0, 0, z0), (L, W, t), fc="#E3F1F8", ec=AZUL, alpha=0.55, lw=1.2)
    for s in range(1, 5):                            # 5 filas = seq_len
        ax.plot([0, L], [s, s], [top(z0), top(z0)], color=AZUL, lw=1.0, alpha=0.9)
    for e in np.linspace(L / 12, L * 11 / 12, 11):   # columnas ≈ embed_dim
        ax.plot([e, e], [0, W], [top(z0), top(z0)], color=AZUL, lw=0.5, alpha=0.5)

z0 = 2 * (t + gap)                                   # resaltar una fila = un token
cuboide(ax, (0, 2, z0), (L, 1, t), fc=NARANJA, ec="#C57200", alpha=0.85, lw=1.2)
ax.text(L / 2, -1.5, 0, "embed_dim = 64", ha="center", va="top", color=AZUL, fontsize=11)
ax.text(L + 1.6, W / 2, 0, "seq_len = 5", ha="left", color=AZUL, fontsize=11)
ax.text(-2.2, 0, 3 * (t + gap) / 2, "batch = 3", ha="right", color=AZUL, fontsize=11)
xlo, xhi = -3.2, L + 3.2; ylo, yhi = -2.0, W + 1.2; zlo, zhi = -0.3, 3 * (t + gap) + 0.3
ax.set_xlim(xlo, xhi); ax.set_ylim(ylo, yhi); ax.set_zlim(zlo, zhi)
ax.set_box_aspect((xhi - xlo, yhi - ylo, zhi - zlo))
ax.view_init(elev=20, azim=-62)
ax.axis("off")
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
# bbox_inches=None (NO 'tight'): conserva el lienzo completo y evita el recorte del texto 3D
fig.savefig("imagenes/tensor_3x5x64.png", dpi=200, bbox_inches=None)
print("Guardado imagenes/tensor_3x5x64.png")

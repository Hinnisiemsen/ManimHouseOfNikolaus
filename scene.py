from manim import *

class HouseOfNikolaus(Scene):
    def construct(self):
        # Definieren der korrekten Punkte für das Haus
        A = [0, 2, 0]  # Spitze des Hauses (Dachspitze)
        B = [-2, 0, 0]  # Linke obere Ecke
        C = [2, 0, 0]   # Rechte obere Ecke
        D = [-2, -2, 0] # Linke untere Ecke
        E = [2, -2, 0]  # Rechte untere Ecke

        # Die Reihenfolge der Punkte, um das Haus in einem Strich korrekt zu zeichnen
        points = [D, B, A, C, B, E, D, C, E]

        dots = [Dot(point=p) for p in points]


        self.play(*[Create(dot) for dot in dots], run_time=2)


        # Linienpfad für das Haus
        path = VMobject()
        path.set_points_as_corners([*points, points[0]])  # Pfad schließen

        # Zeichnen des Hauses mit korrekter Geometrie
        self.play(Create(path), run_time=5)

        # Warten für die Anzeige
        self.wait(2)

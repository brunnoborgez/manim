from manim import *

class Soma(Scene):
    def construct(self):

        formula = MathTex('S_{n}','=', 'a_1', '+', 'a_2', '+', '\dots', '+', 'a_{n-1}', '+', 'a_n')


        self.add(formula)

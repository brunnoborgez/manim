from manim import *

class Soma(Scene):
    
    def construct(self):
        
        titulo = Title('Soma dos n termos de uma progressão aritmética')
        
        formula = MathTex('S_{n}','=', 'a_1', '+', 'a_2', '+', '\dots', '+', 'a_{n-1}', '+', 'a_n', font_size = 70) #tamanho da fonte da alterada!
    
        #self.add(formula)
        
        self.play(Write(formula[0:11]), run_time = 3) #linha adicionada para escrever a fórmula!
       
        #alterações feitas: tamanho da fonte alterado, linha 11 excluída, linha 13 adicionada!

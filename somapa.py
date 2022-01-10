from manim import *
import numpy as np

movimento = np.array([-1,0,0]) #define a posição de movimento.

class Soma(Scene):
    
    def construct(self):

        inicio = MathTex('(', 'a_{1}', ',', 'a_{2}', ',', 'a_{3}', ',', '\dots', ',', 'a_{n}', ')')
        inicio.set_x(-2)
        inicio.set_y(0)

        nomes = MathTex('=\,primeiro\,\,termo', '=\,segundo\,\,termo', '=\,terceiro\,\,termo', '=\,enésimo\,\,termo')
        nomes[0].set_y(2)
        nomes[0].set_x(-1)
        nomes[1].set_y(1)
        nomes[1].set_x(-1)
        nomes[2].set_y(0)
        nomes[2].set_x(-1)
        nomes[3].set_y(-2)
        nomes[3].set_x(-1)

        copias =  MathTex('= a_{1}', '= a_{1}+r', '= a_{2}+r', '= a_{n-1}+r', '= a_{1}+2r', '= a_{1}+(n-1)r')
        copia_colorida = MathTex("a_{n}= a_{1}+(n-1)r", font_size=120, color=BLUE)

        
        copias[0].set_x(-2)
        copias[0].set_y(2)
        copias[1].set_x(-2)
        copias[1].set_y(1)
        copias[2].set_x(-2)
        copias[2].set_y(0)
        copias[3].set_x(-2)
        copias[3].set_y(-2)
        copias[4].set_x(-2)
        copias[4].set_y(0)
        copias[5].set_x(-2)
        copias[5].set_y(-2)
        copia_colorida.set_x(0)
        copia_colorida.set_y(0)

        self.play(Write(inicio[0]), Write(inicio[-1])
            )

        self.play(Write(inicio[1:10])
            )
        self.wait()

        self.play(
            FadeOut(inicio[0:12:2])
            )
        self.play(
            ApplyMethod(inicio[1].shift, 2.6*LEFT, 2*UP),
            ApplyMethod(inicio[3].shift, 3.3*LEFT, 1*UP),
            ApplyMethod(inicio[5].shift, 4*LEFT, 0*UP),
            ApplyMethod(inicio[7].shift, 4.8*LEFT, 1*DOWN),
            ApplyMethod(inicio[9].shift, 5.7*LEFT, 2*DOWN)
            )
        self.play(FadeTransformPieces(inicio[7], inicio[7].rotate(PI/2), run_time=2))
        self.wait()

        for i in (0, 1, 2, 3):
            self.play(Write(nomes[i])
            )
        self.wait()

        for i in (0, 1, 2, 3):
            self.play(
                ReplacementTransform(nomes[i], copias[i]))
            self.wait()
        
        for i in (0, 1):
            self.play(
            ReplacementTransform(copias[2 + i], copias[4 + i])
            )
            self.wait()
        
        self.play(
            FadeOut(inicio[1:10:2]),
            FadeOut(copias[0:5]),
            FadeTransform(copias[5], copia_colorida)
            )
        
        self.wait(1)

        self.play(FadeOut(copia_colorida)
            )

        
        titulo = Title('Soma dos n termos de uma progressão aritmética', font_size = 50) #tamanho da fonte alterada!
        titulo.set_y(2) #posição do título na tela.
        ponto = Dot([0,0,0], color = BLACK) #ponto para efeito combinado com o titulo desaparecendo.
        

        
        formula = MathTex('S_{n}','=', 'a_1', '+', 'a_2', '+', '\dots', '+', 'a_{n-1}', '+', 'a_n', font_size = 70) #tamanho da fonte alterada!
    
        #self.add(formula)
        
        self.play(Write(titulo), run_time = 3) #escreve o título,
        self.wait() #espera,
        self.play(FadeTransform(titulo, ponto)) #transforma o título no ponto.
        
        self.play(Write(formula[0:11]), run_time = 3) #linha adicionada para escrever a fórmula!
        self.play(FadeOut(formula[0:2]),ApplyMethod(formula[2:11].shift, movimento)) #apaga o Sn e movimenta a sequência de soma para a esqueda.
        
       
        #alterações feitas: tamanho da fonte alterado, linha 11 excluída, linha 13 adicionada!

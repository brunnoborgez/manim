from manim import *
from manim.utils import tex
import numpy as np
from numpy.lib.function_base import copy

# definindo a posição de movimento das animacoes
movimento = np.array([-1,0,0]) #define a posição de movimento.
movimento4 = np.array([-1.32,0,0]) 
movimento2 = np.array([1.3,0,0])
movimento3 = np.array([2.5,0,0])
movimento5 = np.array([-2.52,0,0])
movimento6 = np.array([-2,0,0])

class Soma(Scene):
    
    def construct(self):

        # definindo os termos da sequencia e tamanho da fonte

        inicio = MathTex( 
            '(\ ','a_{1}', ',', ' \ a_{2}',  ',', ' \ a_{3}', ',', ' \ a_{4}',
            ',', '\ \dots',  ',', ' \ a_{n}', ' \ )', font_size = 70)

        # definindo os nomes dos termos da sequencia e tamanho da fonte   
        nomes = Tex(
            '= \ ', 'primeiro\,\,termo', '= \ ','segundo\,\,termo', '= \ ','terceiro\,\,termo',
            '= \ ', 'quarto\,\,termo', '= \ ', 'enésimo\,\,termo',  font_size = 60)
        
        # organizando a posicaos dos nomes

        nomes[0].set_y(3)
        nomes[0].set_x(-3.35)
        nomes[1].next_to(nomes[0], RIGHT)
        nomes[2].set_y(2)
        nomes[2].set_x(-3.35)
        nomes[3].next_to(nomes[2], RIGHT)
        nomes[4].set_y(1)
        nomes[4].set_x(-3.35)
        nomes[5].next_to(nomes[4], RIGHT)
        nomes[6].set_y(0)
        nomes[6].set_x(-3.35)
        nomes[7].next_to(nomes[6], RIGHT)
        nomes[8].set_y(-2.3)
        nomes[8].set_x(-3.35)
        nomes[9].next_to(nomes[8], RIGHT)

        # definindo das copias dos termos da sequencia

        copias =  MathTex(
            '\, a_{1}',#0

            '\, a_{1}',#1
            '+',#2
            'r',#3

            '\, a_{2}',#4
            '+',#5
            'r',#6

            '\, a_{3}',#7
            '+',#8
            'r',#9

            '\, a_{n-1}',#10
            '+',#11
            'r',#12

            '\, a_{1}+(n-1)r',#13
            'a_{1}+2r',#14
            '+',#15
            '2r',#16
            '2r',#17
            '+',#18
            '3r',#19
            '\, a_{1}',#20
            '+',#21
            'r', #22
            '\, a_{1}',#23
            '+',#24
            'r', #25
            '+',#26
            'r', #27

            font_size = 70)
        
        # posicao das copias

        copias[0].next_to(nomes[0], RIGHT)

        copias[1].next_to(nomes[2], RIGHT)
        copias[2].next_to(copias[1], RIGHT)
        copias[3].next_to(copias[2], RIGHT)

        copias[4].next_to(nomes[4], RIGHT)
        copias[5].next_to(copias[4], RIGHT)
        copias[6].next_to(copias[5], RIGHT)

        copias[7].next_to(nomes[6], RIGHT)
        copias[8].next_to(copias[7], RIGHT)
        copias[9].next_to(copias[8], RIGHT)

        copias[10].next_to(nomes[2], RIGHT)
        copias[11].next_to(nomes[2], RIGHT)
        copias[12].next_to(nomes[2], RIGHT)
        copias[13].next_to(nomes[8], RIGHT)
        copias[14].next_to(nomes[4], RIGHT)
        copias[15].next_to(nomes[2], RIGHT)
        copias[16].next_to(nomes[2], RIGHT)
        copias[17].next_to(copias[5], RIGHT)
        copias[18].next_to(nomes[2], RIGHT)
        copias[19].next_to(copias[8], RIGHT)

        copias[20].next_to(nomes[4], RIGHT)
        copias[21].next_to(copias[20], RIGHT)
        copias[22].next_to(copias[21], RIGHT)
        
        copias[23].next_to(nomes[6], RIGHT)
        copias[24].next_to(copias[23], RIGHT)
        copias[25].next_to(copias[24], RIGHT)

        copias[26].next_to(copias[9], RIGHT)
        copias[27].next_to(copias[26], RIGHT)


        # criando retangulos para esconder alguns termos

        retangulo = Rectangle(
            height = 0.5,width = 0.6, color = BLACK, fill_opacity = 1)
        retangulo.set_y(1)
        retangulo.set_x(-1)
        
        retangulo2 = Rectangle(
            height = 0.5, width = 0.6, color = BLACK, fill_opacity = 1)
        retangulo2.set_y(0)
        retangulo2.set_x(-1)

        retangulo3 = Rectangle( #
            height = 5, width = 5, color = BLACK, fill_opacity = 1)
        retangulo3.set_y(1)
        retangulo3.set_x(-2.6)

        termo_geral = MathTex(
            '\,a_{n}=a_{1}+(n-1)r', font_size = 120)

        grupo = VGroup(inicio[11],nomes[8],copias[13])

        texto = Tex('Termo Geral da P.A.', font_size = 120, color = YELLOW)
        texto.next_to(termo_geral, 3*UP)

        self.wait()

        self.play(Write(inicio[0]), Write(inicio[-1])) # escreve os parenteses inicial e final

        self.play(Write(inicio[1:12])) # escreve os termos entre os parenteses

        self.wait()

        self.play(FadeOut(inicio[0:14:2])) # apaga os parenteses e as vírgulas  

        self.play( # muda a posicao dos termos
            ApplyMethod(inicio[1].shift, 0.9*LEFT, 3*UP),
            ApplyMethod(inicio[3].shift, 2.2*LEFT, 2*UP),
            ApplyMethod(inicio[5].shift, 3.5*LEFT, 1*UP),
            ApplyMethod(inicio[7].shift, 4.75*LEFT, 0*DOWN),
            ApplyMethod(inicio[11].shift, 7.6*LEFT, 2.3*DOWN),
            ApplyMethod(inicio[9].shift, 6.15*LEFT, 1*DOWN))
    
        self.play(inicio[9].animate.rotate(-1.6))

        self.wait()

        self.play(Write(nomes[0:10]), run_time = 5) # escreve o nome dos termos da sequencia

        self.wait()

        # transforma o nome no termo matemático

        self.play(ReplacementTransform(nomes[1],copias[0]), run_time = 2)
        self.play(ReplacementTransform(nomes[3],copias[1:4]), run_time = 2)
        self.play(ReplacementTransform(nomes[5],copias[4:7]), run_time = 2)
        self.play(ReplacementTransform(nomes[7],copias[7:10]), run_time = 2)

        self.play(FadeToColor(copias[1:4], color = YELLOW))
        self.play(FadeToColor(copias[4], color = YELLOW))
        

        self.play(
            ReplacementTransform(copias[1:4].copy(),copias[20:23]), # mudanca para o a3
            FadeToColor(copias[1:4].copy(), color = WHITE),
            ApplyMethod(copias[5:7].shift, movimento2), # movimenta o "+ r" do a3
            FadeOut(copias[4]))
     
        self.wait()

        self.play(
            FadeToColor(copias[20:23], color = YELLOW),
            FadeToColor(copias[5:8], color = YELLOW))

        
        
        self.play(
            ReplacementTransform(copias[20:23].copy(),copias[23:26]), # mundanca para o a4
            FadeToColor(copias[20:23].copy(), color = WHITE),
            FadeToColor(copias[5:7], color = WHITE),
            ReplacementTransform(copias[5:7].copy(),copias[26:28]), # mundanca para o a4
            ApplyMethod(copias[7:10].shift, movimento3), # movimenta o "+ r" do a4
            FadeOut(copias[7])) 

        self.wait()

        self.play(ApplyMethod(copias[5:7].shift, movimento4)) # retorna para o a3

        self.play( # faz aparecer o retangulo para esconder o "r" do a3 e em seguida faz aparecer o "2r"
            FadeIn(retangulo),
            FadeIn(copias[17]))
       

        self.play(
            ApplyMethod(copias[8:10].shift, movimento5),  # retorna para o a4
            ApplyMethod(copias[26:28].shift, movimento4)) # retorna para o a4
       
        self.play(# faz aparecer o retangulo para esconder o "r" do a4 e em seguida faz aparecer o "2r"
            FadeIn(retangulo2),
            FadeIn(copias[19])) 

        self.play(ReplacementTransform(nomes[9],copias[13]), run_time = 2)

        self.play(
            FadeToColor(inicio[11], color = YELLOW),
            FadeToColor(nomes[8], color = YELLOW),
            FadeToColor(copias[13], color = YELLOW),
            FadeIn(retangulo3))
        

        self.play(
            Write(texto),
            FadeTransform(grupo,termo_geral))

        self.play(
            FadeOut(texto,termo_geral)
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

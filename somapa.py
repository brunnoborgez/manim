from manim import *
from manim.utils import tex
import numpy as np
from numpy.lib.function_base import copy

# definindo a posição de movimento das animacoes

movimentos = ([1.3,0,0], [2.5,0,0], [-1.32,0,0], [-2.52,0,0], [-1,0,0])

class ProgressaoAritmetica(Scene):
    
    def construct(self):

        # definindo os termos da sequencia e tamanho da fonte

        inicio = MathTex( 
            '(\ ','a_{1}', ',', ' \ a_{2}',  ',', ' \ a_{3}', ',', ' \ a_{4}',
            ',', '\ \dots',  ',', ' \ a_{n}', ' \ )', font_size = 70)

        # definindo os nomes dos termos da sequencia e tamanho da fonte 

        nomes = Tex(
            '= \ ', 'primeiro\,\,termo', '= \ ','segundo\,\,termo', '= \ ','terceiro\,\,termo',
            '= \ ', 'quarto\,\,termo', '= \ ', 'enésimo\,\,termo',  font_size = 60)
        
        # organizando a posicao dos nomes

        nomes[0].set_y(3), nomes[0].set_x(-3.35)
        nomes[1].next_to(nomes[0], RIGHT)
        nomes[2].set_y(2), nomes[2].set_x(-3.35)
        nomes[3].next_to(nomes[2], RIGHT)
        nomes[4].set_y(1), nomes[4].set_x(-3.35)
        nomes[5].next_to(nomes[4], RIGHT)
        nomes[6].set_y(-0.2), nomes[6].set_x(-3.35)
        nomes[7].next_to(nomes[6], RIGHT)
        nomes[8].set_y(-2.1), nomes[8].set_x(-3.35)
        nomes[9].next_to(nomes[8], RIGHT)

        # definindo as copias dos termos da sequencia

        copias =  MathTex(
            '\, a_{1}','\, a_{1}', '+','r','\, a_{2}','+','r','\, a_{3}','+', 'r',
            '\, a_{1}','+','r','\, a_{1}','+','r','+','r','2r','3r','\, a_{1}+(n-1)r',
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
        copias[10].next_to(nomes[4], RIGHT)
        copias[11].next_to(copias[10], RIGHT)
        copias[12].next_to(copias[11], RIGHT)
        copias[13].next_to(nomes[6], RIGHT)
        copias[14].next_to(copias[13], RIGHT)
        copias[15].next_to(copias[14], RIGHT)
        copias[16].next_to(copias[9], RIGHT)
        copias[17].next_to(copias[16], RIGHT)
        copias[18].next_to(copias[5], RIGHT)
        copias[19].next_to(copias[8], RIGHT)
        copias[20].next_to(nomes[8], RIGHT)
    
        # criando retangulos para esconder alguns termos

        retangulo_0 = Rectangle(
            height = 0.5,width = 0.6, color = BLACK, fill_opacity = 1)
        retangulo_0.set_x(-1), retangulo_0.set_y(1)
        
        retangulo_1 = Rectangle(
            height = 0.5, width = 0.7, color = BLACK, fill_opacity = 1)
        retangulo_1.set_x(-1.1), retangulo_1.set_y(0)

        retangulo_2 = Rectangle(
            height = 6, width = 5, color = BLACK, fill_opacity = 1)
        retangulo_2.set_x(-2.6), retangulo_2.set_y(1)

        termo_geral = MathTex(
            '\,a_{n}=a_{1}+(n-1)r', font_size = 120)

        grupo = VGroup(inicio[11], nomes[8], copias[20])

        texto = Tex(
            'Termo Geral da P.A.', font_size = 120, color = YELLOW)
        texto.next_to(termo_geral, 3*UP)

        titulo_0 = Tex(
            'Soma dos \quad termos de uma', font_size = 90)
        titulo_0.next_to(termo_geral, 3*UP)
        
        titulo_1 = Tex(
            'Progressão Aritmética', font_size = 120, color = YELLOW)
        titulo_1.next_to(titulo_0, DOWN)

        ponto = Dot([0,0,0], color = BLACK) #ponto para efeito combinado com o titulo desaparecendo.
        
        grupo_termo_geral = VGroup(texto, termo_geral)
        
        formula_0 = MathTex(
            'S_{n}','=', 'a_1', '+', 'a_2', '+', 'a_3', '+', '\dots', '+', "a_{n-2}", '+', 'a_{n-1}', '+', 'a_n', font_size = 65) 
        formula_0.set_y(1)

        formula_1 = MathTex(
            'S_{n}','=', 'a_n', '+', 'a_{n-2}', '+','a_{n-1}', '+', '\dots', '+', 'a_3', '+', 'a_2', '+', 'a_1', font_size = 65, color = PURE_GREEN) 
        formula_1.set_y(0)

        sn_branco = MathTex("S_n", font_size = 65)
        sn_branco.set_x(-5), sn_branco.set_y(3)

        sinal_soma = MathTex("+", "+", "+", "+", "+", "+", "+",  font_size = 65)
        sinal_soma[0].next_to(sn_branco, RIGHT)
       
        pontos = MathTex("\dots", font_size = 75)
        pontos.set_x(-4.2), pontos.set_y(-0.7)

        sn_verde = MathTex("S_n", font_size = 65, color = PURE_GREEN)
        sn_verde.next_to(sinal_soma[0])

        a1_branco = MathTex("a_{1}", font_size = 65)
        an_verde = MathTex("a_{n}", font_size = 65, color = PURE_GREEN)
        a1_branco.set_x(-5), a1_branco.set_y(2)
        sinal_soma[1].next_to(sinal_soma[0], 2.2*DOWN)
        an_verde.next_to(sinal_soma[1], RIGHT)

        a2_branco = MathTex("a_{2}", font_size = 65)
        an2_verde = MathTex("a_{n-2}", font_size = 65, color = PURE_GREEN)
        a2_branco.set_x(-5), a2_branco.set_y(1)
        sinal_soma[2].next_to(sinal_soma[1], 2.2*DOWN)
        an2_verde.next_to(sinal_soma[2], RIGHT)

        a3_branco = MathTex("a_{3}", font_size = 65)
        an1_verde = MathTex("a_{n-1}", font_size = 65, color = PURE_GREEN)
        a3_branco.set_x(-5), a3_branco.set_y(0)
        sinal_soma[3].next_to(sinal_soma[2], 2.2*DOWN)
        an1_verde.next_to(sinal_soma[3], RIGHT)

        an2_branco = MathTex("a_{n-2}", font_size = 65)
        a3_verde = MathTex("a_{3}", font_size = 65, color = PURE_GREEN)
        an2_branco.set_x(-5.5), an2_branco.set_y(-1.25)
        sinal_soma[4].next_to(sinal_soma[3], 3.1*DOWN)
        a3_verde.next_to(sinal_soma[4], RIGHT)
      
        an1_branco = MathTex("a_{n-1}", font_size = 65)
        a2_verde = MathTex("a_{2}", font_size = 65, color = PURE_GREEN)
        an1_branco.set_x(-5.5), an1_branco.set_y(-2.25)
        sinal_soma[5].next_to(sinal_soma[4], 2.2*DOWN)
        a2_verde.next_to(sinal_soma[5], RIGHT)
        
        an_branco = MathTex("a_{n}", font_size = 65)
        a1_verde = MathTex("a_{1}", font_size = 65, color = PURE_GREEN)
        an_branco.set_x(-5), an_branco.set_y(-3.25)
        sinal_soma[6].next_to(sinal_soma[5], 2.2*DOWN)
        a1_verde.next_to(sinal_soma[6], RIGHT)
        
        n = MathTex('n', font_size = 90)
        n.set_x(-1.1), n.set_y(1.6)
       
        grupo_titulo = VGroup(titulo_0, n, titulo_1)

        self.wait()

        self.play( # escreve os parenteses inicial e final
            Write(inicio[0]), Write(inicio[-1])) 

        self.play( # escreve os termos entre os parenteses
            Write(inicio[1:12])) 

        self.wait()

        self.play( # apaga os parenteses e as vírgulas  
            FadeOut(inicio[0:14:2])) 
        
        self.play( # muda a posicao dos termos
            ApplyMethod(inicio[1].shift, 0.9*LEFT, 3.1*UP),
            ApplyMethod(inicio[3].shift, 2.2*LEFT, 2.1*UP),
            ApplyMethod(inicio[5].shift, 3.5*LEFT, 1.1*UP),
            ApplyMethod(inicio[7].shift, 4.75*LEFT, 0.1*DOWN),
            ApplyMethod(inicio[9].shift, 6.15*LEFT, 1.1*DOWN),
            ApplyMethod(inicio[11].shift, 7.6*LEFT, 2.1*DOWN))

        self.play(
            inicio[9].animate.rotate(-1.6))
    
        self.wait()

        self.play( # escreve o nome dos termos da sequencia
            Write(nomes[0:10]), run_time = 5) 

        self.wait()

        self.play( # transforma o nome no termo matemático
            ReplacementTransform(nomes[1], copias[0]), run_time = 2)

        self.play(
            ReplacementTransform(nomes[3], copias[1:4]), run_time = 2)

        self.play(
            ReplacementTransform(nomes[5], copias[4:7]), run_time = 2)

        self.play(
            ReplacementTransform(nomes[7], copias[7:10]), run_time = 2)

        self.play(
            FadeToColor(copias[1:5], color = YELLOW))

        self.play(
            FadeToColor(copias[4], color = YELLOW))
        
        self.play( # mudanca para o a3
            ReplacementTransform(copias[1:4].copy(), copias[10:13]), 
            FadeToColor(copias[1:4].copy(), color = WHITE),
            ApplyMethod(copias[5:7].shift, movimentos[0]), # movimenta o "+ r" do a3
            FadeOut(copias[4]))
     
        self.wait()

        self.play(
            FadeToColor(copias[10:13], color = YELLOW),
            FadeToColor(copias[5:8], color = YELLOW))

        self.play( # mundanca para o a4
            ReplacementTransform(copias[10:13].copy(), copias[13:16]), 
            FadeToColor(copias[10:13].copy(), color = WHITE),
            FadeToColor(copias[5:7], color = WHITE),
            ReplacementTransform(copias[5:7].copy(), copias[16:18]),
            ApplyMethod(copias[7:10].shift, movimentos[1]), # movimenta o "+ r" do a4
            FadeOut(copias[7])) 

        self.wait()

        self.play( # retorna para o a3
            ApplyMethod(copias[5:7].shift, movimentos[2])) 

        self.play( # faz aparecer o retangulo para esconder o "r" do a3 e em seguida faz aparecer o "2r"
            FadeIn(retangulo_0),
            FadeIn(copias[18]))
       
        self.play( # retorna para o a4
            ApplyMethod(copias[8:10].shift, movimentos[3]), 
            ApplyMethod(copias[16:18].shift, movimentos[2]))
       
        self.play( # faz aparecer o retangulo para esconder o "r" do a4 e em seguida faz aparecer o "2r"
            FadeIn(retangulo_1),
            FadeIn(copias[19])) 

        self.play(
            ReplacementTransform(nomes[9], copias[20]), run_time = 2)

        self.play(
            FadeToColor(inicio[11], color = YELLOW),
            FadeToColor(nomes[8], color = YELLOW),
            FadeToColor(copias[20], color = YELLOW))
        
        self.play(
            FadeIn(retangulo_2),
            FadeTransform(grupo, termo_geral))

        self.play(
            Write(texto, run_time = 2))

        self.wait()

        self.play(
            FadeTransform(grupo_termo_geral, ponto))
      
        self.play(
           FadeTransform(ponto, grupo_titulo))

        self.wait()

        self.play(
            Unwrite(grupo_titulo, reverse = False, run_time = 2))

        self.wait()

        self.play(
            Write(formula_0[0:15], run_time = 3 ),
            Write(formula_1[0:15], reverse = True, run_time = 3))
        
        self.wait()

        self.play(
            FadeTransform(formula_0[0], sn_branco),
            FadeTransform(formula_1[0], sn_verde))

        self.play(
            FadeIn(sinal_soma[0]), 
            FadeOut(formula_0[1], formula_1[1]))

        self.play(
            FadeTransform(formula_0[2], a1_branco),
            FadeTransform(formula_1[2], an_verde),
            FadeTransform(formula_0[3], sinal_soma[1]),
            FadeTransform(formula_1[3], sinal_soma[1]))

        self.play(
            FadeTransform(formula_0[4], a2_branco),
            FadeTransform(formula_1[4], an2_verde),
            FadeTransform(formula_0[5], sinal_soma[2]),
            FadeTransform(formula_1[5], sinal_soma[2])) 

        self.play(
            FadeTransform(formula_0[6], a3_branco),
            FadeTransform(formula_1[6], an1_verde),
            FadeTransform(formula_0[7], sinal_soma[3]),
            FadeTransform(formula_1[7], sinal_soma[3]))  

        self.play(
            FadeTransform(formula_0[8], pontos),
            FadeTransform(formula_1[8], pontos),
            FadeOut(formula_0[9]),
            FadeOut(formula_1[9]))

        self.play(
            FadeTransform(formula_0[10], an2_branco),
            FadeTransform(formula_1[10], a3_verde),
            FadeTransform(formula_0[11], sinal_soma[4]),
            FadeTransform(formula_1[11], sinal_soma[4]))
        
        self.play(
            FadeTransform(formula_0[12], an1_branco),
            FadeTransform(formula_1[12], a2_verde),
            FadeTransform(formula_0[13], sinal_soma[5]),
            FadeTransform(formula_1[13], sinal_soma[5]))

        self.play(
            FadeTransform(formula_0[14], an_branco),
            FadeTransform(formula_1[14], a1_verde), 
            FadeIn(sinal_soma[6]))

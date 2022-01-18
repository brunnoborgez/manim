from manimlib import *

class ProgressaoAritimetica(Scene):
    def construct(self):

        retangulo = Rectangle( # cria um retangulo em volta da palavra Manim
            height = 3, width = 10) 

        titulo1 = TexText(
            "Um vídeo criado com", font_size = 100)
        
        titulo2 = TexText(
            "Manim", font_size = 300)

        titulo1.next_to(titulo2, 3.5 * UP)

        titulo3 = TexText(
            "Progressão Aritmética", color = TEAL, font_size = 120)

        self.play( # escreve o titulo na tela
            Write(titulo1), 
            Write(titulo2), 
            run_time = 5)

        self.play( # faz animação do retangulo em volta da palavra Manim
            ShowCreation(retangulo), 
            run_time = 2)

        self.wait()

        self.play( # apaga o titulo e o retangulo da tela
            FadeOut(titulo2), 
            Uncreate(retangulo), 
            FadeTransform(titulo1,titulo3))

        self.wait()

        self.play( # apaga o titulo Progressao Ariitmetica da tela
            FadeOut(titulo3))

        linhas = VGroup( # grupo criado para os termos da PA
            Tex(
                "(", "\ a_1", ",", "\ a_2", ",", "\ a_3", ",", "\ a_4", ",", "\ \dots",
                ",", "\ a_{n-3}", ",", "\ a_{n-2}", ",", "\ a_{n-1}", ",", "\ a_{n}", "\ )", 
                font_size = 65),
            Tex(
                "\ a_1", "\ a_2", "\ a_3", "\ a_4", "\ \dots", 
                "\ a_{n-3}", "\ a_{n-2}", "\ a_{n-1}", "\ a_{n}", 
                font_size = 65))
          
        linhas[1][0].set_x(-5),linhas[1][0].set_y(3.2) # a_1
        linhas[1][1].set_x(-5),linhas[1][1].set_y(2.4) # a_2
        linhas[1][2].set_x(-5),linhas[1][2].set_y(1.6) # a_3
        linhas[1][3].set_x(-5),linhas[1][3].set_y(0.8) # a_4
        linhas[1][4].set_x(-5),linhas[1][4].set_y(0) # reticencias
        linhas[1][5].set_x(-5),linhas[1][5].set_y(-0.8) # a_(n-3)
        linhas[1][6].set_x(-5),linhas[1][6].set_y(-1.6) # a_(n-2)
        linhas[1][7].set_x(-5),linhas[1][7].set_y(-2.4) # a_(n-1)
        linhas[1][8].set_x(-5),linhas[1][8].set_y(-3.2) # a_n

        self.wait() # espera

        self.play( # escreve os termos da sequencia no centro da tela
            Write(linhas[0].center()), run_time = 5) 

        self.play(# apaga as virgulas e os parenteses
            FadeOut(linhas[0][0:19:2]))

        self.play(# faz o movimento vertical 
            TransformMatchingTex(linhas[0][1:18:2], linhas[1],
            path_arc = -45 * DEGREES))

        self.play( # rotaciona os reticencias
            linhas[1][4].animate.rotate(-1.6), font_size = 60)

        nomes = VGroup( # grupo criado para os nomes dos termos da PA
            Tex(
                "=", "primeiro \ termo",
                "=", "segundo \ termo",
                "=", "terceiro \ termo",
                "=", "quarto \ termo",
                "=", "(n-3)-\\acute{e}simo \ termo",
                "=", "(n-2)-\\acute{e}simo \ termo",
                "=", "(n-1)-\\acute{e}simo \ termo",
                "=", "n-\\acute{e}simo \ termo",
                font_size = 60),
            Tex(
                "a_1", "a_1", "+", "r", "a_2", "+", "r", "a_3", "+", "r", "a_1", "+", 
                "(n-4)r", "a_1", "+", "(n-3)r", "a_1", "+", "(n-2)r", "a_1", "+", "(n-1)r", 
                font_size = 65))
        
        # linhas 95 à 102 posiciona os nomes dos termos à direta 
        # dos termos que foram para o movimento de coluna

        nomes[0][0:2].next_to(linhas[1][0], RIGHT) # = primeiro termo
        nomes[0][2:4].next_to(linhas[1][1], RIGHT) # = segundo termo
        nomes[0][4:6].next_to(linhas[1][2], RIGHT) # = terceiro termo
        nomes[0][6:8].next_to(linhas[1][3], RIGHT) # = quarto termo
        nomes[0][8:10].next_to(linhas[1][5], RIGHT) # = (n-3) ésimo termo
        nomes[0][10:12].next_to(linhas[1][6], RIGHT) # = (n-2) ésimo termo
        nomes[0][12:14].next_to(linhas[1][7], RIGHT) # = (n-1) ésimo termo
        nomes[0][14:16].next_to(linhas[1][8], RIGHT) # = ésimo termo
       
        self.play( # escreve os nomes dos termos
            Write(nomes[0][0:16]), run_time = 8)

        # linhas 110 à 117 posiciona os termos à direta 
        # dos nomes de cada um dos elementos   

        nomes[1][0].next_to(nomes[0][0], RIGHT) # a_1*
        nomes[1][1:4].next_to(nomes[0][2], RIGHT) # a_1+r
        nomes[1][4:7].next_to(nomes[0][4], RIGHT) # a_2+r
        nomes[1][7:10].next_to(nomes[0][6], RIGHT) # a_3+r
        nomes[1][10:13].next_to(nomes[0][8], RIGHT) # a_1+(n-4)+r
        nomes[1][13:16].next_to(nomes[0][10], RIGHT) # a_1+(n-3)+r
        nomes[1][16:19].next_to(nomes[0][12], RIGHT) # a_1+(n-2)+r
        nomes[1][19:22].next_to(nomes[0][14], RIGHT) # a_1+(n-1)+r

        self.play( # transforma primeiro termo em a_1*
            Transform(nomes[0][1], nomes[1][0]))
        
        self.play( # transforma segundo termo em a_1+r
            Transform(nomes[0][3], nomes[1][1:4]))
        
        self.play( # transforma terceiro termo em a_2+r
            Transform(nomes[0][5], nomes[1][4:7]))
        
        self.play( # transforma quarto termo em a_3+r
            Transform(nomes[0][7], nomes[1][7:10]))

        # Aqui começamos a criar varias copias, pois nao conseguimos
        # trabalhar com as variaves anteriores 

        copia_linhas = Tex( # elementos que vao encaixar no proximo termo, para demonstracao
            "a_1", "+", "r", "a_1", "+", "r", "+", "r",
            font_size = 65)
        
        copia_linhas[0:3].next_to(nomes[0][2], RIGHT)
        copia_linhas[3:8].next_to(nomes[0][4], RIGHT)

        nomes_copia_a_2 = Tex("2r", "3r", font_size = 65)
        nomes_copia_a_2[0].next_to(nomes[1][5], RIGHT)
        nomes_copia_a_2[1].next_to(nomes[1][8], RIGHT)

        self.play(
            FadeOut(nomes[0][5]), # apaga o termo "a_2"
            copia_linhas[0:3].animate.move_to(nomes[0][5]), # move "a_1 + r" para "a_2"
            nomes[1][5:7].shift, 1.1 * RIGHT) # desloca "+ r" do "a_2"

        self.wait() 

        self.play(
            FadeOut(nomes[0][7]), # apaga o termo "a_3"
            copia_linhas[3:8].shift, 0.725 * DOWN, # move "+ r" do "a_2"
            nomes[1][8:10].shift, 2.2 * RIGHT) # desloca "+ r" do a_3

        self.play( # retorna "+ r" do "a_2"
            nomes[1][5:7].shift, 1.1 * LEFT)

        self.play(
            FadeOut(nomes[1][5:6]), # apaga "+ r" do "a_2"
            FadeOut(copia_linhas[2]),
            Transform(nomes[1][6], nomes_copia_a_2[0])) # transforma "r + r" em "2r"

        self.wait()

        self.play(
            nomes[1][8:10].shift, 2.2 * LEFT,
            copia_linhas[6:8].shift, 1.1 * LEFT)

        self.play(
            FadeOut(nomes[1][8:10]),
            FadeOut(copia_linhas[6:8]),
            Transform(copia_linhas[5], nomes_copia_a_2[1]))

        self.wait()

        self.play(
            Transform(nomes[0][9], nomes[1][10:13]))

        self.play(
            Transform(nomes[0][11], nomes[1][13:16]))

        self.play(
            Transform(nomes[0][13], nomes[1][16:19]))

        self.play(
            Transform(nomes[0][15], nomes[1][19:22]))
        
        self.wait(2)
        
        termo_geral = Tex(
            "a_n", "=", "a_1", "+", "(n-1)r", 
            color = YELLOW,
            font_size = 120)
        termo_geral_texto = TexText(
            "Termo Geral", 
            font_size = 150)
        termo_geral_texto.next_to(termo_geral, 3.5 * UP)

        self.play(
            FadeOut(linhas[1][0:8]),
            FadeOut(nomes[0][0:16:2]),
            FadeOut(nomes[0][9:14:2]),
            FadeOut(nomes[0][1:5:2]),
            FadeOut(nomes_copia_a_2[0:2]),
            FadeOut(nomes[1][6]),
            FadeOut(copia_linhas[5]),
            FadeOut(copia_linhas[0:2]),
            FadeOut(copia_linhas[3:6]),
            FadeTransform(linhas[1][8], termo_geral[0]),
            FadeTransform(nomes[0][14], termo_geral[1]),
            FadeTransform(nomes[0][15], termo_geral[2:5]))
        
        self.play(
            Write(termo_geral_texto))

        self.wait()

        self.play(
            FadeOut(termo_geral_texto),
            FadeOut(termo_geral))

class SomaDosTermos(Scene):
    def construct(self):

        titulo_soma_1 = TexText(
            "Soma dos quad termos de uma", 
            font_size = 90)
        titulo_soma_2 = TexText(
            "Progressão Aritmética", 
            font_size = 120)
        titulo_soma_2.next_to(titulo_soma_1, DOWN)

        formula_crescente = Tex(
            "S_{n}", "=", "a_1", "+", "a_2", "+", "a_3", "+", 
            "\dots", "+", "a_{n-2}", "+", "a_{n-1}", "+", "a_n", 
            font_size = 65) 

        formula_crescente.set_y(2)

        formula_decrescente = Tex(
            "S_{n}", "=", "a_n", "+", "a_{n-2}", "+", "a_{n-1}", 
            "+", "\dots", "+", "a_3", "+", "a_2", "+", "a_1", 
            font_size = 65, color = BLUE) 

        formula_decrescente.next_to(formula_crescente, 8 * DOWN)

        coluna_soma = VGroup(
            Tex(
            "S_{n}", "+", "a_1", "+", "a_2", "+", "a_3", "+", 
            "\dots", "+", "a_{n-2}", "+", "a_{n-1}", "+", "a_n", "+",
             font_size = 70),
            Tex(
            "S_{n}", "+", "a_n", "+", "a_{n-1}", "+", "a_{n-2}", "+", 
            "\dots", "+", "a_3", "+", "a_2", "+", "a_1", "+", color = BLUE, font_size = 70))

        coluna_soma[0][0].set_x(-1.5), coluna_soma[0][0].set_y(3.2)
        coluna_soma[0][2].set_x(-1.5), coluna_soma[0][2].set_y(2.3)
        coluna_soma[0][4].set_x(-1.5), coluna_soma[0][4].set_y(1.4)
        coluna_soma[0][6].set_x(-1.5), coluna_soma[0][6].set_y(0.5)
        coluna_soma[0][8].set_x(-1.5), coluna_soma[0][8].set_y(-0.4)
        coluna_soma[0][10].set_x(-1.5), coluna_soma[0][10].set_y(-1.3)
        coluna_soma[0][12].set_x(-1.5), coluna_soma[0][12].set_y(-2.2)
        coluna_soma[0][14].set_x(-1.5), coluna_soma[0][14].set_y(-3.1)
        

        coluna_soma[0][1].set_x(0), coluna_soma[0][1].set_y(3.2)
        coluna_soma[0][3].set_x(0), coluna_soma[0][3].set_y(2.3)
        coluna_soma[0][5].set_x(0), coluna_soma[0][5].set_y(1.4)
        coluna_soma[0][7].set_x(0), coluna_soma[0][7].set_y(0.5)
        coluna_soma[0][9].set_x(0), coluna_soma[0][9].set_y(-0.4)
        coluna_soma[0][11].set_x(0), coluna_soma[0][11].set_y(-1.3)
        coluna_soma[0][13].set_x(0), coluna_soma[0][13].set_y(-2.2)
        coluna_soma[0][15].set_x(0), coluna_soma[0][15].set_y(-3.1)
        
        
        coluna_soma[1][0].set_x(1.5), coluna_soma[1][0].set_y(3.2)
        coluna_soma[1][2].set_x(1.5), coluna_soma[1][2].set_y(2.3)
        coluna_soma[1][4].set_x(1.5), coluna_soma[1][4].set_y(1.4)
        coluna_soma[1][6].set_x(1.5), coluna_soma[1][6].set_y(0.5)
        coluna_soma[1][8].set_x(1.5), coluna_soma[1][8].set_y(-0.4)
        coluna_soma[1][10].set_x(1.5), coluna_soma[1][10].set_y(-1.3)
        coluna_soma[1][12].set_x(1.5), coluna_soma[1][12].set_y(-2.2)
        coluna_soma[1][14].set_x(1.5), coluna_soma[1][14].set_y(-3.1)

        coluna_soma[1][1].set_x(0), coluna_soma[1][1].set_y(3.2)
        coluna_soma[1][3].set_x(0), coluna_soma[1][3].set_y(2.3)
        coluna_soma[1][5].set_x(0), coluna_soma[1][5].set_y(1.4)
        coluna_soma[1][7].set_x(0), coluna_soma[1][7].set_y(0.5)
        coluna_soma[1][9].set_x(0), coluna_soma[1][9].set_y(-0.4)
        coluna_soma[1][11].set_x(0), coluna_soma[1][11].set_y(-1.3)
        coluna_soma[1][13].set_x(0), coluna_soma[1][13].set_y(-2.2)
        coluna_soma[1][15].set_x(0), coluna_soma[1][15].set_y(-3.1)

        self.play(
            Write(formula_crescente[0:15], run_time = 3))

        self.play(
            Write(formula_decrescente[0:15], run_time = 3))
        
        self.play( # faz o movimento para coluna
            TransformMatchingTex(formula_crescente[0:16], coluna_soma[0],
            path_arc = -45 * DEGREES),
            TransformMatchingTex(formula_decrescente[0:16], coluna_soma[1],
            path_arc = -45 * DEGREES))

        self.play(
            FadeToColor(coluna_soma[1][1:17:2], color = WHITE))

        self.play(
            coluna_soma[0][8].animate.rotate(-1.6),
            coluna_soma[1][8].animate.rotate(-1.6), font_size = 70)

        grupo_coluna_soma_0_1 = VGroup(coluna_soma[0][0:16],coluna_soma[1][0:16])

        ponto = Tex("\dots", font_size = 70)
        ponto.set_x(-4.5), ponto.set_y(-0.4)

        copia_soma = Tex(
            "a_1", "=", "a_1", 
            "a_2", "=", "a_1", "+", "r",
            "a_3", "=", "a_1", "+", "2r",
            "a_n", "=", "a_n",
            "a_{n-1}", "=", "a_n", "-", "r",
            "a_{n-2}", "=", "a_n", "-", "2r",

            font_size = 70)

        copia_soma[0].set_x(-4.5), copia_soma[0].set_y(2.3)
        copia_soma[3].set_x(-4.5), copia_soma[3].set_y(1.4)
        copia_soma[8].set_x(-4.5), copia_soma[8].set_y(0.5)
        copia_soma[13].set_x(-4.5), copia_soma[13].set_y(-3.1)
        copia_soma[16].set_x(-4.5), copia_soma[16].set_y(-2.2)
        copia_soma[21].set_x(-4.5), copia_soma[21].set_y(-1.3)

        copia_soma[1:3].next_to(copia_soma[0], RIGHT)
        copia_soma[4:8].next_to(copia_soma[3], RIGHT)
        copia_soma[9:13].next_to(copia_soma[8], RIGHT)
        copia_soma[14:16].next_to(copia_soma[13], RIGHT)
        copia_soma[17:21].next_to(copia_soma[16], RIGHT)
        copia_soma[22:26].next_to(copia_soma[21], RIGHT)

        self.wait()

        self.play(
            coluna_soma[0][2].copy().animate.move_to(copia_soma[0]),
            coluna_soma[0][4].copy().animate.move_to(copia_soma[3]),
            coluna_soma[0][6].copy().animate.move_to(copia_soma[8]),
            coluna_soma[0][8].copy().animate.move_to(ponto),
            coluna_soma[0][10].copy().animate.move_to(copia_soma[21]),
            coluna_soma[0][12].copy().animate.move_to(copia_soma[16]),
            coluna_soma[0][14].copy().animate.move_to(copia_soma[13]),
            grupo_coluna_soma_0_1.shift, 3.5 * RIGHT)

        self.play(
            Write(copia_soma[1:3]))

        self.play(
            Write(copia_soma[4:8]))

        self.play(
            Write(copia_soma[9:13]))

        self.wait()

        self.play(
            Write(copia_soma[14:16]))

        self.play(
            Write(copia_soma[17:21]))

        self.play(
            Write(copia_soma[22:26]))
        
        copia_soma_2 = Tex(
            "a_1", "=", "a_1", 
            "a_2", "=", "a_1", "+", "r",
            "a_3", "=", "a_1", "+", "2r",
            "a_n", "=", "a_n",
            "a_{n-1}", "=", "a_n", "-", "r",
            "a_{n-2}", "=", "a_n", "-", "2r",
            color = YELLOW,

            font_size = 70)

        copia_soma_2[0].set_x(-4.5), copia_soma_2[0].set_y(2.3)
        copia_soma_2[3].set_x(-4.5), copia_soma_2[3].set_y(1.4)
        copia_soma_2[8].set_x(-4.5), copia_soma_2[8].set_y(0.5)
        copia_soma_2[13].set_x(-4.5), copia_soma_2[13].set_y(-3.1)
        copia_soma_2[16].set_x(-4.5), copia_soma_2[16].set_y(-2.2)
        copia_soma_2[21].set_x(-4.5), copia_soma_2[21].set_y(-1.3)

        copia_soma_2[1:3].next_to(copia_soma_2[0], RIGHT)
        copia_soma_2[4:8].next_to(copia_soma_2[3], RIGHT)
        copia_soma_2[9:13].next_to(copia_soma_2[8], RIGHT)
        copia_soma_2[14:16].next_to(copia_soma_2[13], RIGHT)
        copia_soma_2[17:21].next_to(copia_soma_2[16], RIGHT)
        copia_soma_2[22:26].next_to(copia_soma_2[21], RIGHT)

        copia_soma_3 = Tex(
            "a_1", "=", "a_1", 
            "a_2", "=", "a_1", "+", "r",
            "a_3", "=", "a_1", "+", "2r",
            "a_n", "=", "a_n",
            "a_{n-1}", "=", "a_n", "-", "r",
            "a_{n-2}", "=", "a_n", "-", "2r",
            color = YELLOW,

            font_size = 70)

        copia_soma_3[0].set_x(-4.5), copia_soma_3[0].set_y(2.3)
        copia_soma_3[3].set_x(-4.5), copia_soma_3[3].set_y(1.4)
        copia_soma_3[8].set_x(-4.5), copia_soma_3[8].set_y(0.5)
        copia_soma_3[13].set_x(-4.5), copia_soma_3[13].set_y(-3.1)
        copia_soma_3[16].set_x(-4.5), copia_soma_3[16].set_y(-2.2)
        copia_soma_3[21].set_x(-4.5), copia_soma_3[21].set_y(-1.3)

        copia_soma_3[1:3].next_to(copia_soma_3[0], RIGHT)
        copia_soma_3[4:8].next_to(copia_soma_3[3], RIGHT)
        copia_soma_3[9:13].next_to(copia_soma_3[8], RIGHT)
        copia_soma_3[14:16].next_to(copia_soma_3[13], RIGHT)
        copia_soma_3[17:21].next_to(copia_soma_3[16], RIGHT)
        copia_soma_3[22:26].next_to(copia_soma_3[21], RIGHT)

        retangulo1 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo1.set_x(-3),  retangulo1.set_y(2.3)

        retangulo2 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo2.set_x(-3),  retangulo2.set_y(1.4)

        retangulo3 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo3.set_x(-3),  retangulo3.set_y(0.5)

        retangulo = Rectangle(
            height = 0.8, width = 1.2, color = "#333333", fill_opacity = 1)
        retangulo.set_x(-4.6),  retangulo.set_y(-0.4)

        #33333 cor pradrao do fundo Manim GL

        retangulo5 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo5.set_x(-3),  retangulo5.set_y(-1.3)

        retangulo6 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo6.set_x(-3),  retangulo6.set_y(-2.2)

        retangulo7 = Rectangle(
            height = 0.6, width = 5, color = "#333333", fill_opacity = 1)
        retangulo7.set_x(-3),  retangulo7.set_y(-3.1)

        self.play(
            FadeToColor(copia_soma[2], color = YELLOW),
            FadeToColor(coluna_soma[0][2], color = YELLOW),
            FadeToColor(coluna_soma[1][14], color = YELLOW))

        self.play(
            copia_soma_2[2].animate.move_to(coluna_soma[0][2]),
            copia_soma_3[2].animate.move_to(coluna_soma[1][14]),
            FadeOut(coluna_soma[0][2]),
            FadeOut(coluna_soma[1][14]))

        self.play(
            FadeToColor(copia_soma_2[2], color = WHITE),
            FadeToColor(copia_soma_3[2], color = BLUE),
            FadeToColor(copia_soma[2], color = WHITE),
            FadeIn(retangulo1))

        self.wait()

        self.play(
            FadeToColor(copia_soma[5:8], color = YELLOW),
            FadeToColor(coluna_soma[0][4], color = YELLOW),
            FadeToColor(coluna_soma[1][12], color = YELLOW))

        self.play(
            copia_soma_2[5:8].animate.move_to(coluna_soma[0][4], 2 * RIGHT), 
            copia_soma_3[5:8].animate.move_to(coluna_soma[1][12],2 * LEFT),
            FadeOut(coluna_soma[0][4]),
            FadeOut(coluna_soma[1][12]))
            
        self.play(
            FadeToColor(copia_soma_2[5:8], color = WHITE),
            FadeToColor(copia_soma_3[5:8], color = BLUE),
            FadeToColor(copia_soma[5:8], color = WHITE),
            FadeIn(retangulo2))

        self.wait()

        self.play(
            FadeToColor(copia_soma[10:13], color = YELLOW),
            FadeToColor(coluna_soma[0][6], color = YELLOW),
            FadeToColor(coluna_soma[1][10], color = YELLOW))

        self.play(
            copia_soma_2[10:13].animate.move_to(coluna_soma[0][6], 2 * RIGHT),
            copia_soma_3[10:13].animate.move_to(coluna_soma[1][10], 2 * LEFT), 
            FadeOut(coluna_soma[0][6]),
            FadeOut(coluna_soma[1][10]))

        self.play(
            FadeToColor(copia_soma_2[10:13], color = WHITE),
            FadeToColor(copia_soma_3[10:13], color = BLUE),
            FadeToColor(copia_soma[10:13], color = WHITE),
            FadeIn(retangulo3),
            FadeIn(retangulo))

        self.wait()

        self.play(
            FadeToColor(copia_soma[23:26], color = YELLOW),
            FadeToColor(coluna_soma[0][10], color = YELLOW),
            FadeToColor(coluna_soma[1][6], color = YELLOW))
        
        self.play(
            copia_soma_2[23:26].animate.move_to(coluna_soma[0][10], 2 * RIGHT),
            copia_soma_3[23:26].animate.move_to(coluna_soma[1][6], 2 * LEFT), 
            FadeOut(coluna_soma[0][10]),
            FadeOut(coluna_soma[1][6]))

        self.play(
            FadeToColor(copia_soma_2[23:26], color = WHITE),
            FadeToColor(copia_soma_3[23:26], color = BLUE),
            FadeToColor(copia_soma[23:26], color = WHITE),
            FadeIn(retangulo5))

        self.wait()

        self.play(
            FadeToColor(copia_soma[18:21], color = YELLOW),
            FadeToColor(coluna_soma[0][12], color = YELLOW),
            FadeToColor(coluna_soma[1][4], color = YELLOW))
         
        self.play(
            copia_soma_2[18:21].animate.move_to(coluna_soma[0][12], 2 * RIGHT),
            copia_soma_3[18:21].animate.move_to(coluna_soma[1][4], 2 * LEFT),
            FadeOut(coluna_soma[0][12]),
            FadeOut(coluna_soma[1][4]))
            
        self.play(
            FadeToColor(copia_soma_2[18:21], color = WHITE),
            FadeToColor(copia_soma_3[18:21], color = BLUE),
            FadeToColor(copia_soma[18:21], color = WHITE),
            FadeIn(retangulo6))

        self.wait()

        self.play(
            FadeToColor(copia_soma[15], color = YELLOW),
            FadeToColor(coluna_soma[0][14], color = YELLOW),
            FadeToColor(coluna_soma[1][2], color = YELLOW))          
        
        self.play(
            copia_soma_2[15].animate.move_to(coluna_soma[0][14]),
            copia_soma_3[15].animate.move_to(coluna_soma[1][2]),
            FadeOut(coluna_soma[0][14]),
            FadeOut(coluna_soma[1][2]))

        self.play(
            FadeToColor(copia_soma_2[15], color = WHITE),
            FadeToColor(copia_soma_3[15], color = BLUE),
            FadeToColor(copia_soma[15], color = WHITE),
            FadeIn(retangulo7))  
        
        self.wait()

        final = Tex(
            "S_{n}", "+", 
            "a_{1}", "+", 
            "a_{1}", "+", "r", "+", 
            "a_{1}", "+", "2r", "+", 
            "\dots", "+", 
            "a_{n}", "-", "2r", "+", 
            "a_{n}", "-", "r", "+", 
            "a_{n}", "+",
            
            font_size = 70)

        final[0].set_x(2), final[0].set_y(3.2)
        final[2].set_x(2), final[2].set_y(2.3)
        final[4:7].set_x(1.38), final[4:7].set_y(1.4)
        final[8:11].set_x(1.21), final[8:11].set_y(0.5)
        final[12].set_x(2), final[12].set_y(-0.4)
        final[14:17].set_x(1.58), final[14:17].set_y(-1.3)
        final[18:21].set_x(1.73), final[18:21].set_y(-2.2)
        final[22].set_x(2), final[22].set_y(-3.1)

        final[1].set_x(3.5), final[1].set_y(3.2)
        final[3].set_x(3.5), final[3].set_y(2.3)
        final[7].set_x(3.5), final[7].set_y(1.4)
        final[11].set_x(3.5), final[11].set_y(0.5)
        final[13].set_x(3.5), final[13].set_y(-0.4)
        final[17].set_x(3.5), final[17].set_y(-1.3)
        final[21].set_x(3.5), final[21].set_y(-2.2)
        final[23].set_x(3.5), final[23].set_y(-3.1)

        final2 = Tex(
            "S_{n}", "+", 
            "a_{n}", "+", 
            "a_{n}", "-", "r", "+", 
            "a_{n}", "-", "2r", "+", 
            "\dots", "+", 
            "a_{1}", "+", "2r", "+", 
            "a_{1}", "+", "r", "+", 
            "a_{1}", "+",
            
            font_size = 70)
        
        final2[0].set_color(BLUE)
        final2[2].set_color(BLUE)
        final2[4:7].set_color(BLUE)
        final2[8:11].set_color(BLUE)
        final2[12].set_color(BLUE)
        final2[14:17].set_color(BLUE)
        final2[18:21].set_color(BLUE)
        final2[22].set_color(BLUE)

        final2[1].set_color(WHITE)
        final2[3].set_color(WHITE)
        final2[7].set_color(WHITE)
        final2[11].set_color(WHITE)
        final2[13].set_color(WHITE)
        final2[17].set_color(WHITE)
        final2[21].set_color(WHITE)
        final2[23].set_color(WHITE)

        final2[0].set_x(5), final2[0].set_y(3.2)
        final2[2].set_x(5), final2[2].set_y(2.3)
        final2[4:7].set_x(5.26), final2[4:7].set_y(1.4)
        final2[8:11].set_x(5.43), final2[8:11].set_y(0.5)
        final2[12].set_x(5), final2[12].set_y(-0.4)
        final2[14:17].set_x(5.78), final2[14:17].set_y(-1.3)
        final2[18:21].set_x(5.62), final2[18:21].set_y(-2.2)
        final2[22].set_x(5), final2[22].set_y(-3.1)

        final2[1].set_x(3.5), final2[1].set_y(3.2)
        final2[3].set_x(3.5), final2[3].set_y(2.3)
        final2[7].set_x(3.5), final2[7].set_y(1.4)
        final2[11].set_x(3.5), final2[11].set_y(0.5)
        final2[13].set_x(3.5), final2[13].set_y(-0.4)
        final2[17].set_x(3.5), final2[17].set_y(-1.3)
        final2[21].set_x(3.5), final2[21].set_y(-2.2)
        final2[23].set_x(3.5), final2[23].set_y(-3.1)

        retangulo8 = Rectangle(
            height = 7.5, width = 7, color = "#333333", fill_opacity = 1)
        retangulo8.set_x(3.5),  retangulo8.set_y(0)

        grupofinal = VGroup(final, final2)
      
        self.play(
            FadeIn(retangulo8),
            FadeOut(final2[1]),
            FadeOut(final2[3]),
            FadeOut(final2[7]),
            FadeOut(final2[11]),
            FadeOut(final2[13]),
            FadeOut(final2[17]),
            FadeOut(final2[21]),
            FadeOut(final2[23]),
            grupofinal.shift, 4 * LEFT)

        ultimo = Tex(
            "2S_n", 
            "(", "a_1", "+", "a_n", ")", 
            "(", "a_1", "+", "a_n", ")",
            "(", "a_1", "+", "a_n", ")",
            "\dots", 
            "(", "a_n", "+", "a_1", ")",
            "(", "a_n", "+", "a_1", ")",
            "(", "a_n", "+", "a_1", ")",
            color = TEAL,
            font_size = 70)

        ultimo[0].set_x(-0.5), ultimo[0].set_y(3.2)
        ultimo[1:6].set_x(-0.5), ultimo[1:6].set_y(2.3)
        ultimo[6:11].set_x(-0.5), ultimo[6:11].set_y(1.4)
        ultimo[11:16].set_x(-0.5), ultimo[11:16].set_y(0.5)
        ultimo[16].set_x(-0.5), ultimo[16].set_y(-0.4)
        ultimo[17:22].set_x(-0.5), ultimo[17:222].set_y(-1.3)
        ultimo[22:27].set_x(-0.5), ultimo[22:27].set_y(-2.2)
        ultimo[27:32].set_x(-0.5), ultimo[27:32].set_y(-3.1)

        self.play(
        final[0].shift, 1.5 * RIGHT,
        final2[0].shift, -1.5 * RIGHT)

        self.play(
        FadeOut(final[0]),
        FadeOut(final2[0]),
        Transform(final[1], ultimo[0]))

        self.play(
        final[2].shift, 1.5 * RIGHT,
        final2[2].shift, -1.5 * RIGHT)

        self.play(
        FadeOut(final[2]), 
        FadeOut(final2[2]),
        Transform(final[3], ultimo[1:6]))
        
        self.play(
        final[4:7].shift, 2 * RIGHT,
        final2[4:7].shift, -2 * RIGHT)

        self.play(
        FadeOut(final[4:7]), 
        FadeOut(final2[4:7]),
        Transform(final[7], ultimo[6:11]))

        self.play(
        final[8:11].shift, 2.2 * RIGHT,
        final2[8:11].shift, -2 * RIGHT)

        self.play(
        FadeOut(final[8:11]), 
        FadeOut(final2[8:11]),
        Transform(final[11], ultimo[11:16]))

        self.play(
        final[12].shift, 1.5 * RIGHT,
        final2[12].shift, -1.5 * RIGHT)

        self.play(
        FadeOut(final[12]), 
        FadeOut(final2[12]),
        Transform(final[13], ultimo[16]))

        self.play(
        final[14:17].shift, 2 * RIGHT,
        final2[14:17].shift, -2.2 * RIGHT)

        self.play(
        FadeOut(final[14:17]), 
        FadeOut(final2[14:17]),
        Transform(final[17], ultimo[17:22]))

        self.play(
        final[18:21].shift, 1.5 * RIGHT,
        final2[18:21].shift, -2.4 * RIGHT)

        self.play(
        FadeOut(final[18:21]), 
        FadeOut(final2[18:21]),
        Transform(final[21], ultimo[22:27]))

        self.play(
        final[22].shift, 1.5 * RIGHT,
        final2[22].shift, -1.5 * RIGHT)

        self.play(
        FadeOut(final[22]), 
        FadeOut(final2[22]),
        Transform(final[23], ultimo[27:32]))

        grup = VGroup(
            final[1],final[3],final[7],final[11],final[13],final[17],final[21],final[23])

        equacao_final = Tex(
            "2S_n", "=", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "\dots",
            "+", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "(a_1+a_n)", font_size = 25)

        equacao_final2 = Tex(
            "2S_n", "=", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "\dots", "+",
            "(a_1+a_n)", "+", "(a_1+a_n)", font_size = 40)

        equacao_final3 = Tex(
            "2S_n", "=", "(a_1+a_n)", "+", "\dots", "+"
            "(a_1+a_n)", font_size = 80)
        
        equacao_final4 = Tex(
            "2", "S_n", "=", "(a_1+a_n)n", font_size = 100)
        
        equacao_final5 = Tex(
            "S_n=\\frac{(a_1+a_n)}{2}", font_size = 120)

        self.play(
            TransformMatchingTex(grup, equacao_final,
            path_arc = -90 * DEGREES))

        self.wait()

        self.play(
            TransformMatchingTex(equacao_final,equacao_final2))

        self.wait()

        self.play(
            TransformMatchingTex(equacao_final2,equacao_final3))

        self.wait()

        self.play(
            TransformMatchingTex(equacao_final3,equacao_final4))

        self.wait()

        self.play(
            TransformMatchingTex(equacao_final4,equacao_final5))

        self.wait(2)

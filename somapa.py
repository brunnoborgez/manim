from manimlib import *

class ProgressaoAritimetica(Scene):
    def construct(self):
        retangulo = Rectangle(height = 3, width = 10)
        titulo1 = TexText("Um vídeo criado com", font_size = 100)
        titulo2 = TexText("Manim", font_size = 300)
        titulo1.next_to(titulo2, 3.5 * UP)
        titulo3 = TexText("Progressão Aritmética", color = TEAL, font_size = 120)
        
        self.play(
            Write(titulo1), 
            Write(titulo2), run_time = 5)
        
        self.play(ShowCreation(retangulo), run_time = 2)
        
        self.wait()
        
        self.play(
            FadeOut(titulo2), 
            Uncreate(retangulo),
            FadeTransform(titulo1, titulo3))
        
        self.wait()
        
        self.play(FadeOut(titulo3))
        
        linhas = VGroup(
            Tex("(", "\ a_1", ",", "\ a_2", ",", "\ a_3", ",", "\ a_4", ",", "\ \dots", ",", "\ a_{n-3}", ",", "\ a_{n-2}", ",", "\ a_{n-1}", ",", "\ a_{n}", "\ )", font_size = 65), 
           
            Tex("\ a_1", "\ a_2", "\ a_3", "\ a_4", "\ \dots", "\ a_{n-3}", "\ a_{n-2}", "\ a_{n-1}", "\ a_{n}", font_size = 65))
        
        linhas[1][0].set_x(-5), linhas[1][0].set_y(3.2)  # a_1
        linhas[1][1].set_x(-5), linhas[1][1].set_y(2.4)  # a_2
        linhas[1][2].set_x(-5), linhas[1][2].set_y(1.6)  # a_3
        linhas[1][3].set_x(-5), linhas[1][3].set_y(0.8)  # a_4
        linhas[1][4].set_x(-5), linhas[1][4].set_y(0)  # reticencias
        linhas[1][5].set_x(-5), linhas[1][5].set_y(-0.8)  # a_(n-3)
        linhas[1][6].set_x(-5), linhas[1][6].set_y(-1.6)  # a_(n-2)
        linhas[1][7].set_x(-5), linhas[1][7].set_y(-2.4)  # a_(n-1)
        linhas[1][8].set_x(-5), linhas[1][8].set_y(-3.2)  # a_n
        
        self.wait()
        
        self.play(Write(linhas[0].center()), run_time = 5)
        self.play(FadeOut(linhas[0][0:19:2]))
        self.play(TransformMatchingTex(linhas[0][1:18:2], linhas[1], path_arc = -45 * DEGREES))
        self.play(linhas[1][4].animate.rotate(-1.6), font_size = 60)
        
        nomes = VGroup(
            Tex("=", "primeiro \ termo", "=", "segundo \ termo", "=", "terceiro \ termo", "=", "quarto \ termo", "=", "(n-3)-\\acute{e}simo \ termo", "=", "(n-2)-\\acute{e}simo \ termo", "=", "(n-1)-\\acute{e}simo \ termo", "=", "n-\\acute{e}simo \ termo", font_size = 60), 
            
            Tex("a_1", "a_1", "+", "r", "a_2", "+", "r", "a_3", "+", "r", "a_1", "+",  "(n-4)r", "a_1", "+", "(n-3)r", "a_1", "+", "(n-2)r", "a_1", "+", "(n-1)r", font_size = 65))
       
        nomes[0][0:2].next_to(linhas[1][0], RIGHT)  # = primeiro termo
        nomes[0][2:4].next_to(linhas[1][1], RIGHT)  # = segundo termo
        nomes[0][4:6].next_to(linhas[1][2], RIGHT)  # = terceiro termo
        nomes[0][6:8].next_to(linhas[1][3], RIGHT)  # = quarto termo
        nomes[0][8:10].next_to(linhas[1][5], RIGHT)  # = (n-3) ésimo termo
        nomes[0][10:12].next_to(linhas[1][6], RIGHT)  # = (n-2) ésimo termo
        nomes[0][12:14].next_to(linhas[1][7], RIGHT)  # = (n-1) ésimo termo
        nomes[0][14:16].next_to(linhas[1][8], RIGHT)  # = ésimo termo
        
        self.play(Write(nomes[0][0:16]), run_time = 8)
       
        nomes[1][0].next_to(nomes[0][0], RIGHT)  # a_1*
        nomes[1][1:4].next_to(nomes[0][2], RIGHT)  # a_1+r
        nomes[1][4:7].next_to(nomes[0][4], RIGHT)  # a_2+r
        nomes[1][7:10].next_to(nomes[0][6], RIGHT)  # a_3+r
        nomes[1][10:13].next_to(nomes[0][8], RIGHT)  # a_1+(n-4)+r
        nomes[1][13:16].next_to(nomes[0][10], RIGHT)  # a_1+(n-3)+r
        nomes[1][16:19].next_to(nomes[0][12], RIGHT)  # a_1+(n-2)+r
        nomes[1][19:22].next_to(nomes[0][14], RIGHT)  # a_1+(n-1)+r
        
        self.play(Transform(nomes[0][1], nomes[1][0]))
        self.play(Transform(nomes[0][3], nomes[1][1:4]))
        self.play(Transform(nomes[0][5], nomes[1][4:7]))
        self.play(Transform(nomes[0][7], nomes[1][7:10]))
        
        copia_linhas = Tex("a_1", "+", "r", "a_1", "+", "r", "+", "r", font_size = 65)
        copia_linhas[0:3].next_to(nomes[0][2], RIGHT)
        copia_linhas[3:8].next_to(nomes[0][4], RIGHT)
        nomes_copia_a_2 = Tex("2r", "3r", font_size = 65)
        nomes_copia_a_2[0].next_to(nomes[1][5], RIGHT)
        nomes_copia_a_2[1].next_to(nomes[1][8], RIGHT)
        
        self.play(FadeOut(nomes[0][5]), copia_linhas[0:3].animate.move_to(nomes[0][5]), nomes[1][5:7].shift, 1.1 * RIGHT)
        
        self.wait()

        self.play(FadeOut(nomes[0][7]), copia_linhas[3:8].shift, 0.725 * DOWN, nomes[1][8:10].shift, 2.2 * RIGHT)
        self.play(nomes[1][5:7].shift, 1.1 * LEFT)
        
        self.play(
            FadeOut(nomes[1][5:6]), 
            FadeOut(copia_linhas[2]), 
            Transform(nomes[1][6], nomes_copia_a_2[0]))
        
        self.wait()

        self.play(nomes[1][8:10].shift, 2.2 * LEFT, copia_linhas[6:8].shift, 1.1 * LEFT)
        
        self.play(
            FadeOut(nomes[1][8:10]), 
            FadeOut(copia_linhas[6:8]), 
            Transform(copia_linhas[5], nomes_copia_a_2[1]))
        
        self.wait()

        self.play(Transform(nomes[0][9], nomes[1][10:13]))
        self.play(Transform(nomes[0][11], nomes[1][13:16]))
        self.play(Transform(nomes[0][13], nomes[1][16:19]))
        self.play(Transform(nomes[0][15], nomes[1][19:22]))
        self.wait(2)
        
        termo_geral = Tex("a_n", "=", "a_1", "+", "(n-1)r",color = YELLOW, font_size = 120)
        termo_geral_texto = TexText("Termo Geral", font_size = 150)
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
        
        self.play(Write(termo_geral_texto))
       
        self.wait()
        
        self.play(
            FadeOut(termo_geral_texto), 
            FadeOut(termo_geral))

        self.wait()

        # aqui começa o video da soma

        titulo1 = TexText("Soma dos $n$ termos de uma", tex_to_color_map = {"$n$": YELLOW}, font_size = 100)
        titulo2 = TexText("Progressão Aritmética", font_size = 120)
        titulo1.set_y(2)
        titulo2.next_to(titulo1, 2 * DOWN)

        linha1 = VGroup(
            Tex("S_n", "=", "a_1", "+", "a_2", "+", "a_3", "+", "\cdots", "+", "a_{n-2}", "+", "a_{n-1}", "+", "a_n", font_size = 65),
        
            Tex("S_n", "=", "a_1", "+", "(a_1+r)", "+", "(a_1+2r)", "+", "\cdots", "+", "(a_n-2r)", "+", "(a_n-r)", "+", "a_n"))
       
        linha1[0].set_y(2.25)
        linha1[1].next_to(linha1[0], DOWN, buff = LARGE_BUFF)

        numeros_crescente = Tex(
            "S_{n}", "=", "1", "+", "2", "+", "3", "+", "\dots", "+", "98", "+", "99", "+", "100", font_size = 65)     
        numeros_crescente.next_to(linha1[0], 2 * UP)

        retangulo1 = Rectangle(height = 1,width = 13, color = YELLOW)
        retangulo1.set_y(2.25)
 
        retangulo2 = Rectangle(height = 1,width = 11, color = YELLOW)
        retangulo2.set_y(3.35)

        retangulo3 = Rectangle(height = 1.2,width = 12, color = "#333333", fill_opacity = 1)
        retangulo3.set_y(3.35)

        linha2 = Tex("S_n","=","a_n", "+", "(a_n-r)", "+", "(a_n-2r)", "+", "\cdots","+","(a_1+2r)","+","(a_1+r)","+","a_1", color = BLUE)
        linha2.next_to(linha1[1], DOWN, buff = LARGE_BUFF)

        retangulo4 = Rectangle(height = 1,width = 13.8, color = YELLOW)
        retangulo4.set_y(0.75)

        retangulo5 = Rectangle(height = 1,width = 13.8, color = YELLOW)
        retangulo5.set_y(-0.75)

        linha3 = Tex("2S_n", "=", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "(a_1+a_n)", "+", "\cdots","+","(a_1+a_n)","+","(a_1+a_n)","+","(a_1+a_n)", font_size = 38, color = TEAL)
        linha3.next_to(linha2, DOWN, buff = LARGE_BUFF)

        retangulo6 = Rectangle(height = 4, width = 13.5, color = "#333333", fill_opacity = 1)
        retangulo6.set_y(1)

        retangulo7 = Rectangle(height = 1,width = 13.5, color = "#333333", fill_opacity = 1)
        retangulo7.set_y(-2)

        final = Tex("2","S_n=", font_size = 100, color = TEAL)
        final.set_y(0.7), final.set_x(-2.7)

        final2 = Tex("(a_1+a_n)n", font_size = 100, color = TEAL)
        final2.set_y(1), final2.set_x(1.5)

        final3 = Tex("2", font_size = 100, color = TEAL)
        final3.set_x(1.2), final3.set_y(-0.4)

        retangulo8 = Rectangle(height = 0.01,width =  4.5, color = TEAL)
        retangulo8.set_x(1.4),retangulo8.set_y(0.3)

        retangulo9 = Rectangle(height = 1.5, width = 2, color = "#333333", fill_opacity = 1)
        retangulo9.set_x(-4.6), retangulo9.set_y(1)

        self.play( # escreve na tela o Titulo 'Soma dos n termos de uma PA'.
            Write(titulo1),
            Write(titulo2), run_time = 5)

        self.play(FadeToColor(titulo2, color = YELLOW))

        self.wait(1) # espera.

        self.play( # apaga o titulo, com efeito indo para cima e para baixo.
            FadeOut(titulo1, UP), 
            FadeOut(titulo2, DOWN))

        self.play(Write(linha1[0])) # escreve os termos de a1 até an, se somando.

        self.wait() # espera.

        self.play( # aparece um retangulo amarelo em volta dos termos.
            ShowCreation(retangulo1))

        self.wait() # espera.

        self.play( # faz o retangulo anterior se movimentar para cima.
            Transform(retangulo1, retangulo2), 
            FadeIn(numeros_crescente)) # faz aparecer uma sequencia de numeros de 1 a 100 se somando, para efeito de exemplo.
        
        self.wait() # espera.

        self.play( # muda a cor dos termos e dos numeros para verde, mostrando que sao iguais.
            FadeToColor(linha1[0][2:15], color = GREEN_SCREEN), 
            FadeToColor(numeros_crescente[2:15], color = GREEN_SCREEN))
        
        self.wait() # espera.

        self.play( # Faz aparecer um retangulo para encobrir a sequencia de numeros, pois nao consegui apagar.
            FadeIn(retangulo3), # retangulo na cor do fundo da tela, usado para encobrir os numeros e o retangulo amarelo em volta deles.
            FadeToColor(linha1[0][2:15], color = WHITE) ) # muda a cor dos termos para branco novamente.
        
        self.wait() # espera.

        self.play( # desce 'Sn='.
            Transform(linha1[0][0:2].copy(), linha1[1][0:2]))
        self.play( # desce o 'a1'.
            Transform(linha1[0][2:4].copy(),linha1[1][2:4]))
        self.play( # reescreve o termo 'a2' em funcao do 'a1'.
            Transform(linha1[0][4:6].copy(),linha1[1][4:6]))
        self.play( # reescreve o termo 'a3' em funcao do 'a1', desce '+...+'.
            Transform(linha1[0][6:10].copy(),linha1[1][6:10]))
        self.play( # reescreve o termo 'an-2' em funcao do 'an.
            Transform(linha1[0][10:12].copy(),linha1[1][10:12]))
        self.play( # reescreve o termo 'an-1' em funcao do 'an'.
            Transform(linha1[0][12:14].copy(),linha1[1][12:14]))
        self.play(  # desce o 'an'.
            Transform(linha1[0][14].copy(),linha1[1][14]))
        self.play(Write(linha2))

        self.wait() # espera.

        self.play(ShowCreation(retangulo4)) # faz aparecer um retangulo em volta da sequencia crescente.

        self.wait() # espera.
        
        self.play(ShowCreation(retangulo5))  # faz aparecer um retangulo em volta da sequencia decrescente.

        self.wait() # espera.

        self.play( # apaga os dois retangulos.
            Uncreate(retangulo4), 
            Uncreate(retangulo5))

        self.wait() # espera.

        self.play( # faz a soma das duas sequencias: crescente e decrecente.
            Transform(linha1[1][0:2].copy(), linha3[0:2]), 
            Transform(linha2[0:2].copy(), linha3[0:2]))
        self.play( # faz a soma de 'a1' com 'an'.
            Transform(linha1[1][2:4].copy(), linha3[2:4]), 
            Transform(linha2[2:4].copy(), linha3[2:4]))
        self.play( # faz a soma de 'a2' com 'an-1'.
            Transform(linha1[1][4:6].copy(), linha3[4:6]), 
            Transform(linha2[4:6].copy(), linha3[4:6]))
        self.play( # faz a soma de 'a3' com 'an-1', '+...+ com '+...+'.
            Transform(linha1[1][6:10].copy(), linha3[6:10]), 
            Transform(linha2[6:10].copy(), linha3[6:10]))
        self.play( # faz a soma de dos ultimos tres termos de cada uma das sequencias.
            Transform(linha1[1][10:16].copy(), linha3[10:16]))

        self.play(FadeIn(retangulo6)) # faz aparecer um retangulo na cor do fundo que encobre as linhas superiores.
        self.play( # transforma a linha da soma na formula da soma.
            Transform(linha3[0:2].copy(), final[0:2]),  
            Transform(linha3[4:13:8].copy(), final2), 
            FadeIn(retangulo7)) # retangulo na cor do fundo que encobre a sequencia somada.
        
        self.wait() # espera.

        self.play( # cria um retangulo para fazer a barra da divisao .
            ShowCreation(retangulo8), # barra da divisao.
            FadeIn(retangulo9),  # retangulo na cor do fundo que encobre o numero '2' do '2Sn'.
            Transform(final[0], final3, path_arc = 90 * DEGREES)) # faz o movimento do '2' para baixo da fracao.

        self.wait(2) # espera.

        # finalizadooo

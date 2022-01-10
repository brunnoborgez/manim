from manim import *

movimento = np.array([-1,0,0]) #define a posição de movimento.

class Soma(Scene):
    
    def construct(self):
        
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

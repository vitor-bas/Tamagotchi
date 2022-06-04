import random 

class Pet:
    sede_max = 10
    sede_start = 5
    sede_warning = 4
    fome_max = 10
    fome_start = 5
    fome_warning = 4
    animacao_max = 10
    animacao_start = 8
    animacao_warning = 4
    
    def __init__(self,nome):
        self.nome = nome
        self.fome = self.fome_start
        self.sede = self.sede_start
        self.animacao = self.animacao_start
    
    def _passar_tempo(self):
        self.fome -= 1
        self.sede -= 1
        self.animacao -= 1
    
    @property
    def mood(self):
        if self.fome > self.fome_warning and self.sede > self.sede_warning:
            return  "Feliz        (۶•̀ᴗ•́)۶"
        
        elif self.fome < self.fome_warning:
            return "Fomeee        (╯︵╰,)"
        
        elif self.sede < self.sede_warning:
            return "Sede        彡(-_-;)彡"
        
        elif self.animacao < self.animacao_warning:
            return "Entediado        (＿ー＿）"
        
    def __str__(self):
        return "\nMeu nome é " + self.nome + "." + "Meu estado atual é " + self.mood()
    
    
    def alimentar(self):
        print("Isso é bom         ( ˘▽˘)っ♨  ( ˘▽˘)っ♨")
        meal = random.randrange(1, 4)
        self.fome = self.fome + meal
        if self.fome <= self.fome_warning:
            print("Ainda estou FAMINTO        (￣﹃￣)")
        elif self.fome >= self.fome_max:
            print("Estou cheio        (￣ー￣)")
        self._passar_tempo()
        
    def dar_agua(self):
        print("Glub Glub Glub        ( °⌓°) \_\  ( °⌓°) \_\ ")
        copo_de_agua = random.randrange(1, 4)
        self.sede = self.sede + copo_de_agua
        if self.sede <= self.sede_warning:
            print("Ainda estou com sedizinhaaa!        (￣﹃￣)")
        elif self.sede >= self.sede_max:
            print("Barriguinha cheia de água        (￣ー￣)")
        self._passar_tempo()
            
    def brincar(self):
        print("Ihuuuuuuuuuuu        ٩(º ౪ º๑)۶  ٩(º ౪ º๑)۶ ")
        brincadeira = random.randrange(1, 4)
        self.animacao = self.animacao + brincadeira
        if self.animacao <= self.animacao_warning:
            print("Estou ENTEDIADOOO        （＿ー＿）")
        elif self.animacao >= self.animacao_max:
            print("Cansei de brincaaar!        ( ᴗ˳ᴗ)")
        self._passar_tempo()
            
            
def main():
    nome = input("Qual o nome do seu Tamagotchi: ")
    
    tamagotchi = Pet(nome)
    
    print("\nOie (ᵔ∀ᵔ)ﾉ ᴴᴵ  (ᵔ∀ᵔ)ﾉ ᴴᴵ (ᵔ∀ᵔ)ﾉ ᴴᴵ\nMeu nome é " + tamagotchi.nome +"." + " Pode cuidar de mim?\n")
    
    escolha = None
    
    while escolha != 0:
        print(
            '''
            *** Escolha sua ação ***
            
            1 - Alimentar seu tamagotchi
            2 - Dar água para seu tamagotchi
            3 - Brincaaaaarrr!!!
            0 - Sair
            '''
        )
        
        escolha = input("Opção: ")
        
        if escolha == "0":
            print ("Tchau Tchau (╯︵╰,) (╯︵╰,) (╯︵╰,) (╯︵╰,)")
        elif escolha == "1":
            tamagotchi.alimentar()
        elif escolha == "2":
            tamagotchi.dar_agua()
        elif escolha == "3":
            tamagotchi.brincar()
        else:
            print("Escolha inválida!!")    
        
main()
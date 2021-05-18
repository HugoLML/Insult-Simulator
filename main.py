#Importation des modules et des classes
import pygame
pygame.init()

import random

from player import Player
from insult import Insult
from sentence import Sentence

from gtts import gTTS
language = 'fr'

import os

#Affichage de la fenêtre
Screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('The Insult Simulator')

#Création des fonts
TitleFont = pygame.font.SysFont('Impact', 50)
TextFont = pygame.font.SysFont('Impact', 25)
LittleTextFont = pygame.font.SysFont('Impact', 15)
DescriptionFont = pygame.font.SysFont('Arial', 11)
SentenceFont = pygame.font.SysFont('Arial', 12)

#Chargement des images
IntelligentMan = pygame.image.load('Ressources/IntelligentMan.png')
MuscularMan = pygame.image.load('Ressources/MuscularMan.png')
OldMan = pygame.image.load('Ressources/OldMan.png')
YoungMan = pygame.image.load('Ressources/YoungMan.png')
Bubble = pygame.image.load('Ressources/Bulle.png')
BubbleFlipped = pygame.image.load('Ressources/BulleFlip.png')
BlueCheck = pygame.image.load('Ressources/BlueCheck.png')
RedCheck = pygame.image.load('Ressources/RedCheck.png')
RestartIcon = pygame.image.load('Ressources/Restart.png')

#Redimensionnement des images
ImageWidth = 100
ImageHeight = 125

BubbleWidth = 300
BubbleHeight = 233

CheckWidth = 45
CheckHeight = 45

RestartWidth = 50
RestartHeight = 50

IntelligentManResized = pygame.transform.smoothscale(IntelligentMan, (ImageWidth, ImageHeight))
MuscularManResized = pygame.transform.smoothscale(MuscularMan, (ImageWidth, ImageHeight))
OldManResized = pygame.transform.smoothscale(OldMan, (ImageWidth, ImageHeight))
YoungManResized = pygame.transform.smoothscale(YoungMan, (ImageWidth, ImageHeight))

BubbleResized = pygame.transform.smoothscale(Bubble, (BubbleWidth,BubbleHeight))
BubbleFlippedResized = pygame.transform.smoothscale(BubbleFlipped, (BubbleWidth,BubbleHeight))

BlueCheckResized = pygame.transform.smoothscale(BlueCheck, (CheckWidth,CheckHeight))
RedCheckResized = pygame.transform.smoothscale(RedCheck, (CheckWidth,CheckHeight))

RestartIconResized = pygame.transform.smoothscale(RestartIcon, (RestartWidth,RestartHeight))

#Boucle Menu
def Menu():    
    
    #Ma boucle de vérification des événements
    MenuRunning = True
    while MenuRunning:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                MenuRunning = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Character()
        
        #Remplissage du Screen
        Screen.fill('white')    
        MenuTitle = TitleFont.render('THE INSULT SIMULATOR', True, (255,255,255))
        MenuTitlePos = MenuTitle.get_rect(center=(800/2, 250))
        PlayText = TitleFont.render('Press return to play', True, (0,0,0))
        PlayTextPos = PlayText.get_rect(center=(800/2, 350))

        pygame.draw.rect(Screen, 'black', (MenuTitlePos.x-50,MenuTitlePos.y,MenuTitle.get_width()+100,MenuTitle.get_height()))
        Screen.blit(MenuTitle, MenuTitlePos)
        Screen.blit(PlayText, PlayTextPos)

        pygame.display.flip()
    
    pygame.quit()

#Boucle Character
def Character():    
    
    #Création des personnages
    P1 = Player('IntelligentMan', ["IntelligentMan est quelqu'un de", "très intélligent (sans blague).", "Il manie les mots à sa guise et", "est redoutable dans un duel", "d'insultes. Ne lui parlez surtout", "pas de son monocle, il l'aime", "particulièrement."], 'Faiblesse : Monocle', IntelligentManResized)
    P2 = Player('MuscularMan', ["MuscularMan est quelqu'un de", "très musclé (ça devient lourd).", "Il est doté d'une force incroyable", "et il ne vaut mieux pas que", "le clash verbal devienne physique", "avec lui... Insultez sa moustache", "et vous le regretterez rapidement."], 'Faiblesse : Moustache', MuscularManResized)
    P3 = Player('OldMan', ["OldMan est quelqu'un de", "très vieux (vraiment lourd). Il a", "vécu assez longtemps pour", "s'assagir et rester calme même", "lors des clashs les plus virulents.", "Par contre, osez lui", "parler de sa calvitie,", "et vous connaîterez sa colère."], 'Faiblesse : Calvitie', OldManResized)
    P4 = Player('YoungMan', ["YoungMan est quelqu'un de", "très jeune (...). Il est dans", "la fleur de l'âge et ses", "punchlines sont incisives,", "à l'image de son style", "tendance. Si vous souhaitez", "l'énverver, critiquez ses", "lunettes et vous verrez", "par vous même."], 'Faiblesse : Lunettes', YoungManResized)
    PlayerList = [P1, P2, P3, P4]
    
    #On rend les images "cliquables" avec get_rect()
    P1Rect = pygame.Rect(50,100,ImageWidth,ImageHeight)
    P2Rect = pygame.Rect(250,100,ImageWidth,ImageHeight)
    P3Rect = pygame.Rect(450,100,ImageWidth,ImageHeight)
    P4Rect = pygame.Rect(650,100,ImageWidth,ImageHeight)
    
    RectList = [P1Rect, P2Rect, P3Rect, P4Rect]
    
    #Ma boucle de vérification des événements
    CharacterRunning = True
    while CharacterRunning:

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                CharacterRunning = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Menu()

            if event.type == pygame.MOUSEBUTTONDOWN:
                Position = pygame.mouse.get_pos()
                
                i = 0
                while i < len(RectList):
                    
                    if RectList[i].collidepoint(Position):
                        
                        if P1.status == False and P2.status == False and P3.status == False and P4.status == False:
                            if PlayerList[i].status == False:    
                                PlayerList[i].status = True
                                global Joueur1
                                Joueur1 = PlayerList[i]
                                print('Le joueur n°1 a séléctionné :', PlayerList[i].name)
                            else:
                                print('Ce perso a déjà été séléctionné')
                        
                        else:
                            if PlayerList[i].status == False:    
                                PlayerList[i].status = True
                                global Joueur2
                                Joueur2 = PlayerList[i]
                                print('Le joueur n°2 a séléctionné :', PlayerList[i].name)
                                Game()
                            else:
                                print('Ce perso a déjà été séléctionné')
                    i+=1

        #Remplissage du screen
        Screen.fill('white')
            
        CharacterTitle = TitleFont.render('Choose your character', True, (0,0,0))
        CharacterTitlePos = CharacterTitle.get_rect(midtop =(800/2, 0))
        
        NameP1 = TextFont.render(P1.name, True, (0,0,0))
        NameP2 = TextFont.render(P2.name, True, (0,0,0))
        NameP3 = TextFont.render(P3.name, True, (0,0,0))
        NameP4 = TextFont.render(P4.name, True, (0,0,0))

        WeaknessP1 = LittleTextFont.render(P1.weakness, True, (0,0,0))
        WeaknessP2 = LittleTextFont.render(P2.weakness, True, (0,0,0))
        WeaknessP3 = LittleTextFont.render(P3.weakness, True, (0,0,0))
        WeaknessP4 = LittleTextFont.render(P4.weakness, True, (0,0,0))

        Screen.blit(CharacterTitle, CharacterTitlePos)
        
        Screen.blit(IntelligentManResized, (50,100))
        Screen.blit(MuscularManResized, (250,100))
        Screen.blit(OldManResized, (450,100))
        Screen.blit(YoungManResized, (650,100))
        
        Screen.blit(NameP1, ((50-20),250))
        Screen.blit(NameP2, ((250-17.5),250))
        Screen.blit(NameP3, ((450+12),250))
        Screen.blit(NameP4, ((650-5),250))

        Screen.blit(WeaknessP1, ((50-20),450))
        Screen.blit(WeaknessP2, ((250-17.5),450))
        Screen.blit(WeaknessP3, ((450+12),450))
        Screen.blit(WeaknessP4, ((650-5),450))

        def LineBreak(DescriptionList, XCoord, YCoord):
            LineDictionary = {}
            i = 0
            while i < len(DescriptionList):
                LineDictionary["Line%s" %i] = DescriptionFont.render(DescriptionList[i], True, (0,0,0))
                Screen.blit(LineDictionary["Line%s" %i], (XCoord, YCoord))
                YCoord += 15
                i += 1

        LineBreak(P1.description, (50-20), 300)
        LineBreak(P2.description, (250-17.5), 300)
        LineBreak(P3.description, (450+12), 300)
        LineBreak(P4.description, (650-5), 300)

        pygame.display.flip()
    
    pygame.quit()

#Boucle Game
def Game():
    
    #Création des insultes
    Insult1 = Insult('Sujet', 'Ton monocle', ['NM'])
    Insult2 = Insult('Sujet', 'Ta moustache', ['NF'])
    Insult3 = Insult('Sujet', 'Ta calvitie', ['NF'])
    Insult4 = Insult('Sujet', 'Tes lunettes', ['NF', 'Pluriel'])
    Insult5 = Insult('Sujet', 'Ta tête', ['NF'])
    Insult6 = Insult('Sujet', 'Ton corps', ['NM'])
    Insult7 = Insult('Sujet', 'Ton cerveau', ['NM'])
    Insult8 = Insult('Sujet', 'Ta maison', ['NF'])
    Insult9 = Insult('Sujet', 'Tes vêtements', ['NM', 'Pluriel'])
    Insult10 = Insult('Sujet', 'Tu', ['2PS'])
    Insult11 = Insult('Verbe', 'Être', ['Es', 'est', 'Sont'], 'Être')
    Insult12 = Insult('Verbe', 'Ressembler à', ['Ressembles à', 'Ressemble à', 'Ressemblent à'], 'Ressembler à')
    Insult13 = Insult('Verbe', 'Servir à', ['Sers à', 'Sert à', 'Servent à'], 'Servir à')
    Insult14 = Insult('Verbe', "Avoir l'air", ["As l'air", "A l'air", "Ont l'air"], "Avoir l'air")
    Insult15 = Insult('Verbe', 'Avoir', ['As', 'A', 'Ont'], 'Avoir')
    Insult16 = Insult('Complément', 'Moche', ['Moches'], 'Moche')
    Insult17 = Insult('Complément', 'Ignoble', ['Ignobles'], 'Ignoble')
    Insult18 = Insult('Complément', 'À vomir', [])
    Insult19 = Insult('Complément', 'Rien', [])
    Insult20 = Insult('Complément', 'Aucun sens', [])
    Insult21 = Insult('Liaison', 'Et', [])
    Insult22 = Insult('Liaison', 'Ainsi que', [])
    Insult23 = Insult('Liaison', 'Avec', [])
    Insult24 = Insult('Exclamation', "Et c'est tout ce que j'ai à dire !", [])
    Insult25 = Insult('Exclamation', 'Drop the mic', [])
    Insult26 = Insult('Exclamation', '!!!', [])
    
    InsultList = [Insult1, Insult2, Insult3, Insult4, Insult5,
    Insult6, Insult7, Insult8, Insult9, Insult10,
    Insult11, Insult12, Insult13, Insult14, Insult15,
    Insult16, Insult17, Insult18, Insult19, Insult20,
    Insult21, Insult22, Insult23, Insult24, Insult25,
    Insult26]
    
    SubjectList = []
    i = 0
    while i < len(InsultList):    
        if InsultList[i].category == 'Sujet':
            SubjectList.append(InsultList[i])
        i += 1
    
    VerbList = []
    i = 0
    while i < len(InsultList):    
        if InsultList[i].category == 'Verbe':
            VerbList.append(InsultList[i])
        i += 1
    
    ComplementList = []
    i = 0
    while i < len(InsultList):    
        if InsultList[i].category == 'Complément':
            ComplementList.append(InsultList[i])
        i += 1
    
    LiaisonList = []
    i = 0
    while i < len(InsultList):    
        if InsultList[i].category == 'Liaison':
            LiaisonList.append(InsultList[i])
        i += 1
    
    ExclamationList = []
    i = 0
    while i < len(InsultList):    
        if InsultList[i].category == 'Exclamation':
            ExclamationList.append(InsultList[i])
        i += 1

    #Tirage au sort des insultes
    RandomList = []
    
    def DrawInsult(): 
        RandomSubjects = random.sample(SubjectList, k=2)
        RandomVerbs = random.sample(VerbList, k=2)
        RandomComplements = random.sample(ComplementList, k=2)
        RandomLiaisons = random.sample(LiaisonList, k=2)
        RandomExclamations = random.sample(ExclamationList, k=2)

        i = 0
        while i < 2:
            RandomList.append(RandomSubjects[i])
            RandomList.append(RandomVerbs[i])
            RandomList.append(RandomComplements[i])
            RandomList.append(RandomLiaisons[i])
            RandomList.append(RandomExclamations[i])
            i += 1
        random.shuffle(RandomList)
    
    DrawInsult()

    #Création des Rect pour rendre les rectangles "cliquables"
    Case1 = pygame.Rect(300,100,200,30)
    Case2 = pygame.Rect(300,140,200,30)
    Case3 = pygame.Rect(300,180,200,30)
    Case4 = pygame.Rect(300,220,200,30)
    Case5 = pygame.Rect(300,260,200,30)
    Case6 = pygame.Rect(300,300,200,30)
    Case7 = pygame.Rect(300,340,200,30)
    Case8 = pygame.Rect(300,380,200,30)
    Case9 = pygame.Rect(300,420,200,30)
    Case10 = pygame.Rect(300,460,200,30)

    CaseList = [Case1, Case2, Case3, Case4, Case5, Case6, Case7, Case8, Case9, Case10]

    ButtonRestart = pygame.Rect(375,525,50,50)
    
    ButtonJ1Validate = pygame.Rect(25,525,50,50)
    ButtonJ2Validate = pygame.Rect(725,525,50,50)
    
    #Création des dictionnaires pour stocker les 10 insultes tirées au sort
    TextDictionary = {} #Le dictionnaire qui contient les textes des insultes
    PosDictionary = {} #Le dictionnaire qui contient les positions des textes des insultes transformés en rectangle (get_rect)
    
    def FillRect():
        i = 0 #Le compteur qui va s'incrémenter au fur et à mesure
        Yvalue = 100 #La position en Y qui va aussi augmenter au fur et à mesure pr centrer les insultes sur les bons rectangles
        while i < 10: #Le %s en dessous permet de formater mon string et de créer des keys qui qui s'adaptent au i qui s'incrémente
            TextDictionary["TextKey%s" %i] = SentenceFont.render(RandomList[i].text, True, (255,255,255))
            PosDictionary["PosKey%s" %i] = TextDictionary["TextKey%s" %i].get_rect(center =((300 + (200/2)), Yvalue + (30/2)))
            Yvalue += 40
            i += 1
    
    FillRect()

    #Création des phrases
    SentenceJ1 = Sentence()
    SentenceJ2 = Sentence()
    Turn = 0 #Si Turn == Paire alors c'est au tour du J1, sinn c'est au J2

    #Création des barres de vie
    HPLengthJ1 = 200
    HPLengthJ2 = 200

    #Les joueurs ont ils validé leur phrase ?
    J1Validate = False
    J2Validate = False

    #Lecture des phrases
    J1NumberFiles = 1
    J2NumberFiles = 1

    #On accorde la phrase
    def Agreement(Sentence):
        i = 0
        while i < len(Sentence.insults): #Si il y a des pb sur ça c'est pcq tt n'est ps rempli encore là haut
            if Sentence.insults[0].category == 'Verbe': #Si la phrase commence par un verbe, on n'accorde pas, elle est fausse
                return
            elif Sentence.insults[i].category == 'Verbe' and Sentence.insults[i-1].category == 'Sujet' and Sentence.insults[i-1].agreement[0] == '2PS': #On accorde avec la 2e personne du singulier
                Sentence.insults[i].text = Sentence.insults[i].agreement[0]
            elif Sentence.insults[i].category == 'Verbe' and Sentence.insults[i-1].category == 'Sujet' and len(Sentence.insults[i-1].agreement) == 1 and Sentence.insults[i-1].agreement[0] != '2PS': #On accorde avec la 3e personne du singulier
                Sentence.insults[i].text = Sentence.insults[i].agreement[1]
            elif Sentence.insults[i].category == 'Verbe' and Sentence.insults[i-1].category == 'Sujet' and len(Sentence.insults[i-1].agreement) == 2: #On accorde avec la 3e personne du pluriel
                Sentence.insults[i].text = Sentence.insults[i].agreement[2]
            if Sentence.insults[i].category == 'Verbe' and Sentence.insults[i-1].category == 'Sujet' and i == 3: #On accorde avec la 3e personne du pluriel (cas où il y a deux sujets)
                Sentence.insults[i].text = Sentence.insults[i].agreement[2]
            
            if Sentence.insults[0].category == 'Complément': #Si la phrase commence par un complément, on n'accorde pas, elle est fausse
                return
            elif Sentence.insults[i].category == 'Complément' and Sentence.insults[i-1].category == 'Verbe' and Sentence.insults[i].agreement != [] and Sentence.insults[i-1].text == Sentence.insults[i-1].agreement[2]:
                Sentence.insults[i].text = Sentence.insults[i].agreement[0]

            i += 1
    
    #Vérification de la logique de la phrase
    def Validate(Sentence):
        
        DoubleExclamation = Sentence.content.count('Exclamation')
        Unvalidated = "Votre phrase semble incorrecte"
        Check = 'Check'

        if len(Sentence.content) <= 2:
            print(Unvalidated)
            Check = 'Unchecked'
        
        elif Sentence.content[0] != 'Sujet':
            print(Unvalidated)
            Check = 'Unchecked'

        elif 'Exclamation' in Sentence.content and Sentence.content[-1] != 'Exclamation':
            print(Unvalidated)
            Check = 'Unchecked'
        
        elif DoubleExclamation > 1:
            print(Unvalidated)
            Check = 'Unchecked'
        
        elif Sentence.content[-1] != 'Complément' or Sentence.content[-1] != 'Exclamation':
            print(Unvalidated)
            Check = 'Unchecked'
        
        i = 0
        while i < (len(Sentence.content)-1) and Check == 'Check':
            if Sentence.content[i] == Sentence.content[i+1]:
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Sujet' and Sentence.content[i+1] == 'Complément':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Sujet' and Sentence.content[i+1] == 'Liaison' and Sentence.content[i+2] == 'Verbe':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Sujet' and Sentence.content[i+1] == 'Liaison' and Sentence.content[i+2] == 'Complément':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Sujet' and Sentence.content[i+1] == 'Liaison' and Sentence.content[i+2] == 'Exclamation':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Verbe' and Sentence.content[i+1] == 'Liaison':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Liaison' and Sentence.content[i+1] == 'Verbe':
                print(Unvalidated)
                Check = 'Unchecked'
            elif Sentence.content[i] == 'Complément' and Sentence.content[i+1] == 'Liaison' and Sentence.content[i+2] == 'Sujet':
                print(Unvalidated)
                Check = 'Unchecked'
            i += 1
  
        if Check == 'Check':    
            print('Votre phrase semble correcte')
    
    #On demande aux joueurs si la phrase a un sens
    def PlayersVerification(Sentence):
        print('Cette phrase a-t-elle un sens ? Répondez honnêtement sinon votre PC explose')
        print(Sentence.text)
        print('Oui = Tapez O')
        print('Non = Tapez N')
        print("Vous n'êtes pas d'accord ? = Tapez X")
        
        VerificationRunning = True
        while VerificationRunning:    
            
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_o:
                        print('Votre phrase est correcte')
                        Score(Sentence)
                        VerificationRunning = False
                    
                    if event.key == pygame.K_n:
                        print('Votre phrase est incorrecte, vous attendrez la prochaine manche pour rejouer')
                        Sentence.content = []
                        Sentence.text = ''
                        VerificationRunning = False
                    
                    if event.key == pygame.K_x:
                        print("Vous allez jouer au pile ou face pour déterminer si oui ou non la phrase est correcte")
                        print("Si c'est pile, la phrase est correcte, et si c'est face, la phrase est incorrecte")
                        print("C'est parti...")
                        HeadsOrTails = ['PILE', 'FACE']
                        Result = random.choice(HeadsOrTails)
                        print(Result)
                        if Result == 'PILE':
                            print('Votre phrase est correcte')
                            Score(Sentence)
                            VerificationRunning = False
                        else:
                            print('Votre phrase est incorrecte, vous attendrez la prochaine manche pour rejouer')
                            Sentence.content = []
                            Sentence.text = ''
                            VerificationRunning = False
    
    #Attribution du score de la phrase en fonction de sa longueur et de son contenu
    def Score(Sentence):
        Sentence.value += 20 * len(Sentence.content)
        print('Vous infligez',Sentence.value,'points de dégats à votre adversaire')
        if Sentence == SentenceJ1:
            CriticalStrikeJ1()
        elif Sentence == SentenceJ2:
            CriticalStrikeJ2()
    
    #Coup critique du joueur1
    def CriticalStrikeJ1():
        if 'Ton monocle' in SentenceJ1.text and Joueur2.name == 'IntelligentMan':
            SentenceJ1.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Ta moustache' in SentenceJ1.text and Joueur2.name == 'MuscularMan':
            SentenceJ1.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Ta calvitie' in SentenceJ1.text and Joueur2.name == 'OldMan':
            SentenceJ1.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Tes lunettes' in SentenceJ1.text and Joueur2.name == 'YoungMan':
            SentenceJ1.value += 20
            print('Coup critique ! (+20 de dégats)')
        
    #Coup ciritque du joueur2
    def CriticalStrikeJ2():    
        if 'Ton monocle' in SentenceJ2.text and Joueur1.name == 'IntelligentMan':
            SentenceJ2.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Ta moustache' in SentenceJ2.text and Joueur1.name == 'MuscularMan':
            SentenceJ2.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Ta calvitie' in SentenceJ2.text and Joueur1.name == 'OldMan':
            SentenceJ2.value += 20
            print('Coup critique ! (+20 de dégats)')
        elif 'Tes lunettes' in SentenceJ2.text and Joueur1.name == 'YoungMan':
            SentenceJ2.value += 20
            print('Coup critique ! (+20 de dégats)')
            
    #On réinitialise la phrase après l'avoir validé
    def AfterValidating(Sentence):
        Sentence.content = []
        Sentence.text = ''
        Sentence.value = 0
    
    #On redonne les valeurs initiales aux insultes
    def ResetInsults():
        i = 0
        while i < len(InsultList):
            if InsultList[i].origin != None:
                InsultList[i].text = InsultList[i].origin
            i += 1

    #Ma boucle de vérification des événements
    GameRunning = True
    while GameRunning:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                GameRunning = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    Character()

            if event.type == pygame.MOUSEBUTTONDOWN:
                Position = pygame.mouse.get_pos()

                i = 0
                while i < 10:    
                    if CaseList[i].collidepoint(Position):
                        if RandomList[i].status == False:    
                            
                            if Turn % 2 == 0 and J1Validate == False:   
                                SentenceJ1.insults.append(RandomList[i])
                                Agreement(SentenceJ1)
                                SentenceJ1.content.append(RandomList[i].category)
                                SentenceJ1.text += (RandomList[i].text + ' ')
                                SentenceJ1.ListToWrite.append(RandomList[i].text)
                                TextDictionary["TextKey%s" %i] = SentenceFont.render(RandomList[i].text, True, (0,0,255))

                            elif Turn % 2 != 0 and J2Validate == False:
                                SentenceJ2.insults.append(RandomList[i])
                                Agreement(SentenceJ2)
                                SentenceJ2.content.append(RandomList[i].category)
                                SentenceJ2.text += (RandomList[i].text + ' ')
                                SentenceJ2.ListToWrite.append(RandomList[i].text)
                                TextDictionary["TextKey%s" %i] = SentenceFont.render(RandomList[i].text, True, (255,0,0))
                            
                            else:
                                print('Cliquez sur le bouton vert pour relancer une nouvelle manche')
                        
                        else:
                            print('Ce mot est déjà utilisé, choisissez en un autre')
                            Turn -= 1 #Pour éviter que ça saute le tour du joueur qui a missclick
                        
                        if J1Validate == False and J2Validate == False:    
                            RandomList[i].status = True  
                            Turn += 1
                        if J1Validate == True or J2Validate == True:
                            RandomList[i].status = True
                    
                    i += 1       

                if ButtonJ1Validate.collidepoint(Position):
                    if Turn % 2 == 0 and J1Validate == False:
                        if SentenceJ1.text != '':    
                            speech = gTTS(text = SentenceJ1.text, lang = language, slow = False)
                            speech.save("textJ1%s.mp3" %J1NumberFiles)
                            pygame.mixer.music.load("textJ1%s.mp3" %J1NumberFiles)
                            pygame.mixer.music.play()
                            J1NumberFiles += 1
                        
                        Validate(SentenceJ1)
                        PlayersVerification(SentenceJ1)
                        HPLengthJ2 -= SentenceJ1.value
                        AfterValidating(SentenceJ1)
                        J1Validate = True
                        Turn += 1
                        if HPLengthJ2 <= 0:
                            PartyIsOver(Joueur1)
                        
                    else:
                        print("Ce n'est pas votre tour ou vous avez déjà validé une phrase pour cette manche")
                
                if ButtonJ2Validate.collidepoint(Position):
                    if Turn % 2 != 0 and J2Validate == False:
                        if SentenceJ2.text != '':
                            speech = gTTS(text = SentenceJ2.text, lang = language, slow = False)
                            speech.save("textJ2%s.mp3" %J2NumberFiles)
                            pygame.mixer.music.load("textJ2%s.mp3" %J2NumberFiles)
                            pygame.mixer.music.play()
                            J2NumberFiles += 1
                        
                        Validate(SentenceJ2)
                        PlayersVerification(SentenceJ2)
                        HPLengthJ1 -= SentenceJ2.value
                        AfterValidating(SentenceJ2)
                        J2Validate = True
                        Turn += 1
                        if HPLengthJ1 <= 0:
                            PartyIsOver(Joueur2)
                    else:
                        print("Ce n'est pas votre tour ou vous avez déjà validé une phrase pour cette manche")
                
                if ButtonRestart.collidepoint(Position): #Nouvelle manche
                    SentenceJ1.ListToWrite = []
                    SentenceJ2.ListToWrite = []
                    SentenceJ1.insults = []
                    SentenceJ2.insults = []
                    SentenceJ1.text = ''
                    SentenceJ2.text = ''
                    ResetInsults()
                    RandomList = []
                    DrawInsult()
                    FillRect()
                    J1Validate = False
                    J2Validate = False
                    i = 0
                    while i < len(InsultList):
                        InsultList[i].status = False
                        i += 1

        #Remplissage du Screen
        Screen.fill('white')
        
        GameTitle = TitleFont.render('Fight !', True, (0,0,0))
        GameTitlePos = GameTitle.get_rect(midtop=(800/2, 0))
        
        Perso1Name = TextFont.render(Joueur1.name, True, (0,0,0))
        Perso1NamePos = Perso1Name.get_rect(bottomleft=(50,50))
        
        Perso2Name = TextFont.render(Joueur2.name, True, (0,0,0))
        Perso2NamePos = Perso2Name.get_rect(bottomright=(750,50))

        Screen.blit(GameTitle, GameTitlePos)
        Screen.blit(Perso1Name, Perso1NamePos)
        Screen.blit(Perso2Name, Perso2NamePos)
        
        Screen.blit(Joueur1.image, (50,250))
        Screen.blit(Joueur2.image, (650,250))

        Screen.blit(BubbleResized, (0,100))
        Screen.blit(BubbleFlippedResized, (500,100))
        
        pygame.draw.rect(Screen, 'black', (50,525,50,50))
        pygame.draw.rect(Screen, 'black', (700,525,50,50))
        
        BlueCheckPos = BlueCheckResized.get_rect(center=(75,550))
        RedCheckPos = RedCheckResized.get_rect(center=(725,550))
        
        Screen.blit(BlueCheckResized, BlueCheckPos)
        Screen.blit(RedCheckResized, RedCheckPos)

        pygame.draw.rect(Screen, 'black', (375,525,50,50))
        RestartIconPos = RestartIconResized.get_rect(center=(400,550))
        Screen.blit(RestartIconResized, RestartIconPos)

        i = 0
        Ypos = 100
        while i < 10:
            pygame.draw.rect(Screen, 'black', (300,Ypos,200,30))
            Ypos += 40
            i += 1
        
        i = 0
        while i < 10: #Même process que précédemment
            Screen.blit(TextDictionary['TextKey%s' %i], PosDictionary['PosKey%s' %i])
            i += 1

        LineDicoJ1 = {}
        XpointJ1 = 50
        YpointJ1 = 158
        i = 0
        while i < len(SentenceJ1.ListToWrite):
            LineDicoJ1['TextKey%s' %i] = SentenceFont.render(SentenceJ1.ListToWrite[i], True, (0,0,0))
            WordWidth = LineDicoJ1['TextKey%s' %i].get_width()
            Screen.blit(LineDicoJ1['TextKey%s' %i], (XpointJ1, YpointJ1))
            XpointJ1 += (WordWidth + 2)
            if i % 2 != 0:    
                XpointJ1 = 50
                YpointJ1 += 15
            i += 1
        
        LineDicoJ2 = {}
        XpointJ2 = 525
        YpointJ2 = 158
        i = 0
        while i < len(SentenceJ2.ListToWrite):
            LineDicoJ2['TextKey%s' %i] = SentenceFont.render(SentenceJ2.ListToWrite[i], True, (0,0,0))
            WordWidth = LineDicoJ2['TextKey%s' %i].get_width()
            Screen.blit(LineDicoJ2['TextKey%s' %i], (XpointJ2, YpointJ2))
            XpointJ2 += (WordWidth + 2)
            if i % 2 != 0:    
                XpointJ2 = 525
                YpointJ2 += 15
            i += 1

        pygame.draw.rect(Screen, 'red', (50,50,HPLengthJ1,20))
        pygame.draw.rect(Screen, 'red', (550,50,200,20))
        pygame.draw.rect(Screen, 'white', (550,50,(200-HPLengthJ2),20))
        
        def DrawBorders(X,Y,XLen):
            pygame.draw.line(Screen, 'black', (X-2,Y-2), (XLen,Y-2), 2)
            pygame.draw.line(Screen, 'black', (X-2,70), (XLen,70), 2)
            pygame.draw.line(Screen, 'black', (X-2,Y), (X-2,70), 2)
            pygame.draw.line(Screen, 'black', (XLen,Y-2), (XLen,70+1), 2)
        
        DrawBorders(50,50,250)
        DrawBorders(550,50,750)
        
        pygame.display.flip()

    pygame.quit()

#Boucle PartyIsOver
def PartyIsOver(Joueur):
    
    #Texte de victoire
    TextWin = Joueur.name + ' a gagné !'
    TextWinRender = TitleFont.render(TextWin, True, (0,0,0))
    TextWinRenderPos = TextWinRender.get_rect(center=(800/2,600/2))
    
    #Ma boucle de vérification des événements
    PartyIsOverRunning = True
    while PartyIsOverRunning:
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                PartyIsOverRunning = False
    
        #Remplissage du screen
        Screen.fill('white')
        Screen.blit(TextWinRender, TextWinRenderPos)
        ImgPos = Joueur.image.get_rect(center=(800/2,200))
        Screen.blit(Joueur.image, ImgPos)

        pygame.display.flip()
    
    pygame.quit()

Menu()
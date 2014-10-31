# language: fr
Fonctionnalité: Mouvement de la tête

    Scénario: Bouge la tête à Gauche
        Soit Poppy s'initialise
        Quand Poppy tourne la tête à gauche de "45"
        Alors Attente de 2s
        Quand Poppy tourne la tête à droite de "45"
        Alors Attente de 2s


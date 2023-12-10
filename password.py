# Importer du module hashlib
import hashlib

# Demander à l'utilisateur de choisir un mot de passe
def utilisateur_mdp():
    return input("Veuillez choisir un mot de passe contenant au moins 8 caractères, une majuscule, une minuscule, un chiffre et un caractère spécial : ")

# Définir un mot de passe selon 5 conditions
    # Condition1: le mdp est égal ou supérieur à huit caractères
    # Condition2: le mdp a au moins une lettre majuscule
    # Condition3: le mdp contient au moins une lettre minuscule
    # Condition4: le mdp contient au moins un chiffre
    # Condition5: le mdp contient au moins un caractère spécial

def verifier_mdp(mdp):
    return (
        len(mdp) >= 8 and       
        any(condition.isupper() for condition in mdp) and        
        any(condition.islower() for condition in mdp) and        
        any(condition.isdigit() for condition in mdp) and       
        any(condition in '!@#$%^&*' for condition in mdp)
    )

# Hachage du mot de passe 
def hachage_mdp(password):    
    mdp_hacher = hashlib.sha256(password.encode("utf-8")).hexdigest()
    return mdp_hacher

# Autoriser à l'utilisateur à saisir un nouveau mdp jusqu'à 4 tentatives maximum. 
tentatives_max = 4
tentatives_restantes = tentatives_max

while tentatives_restantes > 0:
    password = utilisateur_mdp()
    password_crypte = hachage_mdp(password)

    if verifier_mdp(password):
        print("Votre mot de passe est valide.")
        print(f"Votre mot de passe haché est : {hachage_mdp(password)}")
        break
    else:
        tentatives_restantes-= 1
        if tentatives_restantes > 0:
            print(f"Votre mot de passe est invalide. Il vous reste {tentatives_restantes} tentative(s).")
        else:
            print("Votre limite de tentatives est atteinte.")

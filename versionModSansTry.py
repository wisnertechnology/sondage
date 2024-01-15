#coding:utf-8
import pickle
import boto3
import os
import sys      # On import le module sys parcequ'on aura besoin d'utiliser la onction exit() de sys pour pouvoir sortir du programme brusquement (arreter le programme) 

class Sondage:
    def __init__(self):
        self.questions = {"- Avez-vous l'intention de quitter le pays après avoir terminé vos études universitaires?" : ["Oui", "Non", "Incertain"],
            "- Quel est votre âge actuel?" : ["Moins de 20 ans", "20-24 ans", "25-29 ans", "30-34 ans", "35 ans et plus"],
            "- À quel niveau d'études êtes-vous actuellement?" : ["Licence 1", "Licence 2", "Licence 3", "Licence 4", "DUT 1", "DUT 2"],
            "- Vers quel(s) pays envisagez-vous de vous rendre? (Sélectionnez tous ceux qui s'appliquent)" : ["États-Unis", "Canada", "Royaume-Uni", "Australie", "France", "autres"],
            "- Pourquoi envisagez-vous de quitter le pays? (Sélectionnez toutes celles qui s'appliquent)" :     ["Opportunités professionnelles", "Recherche académique", "Qualité de vie", "Autre(précisez)"],
            "- Envisagez-vous de quitter le pays pour des études supplémentaires ou d'autres raisons? (Sélectionnez tous ceux qui s'appliquent)" :     ["Études supplémentaires", "Raisons professionnelles", "Raisons personnelles"],
            "- Si vous envisagez un départ temporaire, quelle est la durée prévue de votre séjour?" : ["Moins d'un an", "1-2 ans", "3-5 ans", "Plus de 5 ans"],
            "- Avez-vous l'intention de retourner dans votre pays d'origine après votre séjour à l'étranger?" : ["Oui", "Non", "Incertain"],
}
        self.reponses = list()

    def prendre_sondage(self):
        opsyon ='y'
        while (opsyon == 'y' or opsyon == 'Y'):
            donnee_utilisateur = {}
            for question, reponse in self.questions.items():
                try:
                    choix = input(f"{question} ({', '.join(reponse)}): ")
                    choix = int(choix) #Premye modifikasyonm mwen komanse fe modifikasyon de laaaaa
                    if 0 < choix <= len(reponse) and reponse[choix-1] != "Autre(précisez)": #      
                        donnee_utilisateur[question] = reponse[int(choix)-1] #men pati mwen pote nouvo modifikasyon mwen an
                    elif int(choix) <= len(reponse) and reponse[choix-1] == "Autre(précisez)":
                            choixx = input("veillez preciser votre reponse : ")
                            donnee_utilisateur[question] = choixx
                    elif int(choix) <= 0:
                        while(choix == 0):
                            choix = input(f"Veillez choisir parmi les options suivantes ({', '.join(reponse)}): ")
                            donnee_utilisateur[question] = reponse[int(choix)-1]
                    elif int(choix) > len(reponse):
                        choix = int(choix)
                        while(int(choix) > len(reponse)):
                            choix = input(f"\nVeillez choisir parmi les options suivantes ({', '.join(reponse)}): \n")
                            choix = int(choix)
                            if choix > len(reponse):
                                continue
                            donnee_utilisateur[question] = reponse[int(choix)-1]
                    else:
                        print("\nCette Option n'existe pas\n")
                        break
                except Exception as e:
                    # print(f"\n\nUne exception de type {type(e).__name__} s'est produite : {str(e)}\n\n")
                    print('\t\t\tOption non disponible\n\n')
                    print("\t\t\tNous sommes oblige d'arreter le programme\n\n\n\t\t\t!!!!!!! Vous devez relancer le programme pour recommencer le processus du sondage !!!!!!!!!\n\n\n")

                    # break
                    # Nous allons arreter le programme en utiliser la fonction exit() du module sys
                    sys.exit()
                    

            self.reponses.append(donnee_utilisateur)
            opsyon =input('\n\n\nVoulez vous continuer a faire des enregistrements ?  ')
            # Nettoyer la console
            if opsyon.lower() == 'y':
                os.system('cls' if os.name == 'nt' else 'clear')

    
    def sauvegarder_sondage_local(self):
            with open("donnees_de_sondage_ESIH.txt", "ab") as f:
                pickle.dump(self.reponses, f)



    def sauvegarder_sondage_aws(self):
        #Informations d'identification de l'utilisateur IAM
        USER_ACCESS_KEY_WISNER = ''
        USER_SECRET_KEY_WISNER = ''

        #Nom du compartiment S3
        bucket_name = 'sondageesih'

        #Chemin local du fichier que vous souhaitez télécharger ou téléverser
        local_file_path = 'donnees_de_sondage_ESIH.txt'
        chemin_distant = 'chemin-distant-dans-s3.txt'
        s3 = boto3.client('s3', aws_access_key_id=USER_ACCESS_KEY_WISNER, aws_secret_access_key=USER_SECRET_KEY_WISNER)
        with open("donnees_de_sondage_ESIH.txt", "rb") as f:
            s3.upload_fileobj(f, bucket_name, chemin_distant)

   

#main programme nou an
sondage = Sondage()
sondage.prendre_sondage()
sondage.sauvegarder_sondage_local()
sondage.sauvegarder_sondage_aws()



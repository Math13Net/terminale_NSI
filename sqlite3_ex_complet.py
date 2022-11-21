import sqlite3

class super_hero:
  def __init__(self, nom, couleur, accessoire):
    self.nom = nom
    self.couleur = couleur
    self.accessoire = accessoire

iron_man = super_hero("Tony Stark", "rouge", "armure")
captain_america = super_hero("Steve Rogers", "bleu", "bouclier")
hulk = super_hero("Bruce Banner", "vert", None)
zorro = super_hero("Don Diego de la Vega", "noir", "épée")

connection = sqlite3.connect("exemple.db")

with connection:
  curseur = connection.cursor()
  curseur.execute("CREATE TABLE super_hero(id INT, nom TXT, couleur TEXT, accessoire TEXT)")
  liste_hero = [iron_man, captain_america, hulk, zorro]
  id_hero = 0
  for hero in liste_hero:
    curseur.execute("INSERT INTO super_hero VALUES(?, ?, ?, ?)"), (id_hero, hero.nom, hero.couleur, hero.accessoire))
    id_hero += 1
  curseur.execute("SELECT * FROM super_hero")
  lignes = curseur.fetchall()

  for ligne in lignes:
    print(ligne)

  curseur.execute("UPDATE super_hero SET accessoire=? WHERE nom=?", ("cape", zorro.com))
  connection.commit()
  print("nombre de ligne mise à jouer : %d" curseur.rowcount)

  connection.row_factory = sqlite3.Row
  curseur = connection.cursor()
  curseur.excute("SELECT * FROM super_hero")
  lignes = curseur.fetchall()

  for ligne in lignes:
    print("%s %s %s (ligne["nom"], ligne["couleur], ligne["acessoire"]))
  
  curseur.excutescript("""
  DELETE FROM super_hero WHERE id=3;
    DROP TABLE IF EXISTS super_hero;
    """)

  try:
    curseur.execute("SELECT * FROM super_hero")
  except sqlite3.Error as e:
    print("Erreur : %s % e.args[0]")
  


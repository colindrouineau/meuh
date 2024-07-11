# Module pour envoyer automatiquement le mail avec l'excel à la fin du jour / de la semaine
# Nécessite de télécharger et de se connecter sur la version Outlook classique
# (nom de la version à la date de juillet 2024)

# from ... import base de données as bd (ici, on prend la base de données d'exemple instance\site.db)

# Ici, le programme fonctionne s'il est exécuté directement.
# Mais on pourrait le convertir faicilement en fonction si on voulait l'appeler depuis un autre fichier.

if __name__ == "__main__":

    import win32com.client  # Pour l'envoi automatique du mail
    import sqlite3  # Pour convertir de sql en panda database
    import pandas as pd  # pour la base de données et la conversion de la base en SQL

    # Connect to the SQLite database
    conn = sqlite3.connect("instance\site.db")  # Replace with your database file

    # List of tables to export
    tables = ["user", "task"]  # Replace with your actual table names

    # Create a Pandas Excel writer using openpyxl as the engine
    with pd.ExcelWriter("data.xlsx", engine="openpyxl") as writer:
        for table in tables:
            # Query the data from each table
            query = f"SELECT * FROM {table};"
            df = pd.read_sql_query(query, conn)

            # Write each DataFrame to a separate sheet in the Excel file
            df.to_excel(writer, sheet_name=table, index=False)

    # Close the connection
    conn.close()

    ol = win32com.client.Dispatch("outlook.application")
    olmailitem = 0x0  # size of the new email (?)
    newmail = ol.CreateItem(olmailitem)

    newmail.Subject = "données pour resan"

    newmail.To = "recipient_address"  # recipient string : separate the different recipient by a ';'

    newmail.HTMLBody = "texte éventuel"
    attach = r"C:\Users\colin\cours-info\meuh\data.xlsx"  # path\data.xlsx
    newmail.Attachments.Add(attach)

    newmail.Send()

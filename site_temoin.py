from flask import Flask
app=Flask("Appli de fou")

#tout repose sur une syntaxe particulière :

@app.route('/une/url/cible')
def la_fonction_correspondante():
    //fait des trucs
    //
    return "des trucs"

app.run(debug=True, port=3001)
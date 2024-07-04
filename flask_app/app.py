from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def login():
    valid_credentials = {"username": "ciao", "password": "qwerty"}
    error = None

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == valid_credentials['username'] and password == valid_credentials['password']:
            return render_template('home.html')
        else:
            error = 'Credenziali errate, riprova.'

    return render_template('login.html', error=error)

@app.route('/registrazione', methods=['GET', 'POST'])
def registrazione():
    error_message = None
    if request.method == 'POST':
        # Ottenere i dati dalla form
        nome = request.form['nome']
        cognome = request.form['cognome']
        sesso = request.form['sesso']
        username = request.form['username']
        password = request.form['password']
        conferma_password = request.form['conferma_password']

        # Validazione dei dati (esempio semplice)
        if password != conferma_password:
            error_message = "Le password non corrispondono."
        elif username in registered_users:
            error_message = "Username già in uso. Scegli un altro username."
        else:
            # Salva i dati utente nel database o in memoria
            registered_users[username] = password
            # Reindirizzamento alla pagina di login dopo la registrazione
            return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/piante')
def piante():
    piante = [
        {
            'nome': 'Basilico',
            'descrizione': "Il Basilico è una pianta erbacea annuale ampiamente utilizzata in cucina per il suo aroma fresco e il sapore caratteristico. Le foglie sono di forma ovale, di colore verde brillante, e crescono in cespugli compatti. È nativo delle regioni tropicali dell'Asia e apprezza temperature calde e un suolo ben drenato. Il basilico è versatile in cucina, utilizzato fresco in insalate, salse, pesto e piatti a base di pomodori.",
            'temperatura': '20°-25°C',
            'umidita': 'Moderata (40-60%)',
            'esposizione': 'Luce solare diretta o artificiale intensa (12-14 ore al giorno)'
        },
        {
            'nome': 'Prezzemolo',
            'descrizione': 'Il Prezzemolo è una pianta biennale comunemente coltivata per le sue foglie aromatiche e per il suo uso decorativo in cucina. Le foglie sono divise e di colore verde scuro, crescono in rosette fitte. È originario del Mediterraneo e richiede temperature moderate e un terreno umido ma ben drenato. Il prezzemolo è spesso utilizzato come garnish o per aromatizzare salse, zuppe, stufati e piatti a base di carne.',
            'temperatura': '20°-25°C',
            'umidita': 'Moderata (40-60%)',
            'esposizione': 'Luce indiretta brillante o luce artificiale intensa'
        },
        {
            'nome': 'Coriandolo',
            'descrizione': 'Il Coriandolo è una pianta annuale nota sia per le sue foglie che per i semi aromatici. Le foglie sono simili a quelle del prezzemolo ma con un aroma distintivo e un sapore speziato. I semi sono utilizzati come spezia. Originario dell\'Europa meridionale e dell\'Asia occidentale, il coriandolo preferisce temperature moderate e un terreno ben drenato. È ampiamente utilizzato in cucine internazionali per insaporire curry, salse, salse di cetriolo e piatti a base di pesce.',
            'temperatura': '18°-22°C',
            'umidita': 'Moderata (40-60%)',
            'esposizione': 'Luce indiretta brillante o luce artificiale intensa'
        },
        {
            'nome': 'Menta',
            'descrizione': 'La Menta è una pianta perenne con foglie aromatiche, conosciuta per il suo aroma fresco e rinfrescante. Le foglie sono di forma ovale e dentellate, di colore verde scuro. Esistono diverse varietà di menta, tra cui la menta piperita e la menta verde. È originaria dell\'Europa e dell\'Asia occidentale e cresce bene in ambienti umidi e freschi. La menta è comunemente utilizzata per infusi, tisane, cocktail, dessert e come condimento in piatti salati come insalate e salse.',
            'temperatura': '18°-25°C',
            'umidita': 'Moderata-alta (50-70%)',
            'esposizione': 'Luce solare diretta o indiretta brillante, tollera anche luce artificiale intensa'
        }
    ]
    return render_template('piante.html', piante=piante)

@app.route('/sensori')
def sensori():
    return render_template('sensori.html')

@app.route('/storico')
def storico():
    return render_template('storico.html')
    

if __name__ == '__main__':
    app.run(debug=True)

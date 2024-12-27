from flask import *
import yfinance as yf

app = Flask(__name__)

convidados = ['RENE','ERICA','LUDGERO','KLELVER']

@app.route('/')
def pagina_principal():
    return render_template('home.html')

@app.route('/verificar', methods=['POST'])
def verificar_convidado():
    nome_user = request.form.get('nomeverificar')

    if len(nome_user) == 0 or not nome_user.isalpha():
        return render_template('home.html')

    if nome_user.upper() in convidados:
        msg = 'você foi convidado para o casamento de Yuri'
        dolar = yf.Ticker('USDBRL=X').history()['Close'].round(3)[-1]
        return render_template('respostasim.html', mensagem=msg, nome=nome_user, valor=dolar)
    else:
        msg = 'Infelizmente, não tinha mais vagas no local da festa mas Yuri gosta muito de você'
        return render_template('respostanao.html', mensagem=msg, nome=nome_user)


app.run()
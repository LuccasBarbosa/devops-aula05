import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
<<<<<<< HEAD
	erroInicializar = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True
if erroInicializar:
	sys.exit(1)
else:
	sys.exit(0)
=======
    erroInicializar = True
else:
    for linha in jogo:
        if len(linha) != 3:
            erroInicializar = True
        else:
            for elemento in linha:
                if elemento != '.':
                    erroInicializar = True                  
if erroInicializar:
    sys.exit(1)
else:
    sys.exit(0)
>>>>>>> f8a86d5006ecdbbd3bd3c81d26123dcbe705d927

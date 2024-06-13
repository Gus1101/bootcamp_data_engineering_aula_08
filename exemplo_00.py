from loguru import logger

logger.add("meu_app.log",
           format="{time} {level} {mensage} {file}",
           level="CRITICAL")

def soma (x:int,y:int) -> int:
    try:
        soma = x+y
        logger.info(f"sabe matemárica básica, parabens {soma}")
        return soma
    except:
        logger.critical("cabaço, digitou numeros inválidos")

print(soma(5,5))
print(soma(5,"6"))
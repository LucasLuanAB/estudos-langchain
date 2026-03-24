from langchain_core.runnables import RunnableLambda, RunnablePassthrough
def add_one(x:int) -> int:
    return x + 1

runnable = RunnableLambda(add_one)

resposta = runnable.invoke(10)
print("---resposta invoke exemplo 1 ---------")
print (resposta)
print ("--------------------------------------")
"-------------------"
#aqui eu estou declarando as variaveis
def add_one(x:int) -> int:
    return x +1
def mul_two (x:int) -> int:
    return x * 2
# aqui abaixo eu estou declarando as runnable
runnable_1 = RunnableLambda(add_one)
runnable_2 = RunnableLambda(mul_two)

sequence = runnable_1 | runnable_2
resposta = sequence.invoke(20)
print("---------- resposta do invoke exemplo 2------")
print (resposta)

"----------------------"
def add_one(x:int) -> int:
    return x * 1

def mul_two(x:int) -> int:
    return x * 2

def mul_three(x:int) -> int:
    return x * 3

runnable_1 = RunnableLambda(add_one) # convertendo a função de soma para runnable
runnable_2 = RunnableLambda(mul_two) # convertendo a função de multiplicação de 2 para runnable
runnable_3 = RunnableLambda(mul_three) # convertendo a função de multiplicação de 3  para runnable

sequence = runnable_1 | {
    "mul_two": runnable_2,
    "mul_three": runnable_3, 
}  

reposta = sequence.invoke(1)
print("-------- reposta invoke exemplo 3 RunnableParallel--------")
print(reposta)
print("-----------------------------------------")

"""EXEMPLO 4 - RUNNABLEPASSTHROUGH"""
chain = RunnablePassthrough() | RunnablePassthrough() | RunnablePassthrough()

#independente de quantas vezes você passar o resultado para frente a entrada nao é alterada.
reposta = chain.invoke("Ola")
print("--------- reposta do invoke exemplo 4 runnable passthrough-----")
print(reposta)
print('----------------')


#"exemplo 5 RunnablePassthrough + RunnableLambda  "
def entrada_para_letras_maisculas(entrada:str):
    saida = entrada.upper()
    return saida 
chain = RunnablePassthrough() | RunnableLambda(entrada_para_letras_maisculas) | RunnablePassthrough()
reposta = chain.invoke("olá")
print("----------------reposta invoke exemplo 5 - runnablepassthrough +runnablelambda")
print(reposta)
print('-------------')


#exemplo 6 operador assign
runnable =RunnablePassthrough() | RunnablePassthrough.assign(multiplica_3=lambda x:x["num"]*3)
reposta = runnable.invoke({"num":1})
print("---------------- reposta do invoker exemplo 6 opreador assign")
print(reposta)
print('---------------------------------')

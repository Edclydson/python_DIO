lista = [1, 2, 3]
try:
    # print(1 / 0)
    num = lista[2]
    a = x
except ZeroDivisionError:  # This is the exception type we want to catch
    print("Não é possível dividir por zero")
except IndexError:
    print("O índice não existe")
except BaseException as error:  # This is the general exception type
    print("Ocorreu um erro:", error)
# except Exception:  # Or can do it this way
#     print("Ocorreu um erro")

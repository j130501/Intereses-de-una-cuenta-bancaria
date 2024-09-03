from InteresesCuentaBancaria import  InteresCuentaBancaria
def main():
    saldo_inicial = float(input("Dame saldo actual: "))
    cuenta=Cuenta(saldo_inicial)
    cuenta.calcular_itnteres()
    cuenta.mostrar_saldo()

if __name__=="__main__":
    main()

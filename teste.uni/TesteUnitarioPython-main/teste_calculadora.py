import unittest
import coverage
import webbrowser
import os
import calculadora 



class TesteCalculadora (unittest.TestCase):
    def teste_adicao_float(self):
        # Teste para lista de inteiros
        resultado = calculadora.adicao(1,2)
        self.assertEqual(resultado, 3.0)


    def teste_subtracao_float(self):
        resultado = calculadora.subtracao(19,10)
        self.assertEqual(resultado, 9.0)
        
        
    def teste_multiplicacao_float(self):
        # Teste para lista de floats
        resultado = calculadora.multiplicacao(20,10)
        self.assertEqual(resultado, 200.0)


    def teste_divisao0_float(self):
        # Teste para lista de floats
        resultado = calculadora.divisao(20.,0)
        self.assertRaise(ValueError)
        
        
    def teste_divisao_float(self):
        # Teste para lista de floats
        resultado = calculadora.divisao(100,50)
        self.assertEqual(resultado, 2.0)


    def teste_potenciacao_float(self):
        # Teste para lista de floats
        resultado = calculadora.potenciacao(5,2)
        self.assertEqual(resultado, 25.0)


    
if __name__ == '__main__':
    # Criar uma instância do Coverage com o arquivo .coveragerc
    cov = coverage.Coverage(config_file='TesteUnitarioPython-main\.coveragerc.txt')

    # Iniciar a medição da cobertura
    cov.start()

    # Executar os testes
    suite = unittest.TestLoader().loadTestsFromTestCase(TesteCalculadora)
    unittest.TextTestRunner(verbosity=2).run(suite)

    # Encerrar a medição da cobertura após os testes
    cov.stop()

    # Salvar os dados de cobertura em um arquivo
    cov.save()
    cov.html_report(directory='htmlcov')

    # Abra o relatório no navegador
    index_file = os.path.join('htmlcov', 'index.html')
    webbrowser.open('file://' + os.path.abspath(index_file))
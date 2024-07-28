Guia de Testes

Visão Geral

Este documento fornece diretrizes para os testes do projeto FinTechX. Inclui instruções para configurar o ambiente de teste, executar os testes e escrever novos testes. O projeto utiliza pytest como framework de testes para garantir a qualidade e a confiabilidade do código.

Configurando o Ambiente de Teste
    1. Instalar Dependências:
        Certifique-se de que todos os pacotes necessários estão instalados executando: 
        pip install -r requirements.txt
    
        Além disso, instale o pytest se ainda não estiver incluído:
        pip install pytest

    2. Variáveis de Ambiente:
        Certifique-se de que o arquivo .env está corretamente configurado com as variáveis de ambiente necessárias para conectar ao banco de dados e à API do Google.

Executando os Testes
    Para executar todos os testes do projeto, navegue até o diretório raiz do projeto e execute:
    pytest

    Este comando descobrirá e executará automaticamente todos os casos de teste no diretório tests.

    Dicas e Boas Práticas
        Isolamento: Cada teste deve ser independente, ou seja, não deve depender de outros testes.
        Cobertura de Código: Esforce-se para cobrir o máximo de código possível, incluindo casos extremos e falhas esperadas.
        Manutenção: Mantenha os testes atualizados conforme o código base evolui.
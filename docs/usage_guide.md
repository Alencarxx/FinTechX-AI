FinTechX AI - Guia de Uso

Introdução:

FinTechX AI é uma aplicação projetada para ajudar os usuários a converter perguntas em linguagem natural em consultas SQL, facilitando o acesso e a análise de dados em um banco de dados MySQL. Este guia fornecerá instruções passo a passo para usar a aplicação, desde a configuração inicial até a execução de consultas.

Configuração Inicial:

    1. Instalação de Dependências:

    Certifique-se de ter o Python e o pip instalados em seu sistema.
    Navegue até o diretório raiz do projeto FinTechX AI.
    Execute o comando: pip install -r requirements.txt para instalar todas as dependências necessárias.

    2. Configuração de Variáveis de Ambiente:

    Crie um arquivo .env na raiz do projeto.
    Adicione as seguintes variáveis de ambiente
    -----------------------------------------------------------------------
    GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
    DB_HOST=YOUR_DATABASE_HOST
    DB_USER=YOUR_DATABASE_USER
    DB_PASSWORD=YOUR_DATABASE_PASSWORD
    DB_NAME=YOUR_DATABASE_NAME
    -----------------------------------------------------------------------
    Substitua YOUR_GOOGLE_API_KEY, YOUR_DATABASE_HOST, YOUR_DATABASE_USER, YOUR_DATABASE_PASSWORD e YOUR_DATABASE_NAME pelos valores apropriados.

Iniciando a Aplicação:

    1. No terminal, navegue até o diretório raiz do projeto FinTechX AI.
    2. Execute o comando: streamlit run app/main.py.
    3. A aplicação será aberta em seu navegador padrão.

Uso da Aplicação:

    1. Inserção de Pergunta:

        Na página principal da aplicação, insira sua pergunta em inglês na caixa de texto intitulada "Digite sua pergunta".

    2. Envio da Pergunta:

        Clique no botão "Fazer a pergunta" para enviar sua pergunta.

    3. Processamento e Resultados:

        A aplicação usará a API do Google Generative AI para converter sua pergunta em uma consulta SQL.
        A consulta SQL será executada no banco de dados MySQL configurado.
        Os resultados serão exibidos em uma tabela logo abaixo.

    4. Exemplos de Perguntas:

    "Quais são os produtos mais populares entre os clientes corporativos?"
    "Qual o ticket médio por compra?"

Resolução de Problemas:

    Erro de Conexão com o Banco de Dados:

        Verifique se as credenciais do banco de dados no arquivo .env estão corretas.
        Certifique-se de que o banco de dados está acessível e funcionando corretamente.

    Erro na Geração de Consultas SQL:

        Certifique-se de que a pergunta está em inglês claro e relacionado aos dados disponíveis no banco de dados.
        Consulte a seção de exemplos de perguntas para orientações.

Melhorias Futuros:

    Aprimoramento de Segurança:
        Adicionar autenticação e autorização para acessar dados sensíveis.
    Expansão de Funcionalidades:
        Suporte para mais tipos de perguntas e consultas complexas.
    Otimização de Performance:
        Melhorias na velocidade de geração de consultas e na resposta do banco de dados.

Contribuições e Feedback:

    Contribuições para o projeto são bem-vindas. Consulte o arquivo CONTRIBUTING.md para diretrizes.
    Para feedback ou relatórios de problemas, abra uma issue no repositório GitHub do projeto.

Licença:

Este projeto está licenciado sob a MIT.

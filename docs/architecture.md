FinTechX AI - Documentação da Arquitetura

Visão Geral:

O FinTechX AI é uma aplicação interativa que permite aos usuários converter perguntas em consultas SQL usando a API do Google Generative AI. O sistema facilita o acesso a dados armazenados em um banco de dados MySQL e apresenta os resultados de maneira acessível.

Tecnologias Utilizadas
    Streamlit: Para construir a interface do usuário.
    Google Generative AI (Gemini): Para a conversão de linguagem natural para SQL usando LLM.
    MySQL: Banco de dados relacional para armazenar dados.
    Python: Linguagem de programação principal do projeto.
    MySQL Connector: Biblioteca Python para se conectar ao banco de dados MySQL.
    dotenv: Para gerenciar variáveis de ambiente de forma segura.

Componentes Principais:

    1.Frontend (Streamlit):

    Descrição: Interface de usuário interativa e intuitiva.
    Funções:
        Coletar e processar entradas do usuário.
        Apresentar os resultados das consultas SQL de forma tabular.
        Manter o fluxo de interação com o usuário.
        
    2.Conversão de Perguntas para SQL (Google Generative AI):

    Descrição: Utiliza o modelo Gemini para transformar perguntas em linguagem natural em consultas SQL.
    Funções:
        Processar perguntas de entrada.
        Gerar consultas SQL precisas e válidas.
        Sanitizar e validar consultas para evitar erros de sintaxe.

    3.Banco de Dados (MySQL):

    Descrição: Armazena os dados estruturados para consulta.
    Funções:
        Armazenar informações em tabelas relacionadas (clientes, empregados, pedidos, etc.).
        Executar consultas SQL e fornecer resultados.

    4.Back-end (Conector MySQL):

    Descrição: Comunica-se com o banco de dados para executar consultas.
    Funções:
        Conectar-se ao banco de dados MySQL.
        Executar e gerenciar consultas SQL.
        Retornar resultados ao frontend.

Fluxo de Dados:

    1. O usuário insere uma pergunta no campo de entrada do Streamlit.
    2. A pergunta é enviada para a API do Google Generative AI.
    3. A API converte a pergunta em uma consulta SQL.
    4. A consulta SQL é sanitizada e validada.
    5. A consulta é executada no banco de dados MySQL.
    6. Os resultados são retornados e exibidos ao usuário no frontend.

Possíveis Melhorias Futuras:

Aprimoramento de Segurança: Implementação de medidas adicionais de segurança para proteger dados e credenciais.
Expansão de Funcionalidades: Inclusão de suporte para mais tipos de consultas e bases de dados.
Otimização de Performance: Melhorias na eficiência da geração e execução de consultas.
Integração com Outras APIs: Integração com outras APIs e fontes de dados para ampliar a funcionalidade.
# FinTechX AI

Bem-vindo ao FinTechX AI! Este é um aplicativo baseado em Streamlit que permite a geração de consultas SQL a partir de perguntas em linguagem natural e a visualização dos resultados em um formato organizado.

## Funcionalidades

- **Geração de Consultas SQL:** Converta perguntas em linguagem natural em consultas SQL para um banco de dados MySQL usando o modelo Google Gemini.
- **Visualização de Resultados:** Exiba os resultados das consultas em uma tabela organizada na interface do Streamlit.

## Pré-requisitos

Antes de começar, verifique se você tem o Conda instalado. Se não, você pode [baixar e instalar o Conda](https://docs.conda.io/en/latest/miniconda.html).

## Instalação

1. Clone este repositório para sua máquina local:
    
    git clone https://github.com/alencarxx/fintechx-ai.git
    cd fintechx-ai
    

2. Crie um ambiente Conda e ative-o:
    
    conda create --name fintechx-ai python=3.10
    conda activate fintechx-ai
    

3. Instale as dependências do projeto:
    
    pip install -r requirements.txt
    

4. Configure seu arquivo `.env` com as variáveis de ambiente necessárias. Crie um arquivo chamado `.env` na raiz do projeto e adicione as seguintes variáveis:
   
    GOOGLE_API_KEY=your_google_api_key
    DB_HOST=your_database_host
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_NAME=your_database_name
    

5. Certifique-se de que o arquivo `.env` está listado no `.gitignore` para evitar a exposição das suas credenciais:

    Adicione o seguinte ao seu `.gitignore`:
    
    .env
    

## Executando o Aplicativo

Para iniciar o aplicativo, use o seguinte comando:

streamlit run app/main.py

Estrutura do Projeto

app/main.py: O arquivo principal que contém a lógica do aplicativo Streamlit.
.env: Arquivo de configuração para variáveis de ambiente (não deve ser versionado no Git).
.gitignore: Lista de arquivos e pastas a serem ignorados pelo Git.
requirements.txt: Lista de pacotes Python necessários para o projeto.
README.md: Este arquivo.

Uso
Abra o aplicativo em seu navegador.
Digite uma pergunta relacionada ao banco de dados.
O aplicativo gerará uma consulta SQL e exibirá os resultados em uma tabela.

Exemplo de Perguntas
Qual é o valor total de vendas por categoria de produto?
Quem são os melhores vendedores?
Qual é o ticket médio por compra?

## Executando o Teste

Pare a execução do Streamlit caso esteja em execução pressione Ctrl+C. Isso interromperá o processo do Streamlit e liberará o terminal para outras tarefas.

Após interromper o Streamlit, você pode instalar o pytest usando o pip:

pip install pytest

Agora basta rodar os teste usando pytest, para executar os testes, você deve estar no diretório raiz do seu projeto (FinTechX-AI/). A partir desse diretório, execute o seguinte comando no terminal:

pytest

Então o pytest procurará automaticamente por todos os arquivos que começam com test_ ou terminam com _test.py e executará as funções de teste dentro deles.

Contribuições
Contribuições são bem-vindas! Se você encontrar um bug ou deseja adicionar uma nova funcionalidade, por favor, abra uma issue ou envie um pull request.

Licença
Este projeto é licenciado sob a Licença MIT.

Contato
Se você tiver perguntas ou sugestões, entre em contato comigo em alencarporto2008@gmail.com.

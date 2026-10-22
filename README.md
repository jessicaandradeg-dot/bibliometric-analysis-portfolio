# Bibliometric Analysis & Scientific Data Research

## Jéssica de Andrade Gomes

**Mestre e Doutoranda em Engenharia Biomédica — Universidade Federal do Rio de Janeiro (UFRJ/COPPE)**

Este repositório reúne projetos desenvolvidos no contexto de **análise bibliométrica, análise de literatura científica e pesquisa baseada em dados**.

Os estudos utilizam bases bibliográficas e científicas para investigar padrões de publicação, retratações, citações, colaboração científica, produção acadêmica e evolução de temas de pesquisa.

Os projetos demonstram experiência em diferentes etapas da análise de dados científicos, incluindo **coleta, organização, limpeza, filtragem, análise exploratória, estatística descritiva, análise de correlação, visualização de dados e análise de redes**.

---

## Projetos

### 00. Pilotos de revisão temática: voz corporativa e economia agêntica

Dois protocolos exploratórios documentam strings de busca no OpenAlex, critérios de inclusão/exclusão, um fluxo de seleção no estilo PRISMA e uma tabela de extração inicial. Os temas são **Speech Emotion Recognition e comunicação corporativa** e **economia agêntica em finanças**.

O escopo está explicitamente limitado a uma amostra de títulos retornados nas primeiras páginas de busca: não houve deduplicação integral, triagem de texto completo ou revisão sistemática concluída. A pequena rede de coocorrência usa termos temáticos harmonizados manualmente a partir dos títulos e metadados selecionados; não representa palavras-chave fornecidas pelos autores nem resultados bibliométricos de corpus completo.

- [Protocolo: Speech Emotion Recognition e comunicação corporativa](./reviews/ser_corporate_communication.md)
- [Protocolo: economia agêntica em finanças](./reviews/agentic_finance.md)
- [Tabela de extração dos estudos-semente](./data/studies.csv)
- [Script e instruções para as redes de coocorrência](./tools/keyword_network.py)
- [Rede de termos sobre SER corporativo — GraphML](./reports/keyword_networks/ser_corporate_communication.graphml) · [Arestas CSV](./reports/keyword_networks/ser_corporate_communication_edges.csv)
- [Rede de termos sobre economia agêntica — GraphML](./reports/keyword_networks/agentic_finance.graphml) · [Arestas CSV](./reports/keyword_networks/agentic_finance_edges.csv)

Para gerar as tabelas de nós/arestas e os arquivos GraphML, execute na raiz do repositório `python tools/keyword_network.py`. Para validar a ferramenta, execute `python -m pytest`.

**Lacunas preliminares para investigação:** validade e transparência da inferência de emoção em contextos de trabalho; generalização entre idioma, cultura, canal e ambiente acústico; privacidade e governança de voz; e, na economia agêntica, avaliação de negociação além de simuladores, identidade/autorização de agentes, auditabilidade, proteção do consumidor e integração segura com pagamentos. São hipóteses de agenda derivadas de uma amostra pequena, não conclusões de revisão sistemática.

### 01. Scientific Retractions by Brazilian Authors in Engineering

**Scientific Retractions by Brazilian Authors in Engineering: A Descriptive Study Using the Retraction Watch/Crossref Database**

Estudo descritivo sobre retratações científicas envolvendo autores brasileiros na área de Engenharia, utilizando dados da **Retraction Watch/Crossref**.

A análise partiu de uma base contendo **71.106 registros** e investigou inicialmente a ocorrência de retratações relacionadas à Engenharia Biomédica. Como não foram identificados casos específicos dessa área no conjunto analisado, o estudo foi ampliado para diferentes subáreas da Engenharia.

Foram identificados **29 casos**, posteriormente classificados de acordo com os principais motivos de retratação, incluindo problemas relacionados a fraude, erros ou dados, plágio, duplicação e outras razões.

**Competências demonstradas:**

* Data Cleaning
* Data Filtering
* Exploratory Data Analysis
* Descriptive Statistics
* Data Classification
* Scientific Data Analysis
* Scientific Database Analysis
* Research Data Analysis

📄 [**Leia o artigo completo**](artigo_retracoes_engenharia.pdf)

---

### 02. Persistent Availability of Unmarked Retracted Articles in Academic Social Networks

**An analysis of the persistent availability of unmarked retracted articles in academic social networks**

Estudo transversal sobre a permanência de artigos científicos retratados sem indicação clara de retratação em redes acadêmicas, com foco em **ResearchGate** e **Academia.edu**.

Foram analisados artigos retratados de autores brasileiros na área de Ciências da Saúde, publicados entre **2010 e 2020**, utilizando dados da **Retraction Watch**.

Entre os registros analisados, foram selecionadas **66 retratações**. Destas, **22 artigos completos** e **7 resumos** permaneciam disponíveis sem indicação clara de retratação.

Também foram analisadas as citações posteriores à retratação, totalizando **730 citações para os artigos completos** e **166 para os resumos**.

A relação entre o número de citações pós-retratação e o tempo foi investigada por meio da **correlação de Spearman**.

**Competências demonstradas:**

* Data Collection
* Data Cleaning
* Data Filtering
* Exploratory Data Analysis
* Descriptive Statistics
* Correlation Analysis
* Scientific Literature Analysis
* Research Data Analysis

📄 [**Leia o artigo completo**](artigo_retracoes_redes_academicas.pdf)

---

### 03. Problem-Based Learning in Medical Education

**Problem-Based Learning in Medical Education: A Global Research Landscape of the Last Ten Years (2013–2022)**

Estudo bibliométrico sobre a produção científica relacionada à **Aprendizagem Baseada em Problemas (Problem-Based Learning — PBL)** na educação médica entre 2013 e 2022.

A pesquisa utilizou dados da **Web of Science Core Collection** para investigar a evolução da produção científica, os principais periódicos, áreas de pesquisa, países, instituições e padrões de colaboração científica.

O estudo também empregou **análise de redes** para explorar relações e padrões de colaboração na produção científica sobre o tema.

**Competências demonstradas:**

* Bibliometric Analysis
* Scientific Data Analysis
* Data Visualization
* Network Analysis
* Research Analytics
* Scientific Literature Mining
* Collaboration Network Analysis

📄 [**Leia o artigo completo**](artigo_pbl_medical_education.pdf)

🔗 [**Ver publicação na Springer Nature**](https://link.springer.com/article/10.1007/s40670-024-02003-1)

---

## Competências

Este portfólio demonstra experiência principalmente nas seguintes áreas:

**Scientific Data Analysis**

* Data Cleaning
* Data Filtering
* Exploratory Data Analysis
* Descriptive Statistics
* Data Classification

**Bibliometric & Literature Analysis**

* Bibliometric Analysis
* Scientific Literature Mining
* Citation Analysis
* Research Analytics
* Scientific Database Analysis

**Statistical Analysis**

* Descriptive Statistics
* Correlation Analysis
* Spearman Correlation

**Data Visualization & Networks**

* Data Visualization
* Network Analysis
* Collaboration Network Analysis

---

## Sobre

Os projetos apresentados neste repositório fazem parte da minha trajetória acadêmica e de pesquisa em **Engenharia Biomédica, análise de dados científicos e aplicação de métodos quantitativos à pesquisa em saúde e ciência**.

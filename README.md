# 📊 Análise Demográfica dos Estados do Brasil

## 📌 Visão geral

Este projeto tem como objetivo realizar uma **análise exploratória de dados (EDA)** sobre a população dos estados brasileiros, utilizando dados públicos extraídos da Wikipedia. O foco é demonstrar um fluxo básico, porém profissional, de um projeto de **Análise de Dados**, desde a coleta até a geração de insights.

O projeto foi desenvolvido como parte de estudos e construção de **portfólio na área de Dados**.

---

## 🎯 Objetivos do projeto

* Coletar dados populacionais reais a partir de uma fonte pública
* Aplicar boas práticas de organização de dados (camadas *raw* e *clean*)
* Realizar limpeza e padronização dos dados com Python e pandas
* Explorar os dados por meio de estatísticas e análises descritivas
* Gerar insights sobre crescimento populacional nos estados brasileiros

---

## 🗂️ Estrutura do projeto

```
Estados Brasil/
│
├── data/
│   └── clean/
│       └── clean_estados_brasil.
│   ├── raw/
│   │   └── estados_brasil_wikipedia.csv
│
└── README.md
```

---

## 📥 Fonte dos dados

* **Wikipedia** – Lista de unidades federativas do Brasil por população
* Dados referentes às estimativas populacionais de **2024 e 2025**

Os dados foram coletados diretamente da página web e armazenados inicialmente na camada **raw**, sem qualquer tipo de tratamento.

---

## 🧹 Etapas do projeto

### 1️⃣ Coleta de dados

* Extração das tabelas HTML utilizando `pandas.read_html`
* Uso de `User-Agent` para evitar bloqueios HTTP (403)
* Armazenamento dos dados brutos na pasta `data/raw`

### 2️⃣ Limpeza e tratamento

* Remoção de colunas não relevantes para a análise
* Padronização dos nomes das colunas (snake_case)
* Remoção de caracteres especiais, símbolos e espaços invisíveis
* Conversão correta dos tipos de dados (`int` e `float`)
* Salvamento do dataset tratado na camada `data/clean`

---

## 🛠️ Tecnologias utilizadas

* **Python**
* **pandas**
* **Jupyter Notebook**
* **Git / GitHub**

---

## 👤 Autor

Projeto desenvolvido por **João** como parte do aprendizado e construção de portfólio na área de **Análise de Dados**.

---

📌 *Este projeto é educacional e utiliza dados públicos.*

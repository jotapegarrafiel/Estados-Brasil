#%%
import pandas as pd 

df = pd.read_csv("../data/raw/estados_brasil_wikipedia.csv")

df = df.drop(columns=["País comparável (habitantes)[4][a]"])

df.columns = [
    "unidade_federativa",
    "populacao_2025",
    "populacao_2024",
    "variacao_absoluta",
    "variacao_percentual",
    "percentual_total_2025"
]

def limpar_numero(x):
    return (
        x.replace("\xa0", "")
         .replace(".", "")
         .replace(",", ".")
         .replace("%", "")
         .strip()
    )

#%%
colunas_numericas = [
    "populacao_2025",
    "populacao_2024",
    "variacao_absoluta",
    "variacao_percentual",
    "percentual_total_2025"
]

for col in colunas_numericas:
    df[col] = df[col].astype(str).apply(limpar_numero)

#%%
df["populacao_2025"] = df["populacao_2025"].astype(int)
df["populacao_2024"] = df["populacao_2024"].astype(int)
df["variacao_absoluta"] = df["variacao_absoluta"].astype(int)

df["variacao_percentual"] = df["variacao_percentual"].astype(float)
df["percentual_total_2025"] = df["percentual_total_2025"].astype(float)

#%%
df.to_csv("clean/clean_estados_brasil.csv",
          index=False,
          encoding="utf-8")
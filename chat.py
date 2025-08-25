import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# carregar os dados
df = pd.read_csv("ProcessoSeletivo.csv")

# Configuração estética
sns.set(style="whitegrid")

# 1. Sexo
sexo_counts = df['Sexo'].value_counts()
colors = ['#FFB6C1', '#ADD8E6']  # rosa claro, azul claro
plt.figure(figsize=(5,5))
plt.pie(sexo_counts, labels=sexo_counts.index, autopct='%1.1f%%', 
        startangle=90, colors=colors, textprops={'fontsize': 12})
plt.title("Distribuição por Sexo")
plt.show()

# 2. Idade (em faixas)
plt.figure(figsize=(6,4))
sns.histplot(data=df, x="Idade", binwidth=3, color="skyblue", edgecolor="black")
plt.title("Distribuição de Idade")
plt.ylabel("Frequência")
plt.xlabel("Idade")
plt.xticks(range(df['Idade'].min(), df['Idade'].max()+1))  # ticks em cada idade
plt.show()

# 3. Raça/Cor
plt.figure(figsize=(8,4))
sns.countplot(data=df, x="Raça-cor", order=df["Raça-cor"].value_counts().index)
plt.title("Distribuição por Raça/Cor")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.show()

# 4. Orientação Sexual
plt.figure(figsize=(10,4))
sns.countplot(data=df, x="OrientacaoSexual", order=df["OrientacaoSexual"].value_counts().index)
plt.title("Distribuição por Orientação Sexual")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.show()

# 5. Deficiência
plt.figure(figsize=(8,4))
sns.countplot(data=df, x="Deficiência", order=df["Deficiência"].value_counts().index)
plt.title("Distribuição por Deficiência")
plt.ylabel("Frequência")
plt.xticks(rotation=45)
plt.show()

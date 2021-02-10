# Gráficos interativos com o *plotly*

## Gráficos de linha

Vamos começar criando gráficos de linha.

Primeiramente utilizaremos um pacote rápido e eficiente para a construção de gráficos interativos: o **plotly.express**

Para este tipo de plot é conveniente ter apenas um valor possível para a coordenada *y* e ter uma segunda coluna determinando a cor a ser utilizada.

Vamos então refazer nosso exemplo do Covid por regiões.

import plotly.express as px

Preparando o banco de dados para o **plotly.express**:

covid_regioes_px = covid_BR.set_index('data').query('regiao != "Brasil"')[['obitosAcumulado', 'regiao']].reset_index().rename(
    {'obitosAcumulado':'Total de Óbitos','regiao':'Região','data':'Data'},axis=1)
covid_regioes_px = covid_regioes_px.groupby(['Região','Data']).sum()/2
covid_regioes_px = covid_regioes_px.reset_index().set_index('Data')

fig = px.line(covid_regioes_px, y="Total de Óbitos", color="Região",
              line_group="Região", hover_name="Região", title='Óbitos de COVID-19 nas regiões do Brasil')
fig.show()

Podemos fixar o mesmo valor da coordenada *x* para todas as regiões na hora de passar o *mouse*:

fig = px.line(covid_regioes_px, y="Total de Óbitos", color="Região",
              line_group="Região", hover_name="Região", title='Óbitos de COVID-19 nas regiões do Brasil')
fig.update_layout(hovermode='x unified')
fig.show()

Vamos agora construir o mesmo gráfico com o pacote **plotly.graph_objects**.

Não possui a simplicidade do **plotly.express**, porém possui mais flexibilidade e é mais "customizável".

Para exemplificar a utilidade dele, vamos utilizar no conjunto de dados *covid_regioes* que possui 5 colunas distintas como valores de *y*. 

Além disso, veremos que o gráfico com *x* unificado ficará naturalmente melhor no **plotly.graph_objects**.

Muitos argumentos disponíveis no **plotly.graph_objects** não estão disponíveis no **plotly.express**.

import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Norte'], mode='lines', name='Norte'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Nordeste'], mode='lines', name='Nordeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Centro-Oeste'], mode='lines', name='Centro-Oeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Sudeste'], mode='lines', name='Sudeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Sul'], mode='lines', name='Sul'))
fig.update_layout( title='Óbitos de COVID-19 nas regiões do Brasil',
                   xaxis_title='Data', yaxis_title='Total de Óbitos', legend_title_text='Região', hovermode='x unified')

Vamos agora reordenar para melhor apresentação:

fig = go.Figure()
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Sudeste'], mode='lines', name='Sudeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Nordeste'], mode='lines', name='Nordeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Norte'], mode='lines', name='Norte'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Centro-Oeste'], mode='lines', name='Centro-Oeste'))
fig.add_trace(go.Scatter(x=covid_regioes.index, y=covid_regioes['obitos_Sul'], mode='lines', name='Sul'))
fig.update_layout( title='Óbitos de COVID-19 nas regiões do Brasil', 
                  xaxis_title='Data', yaxis_title='Total de Óbitos', legend_title_text='Região', hovermode='x unified')

## Gráficos de coluna

fig = px.bar(covid_Regioes.reset_index().rename({'regiao':'Região','obitosNovos':'Total de Óbitos'}, axis=1), 
                                                x='Região', y='Total de Óbitos', 
                                                title='Óbitos por COVID-19 nas Regiões do Brasil')
fig.show()

Neste caso é bem simples fazer este gráfico com **graph_objects**:

covid_coluna = covid_Regioes.reset_index().rename({'regiao':'Região','obitosNovos':'Total de Óbitos'}, axis=1)

fig = go.Figure([go.Bar(x=covid_coluna['Região'], y=covid_coluna['Total de Óbitos'])])
fig.update_layout( title='Óbitos de COVID-19 nas regiões do Brasil', 
                  xaxis_title='Região', yaxis_title='Total de Óbitos')
fig.show()

covid_coluna = covid_Regioes.reset_index().rename({'regiao':'Região','obitosNovos':'Total de Óbitos'}, axis=1)
covid_coluna['Até 18/07/2020'] = '' #Criamos uma coluna igual para todos para servir de coordenada x
fig = px.bar(covid_coluna, 
                                                x='Até 18/07/2020', y='Total de Óbitos', color='Região',
                                                title='Óbitos por COVID-19 nas Regiões do Brasil',
             barmode='group') #Esse argumento coloca as colunas lado a lado
fig.show()

Vamos recriar o gráfico anterior com **graph_objects**, neste caso sem colocar nenhuma informação no eixo *x*.

fig = go.Figure(data=[
    go.Bar(name='Norte', x=['Óbitos'], y=covid_Regioes.loc['Norte']),
    go.Bar(name='Nordeste', x=['Óbitos'], y=covid_Regioes.loc['Nordeste']),
    go.Bar(name='Centro-Oeste', x=['Óbitos'], y=covid_Regioes.loc['Centro-Oeste']),
    go.Bar(name='Sudeste', x=['Óbitos'], y=covid_Regioes.loc['Sudeste']),
    go.Bar(name='Sul', x=['Óbitos'], y=covid_Regioes.loc['Sul'])
])
fig.update_layout(barmode='group', title='Óbitos por COVID-19 nas Regiões do Brasil', 
                  yaxis_title='Total de Óbitos', legend_title_text='Região')
fig.update_xaxes(showticklabels=False)
fig.show()

fig = px.bar(covid_coluna, x='Até 18/07/2020', y='Total de Óbitos', color='Região',
                                                title='Óbitos por COVID-19 nas Regiões do Brasil')
#Sem o argumento barmode='group' ficamos com as colunas empilhadas
fig.show()

fig = go.Figure(data=[
    go.Bar(name='Norte', x=['Óbitos'], y=covid_Regioes.loc['Norte']),
    go.Bar(name='Nordeste', x=['Óbitos'], y=covid_Regioes.loc['Nordeste']),
    go.Bar(name='Centro-Oeste', x=['Óbitos'], y=covid_Regioes.loc['Centro-Oeste']),
    go.Bar(name='Sudeste', x=['Óbitos'], y=covid_Regioes.loc['Sudeste']),
    go.Bar(name='Sul', x=['Óbitos'], y=covid_Regioes.loc['Sul'])
])
fig.update_layout(barmode='stack', title='Óbitos por COVID-19 nas Regiões do Brasil', 
                  yaxis_title='Total de Óbitos', legend_title_text='Região')
fig.update_xaxes(showticklabels=False)
fig.show()

## Gráfico de Setores

O método *pie* das bibliotecas **plotly.express** e **plotly.graph_objects** são bastante imediatos e se assemelham muito ao que vimos anteriormente para o **matplotlib**.

fig = px.pie(covid_Regioes_pct, values='obitosNovos', names=covid_Regioes_pct.index, 
             title = 'Distribuição dos Óbitos por COVID-19 nas Regiões do Brasil até 18/07/2020')
fig.show()

fig = go.Figure(data=[go.Pie(labels=covid_Regioes_pct.index, values=covid_Regioes_pct.obitosNovos, 
                             pull=covid_Regioes_pct.explodir)])
fig.update_layout(title='Distribuição dos Óbitos por COVID-19 nas Regiões do Brasil até 18/07/2020', 
                  yaxis_title='Total de Óbitos', legend_title_text='Região')
fig.show()

## Gráfico de Dispersão

Na prática os gráficos de linha e de dispersão são realizados com o mesmo método no **plotly.graph_objects**. Já no **plotly.express** é análogo ao método que vimos para o **matplotlib**. 

df_exemplo_px = pd.DataFrame(df_exemplo['coluna_1']).rename({'coluna_1':'Valor'}, axis=1)
df_exemplo_px['Coluna'] = 'Coluna 1' 
df_exemplo_px_temp = pd.DataFrame(df_exemplo['coluna_2']).rename({'coluna_2':'Valor'}, axis=1)
df_exemplo_px_temp['Coluna'] = 'Coluna 2'
df_exemplo_px = pd.concat([df_exemplo_px, df_exemplo_px_temp])
df_exemplo_px_temp = pd.DataFrame(df_exemplo['coluna_3']).rename({'coluna_3':'Valor'}, axis=1)
df_exemplo_px_temp['Coluna'] = 'Coluna 3'
df_exemplo_px = pd.concat([df_exemplo_px, df_exemplo_px_temp])
df_exemplo_px.head()

fig = px.scatter(df_exemplo_px, x=df_exemplo_px.index, y='Valor', color='Coluna')
fig.show()

Utilizando o pacote podemos trabalhar diretamente com o *df_exemplo*:

fig = go.Figure()
fig.add_trace(go.Scatter(x=df_exemplo.index, y=df_exemplo['coluna_1'], mode='markers', name='Coluna 1'))
fig.add_trace(go.Scatter(x=df_exemplo.index, y=df_exemplo['coluna_2'], mode='markers',name='Coluna 2'))
fig.add_trace(go.Scatter(x=df_exemplo.index, y=df_exemplo['coluna_3'], mode='markers',name='Coluna 3'))
fig.update_layout( title='Gráfico de Dispersão do df_exemplo',
                   xaxis_title='Data', yaxis_title='Valor', legend_title_text='Coluna')

## Histograma

Com o **plotly.express** podemos aplicar o método diretamente com poucas diferenças entre os argumentos. Vemos que no lugar de *bins*, devemos utilizar *nbins* e no lugar de *alpha*, devemos combinar *barmode='overlay'* com *opacity*.

Vamos preparar o banco de dados para o histograma.

covid_regioes_diarios = pd.DataFrame()

regioes = covid_BR.query('regiao != "Brasil"')['regiao'].drop_duplicates().array

for regiao in regioes:
    temp_series = covid_BR.set_index('data').query('regiao == @regiao')['obitosNovos'].groupby('data').sum()/2
    temp_series.name = 'obitos_' + regiao
    covid_regioes_diarios = pd.concat([covid_regioes_diarios, temp_series], axis=1)
    
covid_regioes_diarios.index = pd.to_datetime(covid_regioes_diarios.index)
covid_regioes_diarios

fig = px.histogram(covid_regioes_diarios.obitos_Nordeste, nbins=30, title='''
Distribuição da quantidade de óbitos diários de COVID-19 no nordeste do Brasil
                   ''')
fig.show()

covid_regioes_diarios_px = covid_BR.set_index(
    'data').query('regiao != "Brasil"')[['obitosNovos', 'regiao']].reset_index().rename(
    {'obitosNovos':'Óbitos','regiao':'Região','data':'Data'},axis=1)
covid_regioes_diarios_px = covid_regioes_diarios_px.groupby(['Região','Data']).sum()/2
covid_regioes_diarios_px = covid_regioes_diarios_px.reset_index().set_index('Data')

fig = px.histogram(covid_regioes_diarios_px, nbins=30, color='Região', opacity=0.5, barmode='overlay', title='''
Distribuição da quantidade de óbitos diários de COVID-19 nas regiões do Brasil
                   ''')
fig.show()

Agora vejamos com **plotly.graph_objects**:

def fazer_histograma_plotly():
    fig = go.Figure()
    fig.update_layout(barmode='overlay', title='''
Distribuição da quantidade de óbitos diários de COVID-19 nas regiões do Brasil
                   ''',
                     yaxis_title="Quantidade de Dias", xaxis_title="Óbitos",legend_title_text='Região')
    fig.add_trace(go.Histogram(x=covid_regioes_diarios['obitos_Norte'], name='Norte'))
    fig.add_trace(go.Histogram(x=covid_regioes_diarios['obitos_Nordeste'], name='Nordeste'))
    fig.add_trace(go.Histogram(x=covid_regioes_diarios['obitos_Centro-Oeste'],  name='Centro-Oeste'))
    fig.add_trace(go.Histogram(x=covid_regioes_diarios['obitos_Sudeste'], name='Sudeste'))
    fig.add_trace(go.Histogram(x=covid_regioes_diarios['obitos_Sul'],  name='Sul'))
    fig.update_traces(opacity=0.5, xbins={'size':50})
    fig.show()

fazer_histograma_plotly()

## BoxPlot

No **plotly** os argumentos do *boxplot* são muito semelhantes aos do histograma, mudando essencialmente que o argumento dos dados no histograma é *x* e do *boxplot* é *y*.

fig = px.box(df_exemplo_px, x="Coluna", y="Valor")
fig.show()

fig = px.box(covid_regioes_diarios_px, x="Região", y="Óbitos")
fig.show()

fig = px.box(covid_regioes_diarios_px, x='Região', y='Óbitos', notched=True, color='Região',
            title='Distribuição da quantidade de óbitos diários de COVID-19 nas regiões do Brasil')
fig.show()

def fazer_boxplot_plotly():
    fig = go.Figure()
    fig.update_layout(barmode='overlay', title='''
Distribuição da quantidade de óbitos diários de COVID-19 nas regiões do Brasil
                   ''',
                     yaxis_title="Óbitos", legend_title_text='Região')
    fig.add_trace(go.Box(y=covid_regioes_diarios['obitos_Norte'], name='Norte'))
    fig.add_trace(go.Box(y=covid_regioes_diarios['obitos_Nordeste'], name='Nordeste'))
    fig.add_trace(go.Box(y=covid_regioes_diarios['obitos_Centro-Oeste'],  name='Centro-Oeste'))
    fig.add_trace(go.Box(y=covid_regioes_diarios['obitos_Sudeste'], name='Sudeste'))
    fig.add_trace(go.Box(y=covid_regioes_diarios['obitos_Sul'],  name='Sul'))
    fig.show()

fazer_boxplot_plotly()
# COVID-19 Dashboard

Um dashboard interativo e responsivo para análise de dados da pandemia COVID-19, desenvolvido com Django, Chart.js e Bootstrap. O sistema apresenta visualizações comparativas entre países selecionados com dados em tempo real.

## 📊 Funcionalidades

### Visualizações Disponíveis
- **Evolução Temporal**: Gráfico de linha mostrando a curva epidemiológica com ascensão, pico e declínio
- **Distribuição Geográfica**: Comparação de casos entre países selecionados
- **Eficiência do Sistema de Saúde**: Correlação entre gastos em saúde e taxa de mortalidade
- **Impacto Econômico**: Análise da relação entre mortalidade e impacto econômico
- **Comparação por Continente**: Dados agrupados por região
- **Ranking de Desempenho**: Classificação dos países baseada em múltiplos indicadores

### Países Incluídos
- Global (dados mundiais)
- Brasil
- Estados Unidos
- Reino Unido
- Alemanha
- França
- Índia
- Rússia

## 🚀 Tecnologias Utilizadas

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualização**: Chart.js 4.4.0
- **Interface**: Bootstrap 5.3.8
- **APIs**: Disease.sh COVID-19 API
- **Responsividade**: CSS Grid e Flexbox

## 📁 Estrutura do Projeto

```
covid-dashboard/
│
├── static/
│   ├── css/
│   │   └── style.css           # Estilos personalizados
│   └── js/
│       └── charts.js           # Lógica dos gráficos
│
├── templates/
│   └── dashboard.html          # Template principal
│
└── README.md
```

## ⚙️ Instalação e Configuração

### Pré-requisitos
- Python 3.8+
- Django 4.0+
- Conexão com internet (para APIs externas)

### Instalação
```bash
# Clone o repositório
git clone [seu-repositorio]
cd covid-dashboard

# Instale as dependências
pip install django

# Execute o servidor de desenvolvimento
python manage.py runserver
```

### Configuração Django
```python
# settings.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
```



## 🔗 APIs Utilizadas

### API Principal
```javascript
https://disease.sh/v3/covid-19/countries
```

### API de Dados Históricos
```javascript
https://disease.sh/v3/covid-19/historical/{country}?lastdays=1200
```

### Fallback API
```javascript
https://api.covid19api.com/summary
```

## 📱 Responsividade

O dashboard é totalmente responsivo, adaptando-se a:
- **Desktop**: Layout completo com todos os gráficos
- **Tablet**: Gráficos em 2 colunas
- **Mobile**: Layout vertical com gráficos empilhados


### Modificar Países
Para alterar a lista de países, edite:
```javascript
// charts.js
this.allowedCountries = ['Brazil', 'USA', ...];
this.allowedCountryCodes = ['BR', 'US', ...];
```

## 🔧 Solução de Problemas

### Chart.js não carrega
- Verifique a conexão com internet
- O sistema possui fallback para arquivo local

### Dados não aparecem
- Confirme se as APIs estão acessíveis
- Verifique o console do navegador para erros

### Layout quebrado
- Confirme se o Bootstrap está carregando corretamente
- Verifique se os arquivos CSS estão sendo servidos

## 📈 Recursos Avançados

### Análise Epidemiológica
- Identificação automática do pico da pandemia
- Cálculo de fases (ascensão, pico, declínio)
- Estatísticas detalhadas por período

## 📊 Indicadores Calculados

- **Taxa de Letalidade**: (Mortes / Casos) × 100
- **Casos per Capita**: Casos / População
- **Score de Performance**: Baseado em múltiplos fatores
- **Impacto Econômico**: Estimativa baseada em mortalidade

## 🤝 Contribuição

Para contribuir com o projeto:
1. Faça um fork do repositório
2. Crie uma branch para sua feature
3. Implemente as modificações
4. Teste em diferentes dispositivos
5. Submeta um pull request

## 📄 Licença

Este projeto é de uso educacional e acadêmico. Os dados são fornecidos por APIs públicas e devem ser utilizados respeitando os termos de uso das fontes originais.

## ⚠️ Disclaimer

Os dados apresentados são para fins informativos e educacionais. Para decisões médicas ou de saúde pública, consulte sempre fontes oficiais como OMS, ministérios da saúde e instituições especializadas.
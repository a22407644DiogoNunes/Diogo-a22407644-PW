# Modelação

<img src="media/IMG_20260424_230347.jpg" width="300">

1. ligação Licenciatura-Docente é N para N, pois um curso por exemplo Licenciatura Engenharia Informatica tem varios docentes/professores ao mesmo tempo que esse docente pode estar em varios cursos
2. ligação Licenciatura-Unidade_Curricular tembem é N para N pelo mesmo motivo que Licenciatura-Docente exemplo, tanto Engenharia Informatica e Engenharia Informatica de Redes e Telecumincações tem uma unidade curricular chamada Redes e Telecuminações
3. ligação Unidade_Curricular-Docente é N para N, pelo mesmo motivo da ligação Licenciatura-Docente o mesmo Docente pode dar varias cadeiras no mesmo semestre
4. ligação Unidade_Curricular-Tecnologias é N para N, Java esta presente em Algoritmia de Dados e LP2 ou Desenvolvimento de Interface Web usa HTML, CSS, JavaScript, Next, Vercel,...
5. ligação Unidade_Curricular-Projeto aqui já faz sentido sser ligação de 1 para N pois o projeto foi desenvolvido apenas para aquela cadeira exemplo o Portfolia é desenvolvida para Programação Web, mas Programação web terá varios projetos
6. ligação Tecnologia-TFC é N para N, pois um TFC como podemos ver no JSON tem varias tecnologias, essas que tambem são usadas em varios TFCs
7. ligação Tecnologia-Formação é N para N, pois uma formação pode abordar varias tecnologias no qual essa mesmas tecnologias pode estar em varias formações
8. ligação Tecnologia-Projetos é N para N, sendo a mesma logica do Tecnologia-TFC
9. ligação Competecias-Projetos é N para N, pois o desemvolvimento de um projeto pode dar varias competencias tanto tecnicas como socias, competencias essa que podem ser reforçadas com o desenvolvimento de mais projetos
10. ligação Competencias-Tecnologia é 1 para N, pois não é possivel a pessoa ter a mesma competencia neste caso técnica duas vezes, nesse caso seria só repetição de informação na nossa base de dados

# Dificuldades e Erros
1. Dificuldades numa pequena questão de lógica mas com ajuda de AI lá consegui resolver

# Usei AI no que?
1. Usei para ajudar a finalizar a modelação, pois é muito chato estar a escrever "nome = models.CharField(max_length=100)" fazendo a mão as tres primeiras classes depois pedi para fazer o resto usando o que já tinha como modelo, para evitar alucinação.
2. Usei para ajudar a resolver um problema na minha logica no loader.

## Lab7

#Dificuldades e Erros
1. Honestamente não muitos mas os urls ainda tenho que trabalhar um pouco mais pois perco-me um pouco com os varios nomes

# Usei Ai no que?
1. Usei para me ajudar a fazer os html e o css
2. Usei para me ajudar os erros que tinha no urls resumidamente era so erros de caminhos nada de muito grave

## Lab 9 - Autenticação

# Modelação

1. Criação da app `accounts` para gerir toda a autenticação do projeto
2. Uso do modelo `User` já incluído no Django, sem necessidade de criar models próprios
3. Criação do modelo `PerfilUtilizador` com ligação 1 para 1 ao `User`, para guardar o token do link mágico
4. Criação da app `artigos` com o modelo `Artigo` ligado ao `User` por uma relação N para 1 (vários artigos podem pertencer ao mesmo autor)
5. Modelo `Artigo` tem ligação N para N com `User` para os likes, pois vários utilizadores podem gostar de vários artigos
6. Modelo `Comentario` ligado ao `Artigo` por 1 para N, pois um artigo pode ter vários comentários, e ligado ao `User` também por 1 para N pois um utilizador pode fazer vários comentários

# Dificuldades e Erros
1. Dificuldade em perceber que o `base.html` estava em `escola/base.html` e não em `base.html` diretamente, o que causou um `TemplateDoesNotExist`
2. Erro `NoReverseMatch` porque o nome da URL da página principal era `portfolio_home` e não `portfolio`
3. Erro `MultipleObjectsReturned` no link mágico porque havia dois utilizadores com o mesmo email na base de dados, resolvido com `filter().first()` em vez de `get()`
4. Dificuldade em configurar o email do Gmail pois a conta era escolar e não permitia criar app passwords, resolvido usando a conta pessoal com verificação em dois passos ativa

# Usei AI no que?
1. Quando estava a implementar a app `accounts` fui buscar ajuda para perceber como estruturar tudo junto — o AI funcionou como um guia para não me perder entre os vários ficheiros
2. Na parte do link mágico precisei de apoio para ligar as peças todas, o conceito estava nos slides mas a implementação tinha alguns detalhes que não eram óbvios
3. Na app `artigos` usei para não ter de escrever tudo do zero, explicava o que queria e ia ajustando o resultado ao meu projeto
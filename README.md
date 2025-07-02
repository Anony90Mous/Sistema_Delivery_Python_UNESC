<h1>Sistema_Delivery_Python_UNESC</h1>
<p>Projeto/Trabalho Final da disciplina <em><strong>Resolução de Problemas Estruturados I</strong></em> do curso <em><strong>Ciência da Computação</strong></em> na <strong>UNESC</strong></p>
<p>Este projeto oferece uma aplicação interativa com interface gráfica construída com a biblioteca customtkinter, permitindo gerenciar pedidos de delivery de forma prática e intuitiva. O sistema realiza validação de dados com <code><em>regex</em></code>, ordenação cronológica de pedidos com o algoritmo <code><strong>Merge Sort</strong></code> e armazenamento eficiente em arquivos <code>.json</code>.</p>
<hr>
<h2>Objetivo</h2>
<p>Desenvolver um sistema de delivery com interface gráfica utilizando Python e a biblioteca customtkinter, com foco em praticidade e organização dos pedidos utilizando mergeSort. O sistema permite ao usuário:</p>
<ul>
  <li>Preencher os dados do cliente e horário do pedido <code><strong>Horário Preenchido Automaticamente ou Manualmente</strong></code></li>
  <li>Selecionar itens de um cardápio</li>
  <li>Visualizar o resumo do pedido com cálculo automático do total</li>
  <li>Finalizar e salvar pedidos em formato <code>.json</code></li>
  <li>Visualizar todos os pedidos em ordem cronológica, utilizando o algoritmo de ordenação Merge Sort</li>
  <li>Validar a entrada de data/hora com expressões regulares<em> (regex)</em> e <code>datetime</code></li>
  <li>Limpar os pedidos registrados, quando necessário</li>
</ul>
<hr>
<h2>Tecnologia</h2>
<ul>
  <li>Python 3.13.5 <em>(versão de desenvolvimento</em>) – Linguagem principal do projeto</li>
  <li>CustomTkinter – Biblioteca para criação da interface gráfica com visual moderno <em>(Necessario a instalação da biblioteca com <code>pip install customtkinter</code>)</em></li>
  <li>JSON – Para armazenamento e leitura dos pedidos finalizados</li>
  <li>Regex <code><em>(re)</em></code> – Para validação do formato de data e hora</li>
  <li>Datetime – Para manipulação e ordenação das datas e horários</li>
  <li><code>OS</code> – Para verificação e manipulação de arquivos locais</li>
</ul>
<hr>
<h2>Uso</h2>
<ul>
  <li>Preencha o nome, endereço e horário do cliente <em>(o campo de horário já vem preenchido automaticamente com a data e hora atual)</em></li>
  <li>Selecione os itens desejados no cardápio marcando as caixas de seleção</li>
  <li>Acompanhe o resumo da compra e o valor total na área inferior da tela</li>
  <li>Clique em <strong>Finalizar Compra</strong> para salvar o pedido</li>
  <li>Use o botão <strong>Mostrar Pedidos</strong> para visualizar todos os pedidos finalizados, ordenados por horário.</li>
  <li>Na nova janela, você também pode <strong>limpar todos os pedidos</strong> com um clique</li>
</ul>
<hr>
<h2>Instalação</h2>
<ol>
  <li>
    <strong>Clone o repositório</strong>
    <pre><code>git clone https://github.com/Anony90Mous/Sistema_Delivery_Python_UNESC.git
cd Sistema_Delivery_Python_UNESC</code></pre>
  </li>
  <li>Certifique-se de que o Python está instalado <em>(versão recomendada: Python 3.13.5)</em></li><br>
  <li>
    Instale as dependências (caso necessário)
    <pre><code>pip install customtkinter</code></pre>
  </li>
  <li>
    Execute o programa
    <pre><code>python main.py</code></pre>
  </li>
</ol>
<hr>
<h2>Equipe</h2>
<ul>
  <li>Bryan Pereira Gonçalves — [GitHub](https://github.com/bryanpg18)</li></li>
  <li>Davi Mendes</li>
  <li>Karen Suélen da Silva</li>
  <li>Luiz Othavio — [GitHub](https://github.com/Anony90Mous)</li>
  <li>Miguel Alexandre Pickler Domingues</li>
  <li>Pedro Henrique Moroso da Silva</li>
</ul>
<h2>Lincença</h2>
<p>Este projeto está licenciado sob os termos da licença <strong>MIT</strong> © 2025.</p>
<p>Você é livre para usar, modificar e distribuir este código, desde que mantenha os créditos aos autores.</p>
<hr>

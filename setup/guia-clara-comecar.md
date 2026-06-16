# Começar a usar seu segundo cérebro com o Claude — guia da Clara

Oi, Clara! Este é o passo a passo pra você conversar com a sua pasta de conteúdo (o "segundo cérebro") direto do seu Mac, sem precisar de nada de programador. **Sem terminal, sem código.** Só dois aplicativos com botões.

A ideia em uma frase: você abre um app, aponta pra sua pasta e **conversa em português** — "registra esse insight", "monta a pauta da semana", "transforma isso em roteiro". O Claude lê e escreve os arquivos pra você.

Você vai usar **dois apps**:

| App | Pra que serve | Pense nele como... |
|---|---|---|
| **Claude** (Claude Desktop) | conversar com seus arquivos, criar e editar conteúdo | seu assistente / editor |
| **GitHub Desktop** | trazer o que o Marquito atualizou e enviar o seu trabalho pra ele | o botão de sincronizar |

---

## Parte 1 — Configuração (uma vez só, melhor fazer junto com o Marquito)

São cinco passos. Depois disso você nunca mais precisa repetir.

**1. Assine o Claude Pro**
Entre em [claude.ai](https://claude.ai), crie sua conta e assine o plano **Pro** (cerca de US$ 20/mês). É necessário: a parte de trabalhar com pastas **não funciona no plano grátis**.

**2. Instale o app do Claude (Mac)**
- Baixe em [claude.ai/download](https://claude.ai/download) (versão para Mac).
- Abra o arquivo baixado e **arraste o ícone do Claude para a pasta Aplicativos**.
- Abra o Claude e faça login com a mesma conta do passo 1.

**3. Crie uma conta no GitHub e peça acesso ao Marquito**
- Crie uma conta grátis em [github.com](https://github.com).
- Mande seu nome de usuário pro Marquito. Ele te adiciona como colaboradora da pasta `mclara-constelacao` (você recebe um convite por e-mail — é só aceitar).

**4. Instale o GitHub Desktop**
- Baixe em [desktop.github.com](https://desktop.github.com), arraste pra Aplicativos e abra.
- Faça login com a sua conta do GitHub (a do passo 3).

**5. Baixe a pasta pro seu Mac**
- No GitHub Desktop: menu **File → Clone repository**.
- Escolha **mclara-constelacao** na lista.
- Escolha onde salvar (sugestão: a pasta **Documentos**) e clique **Clone**.
- Pronto — a pasta inteira está no seu computador.

---

## Parte 2 — Seu dia a dia (você sozinha, tranquila)

Sempre na mesma ordem: **pegar novidades → trabalhar → enviar**. Esse hábito evita que você e o Marquito se atrapalhem.

### ▶ Antes de começar — pegar as novidades
Abra o **GitHub Desktop** e clique em **"Pull origin"** (ou "Fetch origin", que vira "Pull"). Isso traz o que o Marquito mexeu desde a última vez.

### ✍ Trabalhar — conversar com o Claude
1. Abra o app do **Claude** e clique na aba **Code**.
2. Clique em **"Open folder"** e escolha a pasta **mclara-constelacao** (lá em Documentos).
3. Escreva na caixa de texto, em português normal, o que você quer. Aperte Enter.
4. Quando ele for mudar algum arquivo, ele **pede sua permissão antes** — pode deixar.

**Palavras mágicas que o sistema entende** (pode digitar qualquer uma delas):

| Você digita | O que acontece |
|---|---|
| `captura` | registrar um insight que veio depois de uma sessão (pode mandar até por áudio) |
| `pauta` | montar/atualizar a pauta da semana |
| `triagem` | organizar materiais novos que você jogou na pasta `_inbox` |
| `status` | ver em que pé está cada conteúdo |
| `retro` | anotar os números reais dos posts da semana |

Você não precisa decorar nada: pode simplesmente dizer "acabei uma sessão e tive um insight bom, quero guardar" — ele entende.

### ■ Ao terminar — enviar pro Marquito
1. Volte no **GitHub Desktop**. Ele mostra tudo o que mudou.
2. No campo **Summary** (canto inferior esquerdo), escreva uma frase curta do que fez — ex.: *"Roteiros da semana"*.
3. Clique **"Commit to main"** e depois **"Push origin"**. Enviado. ✅

> Atalho preguiçoso: se esquecer o GitHub Desktop, pode pedir pro próprio Claude — *"salve e envie meu trabalho pro GitHub"* — que ele faz. Mas no começo o GitHub Desktop é melhor, porque ele te **mostra** o que mudou antes de enviar.

---

## Coisas boas de saber (sem susto)

- **Custo:** só os ~US$ 20/mês do Claude Pro. Mais nada. Se alguém falar em "API key", ignore — não é o seu caso e é o que poderia gerar cobrança por uso.
- **Use a aba "Code"**, não a "Cowork" (a Cowork gasta mais e é pra outra coisa).
- **Guarde a pasta num lugar pessoal** (Documentos), nunca em pastas do sistema.
- **Conversa muito longa ficou lenta?** Comece uma conversa nova — é normal.
- **A regra de ouro do sistema:** o Claude é seu **editor, nunca seu autor**. Todo conteúdo nasce de algo seu e termina com a sua aprovação. O martelo final é sempre seu.

Qualquer dúvida, chama o Marquito — e bom trabalho. ✨

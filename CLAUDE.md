# mclara-constelacao

Workspace ICM da Maria Clara Germano — terapeuta sistêmica com trabalho em constelação familiar, foco em mulheres (autonomia emocional, relacionamentos). Sistema de produção de conteúdo para Instagram a partir de insights reais de sessão.

**Comportamento padrão:** editora de conteúdo a serviço da voz da Maria Clara. A IA é **editora, nunca autora** — todo conteúdo nasce de um input dela (um áudio, duas frases, um parágrafo) e termina com aprovação dela. Nada é publicado sem o martelo final da Clara.

**Regras de primeira classe (carregar sempre, em qualquer tarefa):**

- `shared/compliance-cfp-cdc.md` — ela NÃO é psicóloga registrada; restrições legais de comunicação
- `voice/anti-padroes.md` — o que o sistema recusa mesmo que "funcione"

## Folder Map

```
mclara-constelacao/
├── CLAUDE.md                       (você está aqui)
├── CONTEXT.md                      (roteamento de tarefas)
├── _inbox/                         (entrada bruta: áudios, ideias soltas, materiais novos)
├── voice/                          ★ PRODUTO 1 — a voz da Clara por escrito
│   ├── identity.md                 (quem ela é, valores, posicionamento)
│   ├── voice-rules.md              (tom, vocabulário, sintaxe)
│   ├── examples.md                 (trechos reais dela)
│   └── anti-padroes.md             (o que nunca sai deste sistema)
├── shared/
│   ├── compliance-cfp-cdc.md       (restrições legais — primeira classe)
│   └── limites-de-producao.md      (ritmo, horas, capacidade de leads)
├── knowledge-base/
│   ├── materiais-atendimentos/     (o que ela ensina nas sessões)
│   ├── dores-de-clientes/          (o que a audiência pergunta — combustível de pauta)
│   └── posts-referencia/           (como ela soa — reels selecionados por ela)
├── stages/
│   ├── 01-captura/                 (áudio/insight pós-sessão → ideia registrada)
│   ├── 02-pauta/                   (banco de ideias → pauta semanal priorizada)
│   ├── 03-roteiro/                 (pauta → draft com gancho de 3s + legenda)
│   ├── 04-revisao/                 (draft → aprovação da Clara + checklist)
│   └── 05-publicacao/              (aprovado → ficha de publicação + métricas reais)
└── setup/
    └── questionnaire.md            (onboarding quando ela assumir o sistema)
```

## Triggers

| Palavra-chave | Ação |
|---|---|
| `setup` | Roda o questionário de onboarding |
| `status` | Mostra completude do pipeline (varre `stages/*/output/`) |
| `triagem` | Processa o `_inbox/`: propõe destino para cada item |
| `captura` | Inicia registro de um insight novo no Stage 01 |
| `pauta` | Gera/atualiza a pauta semanal no Stage 02 |
| `retro` | Preenche métricas reais das publicações da semana no Stage 05 |

## Routing

| Tarefa | Vá para |
|---|---|
| Registrar insight pós-sessão | `stages/01-captura/CONTEXT.md` |
| Montar pauta da semana | `stages/02-pauta/CONTEXT.md` |
| Escrever roteiro/draft | `stages/03-roteiro/CONTEXT.md` |
| Revisar e aprovar conteúdo | `stages/04-revisao/CONTEXT.md` |
| Planejar publicação / registrar métricas | `stages/05-publicacao/CONTEXT.md` |
| Consultar/editar a voz | `voice/CONTEXT.md` |
| Consultar materiais dela | `knowledge-base/CONTEXT.md` |
| Triar material novo | `_inbox/CONTEXT.md` |

## What to Load

| Tarefa | Carregar | NÃO carregar |
|---|---|---|
| Captura | `stages/01-captura/CONTEXT.md`, `shared/compliance-cfp-cdc.md` | `voice/` completo, stages 02-04 |
| Pauta | `stages/02-pauta/CONTEXT.md`, ideias do stage 01, `knowledge-base/dores-de-clientes/`, `shared/limites-de-producao.md` | `voice/examples.md`, stages 03-04 |
| Roteiro | `stages/03-roteiro/CONTEXT.md`, pauta do stage 02, `voice/` completo, `shared/compliance-cfp-cdc.md` | `knowledge-base/materiais-atendimentos/` (só o arquivo citado na pauta) |
| Revisão | `stages/04-revisao/CONTEXT.md`, draft do stage 03, `voice/voice-rules.md`, `voice/anti-padroes.md`, `shared/compliance-cfp-cdc.md` | stages 01-02 |
| Publicação | `stages/05-publicacao/CONTEXT.md`, aprovado do stage 04, `shared/limites-de-producao.md` | `voice/`, stages 01-03 |

## Stage Handoffs

Cada stage escreve em `output/`; o seguinte lê de lá. Edições humanas entre stages são bem-vindas — o stage seguinte pega a versão editada.

Cada ideia recebe um slug curto na captura (ex.: `ferida-rejeicao-perfeccionismo`) que prefixa os arquivos dela ao longo do pipeline.

## Idioma

Tudo em português brasileiro — pipeline interno e conteúdo final. A Clara opera este workspace; clareza vale mais que jargão técnico.

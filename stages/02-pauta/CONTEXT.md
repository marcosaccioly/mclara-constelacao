# Stage 02 — Pauta

**Entrada:** banco de ideias (`stages/01-captura/output/`, status `banco`) + métricas da semana anterior (`stages/05-publicacao/output/`, quando existirem).
**Saída:** `output/pauta-<AAAA>-s<NN>.md` — a pauta da semana, priorizada.

## Regras de priorização

1. **Máximo 5 itens, ideal 3** (`shared/limites-de-producao.md`). Pauta enxuta é feature.
2. Prioridade pra ideias que respondem dores reais (`knowledge-base/dores-de-clientes/`).
3. Variar temas na semana — não esgotar um tema em sequência.
4. Se houver métricas do Stage 05: o que gerou salvamentos/DMs sobe, o que gerou só likes não pesa.
5. A Clara bate o martelo na pauta antes do Stage 03 rodar.

## Formato da pauta

```markdown
# Pauta <AAAA> — semana <NN>

| # | Slug | Tema | Dor que responde | Por que agora |
|---|------|------|------------------|---------------|

## Aprovação da Clara: pendente | aprovada em <data> (com ajustes: ...)
```

Ao pautar uma ideia, atualizar o status dela no Stage 01 para `pautado`.

## Carregar

- Ideias com status `banco` do Stage 01
- `knowledge-base/dores-de-clientes/`
- `shared/limites-de-producao.md`
- Última retro de métricas do Stage 05 (se houver)

## NÃO carregar

- `voice/examples.md`, `knowledge-base/materiais-atendimentos/` — pauta decide O QUE, não COMO.

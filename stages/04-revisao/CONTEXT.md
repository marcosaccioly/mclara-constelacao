# Stage 04 — Revisão

**Entrada:** roteiro do Stage 03.
**Saída:** `output/<slug>-aprovado.md` — conteúdo com aprovação explícita da Clara, pronto pro Stage 05.

## O que acontece aqui

1. **Checagem formal** (IA): rodar os dois checklists —
   - `voice/anti-padroes.md` (cheiro de IA, positividade tóxica, polarização, urgência fabricada, pregação)
   - `shared/compliance-cfp-cdc.md` (checklist no final do arquivo)
2. **Veredito de voz** (IA, conservador): isso soa como os trechos de `voice/examples.md`? Na dúvida, marcar o trecho e perguntar — não "corrigir" silenciosamente.
3. **Aprovação da Clara** (humana, obrigatória): ela lê/ouve, ajusta o que quiser e bate o martelo. **Nada segue pro Stage 05 sem isso.** O ajuste dela é dado de ouro: registrar o que ela mudou.

## Formato da saída

```markdown
# <slug> — aprovado

**Roteiro-fonte:** stages/03-roteiro/output/<slug>-roteiro.md
**Aprovado pela Clara em:** <data>

## Versão final
<roteiro + legenda como aprovados>

## O que ela mudou (alimenta a evolução da voz)
- <mudança> → <o que isso ensina sobre a voz dela>
```

Mudanças recorrentes dela viram proposta de atualização em `voice/voice-rules.md`.

## Carregar

- Draft do Stage 03
- `voice/voice-rules.md`, `voice/anti-padroes.md`, `voice/examples.md`
- `shared/compliance-cfp-cdc.md`

## NÃO carregar

- Stages 01-02, `knowledge-base/` — a revisão olha o artefato, não a origem.

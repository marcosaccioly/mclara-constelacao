# Stage 01 — Captura

**Entrada:** um insight bruto da Clara — áudio gravado ao sair da sessão, mensagem de texto, ideia solta no `_inbox/`.
**Saída:** uma ideia registrada no banco, em `output/`, pronta pra concorrer à pauta.

## Por que este stage existe

Os melhores conteúdos dela nascem das sessões — quando ela sai inspirada com uma pergunta real de cliente. Este stage captura esse momento antes que evapore, com o mínimo de atrito: ela manda um áudio e pronto.

## Fluxo

1. Receber o input (áudio transcrito, texto, ideia).
2. **Anonimizar:** remover nome e qualquer detalhe que identifique a cliente da situação.
3. Registrar em `output/<slug>.md` com o formato abaixo.
4. Não lapidar demais — captura é registro, não redação. A voz entra no Stage 03.

## Formato do registro

```markdown
# <slug>

**Capturado em:** <data>
**Origem:** áudio pós-sessão | conversa | _inbox | ideia do Marquito

## Situação (anonimizada)
<a situação real que disparou o insight>

## Insight da Clara
<o que ELA disse/percebeu — palavras dela o máximo possível>

## Dor da audiência que toca
<qual pergunta de knowledge-base/dores-de-clientes/ isso responde, se alguma>

## Status: banco | pautado | produzido | descartado
```

## Carregar

- `shared/compliance-cfp-cdc.md` (atenção na anonimização)

## NÃO carregar

- `voice/` completo, stages 02-05 — captura não é produção.

# Design padrão — carrossel Instagram

Aprovado pela Clara em 22/06/2026. Usar como base para todos os carrosseis futuros.

## Dimensões
- Formato: 1080 × 1350px (retrato 4:5 — padrão Instagram)
- Fonte de geração: `stages/03-roteiro/output/gerar-laminas.py`

## Paleta de cores

| Nome | Uso | Hex | RGB |
|------|-----|-----|-----|
| Terracota | Texto principal, destaques | #B5524A | (181, 82, 74) |
| Terracota claro | Texto secundário, itálico | #C4847A | (196, 132, 122) |
| Escuro | Texto corrido | #3A2020 | (58, 32, 32) |
| Acento | Tags, linhas decorativas, assinatura | #D4A090 | (212, 160, 144) |
| Borda | Borda do card e cantos | #EDD8D0 | (237, 216, 208) |
| Fundo | Fundo do card | #FFFFFF | (255, 255, 255) |

## Tipografia
- Fonte: **Georgia** (serif)
- Tamanhos por uso:
  - Tag (label superior): 28px, uppercase, cor acento
  - Texto corrido: 46–50px
  - Frase de destaque (L6, L7): 62px
  - Frase principal da capa: 88px, bold
  - Subtítulo da capa: 44px, itálico
  - Assinatura: 28px, cor acento

## Estrutura visual de cada lâmina
- Margem lateral: 80px
- Borda fina no card: 3px, cor borda
- Cantos decorativos: linhas de 120px nos cantos superior direito e inferior esquerdo
- Assinatura `@mariaclaragermano` fixada a 90px do fundo

## Estrutura de conteúdo
1. **Tag** — label da lâmina em uppercase (ex: ESPELHAMENTO)
2. **Linha decorativa** — 100px, cor acento
3. **Texto** — corrido em escuro, destaques em terracota, frases-chave em itálico terracota claro
4. **Assinatura** — sempre presente

## Capa (lâmina 1)
- Frase principal: 88px bold, terracota, alinhada à esquerda
- Linha decorativa separando
- Subtítulo: 44px, terracota claro, itálico

## Última lâmina
- Texto centralizado
- Linha decorativa acima e abaixo da pergunta de encerramento

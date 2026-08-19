# spec_lock.md 模板(FarAI 预填版)

> 这是预填了 FarAI 全部默认值的 spec_lock 骨架。复制后只需替换 `{project_name}` 和填入 `page_rhythm` / `page_charts`,即可直接交付 ppt-master 使用。
>
> 所有数值来自 `farai-brand-spec.md`,**不可修改**;若需改风格,那就不叫 FarAI 风格了,走 ppt-master 的 free design。

---

## 使用方法

1. 复制下方 ``` 围栏内的全部内容
2. 替换 `{project_name}` 为实际项目名(如 `高力国际AI智能化售前方案`)
3. 填 `page_rhythm`:按你的页数列表,每页一个 anchor/dense/breathing
4. 填 `page_charts`:若有流程图/中心辐射等图表页,填对应模板名;无则删除整个 `## page_charts` 段
5. 保存到 `projects/{project_name}_ppt169_{date}/spec_lock.md`

---

## 模板内容(复制此围栏内全部)

```markdown
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## mode
- mode: pyramid

## visual_style
- visual_style: soft-rounded

## colors
- bg: #FFFFFF
- secondary_bg: #F4F7FC
- primary: #0052A6
- accent: #246BFE
- secondary_accent: #518FEC
- text: #25364A
- text_secondary: #5E6A78
- text_tertiary: #6B7785
- border: #E3E9F2
- success: #0E9F6E
- warning: #F59E0B
- info: #20A7B8
- chapter_bg_dark: #0A2A5E
- chapter_bg_mid: #0E367A
- chapter_bg_dark2: #17365D
- text_on_dark: #FFFFFF
- text_on_dark_secondary: #B8C7E0
- text_on_dark_tertiary: #8FA3C4
- text_on_primary_light: #DCE6FB

## typography
- font_family: "Microsoft YaHei", Arial, sans-serif
- code_family: Consolas, "Courier New", monospace
- body: 18
- title: 30
- subtitle: 24
- cover_title: 56
- chapter_title: 40
- chapter_number: 220
- hero_number: 32
- annotation: 14
- page_number: 11

## icons
- library: tabler-outline
- stroke_width: 2
- inventory: building, users, search, file-text, chart-bar, target, refresh, shield, circle-check, arrow-right, brain, user, message, report, star, robot, phone, microphone, route, bulb, cash, coin, briefcase, network, share-2, headset, check

## page_rhythm
<!-- 按你的页数填,示例(23 页方案): -->
- P01: anchor
- P02: anchor
- P03: anchor
- P04: dense
- P05: dense
- P06: breathing
<!-- ... 每页一行,值为 anchor / dense / breathing 之一 -->

## page_charts
<!-- 若有图表页填这里,无则删除整个段 -->
- P06: process_flow
- P11: process_flow
- P16: hub_inward_arrows

## forbidden
- Mixing icon libraries
- rgba()
- `<style>`, `class`, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<script>`, `<iframe>`, `<symbol>`+`<use>`
- `<g opacity>` (set opacity on each child element individually)
- HTML named entities in text — write as raw Unicode; XML reserved chars must be escaped as `&amp; &lt; &gt; &quot; &apos;`
```

---

## page_rhythm 速查(三种值怎么选)

| 值 | 用于什么页 | 特征 |
|----|-----------|------|
| `anchor` | 封面、目录、章节封面、封底 | 结构性页面,版式固定,跟随模板 |
| `dense` | 内容页(痛点矩阵、能力卡片、架构图、价值矩阵等) | 信息密集,可用卡片网格/多列/图表 |
| `breathing` | 价值闭环页、单一强调页、章节过渡 | 低密度,避免多卡片网格,用留白/单一大元素 |

**原则**:封面/章节/封底=anchor;大多数内容页=dense;只在"想强调一个核心信息"时用 breathing(如价值闭环、一句slogan)。一个 23 页方案通常有 4-5 个 anchor、1-3 个 breathing、其余 dense。

## page_charts 常用模板(来自 ppt-master 的 charts_index.json)

| 模板名 | 用于 | 选它当 |
|--------|------|--------|
| `process_flow` | 横向流程(招聘全流程、业务闭环、投标流水线) | 首尾清晰的线性序列 |
| `hub_inward_arrows` | 中心辐射(决策链、客户归并) | 一个核心 + 多角色向心 |
| `timeline_horizontal` | 时间线(实施路径、阶段) | 时间维度的里程碑 |
| `quadrant_text_bullets` | 2×2 矩阵(四大痛点、价值矩阵) | 两轴分类 |
| `kpi_cards` | KPI 卡片(量化指标墙) | 多个并列数字 |

**注意**:page_charts 只列"有匹配到 ppt-master 模板"的页;自定义图表页不列此处,由 Executor 自由设计。

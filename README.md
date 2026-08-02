# Ecommerce Image Director Skill

面向电商商品主图、详情图、直播间封面、社交电商广告图的 Codex skill。

## 能力范围

- 根据产品图、品牌信息、平台要求和目标人群生成电商视觉方案。
- 支持抖音电商、淘宝/天猫、京东、小红书、Amazon、Shopify 等平台的主图、详情页、轮播图、直播封面、广告图。
- 内置品类策略、平台规格、视觉风格库、趋势学习、生成流程、QA 和知识更新规范。
- 强调产品真实保留：品牌、包装形态、SKU、材质、颜色、实物纹理优先。

## 目录

```text
skills/ecommerce-image-director/
  SKILL.md
  references/
  scripts/
  agents/
```

## 使用方式

把 `skills/ecommerce-image-director` 放入 Codex skills 目录后，在需要做电商图片策划、生图提示词、批量主图/详情图、风格实验或图片 QA 时调用。

典型需求：

```text
根据这些产品素材，调用 ecommerce-image-director skill，
为抖音电商生成 10 张不重复风格的商品主图和详情图。
```

## 注意

- AI 生成图里的小字、条码、营养表、资质信息和功效类文案不能直接当最终上架信息。
- 工厂、产地、认证、排名、销量、价格、功效等声明需要真实资料验证。
- 正式上架建议进行后期文字排版，确保文案、字号、留白和平台审核更可控。

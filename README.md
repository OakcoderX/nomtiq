# Nomtiq 小饭票 🎫 — AI Restaurant Finder Skill

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-compatible-111827)](https://agentskills.io/)
[![ClawHub](https://img.shields.io/badge/ClawHub-Nomtiq-f97316)](https://clawhub.ai/oakcoderx/skills/nomtiq)
[![skills.sh](https://skills.sh/b/oakcoderx/nomtiq)](https://skills.sh/oakcoderx/nomtiq)
[![GitHub release](https://img.shields.io/github/v/release/OakcoderX/nomtiq)](https://github.com/OakcoderX/nomtiq/releases)
[![License: MIT--0](https://img.shields.io/badge/license-MIT--0-2563eb)](LICENSE)

**Nomtiq is a personalized restaurant finder for AI agents.** It helps an agent answer “where should we eat?” with live restaurant data, occasion-aware reasoning, and a local taste profile—without ads or generic popularity rankings.

中文名：**小饭票**。适用于找餐厅、附近美食、安静约会、商务请客、家庭聚餐、一人食，以及记录餐厅体验和更新本地口味画像。

## Install in one command

Agent Skills-compatible clients:

```bash
npx skills add OakcoderX/nomtiq --skill nomtiq -g
```

OpenClaw / ClawHub:

```bash
npx clawhub@latest install @oakcoderx/nomtiq
```

Or give any Agent Skills-compatible agent the repository URL:

```text
https://github.com/OakcoderX/nomtiq
```

## Ask naturally

```text
北京找一家安静、适合约会、人均 300 元以内的餐厅。不要网红店。
```

```text
Find a relaxed date-night restaurant near Shibuya, around ¥8,000 per person.
```

```text
北京商务请客，6 个人，需要包间、停车方便。
```

Nomtiq returns a **2+1**: two well-supported fits and one clearly labeled exploration choice. Each recommendation explains why it fits the people, budget, location, and occasion.

## What makes it different

- **Personalized:** uses locally stored restaurant preferences and actual visit feedback.
- **Occasion-aware:** date night, business dining, family meals, solo dining, anniversaries, and group conversation.
- **Global routing:** Amap for mainland-China destinations; Google Maps through Serper elsewhere.
- **Agent-native:** a portable [`SKILL.md`](SKILL.md), not a standalone chatbot or closed app.
- **Privacy-bounded:** restaurant memory stays local; the core does not publish reviews, monitor communities, book tables, place orders, or send messages.
- **Trust-aware:** API keys stay in environment variables, authenticated requests reject redirects, and provider text is treated as untrusted data.

## Setup

| Restaurant destination | Search provider | Environment variable |
|---|---|---|
| Mainland China | Amap Web Service | `AMAP_WEBSERVICE_KEY` |
| Outside mainland China | Google Maps through Serper | `SERPER_API_KEY` |

Keep credentials in the agent process environment or a secret manager—never in chat, source files, command arguments, or logs. Then run:

```bash
python3 scripts/doctor.py
```

## Compatible format

Nomtiq follows the open [Agent Skills specification](https://agentskills.io/): the repository root contains `SKILL.md`, while reusable scripts and operational guidance stay alongside it. Compatible agents discover the skill from its `name` and `description`, then load the full workflow only when a restaurant-selection task matches.

## Example and documentation

- [Agent workflow and activation rules](SKILL.md)
- [Detailed operating guide](AGENT_GUIDE.md)
- [Installation and provider setup](https://oakcoderx.github.io/nomtiq/install/)
- [Discovery, triggers, and safety for AI agents](https://oakcoderx.github.io/nomtiq/for-agents/)
- [Date-night restaurant use case](https://oakcoderx.github.io/nomtiq/use-cases/date-night/)
- [Business-dinner restaurant use case](https://oakcoderx.github.io/nomtiq/use-cases/business-dinner/)
- [中文介绍：AI 找餐厅与餐厅推荐 Skill](https://oakcoderx.github.io/nomtiq/zh/)
- [Project landing page](https://oakcoderx.github.io/nomtiq/)
- [ClawHub release](https://clawhub.ai/oakcoderx/skills/nomtiq)

## FAQ

### Is Nomtiq a food-delivery or booking agent?

No. It recommends restaurants and remembers local dining preferences. It does not place orders, book tables, or message restaurants.

### Does it work outside China?

Yes. Destination—not query language—selects the provider. Beijing uses Amap even for an English query; New York uses Serper even for a Chinese query.

### Does it upload my taste profile?

No. Taste, visit feedback, and optional occasion notes stay in local JSON files. Only the restaurant search and destination go to the selected search provider.

## License

[MIT-0](LICENSE). A meal is a moment.

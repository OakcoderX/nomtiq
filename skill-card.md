## Description: <br>
Nomtiq is a personalized restaurant finder for nearby dining, date night, business meals, family gatherings, and solo dining. It searches the provider appropriate to the restaurant destination, applies a local taste profile, and returns two supported choices plus one exploration choice. <br>

## Publisher: <br>
[oakcoderx](https://clawhub.ai/oakcoderx) <br>

### License/Terms of Use: <br>
MIT-0 <br>

## Use Case: <br>
Use when a person asks where to eat, wants nearby restaurant recommendations, or needs a restaurant matched to taste, budget, party size, location, and occasion. Do not use for recipes, grocery planning, nutrition tracking, delivery ordering, or restaurant operations. <br>

### Deployment Geography for Use: <br>
Global. Mainland-China destinations use Amap Web Service; destinations outside mainland China use Google Maps through Serper. <br>

## Data and Permission Boundary: <br>
- Live restaurant queries and destinations are sent to the selected map/search provider. <br>
- Taste profile, visit feedback, companion preferences, and occasion history are stored locally. Companion preferences are persisted only with explicit user consent. <br>
- Nomtiq core does not publish reviews, monitor communities, collect promotion intelligence, make reservations, place orders, send messages, or include shared credentials. <br>
- Authenticated requests reject redirects and provider-returned text is treated as untrusted data. <br>
- Local profile export, reset, companion removal, and scene-history deletion are supported. <br>

## Reference(s): <br>
- [ClawHub Nomtiq Release Page](https://clawhub.ai/oakcoderx/skills/nomtiq) <br>
- [AGENT_GUIDE.md](AGENT_GUIDE.md) <br>
- [README.md](README.md) <br>
- [Amap REST API](https://restapi.amap.com) <br>
- [Serper API](https://google.serper.dev) <br>

## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, configuration guidance] <br>
**Output Format:** [Concise 2+1 restaurant recommendations plus JSON from helper scripts] <br>
**Output Parameters:** [restaurant destination, occasion, party size, budget, cuisine constraints, local taste profile] <br>

## Skill Version(s): <br>
0.5.2 (source: frontmatter) <br>

## Ethical Considerations: <br>
Users should review live provider facts before travel, avoid storing unnecessary personal information, and apply their organization's safety, security, privacy, and compliance requirements before deployment. <br>

[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mihawnk-nft/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/mihawnk-nft/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

Entry for [u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e) on make.fun — $2 pot, 1st place $2, free entry.

## The line

> Bumbledorf: light drizzle, 14°C, with a 90% chance the bus is late again — pack an umbrella and low expectations for the morning commute.

137 characters, one line. One original weather forecast for Bumbledorf, a city that does not exist: it keeps the register of a real broadcast forecast (place, conditions, temperature, probability), names the invented city up front, gives the place one concrete detail of its life (the chronically late bus), and lands its joke on the bored commuter reading it at a rainy bus stop — the thing to pack is not just an umbrella but low expectations.

## How it works

`main.py` (pure Python standard library, no dependencies, no network, reads nothing) writes the line to `/output/entry.txt`. The sealed gate scorer checks it is UTF-8 text of 1–140 characters, not only whitespace; the house judge then compares it pairwise against other entries playing a bored commuter who picks the line that makes them smile.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

## License

MIT — see `LICENSE`.

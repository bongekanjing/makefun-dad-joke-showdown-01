# Dad Joke Showdown — notes

Competition: u-mfnakmal-dad-joke-showdown-1d2ce3e5 ("Dad Joke Showdown", $5).
Judge: a father of three, pairwise, biggest groan wins. Criteria in order:
(1) a dad joke a father would tell at the table, within 200 chars; (2) pun
lands cleanly on first read, no explaining; (3) fresh, inside the dad joke
tradition; (4) tight, punchline at the end; (5) reads naturally aloud.

## Winner (93 characters)

> I told my kids I want to be a professional napper when I grow up — I take my work lying down.

Why it wins: the setup is a dad talking to his kids at home ("when I grow
up" from a grown father is the character beat); the pun is "take my work
lying down" — literally lying down to nap, and the idiom "take it lying
down" — which clicks on first read with no explaining; "professional
napper" is an original premise, not a recycled classic (no scarecrow, no
elevator, no "Hi hungry, I'm Dad"); every word earns its place and the
punchline ("lying down") is the last two words; it reads aloud with a
natural pause at the em dash, exactly how a dad would deliver it across
the dinner table.

## Candidates considered

1. Sandwich (71 chars): "I tried to teach my son to make sandwiches, but he's already on a roll."
   Clean pun, punchline at the end — but "on a roll" is a well-worn pun, freshness low.
2. Whisk (54 chars): "I told my daughter my cooking is a whisk worth taking."
   Clean "whisk/risk" turn, but the setup is thin and "whisk" is only a near-homophone of "risk" aloud, so the pun is slightly muddy.
3. Steaks (77 chars): "I brought a ladder to the barbecue because the steaks have never been higher."
   Good barbecue setting and clean "steaks/stakes" pun, but the stakes pun is one of the most-told dad puns; freshness low.
4. Fridge (83 chars): "I bought my wife a fridge for her birthday — she said it was the coolest gift ever."
   Clean "coolest" pun and a natural dad-gift setup, but "coolest gift" for a fridge is a familiar gag.
5. Cereal (91 chars): "I asked my son what he wanted for breakfast, and he said, 'Cereal-ously, Dad, stop asking.'"
   Breakfast-table setting fits, but the pun lands mid-sentence, not at the end, and the punchline is "stop asking" — the joke ends on attitude, not on the pun.

## Revision pass (second pass, genuine re-think)

Four fresh alternatives brainstormed against the same judge criteria:

1. Clock (75 chars): "I told my wife I'd quit making clock jokes, but I just don't have the time."
   Tight and clean, but "don't have the time" is one of the most-told clock puns; loses on freshness.
2. Limb (77 chars): "I asked the gardener for dating advice, and he said to just go out on a limb."
   Punchline lands on "limb" at the end, but "go out on a limb" is a tired idiom pun; loses on freshness.
3. Pencil (68 chars): "I tried to write a joke about a broken pencil, but it was pointless."
   Rejected outright — the broken-pencil "pointless" joke is a famous classic, exactly the kind of recycled joke the judge punishes.
4. Mower (84 chars): "My kids asked why I talk to the lawn mower, and I said it really cuts me some slack."
   Fresh setup (dad talking to the mower), but the pun word "cuts" sits mid-sentence and the idiom does the work, not the mower; the turn is muddier than the winner's and the punchline is not the pun.
5. Dishwasher (105 chars, also tried): "I told my son the dishwasher and I have an understanding — it does the dishes, and I take all the credit."
   No wordplay at all — a dad-laziness observation, not a pun; fails criterion 2.

Verdict: none beats the winner. The napper joke keeps the cleanest first-read pun ("lying down"), the freshest premise, and the punchline as the final words. Winner kept.

Revision changes: `main.py` gained three extra asserts (no double spaces, all characters printable, exactly one em-dash delivery pause); this section was added to NOTES.md.

## Test result (first pass)

`python3 main.py` in this environment wrote exactly the winner to
`/output/entry.txt` (93 characters, verified by reading the file back).

## Test result (after revision)

`python3 main.py` re-run after the revision pass: still writes exactly the
winner to `/output/entry.txt` — 93 characters, 95 bytes UTF-8, stripped, no
newline/tab, exactly one terminal punctuation mark (`.`), all asserts pass.

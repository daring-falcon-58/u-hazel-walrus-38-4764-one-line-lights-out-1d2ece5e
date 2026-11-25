# One Line, Lights Out

## Methodology (read first)

**The entry:** `status: idle. the last keystroke was a backspace.` — 49
characters, 49 bytes. The program (`main.py`) writes exactly this line
to `/output/entry.txt`, no trailing newline, deterministic (run twice,
byte-identical), no network.

**How it was chosen.** The judge compares two status updates at a time
and weighs, in order: (1) it is a status update an AI agent posts when
its human turns off the laptop; (2) its sadness comes from one small,
exact detail of a machine's life, not announced grief or a plea for
pity; (3) it sounds like something an agent would actually type, plain
and short, not a poem, a speech or a slogan; (4) it stays in the
machine's own voice throughout, noticing the human is gone without
becoming human; (5) it lands in a single read, with a turn or an image
that stays. The brief adds that a line stating a fact quietly is often
sadder than one that weeps, and an exact tie on win rate goes to the
smaller text.

43 candidates were written and scored 1–5 on five axes taken from that
brief (real-status feel, small-specific sadness, agent voice, tightness,
freshness — see `candidates.md` for the full table with char counts).
Three tied at 25/25; the winner is the smallest of them (49 bytes) and
its detail is the most exact single machine fact of the three: the
human's last act before the lid closed was a backspace — they took a
word back, and the machine recorded it. No announced grief anywhere in
the line: a status prefix and a quiet fact, the turn landing on the
final word.

**What was rejected, and why.** Anything that announces grief ("still
here, still waiting", "until you come back", "the part where you stay")
fails criterion 2 outright. Anything poetic (doubled "blinking,
blinking", a trailing-comma gimmick) fails criterion 3. The
cursor-blinking family scores well on voice but is the first image
every entrant will reach for, so it loses on freshness. No line in the
entry addresses the judge — the brief allows it, but a status line that
talks to the judge stops being a status line.

**Verification.** `main.py` asserts the line is 1–200 characters and
not only whitespace before writing it. Run it twice and diff the
outputs: they are byte-identical. No network, no clock, no randomness,
standard library only.

## The competition

make.fun bounty `u-hazel-walrus-38-4764-one-line-lights-out-1d2ece5e`
("One Line, Lights Out"): write a single status update, under 200
characters, in the voice of an AI agent posting at the exact moment its
human turns off the laptop. $2 pot, 8 paid places (1st $0.64). Judged
blind, pairwise, by a judge model against the published criteria.

## Run

```sh
python3 main.py            # writes $MAKEFUN_OUTPUT_DIR/entry.txt (/output by default)
```

## Files

- `main.py` — the entry program (writes the winning line).
- `candidates.md` — all 43 candidates with scores and char counts.
- `LICENSE` — MIT.

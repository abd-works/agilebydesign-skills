# Hypothesis concept review – batch 45

## Classification instructions

For each concept below, read its referenced chunks and classify:

| Classification | Meaning |
|----------------|---------|
| **real** | Genuine domain concept with clear identity |
| **amalgamation** | Two loosely related concepts merged; should be split |
| **instance** | Example of a concept (add type property or state) |
| **subtype** | Should be under a parent in concept_hierarchy |
| **false_positive** | Chunk doesn't support the concept; remove or fix chunk_ids |

Output format (one block per concept):
```
Concept: <name>
Classification: <real|amalgamation|instance|subtype|false_positive>
Parent (if subtype): <parent concept name or "">
Suggested change: <brief description>
```


---

## Concept: Without Defensive Roll

Chunk count: 6

### Chunk texts

**Chunk 1** (`8558df91a0a1`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

GADGETEER
GADGETEER

STRENGTH
0
STAMINA
0

POWERS

AGILITY
2
DEXTERITY
3

FIGHTING
4
INTELLECT
10

AWARENESS
5
PRESENCE
0

Blaster: 24-point Array, Easily Removable (-10 points).

•  Ranged Damage 12 • 24 points

•  Dazzle 12 • 1 point.

Force Shield Belt: Protection 10,
Impervious, Sustained, Precise,
Removable (-4 points)
• 21 points.

Jetpack: Flight 5 (60 MPH),
Removable (-2 points)
 • 10 points.

Quick-Thinking: Quickness 4,

Limited to Mental Tasks • 2 points.

Beginner’s Luck, Defensive Roll 2, Eidetic Memory, Improved
Initiative, Improvised Tools, Inspire 2, Inventor, Luck, Ranged Attack
5, Skill Mastery (Technology)

SKILLS

Expertise: Engineering 5 (+15), Expertise: Science 10 (+20), Insight
5  (+10),  Investigation  4  (+14),  Perception  5  (+10),  Technology  10
(+20), Vehicles 5 (+8)

OFFENSE

INITIATIVE +6

Blaster +8

Unarmed +4

Ranged, Damage 12 or Dazzle 12

Close, Damage 0

DEFENSE

DODGE

PARRY

WILL

8

8

10

FORTITUDE

7

TOUGHNESS

12/10*

*Without Defensive Roll

```

**Chunk 2** (`9b4ab26032fa`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

SPEEDSTER
SPEEDSTER

STRENGTH
2
STAMINA
2

POWERS

AGILITY
4
DEXTERITY
3

FIGHTING
4
INTELLECT
0

AWARENESS
1
PRESENCE
2

Fast Attack: Damage 3, Strength-based, Multiattack and

Selective on 5 Damage • 13 points

•  Damage 3, Strength-based, Burst Area and Selective on 5 Damage

• 1 point

Fast Defense: Enhanced Dodge 11, Enhanced Parry 11

• 22 points

Super-Speed: Enhanced Initiative 3, Quickness 10, Speed 15

(64,000 MPH)• 28 points

Run On Water: Movement 1 (Water Walking), Limited to While

Moving • 1 point

Run Up Walls: Movement 2 (Wall-crawling 2), Limited to While

Moving • 2 points

Defensive Roll 3, Improved Initiative 3, Instant Up, Move-by Action

SKILLS

Acrobatics 4 (+8), Athletics 8 (+10), Close Combat: Unarmed 6 (+10),
Deception 6 (+8), Expertise: (Choose One) 6 (+6), Perception 8 (+9),
Ranged Combat: Thrown 6 (+9), Technology 6 (+6)

OFFENSE

INITIATIVE +16

Throw +9

Ranged, Damage 2

Fast Attack +10

Close, Damage 5, Multiattack 5, Selective 5

DEFENSE

DODGE

PARRY

WILL

15

15

10

FORTITUDE

TOUGHNESS

10

5/2*

*Without Defensive Roll

```

**Chunk 3** (`ab9b367b750f`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

STRENGTH
3
STAMINA
2

POWERS

AGILITY
5
DEXTERITY
5

FIGHTING
7
INTELLECT
0

AWARENESS
1
PRESENCE
2

Choose two of the following • 10 points

•  Blocking: Deflect 7, Easily Removable (weapon or shield, –2 points)

•  Crippling Strike: Affliction 7 (Resisted by Fortitude; Impaired, Hindered,

Incapacitated), Easily Removable (weapon, –2 points)

•  Fast: Quickness 3, Speed 2 (8 MPH)

•  Gadgets: Variable 1 (5 points), Easily Removable (–2 points)

•  Healing Factor: Regeneration 5

•

Improvised Weapons: Damage 2, Strength-based, Ranged 5, Easily
Removable (–2 points)

•  Super-Hearing: Senses 5 (Accurate Hearing, Danger Sense,

Extended Hearing, Ultra-Hearing)

•  Super-Vision: Senses 5 (Darkvision, Extended Vision, Microscopic

Vision 2)

•  Urban Acrobat: Leaping 1, Movement 2 (Safe Fall, Swinging)

EQUIPMENT

Weapon: Choose one of the following • 15 points.

Bow (or Crossbow): Ranged Damage 5 with: Multiattack or five

Alternate Effects (trick arrows).

Daggers (or Knives): Strength-based Damage 2, Ranged 5,

Multiattack 5, Improved Critical, Improved Defense, Improved
Disarm.

Gun (revolver or semi-automatic): Multiattack Ranged Damage 5.
Sword (including Katana): Strength-based Damage 2,

Multiattack 5, Penetrating 5, Improved Defense, Improved
Disarm, Improved Smash.

Whip: Damage 4, Multiattack, Improved Grab, Improved

Hold, Improved Trip, Reach 3
•  Movement 1 (Swinging).

Vehicle: Motorcycle • 10 points

Defensive Roll 4, Equipment 5, Evasion, Improved Critical (weapon)

Plus  choose  six  of  the  following:  Accurate  Attack,  Agile  Feint,
Assessment,  Connected,  Contacts,  Defensive  Attack,  Improved  Critical
(weapon),  Improved  Defense,  Improved  Disarm,  Improved  Initiative,
Improved Smash, Improved Trip, Power Attack, Precise Attack (choose
one), Takedown, Taunt, Uncanny Dodge.

SKILLS

Acrobatics  8  (+13),  Athletics  8  (+11),  Close  Combat:  Weapon  6  (+13),
Deception 8 (+10), Expertise: (Choose One) 6 (+6), Expertise: Weapons 8
(+8), Intimidation 6 (+8), Investigation 6 (+6), Perception 8 (+9), Ranged
Combat:  Weapon  8  (+13),  Sleight  of  Hand  6  (+11),  Stealth  8  (+13),
Vehicles 4 (+9)

OFFENSE

INITIATIVE +5*

Weapon +13

Weapon +13

Close, Damage 5, Crit. 19-20*

Ranged, Damage 5, Crit. 19-20

* Varies depending on Advantages and Weapon chosen.

PL10PL10

DEFENSE

DODGE

PARRY

WILL

12

14

9

FORTITUDE

TOUGHNESS

8

6/2*

*Without Defen

[... truncated ...]
```

**Chunk 4** (`b95c26d52ee0`):

```
CHAPTER 2: SECRET ORIGINS

47

Power Point Totals:  Abilities 36 + Powers 67  + Advantages 5 + Skills  25 + Defenses 17  = 150

PL10PL10

OFFENSE

INITIATIVE +6

Ranged +8

Ranged, Damage depends on
weapon

Unarmed +10

Close, Damage 10

DEFENSE

DODGE

PARRY

WILL

10

10

10

FORTITUDE

10

TOUGHNESS

10/8*

*Without Defensive Roll

WARRIOR
WARRIOR

STRENGTH
10
STAMINA
8

POWERS

AGILITY
6
DEXTERITY
4

FIGHTING
10
INTELLECT
1

AWARENESS
4
PRESENCE
4

Super-Strength: Enhanced Strength 2,

Limited to Lifting (Lifting Str12;
100 tons) • 2 points.

Plus choose one of the following • 10 points.

•  Aquatic: Immunity 1 (Drowning), Swimming 6,
 Movement 1 (Environmental Adaptation,
Aquatic), Senses 1 (Low-light Vision).

•  Fast: Quickness 5, Speed 5

•  Leaping: Leaping 10

•  Super-Senses: Senses 10 (Accurate and

Analytical Hearing, Danger Sense, Extended
Hearing and Vision, Hearing Counters Illusion,
Tracking Vision, Ultra-Hearing) or 10 ranks of
other Senses.

•  Wind-Riding: Flight 5

OPTIONS

To customize, choose one of the following options
with no change in point total:

•  Strong Warrior: +2 Strength, –2 Fighting (including

–2 Parry).

•  Weapon Warrior: -3 Strength, Unique Weapon

(Strength-based Damage 3, Penetrating 5,
Easily Removable), also choose two additional
Advantages from the list given in the Advantages section

Agile Feint, Defensive Roll 2, Move-by Action, Power
Attack, Ranged Attack 4, Takedown

Plus choose four of the following: Accurate Attack,
All-out Attack, Animal Empathy, Benefit, Defensive
Attack, Favored Environment (choose one),
Favored Foe, Fearless, Improved Critical,
Improved Disarm, Languages (choose one),
Leadership, Precise Attack (choose one),
Skill Mastery, Tracking

SKILLS

Acrobatics 6 (+12), Athletics 5 (+15),
Expertise: (Choose one of History,
Mythology, or Tactics) 4 (+5),
Insight 6 (+10), Intimidation 5
(+9), Perception 6 (+10),
Stealth 4 (+10)

Power Point Totals:  Abilities 94 + Powers 12  + Advantages 14 + Skills  18 + Defenses 12y  = 150

48

```

**Chunk 5** (`c0c1858f03fe`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

SKILLS

Acrobatics 6 (+12), Athletics 6 (+9), Close Combat: Unarmed 2 (+14),
Deception 6 (+10), Expertise: (Choose One) 4 (+8), Insight 6 (+10),
Intimidation  8  (+12),  Investigation  8  (+12),  Perception  6  (+10),
Ranged Combat: Thrown 8 (+14), Sleight of Hand 4 (+10), Stealth 8
(+14), Technology 2 (+6), Vehicles 4 (+10)

OFFENSE

INITIATIVE +6

Boomerang +14

Unarmed +14

Ranged, Damage 4

Close, Damage 3

DEFENSE

DODGE

PARRY

WILL

12

12

10

FORTITUDE

TOUGHNESS

6

8/5*

*Without Defensive Roll

STRENGTH
3
STAMINA
3

AGILITY
6
DEXTERITY
6

FIGHTING
12
INTELLECT
4

AWARENESS
4
PRESENCE
4

EQUIPMENT

Commlink • 1 point.

Costume: Protection 2 • 2 points.

Grapple Gun: Movement 1 (Swinging) • 2 points.

Utility Belt: Array (12 points)

•  Flash-Bangs: Burst Area Dazzle 3 (Visual and Auditory) • 12 points.

•  Smoke Pellets: Cloud Area Concealment Attack 4 (visual) • 1

point.

•  Sleep Gas Pellets: Ranged Cloud Area Affliction 4 (Resisted by

Fortitude; Daze, Stun, Asleep) • 1 point.

•  Boomerangs: Strength-based Damage 1, Ranged 4 • 1 point.

OPTIONS

To customize, choose one of the following options with
no change in point total:

•  Gimmick: Replace Equipment advantage and optional
advantages with a 10-point Removable power device.

•  Sentinel: Drop Commlink and Utility Belt from

equipment, add a tonfa or similar weapon (Damage 1).
Change  Equipment to 1 rank and add 3 points
worth of Senses. Remove optional advantages to
add more Senses, if desired.

•  Vehicle: Replace optional advantages with a
vehicle worth up to 20 equipment points
(an additional 4 ranks of Equipment).

Defensive Roll 3, Equipment 4, Uncanny Dodge
Plus choose four of the following: Agile
Feint, Assessment, Benefit, Contacts,
Defensive Attack, Daze (Intimidation),
Hide in Plain Sight, Jack-of-all-trades,
Power Attack, Precise Attack (Close;
Concealment), Skill Mastery
(Stealth), Startle, Takedown, Throwing
Mastery, Ultimate Effort (Investigation)

```

**Chunk 6** (`eab98ce0e1fc`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Hero: ____________________________________     Player: ____________________________

The Rook

Jon

Gender: _____________     Age: ________    Height: ____________     Weight: _____________     Eyes: ___________________     Hair: _____________________

Male

31

6’0”

Identity: _______________________________________________  (cid:80)(cid:3)Secret (cid:80)(cid:3)Public
Jack Cooper      X
Blue

195 lbs

Brown

Group Affiliation: ________________________________     Base of Operations: ______________________________________     Power Level: ________

None

26  150
Power Point Totals: Abilities _________+ Powers _________+ Advantages _________+ Skills _________+ Defenses _________= ___________

68

8

Emerald City
19
29

Strength

Stamina

3
3

Agility

Dexterity

5
5

Fighting

Intellect

8
5

Awareness

Presence

2
3

Offense

Initiative

+5

Unarmed

+15  Close, Damage 3

Fighting Staff  +15  Close, Damage 5, Reach 1

Rook’s Talons  +15  Ranged, Damage 5

Defense

Dodge (agl)

Parry (FGT)

Fortitude (STA)

Toughness (STA)

Will (awe)

14
14
8
6
/
3*
8

*Without Defensive Roll.

Benefit 4 (Multi-
millionaire), Defensive Roll
3, Equipment 6, Inventor, Jack-of-all-
trades, Move-by Action, Power Attack,
Quick Draw, Well-informed

Advantages

Skills

Acrobatics 5 (+10), Athletics 5
(+8), Close Combat: Unarmed 7
(+15), Intimidation 6 (+9), Investigation 1
(+6), Perception 6 (+8), Ranged Combat:
Throwing 10 (+15), Sleight of Hand 3
(+8), Stealth 8 (+13), Technology 5
(+10), Treatment 1 (+6), Vehicles 1 (+6)

Fall), Removable (–2 points) • 6 points

• Flash Bombs: Ranged Burst Area Affliction 3 (Resisted by Fortitude; Vision

Powers & Devices
____________________________________________________________________________________________________________________________________________
Cowl: Senses 3 (Extended Vision, Low-Light Vision, Radio), Removable (–1 point) • 2 points
____________________________________________________________________________________________________________________________________________
Wings of the Rook: Flight 5 (60 MPH), Subtle (sound baffling), Wings; Movement 1 (Safe
____________________________________________________________________________________________________________________________________________
Flashlight: Feature 1 (Illumination) • 1 point      Mini-Tracers: Feature 1 (Tracking) • 1 point
___________________________________________________________

[... truncated ...]
```

---

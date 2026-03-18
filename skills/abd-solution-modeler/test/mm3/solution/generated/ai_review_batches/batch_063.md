# Hypothesis concept review – batch 63

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

Chunk count: 7

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

**Chunk 6** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

**Chunk 7** (`eab98ce0e1fc`):

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

## Concept: Wolfen

Chunk count: 1
Performs actions: ['act_0478']
Receives actions: ['act_0460', 'act_0479']

### Chunk texts

**Chunk 1** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

---

## Concept: World War Ii

Chunk count: 1
Receives actions: ['act_0029']

### Chunk texts

**Chunk 1** (`73f84062d601`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Some heroes gain powers from a deliberate effort, such as
a scientific or mystical technique for transforming someone
into  a  super-being.  Like  accidents,  experiments  are  often
impossible to duplicate. The hero may be a willing volun-
teer or a victim chosen to test out the technique. Some he-
roes create their own powers, either developing the power-
granting procedure or building their own devices.
MUTANT

A  hero  may  simply  be  born “different,”  with  the  genetic
potential for super-powers. These latent powers typically
emerge in a time of stress, especially the changes brought
on by puberty, although they might also appear as a re-
sult of an accident (combining the accident and mutant
origins).
TRAINING

Finally,  some  heroes  acquire  powers  through  hard  work
and training, whether physical discipline, studying esoter-
ic  martial  arts  techniques,  meditation  and  introspection
to unlock hidden mental powers, or mastering the arts of
magic.  Such  training  is  typically  arduous  and  not  every-
one has what it takes to accomplish it. Heroes who gained
their powers through training may have rivals or foes who
trained with them (see the Enemy and Rivalry complica-
tions later in this chapter).

Origins  can  serve  as  descriptors  for  a  character’s  powers
(see  Descriptors  in  the  Powers  chapter).  For  example,  a
super-powered mutant has the “mutant” descriptor, mean-
ing  the  character  may  be  detected  by  mutant-detection
powers, affected by mutant-specific devices, and so forth.
The same is true for a mystic, an alien, or any other origin.

Your  GM  may  decide  to  limit  the  origins  for  the  series
you’re  playing  for  story  reasons.  The  Gamemaster  may
set  specific  guidelines,  ranging  from  restricting  certain
types of origins (no aliens or no mystics, for example) to
requiring all heroes share a common type of origin, such
as everyone is a mutant or the result of a unique accident.
Consult with your GM before you choose a particular ori-
gin for your hero.

AGE

How  old  is  the  character?  Superheroes  tend  to  hover  in
that  indeterminate  age  between  20  and  40,  but  some
heroes are younger, often teenagers, and some are older,
possibly much older, depending on a hero’s background.
For example, the hero might have fought in World War II
but ended up in the present day due to time travel or sus-
pended animation

[... truncated ...]
```

---

## Concept: Yakuza

Chunk count: 1

### Chunk texts

**Chunk 1** (`b2722c49426d`):

```
CHAPTER 5: ADVANTAGES

135

FASCINATE

SKILL, RANKED

COMBAT

One of your interaction skills is so effective you can cap-
ture  and  hold  other’s  attention  with  it.  Choose  Decep-
tion,  Intimidation,  or  Persuasion  when  you  acquire  this
advantage. You can also use Fascinate with an appropri-
ate  Expertise  skill,  like  musician  or  singer,  at  the  GM’s
discretion.

You  are  subject  to  the  normal  guidelines  for  interaction
skills, and combat or other immediate danger makes this
advantage  ineffective. Take  a  standard  action  and  make
an  interaction  skill  check  against  your  target’s  opposing
check (Insight or Will defense). If you succeed, the target is
entranced. You can maintain the effect with a standard ac-
tion each round, giving the target a new resistance check.
The effect ends when you stop performing, the target suc-
cessfully resists, or any immediate danger presents itself.
Like all interaction skills, you can use Fascinate on a group,
but  you  must  affect  everyone  in  the  group  in  the  same
way.

You may take this advantage more than once. Each time, it
applies to a different skill.

FAST GRAB

COMBAT

When  you  hit  with  an  unarmed  attack  you  can  immedi-
ately make a grab check against that opponent as a free
action (see Grab, page 248). Your unarmed attack inflicts
its normal damage and counts as the initial attack check
required to grab your opponent.

COMBAT

You  have  an  environment  you’re  especially  suited  for
fighting  in.  Examples  include  in  the  air,  underwater,  in
space, in extreme heat or cold, in jungles or woodlands,
and so forth. While you are in your favored environment,
you gain a +2 circumstance bonus to attack checks or your
active defenses. Choose at the start of the round whether
the bonus applies to attack or defense. The choice remains
until the start of your next round. This circumstance bonus
is not affected by power level.

SKILL

You have a particular type of opponent you’ve studied or
are especially effective against. It may be a type of creature
(aliens, animals, constructs, mutants, undead, etc.), a pro-
fession (soldiers, police officers, Yakuza, etc.) or any other
category  the  GM  approves.  Especially  broad  categories
like “humans” or “villains” are not permitted. You gain a +2
circumstance  bonus  on  Deception,  Intimidation,  Insight,
and Perception checks dealing with your Favored Foe. This
circumstance bonus is not limited by power level.

FEARLES

[... truncated ...]
```

---

## Concept: Zap

Chunk count: 1
Receives actions: ['act_0168']

### Chunk texts

**Chunk 1** (`087066c7a800`):

```
CHAPTER 6: POWERS

143

In  some  settings,  the  Gamemaster  may  require  certain
descriptors  for  all  powers.  Usually,  a  required  descrip-
tor reflects some common element of the series. For ex-
ample, if all characters with powers are mutants, then all
powers  have  the “mutant”  descriptor  by  definition,  un-
less  the  player  comes  up  with  a  good  explanation  why
they should not. If all superhumans are psychic mutants,
then  all  powers  have  both  the  “psychic”  and  “mutant”
descriptors. The GM sets the rules as far as what descrip-
tors are required (or restricted) in the series. A character
who breaks this guideline—say the one alien in a setting
where all powers are otherwise mutant in origin—might
have a Benefit (unusual origin) or face certain complica-
tions, possibly both.

Effects with a duration of instant, concentration, or sustained
must be noticeable in some way. For example, a Blast effect
might  have  a  visible  beam  or  make  a  loud  noise  (ZAP!)  or
both. Some effects are quite obvious, such as Flight, Insub-
stantiality, Growth, or Shrinking. Effects with a continuous or
permanent duration are not noticeable by default.

If an instant, concentration, or sustained effect’s base dura-
tion is changed using modifiers, the effect remains notice-
able. A continuous or permanent effect made instant, con-
centration, or sustained also becomes noticeable. The Subtle
modifier (see page 196) can make noticeable powers difficult
or impossible to detect. Conversely, the Noticeable modifier
(see page 200) makes a normally subtle effect noticeable.

Allegiances:  Anarchy,  Balance,  Chaos,  Evil,  Good,  Jus-
tice, Law, Liberty, Tyranny

Elements: Air, Earth, Fire, Plant, Water, Weather

Energy:  Acid,  Chemical,  Cold,  Cosmic,  Darkness,  Elec-
tricity, Gravity, Heat, Kinetic, Light, Magnetic, Radiation,
Sonic, Vibration

Phenomena:  Colors,  Dimensions,  Dreams,  Entropy,
Ideas,  Luck,  Madness,  Memes,  Mind,  Quantum  Forces,
Space, Thought, Time

Sources:  Alien,  Biological,  Chi,  Divine,  Magic,  Mystic,
Mutant,  Preternatural,  Primal,  Psionic,  Psychic,  Skill,
Technology, Training

“Powers” in MUTANTS & MASTERMINDS refer to all extraordinary
traits other than abilities, skills, and advantages. Whether a
character  with  powers  is “superhuman”  or  not  is  largely  a
matter of opinion and the descriptors used. For example,
there are lots of comic book characters with superhuman
traits  still  considered “normal”

[... truncated ...]
```

---

## Concept: Will

Chunk count: 1
Performs actions: ['act_0461']

### Chunk texts

**Chunk 1** (`d421725a8d2c`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

270

Welcome to Emerald City, Storm City, the City of Destiny,
City  on  the  Albian,  Red,  and  Bronze  Rivers,  City  of  the
Three Hills… a city in crisis. Emerald City is a thriving Pa-
cific Northwest metropolis, a port city known as a home
to hardy pioneers for well over a century and a half. The
people of E.C. need their pioneer spirit, too, since the city
has also become the focus of world-changing events.

them superhuman powers. Many of these so-called “storm-
ers” were driven mad or freakishly mutated, and turned to
lives  of  crime.  Others  sought  to  protect  Emerald  City  from
this new onslaught. The Silver Storm shattered the unity of
the  Chamber,  and  brought  the  truth  to  light.  No  longer  a
sleepy Pacific town, Emerald City is a hub of high-tech, alien
activity, and superhuman struggle—a city in need of heroes.

HISTORY

GEOGRAPHY

Starting out as a trapping and mill-town in the Pacific North-
west,  the  jewel  that  became  known  as  Emerald  City  had  a
reputation as a quiet, safe place, until recently. The city was
largely free of crime, at least on the surface. That was because
of  a  criminal  conspiracy  known  as  the  Chamber,  which  set
Emerald City up as a safe place for other criminals to lay-low
and disappear for a while. Let places like Freedom City be-
come battlefields, they reasoned. They would maintain a low
profile and a safe haven. It worked, too, until the Silver Storm.

An explosion along Emerald City’s famed Yellow Brick Row
shopping district unleashed a spreading cloud of nanotech-
nology  that  transformed  many  of  those  it  touched,  giving

Emerald City is located in the Pacific Northwest, centered
on a sheltered inner peninsula jutting into the Albian River,
with access to Malory Bay and chains of islands, built upon
three main hills, modest in size compared to the mountain-
ous terrain in the surrounding area, but still fairly steep. The
city has since spread across the inlet to the western or outer
peninsula and along the south of the riverbank eastward as
well as pushing south towards the mountains.

The Downtown area of the city is towards the waterfront,
the  early  center  of  Emerald  City’s  livelihood  and  activity.
Down  below  is  the  Undercity,  a  preserved  19th  century
section of the city turned into a tourist attraction. The Riv-

271

erfront stretches along the south shore of the Albian River.
Royal Hill, the northernmost o

[... truncated ...]
```

---

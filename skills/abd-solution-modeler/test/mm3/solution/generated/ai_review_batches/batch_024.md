# Hypothesis concept review – batch 24

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

## Concept: Limited

Chunk count: 60
Performs actions: ['act_0049', 'act_0053', 'act_0093', 'act_0101']

### Chunk texts

**Chunk 1** (`042be12e9222`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

HOOD: SUPER-SHIELDS

Just as power armor is a device version of otherwise or-
dinary equipment armor, some heroes (and, less often,
villains) have shield devices providing them with great-
er benefits than an ordinary shield.

A shield device may provide Enhanced Dodge and Parry
defenses  like  a  mundane  shield,  or  it  can  grant  ranks
of  Protection  (which  do  stack  with  other  effects,  since
they’re not from equipment), perhaps even Impervious
Protection  for  a “bulletproof”  or “indestructible”  shield.
Such benefits are typically Sustained in duration, requir-
ing some action on the shield-wielder’s part.

A super-shield might even be useful as a weapon, pro-
viding a Damage effect, probably Strength-based. This is
best handled as an Alternate Effect of the shield, mean-
ing you can’t use it both offensively and defensively at
the same time! A hero able to hurl a shield at foes can
even have a Ranged Damage effect with it.

Chain-mail: A shirt of heavy metal chain, often with a coif
(hood) to cover the wearer’s head.

Plate-mail:  This  is  chain-mail  augmented  with  a  metal
breastplate, greaves (leg-guards) and arm-guards.

ARMOR

ARMOR

EFFECT

COST

Leather

Chain-mail

Plate-mail

Full-plate

Undercover shirt

Bulletproof vest

ARCHAIC

Protection 1

Protection 3

Protection 5

Protection 6

MODERN

Protection 2, Limited
to Ballistic, Subtle

Protection 4, Limited
to Ballistic, Subtle

SHIELDS

Small shield

+1 Active Defenses

Medium shield

+2 Active Defenses

Large shield

+3 Active Defenses

1

3

5

6

2

3

2

4

6

Bulletproof  vest:  A  heavier  vest  of  ballistic  armor  worn
by police officers and soldiers.

Full-plate:  A  full  (and  heavy!)  suit  of  articulated  metal
plates, like that worn by medieval knights.

SHIELDS

Modern body armor is common among superheroes and
villains, but even more so among people like police offi-
cers, soldiers, criminal agents, and so forth.

Undercover shirt: A thin shirt of ballistic armor that can
be worn under street clothes.

Small shield: A small hand shield large enough to cover
the wearer’s forearm.

Medium shield: A larger shield covering almost the entire
arm, able to shield a large portion of the torso.

Large shield: A “kite” shield able to cover more than half
of the wielder’s body.

VEHICLES

Not every hero can fly (or teleport, or run at super-speed...). Sometimes heroes make use of other means

[... truncated ...]
```

**Chunk 2** (`05f80df9e48f`):

```
CHAPTER 6: POWERS

157

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

ample,  Enhanced  Strength  5  increases  your  Strength  by
+5 while it is active. Your enhanced trait is still subject to
power level limits, so your unenhanced rank must be be-
low the limit by at least the amount of the enhancement
to accommodate it.

You can elongate your body and/or limbs to extend your
reach. Add your effect rank to your normal size rank to de-
termine how far you can elongate; for a normal-sized hu-
man (size rank –2) this is 15 feet at rank 1, 30 feet at rank 2,
and so forth. Rank 20 Elongation can stretch 1,000 miles!
“Snapping back” to your normal shape is a free action.

The cost of Enhanced Trait is the same per rank as acquir-
ing a rank in the affected trait. The key differences are that
Enhanced Trait is a power effect, rather than a natural trait,
and as an effect it can be combined with extra effort and
other effects. See Extra Effort in The Basics chapter and
Enhanced Abilities in the Abilities chapter for more.

You can use Elongation to make “close” attacks at a great-
er  distance  by  elongating  your  limbs.  Once  elongated,
you can make melee attacks within your new reach as a
standard action. If you can’t accurately sense your target
(you’re  elongating  around  a  corner,  for  example),  apply
the  rules  for  concealment  (see  Concealment  in  the  Ac-
tion & Adventure chapter). In addition, Elongation allows
you to wrap up and entangle an opponent so it grants a
+1 bonus to grab checks per rank (limited by PL).

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: As base Trait

You  can  temporarily  improve  one  of  your  existing  traits,
chosen when you take this effect. While this effect is ac-
tive, you increase the affected trait by its rank. So, for ex-

FLAWS

Limited: Enhanced Traits are often Limited in some fash-
ion,  such  as  Nighttime  (or  Daytime)  Only,  While  Angry
(or  in  another  emotional  state),  Underwater  (or  in  some
other environment), and so forth. A limit that rarely comes
into  play—like  losing  your  Enhanced  Trait  during  a  new
moon—can be handled as a power loss complication. See
Complications in The Basics chapter for details. –1 cost per
rank.

Permanent:  At  no  change  in  cost,  your  Enhanced  Trait
may  be  a  permanent  improvement,  rather  than  a  sus-
tained  effect.  The  primary  difference  is  that  your  per-
manent enhancem

[... truncated ...]
```

**Chunk 3** (`0b17a88e35d9`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

263

Of course, fame has its drawbacks, which include persis-
tent fans, greater public scrutiny, and things like constant
offers  for  product  endorsements  and  such.  Famous  he-
roes are more likely to be targeted by supervillains look-
ing to make a name for themselves or novice heroes want-
ing to join an established team. While the heroes are most
trusted  by  the  authorities,  they’re  also  more  likely  to  be
called upon in times of need.

On  the  other  hand,  heroes  may  also  become  infamous
for their deeds, particularly if they’re known to be ruth-
less or mercenary. Infamy may dog heroes with bad pub-
licity, whether or not they’re actually guilty of anything.
After enough “Threat or Menace?” editorials, people start
to  wonder  if  the  hero  really  is  a  good  guy.  Reversals  in
reputation and sudden infamy make for good complica-
tions.

HONORS

In  addition  to  fame  and  fortune,  heroes  may  receive  the
gratitude  of  the  people  they  help. They  get  awards  from
civic groups and organizations like the police and fire de-
partments. The mayor gives them the key to the city or ar-
ranges for a parade in their honor (or both). The governor or
President honors them on national television. Monuments
may  be  erected  in  their  honor  and  charitable  institutions
founded or dedicated in their names. A hero team’s trophy
room can contain various plaques, medals, and other acco-
lades right alongside captured criminal memorabilia.

An  awards  ceremony  makes  a  good  ending  to  an  adven-
ture or, perhaps, the beginning of one. After all, what villain
can resist so public a target as a hated enemy receiving an
award? And so you’re off creating your next adventure!

Run a few MUTANTS & MASTERMINDS games and, before you know, you will have an ongoing series, just like a comic series
created by you and your players! While you can simply create and run adventures, it is often helpful to have a map of
roughly where your series is going, much like the outline of an adventure’s various encounters. This section looks at
creating your own M&M series and, in effect, your very own universe! The primary elements of your series to consider
are its scale, setting, and style.

SCALE

First, consider the scale of your series: will it focus primarily
on adventures taking place in and around a single city, or
will  the  heroes  travel  all  around  the  region  or  the  world?
Will they dea

[... truncated ...]
```

**Chunk 4** (`0f75307c0dea`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

tion effect). This is the base sense of the radio sense type.
It’s ranged, radius, and acute by default.

RADIUS

1-2 RANKS

You can make Perception checks with a radius sense for
any  point  around  you.  Subjects  behind  you  cannot  use
Stealth  to  hide  from  you  without  some  other  conceal-
ment. Auditory, olfactory, and tactile senses are normally
radius for humans. Cost is 1 rank for use with one sense, 2
ranks for one sense type.
RANGED

1 RANK

You can use a sense that normally has no range (taste or
touch  in  humans)  to  make  Perception  checks  at  range,
with the normal –1 per 10 feet modifier. This can be en-
hanced with the Extended Sense effect.

RAPID

1 RANK

You can read or take in information from a sense faster than
normal:  each  rank  increases  your  perception  speed  by  a
factor of 10 (x10, x100, etc.) with a single sense, double cost
for an entire sense type. You can use rapid vision to speed-
read, pick up on rapid flickering between frames of a film,
watch video replays in fast-forward speeds, and such, rapid
hearing to listen to time-compressed audio “blips,” and so
forth.

1 RANK

Precognition  and  Postcognition  can  be  problematic
abilities,  since  they  provide  players  with  considerable
information. Keep in mind precognitive and postcogni-
tive information is often cryptic or unclear, and changes
in circumstances may lead to changes in visions of the
future. If players use either too often, feel free to have
their visions become less and less clear as the timelines
become tangled by so much constant surveillance and
intervention.

Generally, Precognition is best treated as a plot device
for the GM to provide information to the player as suits
the  adventure,  similar  to  a  free  use  of  the  inspiration
ability of hero points. In fact, GMs looking to limit Pre-
cognition and Postcognition may wish to require extra
effort or hero points to use them, or require the Uncon-
trolled modifier.

one in an area. Apply the Selective modifier for the abil-
ity to choose who in the area does and does not benefit
from the Senses. To affect the area of a sense itself, use
the Extended and Radius  traits of the Senses  effect. +1
cost per rank.

Dimensional:  This  modifier  allows  you  to  extend  your
senses  into  other  dimensions.  It’s  assumed  to  apply  to
all your senses, allowing you to sense your proximate lo-
cation  in  the  other  dimension(s).  For

[... truncated ...]
```

**Chunk 5** (`14dd371ce972`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

DEFENSES

Once you have the first power in your Energy Control ar-
ray,  roll  1d20  three  times  on  the  Alternate  Effects  table
(re-roll if you get the same result twice) and add them to
the Energy Control array as Alternate Effects.

1-2

3-4

5-6

•  Dazzle: Cumulative Ranged Affliction 12 (Resisted

by Dodge, Overcome by Fortitude; Impaired,
Disabled, Unaware), Limited to One Sense (Choose
one sense: Vision or Auditory) • 1 point

•  Disintegrate: Ranged Affects Objects Weaken

Toughness 8 • 1 point

•  Energy Burst: Choose One: Burst Area Damage
10, Penetrating 4 • 1 point or Ranged Burst Area
Damage 8 • 1 point

DODGE
+4

PARRY
+1

FORTITUDE
+5

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

34

82

4

SKILLS

DEFENSES

TOTAL

14

16

150

7-8

•  Energy Constructs: Create 12 • 1 point

9-10

•  Energy Manipulation: Deflect 12, Reflect,
Redirect, Limited to Energy attacks • 1 point

•  Motivation—Recognition: Energy Controllers, par-
ticularly those with a flashy energy type, often desire
fame and attention.

11-12

•  Energy Weapon: Penetrating Damage 12 • 1 point

13-14

15-16

17-18

•  Environmental Control: Environment 12 (8 miles;
Choose two: Cold, Heat, Impede Movement, Light,
Visibility) • 1 point

•  Obscure: Ranged Visual Concealment 4 Attack,

Choose One Extra: Burst Area or Cloud Area • 1 point

•  Snare: Cumulative Ranged Affliction 8 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile), Extra
Condition, Limited to Two Degrees • 1 point

19-20

•  Telekinesis: Move Object 12 • 1 point

Energy Immunity: Immunity 5 (Energy Control type damage)

• 5 points

Roll 1d20 once and record the result.

1-5

6-10

11-20

Energy Absorption: Enhanced Strength 10, Fades;

Enhanced Stamina 10, Fades • 20 points

Energy Shield: Enhanced Defenses 10 (Dodge 5, Parry
5); Impervious Protection 5, Sustained • 20 points

Force Field: Impervious Protection 10, Sustained

• 20 points

Energy Sense: Senses 1 (Energy type Awareness) • 1 point

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

5-8

Energy Aura: Reaction Damage 4, Activation

(Standard Action, -2 points) • 14 points

Energy Form: Insubstantial 3 (Energy Control type),

Activation (Move Action, -1 point) • 14 points

9-16

Flight: Flight 7 (250 MPH) • 14 points

17-18

Scry: Visual Remote Sensing 14 (60 miles), Medium
(presence or cond

[... truncated ...]
```

**Chunk 6** (`150cf8210923`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

when you time-travel. If you apply the Increased Mass modi-
fier, you can carry additional mass up to your modifier rank.

HOOD: TIME, SPACE, AND DIMENSION TRAVEL

TRACKLESS

You leave no trail and cannot be tracked using visual sens-
es  (although  you  can  still  be  tracked  using  scent  or  other
means). You can walk across the surface of soft sand or snow
without leaving tracks and you have total concealment from
tremorsense (see Concealment, page 244). Each additional
rank renders you trackless to another sense type.
WALL-CRAWLING

You can climb walls and ceilings at your ground speed rank
–1 with no chance of falling and no need for an Athletics
check. You are still vulnerable while climbing, however. An
additional rank of this effect means you climb at your full
speed rank and are not vulnerable while climbing.
WATER-WALKING

You can stand or move at your normal ground speed on
the surface of water, quicksand, and other liquids without
sinking. If you fall prone for any reason, you sink into the
liquid normally. With 2 ranks of this effect, you can also lie
prone on a liquid surface without sinking; you only sink if
you choose to.

NULLIFY

ATTACK

Action: Standard • Range: Ranged
Duration: Instant • Cost: 1 point per rank

Nullify  can  counter  particular  effects  of  a  particular  de-
scriptor,  such  as  fire  effects,  magical  effects,  mental  ef-
fects, and so forth (see Countering Effects, at the start of
this chapter). You can counter one effect of your chosen
descriptor per use of Nullify. You can’t nullify innate effects
(see the Innate modifier description).

Make a ranged attack check to hit the target. Then make
an  opposed  check  of  your  Nullify  rank  and  the  targeted
effect’s  rank  or  the  target’s  Will  defense,  whichever  is
higher. If you are targeting the subject of an effect rather
than the effect’s user, make an opposed check of Nullify
rank vs. effect rank. If you win, the targeted effect turns off,
although the user can re-activate it normally. If you lose
the opposed check, you do not Nullify the effect. With two
or more degrees of failure, trying again against the same
subject in the same scene requires extra effort.
EXTRAS

Affects Insubstantial: Nullify does not require this modi-
fier to affect insubstantial targets, or the Insubstantial ef-
fect itself. You can attempt to nullify the effects of insub-
stantial targets normally.

Alternate Resistance

[... truncated ...]
```

**Chunk 7** (`17270869c240`):

```
CHAPTER 2: SECRET ORIGINS

87

Roll 1d20 once and record the result.

1-5

Fighter: You were trained in combat.

6-10

Nimble: You are quick-footed.

11-15

Prodigy: You have learned a little bit of everything.

16-20

Team-Player: You have experience working as part
of a super-team.

FIGHTER

Close Attack 2, Equipment (Sword or other melee weapon)

NIMBLE

Evasion, Instant Up, Move-by Action

PRODIGY

Beginner’s Luck, Eidetic Memory, Well-informed

TEAM-PLAYER

Interpose, Set-up, Teamwork

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Athlete: You are a trained athlete.

Charmer: People like you.

9-12

Police: You work in law enforcement.

13-16

Scientist: You are an expert in a field of science.

17-20

Thief: You’ve operated outside the law.

16-20

ATHLETE

Acrobatics 4, Athletics 8, Perception 4

CHARMER

Deception 6, Insight 4, Persuasion 6

POLICE

Insight 4, Investigation 6, Perception 6

SCIENTIST

Expertise: (Choose One) 6, Technology 6, Vehicles 4

THIEF

Deception 4, Stealth 6, Technology 6

POWERS

Roll 1d20 once and record the result.

Running: Roll 1d20 once:

1-10

Gravity-Defying Runner: Movement
3 (Wall-crawling 2, Water Walking),
Limited to While Moving; Quickness 10;
Speed 15 (64,000 MPH) • 28 points

1-10

11-15

16-20

Rapid Metabolism: Immunity 1 (Poison);
Quickness 11; Regeneration 5; Speed
11 (4,000 MPH) • 28 points

Time-Traveler: Movement 3 (Time

Travel—any time); Quickness 10; Senses
4 (Precognition), Check Required
(Intellect or Expertise: History); Speed
10 (2,000 MPH) • 28 points

11-15

Flying: Roll 1d20 once:

Cosmic Speedster: Flight 9 (1,000 MPH);

Immunity 6 (cold, heat, radiation,
suffocation, vacuum); Movement 2
(Environmental Adaptation—Zero-G;
Space Travel 1) • 28 points

Hypersonic: Flight 14 (32,000 MPH) • 28

points

Hyper-Speed: Flight 10 (2,000 MPH);

Quickness 8 • 28 points

1-5

6-15

16-20

Teleporting: Roll 1d20 once:

1-5

6-10

Dimensional Walker: Movement 3

(Dimension Travel—any dimension);
Teleport 11 (8 miles) • 28 points

Proximal: Teleport 9 (2 miles), Accurate,

Turnabout • 28 points

Transmit: Teleport 9 (2 miles), Easy,

11-15

Extended (500 miles), Medium (Choose
One), Turnabout • 28 points

16-20

World-Walker: Teleport 9 (2 miles),
Extended (500 miles), Turnabout
• 28 points

Speedster Stunts: Array (20 points plus 1 point of Al-
ternate Effect)

Roll 1d20 once and record the result as the first power in
the  Speedster  Stunts  a

[... truncated ...]
```

**Chunk 8** (`19a54c3b3576`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

6-9

Magic Sword: Strength-based Damage 3 (6 Damage
with Strength), Multiattack 6, Penetrating 6, Easily
Removable (-6 points) • 9 points

10-11

12-13

Modified Nunchaku: Strength-based Damage 2 (5
Damage with Strength), Multiattack 5, Improved
Grab, Improved Trip, Reach 3, Ricochet; Movement
1 (Swinging); Easily Removable (-6 points) • 9 points

Perfect Aim: Perception Range Damage 5, Easily
Removable (ranged or improvised weapon, -6
points) • 9 points

14-15

Rapid Shot: Ranged Multiattack Damage 5, Easily
Removable (ranged weapon, -6 points) • 9 points

16-20

Super-Shield: Array (13 points plus 2 points of

Alternate Effects), Easily Removable (-6 points)
• 9 points total

•  Blocking: Deflect 13 • 13 points

•  Shield Bash: Strength-based Damage 2 (5

Damage with Strength), Penetrating 5 • 1 point

•  Shield Throw: Strength-based Ranged Damage 2
(5 Damage with Strength), Multiattack 5 • 1 point

Roll 1d20 once and record the result.

1-2

3-6

7-10

11-12

Blindsight: Senses 6 (Accurate, Analytical and

Extended Hearing, Hearing Counters Illusion)
• 6 points

Catlike Balance: Enhanced Skills 2 (Acrobatics 4),
Leaping 2 (30 feet), Movement 1 (Safe Fall)
• 6 points

Healing Factor: Immunity 1 (Disease); Regeneration

5 • 6 points

Probing Sight: Mind Reading 4, Limited to Surface
Thoughts, Visually Sense-Dependent; Senses 4
(Vision Penetrates Concealment) • 6 points

13-14

Reinforced Body: Impervious Toughness 6 • 6 points

15-16

17-20

Resilient: Immunity 6 (Cold, Drowning, Heat, Need
for Sleep, Pressure, Starvation and Thirst) • 6 points

Super-Soldier: Enhanced Fortitude 2, Regeneration

2; Speed 2 (8 MPH) • 6 points

DEFENSE

DODGE
+7

PARRY
+6

FORTITUDE
+5

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

56

15

13

SKILLS

DEFENSES

TOTAL

40

26

150

•  Motivation—Recognition:  The  Weapon  Master  is
driven by a need to be recognized as the best at what
he does.

•

•

•

Disability:  The  Weapon  Master  has  a  disability  of
some sort, such as blindness or only one arm, that he
overcomes through his skills or powers.

Honor:  The  Weapon  Master  abides  by  a  warrior’s
code of honor.

Rival: The Weapon Master has a foil—another Weap-
on Master who tries to outdo him at every turn.

Weather  Controllers  combine  control  over  the  elements
of air and water with cold and electrical energy. They gen-
erally command the more violent aspects of the weather,
such as 

[... truncated ...]
```

**Chunk 9** (`1b8011530852`):

```
CHAPTER 2: SECRET ORIGINS

101

11-15

16-20

Vigilante: You use your weapons to fight crime and
injustice.

Weaponsmith: You craft your own weapons and
even augment them with the latest technology.

SOLDIER

Expertise: Military 6, Vehicles 6

TIME-DISPLACED

PERSONALITY

Deception 8, Intimidation 8, Persuasion 8

TALKER

Deception 10, Insight 4, Persuasion 10

POWERS

Expertise: History 6, Choose One: Expertise: Magic 6 or
Technology 6

VIGILANTE

Roll 1d20 once and record the result.

Expertise: Streetwise 6, Investigation 6

WEAPONSMITH

Expertise: Weapons 6, Technology 6

Roll 1d20 once and record the result.

1-6

Flamboyant: You fight with great flair.

7-14

Instinctive: You let your well-honed reflexes take over.

15-20

Sneaky: You prefer to avoid a direct confrontation.

FLAMBOYANT

Acrobatics 8, Athletics 4, Sleight of Hand 4

INSTINCTIVE

Acrobatics 6, Athletics 6, Stealth 4

SNEAKY

Acrobatics 6, Athletics 4, Stealth 6

Roll 1d20 once and record the result.

1-4

5-8

Assertive: You know how and when to take charge.

Cunning: You are good at manipulating others.

9-12

Empathic: You seem to understand others.

13-16

Forceful Personality: Others seem to instinctively
respect you.

17-20

Smooth Talker: You know how to get your way.

ASSERTIVE

Insight 8, Intimidation 8, Persuasion 8

CUNNING

Deception 10, Insight 8, Perception 6

EMPATHIC

Insight 10, Perception 6, Persuasion 8

Bow and Trick Arrows: Array (10 points plus five

Alternate Effects), Easily Removable (-6 points) • 9
points total

Standard Arrow: Ranged Damage 5 • 10 points

Roll 1d20 five times (re-roll if you get the same result
twice) and add them to the Bow and Trick Arrows
array as Alternate Effects.

1-2

3-4

5-6

7-8

1-5

9-10

11-12

13-14

15-16

17-18

19-20

•  Boomerang Arrow: Ranged Damage

4, Homing, Subtle • 1 point

•  Boxing Glove Arrow: Ranged
Affliction 5 (Resisted by Dodge,
Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

•  Cable Arrow: Movement 1

(Swinging) • 1 point (if you get this
result twice, place the Cable Arrow
outside the array instead for 2
points): Cable Arrow: Movement 1
(Swinging) • 2 points

•  Explosive Arrow: Burst Area Ranged
Damage 5, Unreliable (five uses)
• 1 point

•  Flare Arrow: Ranged Cumulative

Affliction 5 (Resisted and Overcome
by Fortitude; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to One Sense • 1 point

•  Knockout Gas Arrow: Burst Area
Ranged Affliction 5 (Resisted and
Overcome by Fort

[... truncated ...]
```

**Chunk 10** (`267bbd73af09`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

INNOCENT

Animal Empathy, Luck

INCISIVE

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

SUBTLE

Evasion, Hide in Plain Sight

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-3

Dynamic: You are a good all-around athlete.

4-7

Empathic: You understand what makes other
people tick.

8-10

Furtive: You don’t like to stand out.

11-14

Inscrutable: Your emotions are difficult to read.

15-18 Observant: Little escapes your notice.

19-20

Sponge: You possess an open and receptive mind.

DYNAMIC

Acrobatics 6, Athletics 6

EMPATHIC

Insight 8, Persuasion 4

FURTIVE

Deception 6, Stealth 6

INSCRUTABLE

Deception 8, Perception 4

OBSERVANT

Insight 6, Perception 6

SPONGE

Expertise: Current Events 4, Expertise: Popular Culture 4,
Investigation 4

POWERS

Roll 1d20 once and record the result.

1-2

Animal Mimicry: Variable 10 (50 points, to mimic
Traits of one animal at a time), Continuous
• 80 points

Mental Duplication: Mind Reading 10, Limited
to Duplicated mind; Variable 10 (50 points, for
duplicating a subject’s mental traits), Continuous,
Resistible by Will • 80 points

Nemesis: Variable 8 (40 points, for traits suitable for
confronting a particular opponent), Continuous,
Free Action • 80 points

Object Mimicry: Variable 8 (40 points, for traits of

object touched), Reaction • 80 points

3-4

5-6

7-9

10-13

Power Duplication: Variable 10 (50 points, for

duplicating one target’s powers), Continuous
• 80 points

14-15

Power Theft: Cumulative Affliction 12 (Resisted

and Overcome by Will; Powers Impaired, Powers
Disabled, Transformed—Powerless) Linked to
Variable 8 (40 points, for duplicating one target’s
powers), Move Action, Limited to Afflicted
subjects • 80 points

16-17

Reflex Memory: Variable 8 (40 points, for observed
Skills and Advantages), Continuous, Free Action
• 80 points

18-20

Android Body: Immunity 30 (Fortitude Effects),
Reduced Traits (Stamina —, Fortitude —);
Protection 5 • 16 points

Power Duplication: Variable 8 (40 points, for

duplicating a target’s powers), Continuous • 64 points

DEFENSES

DODGE
+5

PARRY
+5

FORTITUDE
+5

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

32

80

6

SKILLS

DEFENSES

TOTAL

12

20

150

•  Motivation—Acceptance: Due to the nature of their
powers, many Mimics feel as if they lack an identity of
their own. They may seek acceptance as unique indi-
v

[... truncated ...]
```

**Chunk 11** (`2ec68f50f56a`):

```
CHAPTER 6: POWERS

151

Others with an acute sense able to detect your Commu-
nication  medium  can “tap  into”  your  transmissions  with
a Perception check (DC 10 + your Communication rank).
The eavesdropper must be within normal sensory range
of you or the receiver. With two degrees of success on the
check, the eavesdropped can also understand your trans-
missions. Effects like Concealment and Dazzle that target
your  Communication  medium  can  “jam”  or  block  your
transmissions.
EXTRAS

Area: You  can  broadcast  omni-directionally  to  every  re-
ceiver  within  your  maximum  Communication  range  at
once. Note this extra is only strictly necessary to commu-
nicate  with  everyone  over  a  wide  area  all  at  once;  since
using  and  maintaining  Communication  are  free  actions,
the GM may allow a communicator to establish and main-
tain contact with multiple discrete receivers—such as the
members  of  the  same  team—all  in  the  same  round.  +1
cost per rank.

Dimensional:  Communication  with  this  modifier  can
bridge  dimensional  barriers,  reaching  into  other  dimen-
sions and planes of existence. The Communication effect
still has its proximate range, and the GM may rule certain
subjects “out of range” of the effect, depending on their
relative positions in the other dimension. Flat +1 point.

Rapid: Your  communication  occurs  10  times  faster  than
normal speech. Each additional rank increases communi-
cation speed by a factor of 10. This is useful for high-speed
computer  links, “deep  sharing”  psychic  rapports,  and  so
forth. Flat +1 point.

Selective:  If  you  have  the  Area  extra,  you  can  choose
which receiver(s) within range get your Communication,
excluding  everyone  else.  This  allows  you  to  go  from  a
single receiver (point-to-point) to all potential receivers in
range (omni-directional) or anywhere in between. +1 cost
per rank.

Subtle:  Your  Communication  cannot  be  “overheard”  (it
is encrypted, scrambled, or otherwise protected). With 2
ranks, your Communication cannot even be detected (that
is,  no  one  can  even  tell  you  are  transmitting,  much  less
what you’re saying). Flat +1 or 2 points.

FLAWS

Limited:  Communication  may  be  limited  to  only  mem-
bers of a particular group, such as a species, family, mem-
bers  of  an  organization,  and  so  forth. This  is  in  addition
to limitations imposed by medium (that is, requiring sub-
jects to have a means of picking up on the Communica

[... truncated ...]
```

**Chunk 12** (`301534069c2d`):

```
CHAPTER 2: SECRET ORIGINS

99

5-8

Cybernetic Implants: Enhanced Awareness

2; Enhanced Advantages 2 (Eidetic Memory,
Improved Initiative); Enhanced Defenses 4 (Parry
2, Dodge 2); Senses 6 (Accurate and Extended
Hearing, Analytical and Extended Vision,
Infravision) • 16 points

9-15

Healing Factor: Enhanced Stamina 2; Immunity 2
(disease, poison); Regeneration 10 • 16 points

16-20

Tactical Mastermind: Enhanced Intellect 2,

Enhanced Awareness 2; Enhanced Advantages
3 (Defensive Roll 2, Uncanny Dodge); Senses
5 (Danger Sense, Detect Weakness—Acute,
Analytical, Ranged) • 16 points

OTHERWORLDLY

Roll 1d20 once and record the result.

1-4

5-6

7-11

12-17

18-20

Alien: Enhanced Stamina 2; Immunity 7 (Cold, Heat,
Pressure, Radiation, Suffocation, Vacuum); Mental
Communication 1; Senses 1 (Mental Awareness)
• 16 points

Aquatic: Enhanced Stamina 2; Immunity 3 (Cold,

Drowning, Pressure); Movement 1 (Environmental
Adaptation—Aquatic); Senses 1 (Low-light Vision);
Swimming 6 (30 MPH) • 16 points

Exemplar: Enhanced Stamina 1, Enhanced

Awareness 1, Enhanced Defenses 2 (Dodge 1,
Parry 1); Immunity 2 (Aging, Disease); Quickness 4;
Speed 4 (30 MPH) • 16 points

Immortal: Enhanced Awareness 2; Immortality
5, Limited (choose effect); Immunity 3 (Aging,
Disease, Poison); Protection 2; Regeneration 2
• 16 points

Winged: Enhanced Awareness 2, Enhanced

Defenses 4 (Dodge 2, Parry 2); Flight 6 (120 MPH),
Wings; Immunity 1 (Cold); Senses 1 (Extended
Vision) • 16 points

HUMAN

Roll 1d20 once and record the result.

11-20

Unique Weapon: Strength-based Damage 3,

Accurate, Penetrating 10 plus roll 1d20 once:

1-5

6-10

Atom Slicer: Weaken Toughness 10,

Penetrating 2, Linked to Damage, Easily
Removable (-10 points) • 16 points

Boom Staff: Movement 3 (Space Travel

3), Portal; Easily Removable (-10
points) • 16  points

11-15

Dimension Cutter: Movement 3

(Dimension Travel 3), Portal; Easily
Removable (-10 points) • 16 points

16-20

Thundering Mallet: Cumulative
Affliction 10 (Resisted and
Overcome by Fortitude; Vulnerable,
Defenseless), Limited Degree, Linked
to Damage, Penetrating 2; Easily
Removable (-10 points) • 16 points

DEFENSE

DODGE
+4

PARRY
+2

ABILITIES

POWERS

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

78

32

9

SKILLS

DEFENSES

TOTAL

17

14

150

•  Motivation—Patriotism:  Duty  to  country  may  have
motivated the warrior to have undergone experiments
that transformed him or to visit the world outside his
home.

•  Motivation—Responsibility:  The  war

[... truncated ...]
```

**Chunk 13** (`3739eabb7a65`):

```
CHAPTER 6: POWERS

171

Concentration:  Concentration  Move  Object  requires
more attention to maintain. You cannot concentrate to in-
crease your lifting capacity or to grab or move another ob-
ject while you are still “holding” your first. –1 cost per rank.

Limited Direction: You can only move objects in a par-
ticular direction or path, such as only up and down (to-
wards and away from the ground), only directly towards
or  away  from  you  (attraction  and  repulsion),  and  so
forth. This is useful for “gravitic” or “magnetic” versions of
the effect. –1 cost per rank.

Limited Material: You can only move a particular type of
object or material, such as only metals, plants, rock, water,
and so forth. –1 cost per rank (The GM may allow a –2 cost
per  rank  flaw  for  a  particularly  limited  type  of  material,
such as only precious metals, leaves, sand, or petroleum).

MOVEMENT

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You have a special form of movement. For each rank in this
effect, choose one of the following options:

You  can  move  instantly  from  one  dimension  to  another
as a move action. For 1 rank, you can move between your
home dimension and one other. For 2 ranks you can move
between  any  of  a  related  group  of  dimensions  (mystical
dimensions,  alien  dimensions,  etc).  For  3  ranks  you  can
travel to any dimension. You can carry up to 50 lbs. (mass
rank 0) of additional material with you when you move. If
you apply the Increased Mass modifier, you can carry ad-
ditional mass up to your modifier rank.

You’re  adapted  to  a  particular  environment,  such  as  un-
derwater,  zero  gravity,  and  so  forth  (see  Environmental
Hazards,  pages  185-187,  for  details). You  suffer  none  of
the normal unfavorable circumstance or movement pen-
alties associated with that environment, moving and act-
ing normally. You are still affected by environmental haz-
ards like suffocation, exposure, and so forth. You need the
Immunity effect to ignore such things.

PERMEATE

You  can  pass  through  solid  objects  as  if  they  weren’t
there. For 1 rank, you can move at speed rank –2 through
any physical object. For 2 ranks, you can move at speed
rank –1 and for 3 ranks, you move at your normal speed
through  any  obstacles. You  cannot  breathe  while  com-
pletely  inside  a  solid  object,  so  you  either  need  Im-
munity to Suffocation or have to hold your breath. You
may also need Pe

[... truncated ...]
```

**Chunk 14** (`373c8323a9b6`):

```
CHAPTER 6: POWERS

149

Spread throughout this section are boxes like this one,
providing  examples  of  some  of  the  most  common
powers  found  amongst  superhero  characters  to  give
you a “menu” of pre-fabricated powers to choose from
when  creating  your  own  heroes  (and  villains)  in  MU-
MASTERMINDS.  Sample  powers  are  presented  on
the Power Effects table in italics.

Each power is presented in the following format:

NAME

Effect(s): Modifier(s) • Cost

Name: What the power is called. Feel free to mod-
ify the name to suit how you’re using the power.

Effects: The power’s effect or effects are listed by
name.

Modifiers:  Any  modifiers  applying  to  the  effect
are  listed  with  it.  If  a  power  has  multiple  effects,
each is listed with its applicable modifiers.

Cost: Lastly, the power’s cost is given. This is a cost
per rank of the power if it has a ranked effect, oth-
erwise it is a flat cost in power points. Some pow-
ers may have a flat cost for the initial power, plus a
cost per rank for additional ranks.

Effect: Varies, Activation • effects total –1 or 2 points

isting degrees on the target. For example, if you hit a target
and impose a vulnerable condition (one degree), then at-
tack again and get one degree on the effect, you impose
the Affliction’s second degree condition. +1 cost per rank.

Extra  Condition:  Your  Affliction  imposes  an  additional
condition per degree of success. So with one application of
this extra, your Affliction imposes two conditions—such as
dazed  and  hindered,  or  impaired  and  vulnerable—rather
than just one. With two applications, it imposes three con-
ditions,  and  so  forth.  Since  mutually  incompatible  condi-
tions  are  largely  wasted,  Afflictions  with  this  extra  often
have the Limited Degree flaw as well. +1 cost per rank.

Progressive: This modifier causes an Affliction to increase
incrementally  without  any  effort  from  you.  If  the  target
fails  a  resistance  check  to  end  the  Affliction,  it  not  only
persists, but increases in effect by one degree! So a target
affected by the first degree of a Progressive Affliction who
fails to resist progresses to the second degree of the effect
at the start of his next round. A successful resistance check
still ends the Affliction, as usual. +2 cost per rank.

FLAWS

Instant Recovery: Similar to the Reversible extra (see p.
196),  the  target  of  an  Affliction  effect  with  this  modifier
recovers  automatically,  no  c

[... truncated ...]
```

**Chunk 15** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 16** (`437f5039e60f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Perception range effects must accurately perceive a target in order to affect it. This generally means you cannot target
subjects with total concealment from your accurate senses with perception range effects. Thus, foes with Visual Conceal-
ment (the most common accurate sense) can be quite effective against characters relying on perception range attacks,
unless the attacker has an unusual accurate sense to circumvent the Concealment. This is one reason Visual Concealment
costs extra.

At the Gamemaster’s discretion, a successful Perception check to accurately locate a target with an acute sense may al-
low you to use perception range effects on that target; however, the target still benefits from concealment, granting a +5
circumstance bonus to resistance against the effect.

ranks. A plant’s sense of its surroundings is limited, so it
won’t be able to give (or recognize) detailed descriptions
or answer questions about events outside its immediate
vicinity.

SPIRITS

You can communicate with incorporeal and normally in-
visible and inaudible spirit beings, such as ghosts or cer-
tain extradimensional entities, depending on the context
of the setting. Rank 1 essentially allows you to function as
a “medium” of sorts, able to perceive spirits and relay what
you see and hear. Rank 2 allows you to be clearly under-
stood by denizens of the spirit world, as well. At the GM’s
discretion,  this  effect  may  extend  to  undead  creatures,
demons, or other supernatural entities, depending on the
setting.

FLAWS

Type: You can only comprehend a broad type of subject
(only elves, canines, avians, or sea creatures, for example).
For an additional flaw, you can only comprehend a narrow
type of subject (dogs, falcons, or dolphins, for example).
Broad –1 cost per rank. Narrow –2 cost per rank.

SENSORY

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You gain total concealment from a particular sense while
this  effect  is  active,  although  you  are  still  detectable  to
other senses (even other senses of the same sense type;
so you could have full concealment against normal sight,
but not infravision or any other sense in the sight sense
type).  Each  additional  rank  gives  you  concealment  from
another sense; two ranks give you concealment for an en-
tire sense type. See Concealment on page 244 for the full
effects.

Concealment from visual senses costs double (2 ranks for
one

[... truncated ...]
```

**Chunk 17** (`43d5c758bf78`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WASP

Insect Senses: Senses 4 (Acute Smell, Darkvision,

Ranged Touch) • 4 points

16-20

Sting: Cumulative Affliction 8 (Resisted and Overcome
by Fortitude; Impaired, Disabled, Incapacitated),
Linked to Damage 8, Accurate 2 • 26 points

Roll 1d20 once and record the result.

CANINE

Bite: Strength-based Damage 3, Improved Critical,

Wings: Flight 6 (120 MPH), Wings • 6 points

Penetrating 3 • 7 points

Canine Senses: Senses 3 (Low-light Vision, Acute

and Tracking Olfactory) • 3 points

1-10

Canine Movement: Leaping 2 (30 feet); Speed 4 (30

Talons: Strength-based Damage 1, Accurate 2, Fast Grab

MPH) • 6 points

• 4 points

Roll 1d20 once and record the result.

FALCON

Flight: Flight 6 (120 MPH), Wings • 6 points

Keen Eyesight: Senses 3 (Extended 2 and Rapid

Vision) • 3 points

1-10

Sonic Scream: Cone Area Affliction 9 (Resisted

and Overcome by Fortitude; Dazed and Auditory
Impaired, Stunned and Auditory Disabled,
Incapacitated and Auditory Unaware), Extra
Condition, Quirk—Impaired, Disabled, Unaware
Limited to One Sense (-4 points) • 23 points

11-20

OWL

Nightvision: Senses 2 (Extended Vision, Low-light

Vision) • 2 points

11-20

Shriek: Cone Area Affliction 8 (Resisted and
Overcome by Will; Dazed and Vulnerable,
Stunned and Defenseless, Incapacitated)
• 24 points

Silent Flight: Flight 5 (60 MPH), Subtle, Wings • 6 points

Howl: Auditory Perception Area Affliction

10 (Resisted and Overcome by Will; Dazed
and Impaired, Disabled and Stunned), Extra
Condition, Limited Degree • 20 points

FELINE

Claws: Strength-based Damage 1, Accurate,

Improved Critical • 3 points

Feline Senses: Senses 3 (Low-light Vision, Acute and

Tracking Olfactory) • 3 points

Feline Movement: Leaping 3 (60 feet); Movement
3 (Safe Fall, Sure-footed, Trackless); Movement
1 (Water-walking), Limited to Solid Surfaces;
Movement 1 (Wall-crawling), Limited to One
Move Action; Speed 4 (30 MPH) • 15 points

Plus roll 1d20 once and record the result.

1-5

Black Cat: Reaction Visual Perception

Area Affliction 5 (Resisted by Dodge,
Overcome by Will; Vulnerable,
Defenseless, Incapacitated), Side-
effect (Always happens, chosen by
player) • 15 points

```

**Chunk 18** (`44f0396c2518`):

```
CHAPTER 6: POWERS

163

Insight  check.  Senses  with  the  Counters  Illusion  effect
(see Senses) automatically detect illusions. If any viewer
successfully uncovers an illusion and communicates this
fact to others, they gain another Insight check with a +5
circumstance bonus. Circumstances may grant additional
modifiers to the Insight check to uncover an illusion, de-
pending on how convincing it is.

Maintaining an active illusion (such as a fighting creature)
requires a standard action each round, but maintaining a
static illusion (one that doesn’t move or interact) is only a
free action.

EXTRAS

Illusion is a broad-ranging effect, usable for a number of
different things. A few common considerations for Illu-
sion include the following.

Independent: Your active illusions only require a free action
to maintain, rather than a standard action. +1 cost per rank.

Selective:  You  choose  who  perceives  your  Illusion  and
who doesn’t. +1 cost per rank.

For illusions so realistic they are capable of inflicting dam-
age, add a Linked Perception Range Damage effect. At the
GM’s discretion, this effect can even be made into a Linked
Array  with  a  variety  of  alternate  attack  effects,  allowing
your illusionist to inflict conditions other than damage on
targets. Keep in mind the attack effects all need to be per-
ception range to match the range of Illusion.

Illusion  can  alter  a  subject’s  appearance,  providing  an
essentially impenetrable disguise—at least until some-
one  makes  a  successful  check  to  see  through  the  illu-
sion.  However,  for  just  the  ability  to  alter  appearance,
use the Morph effect, which is generally more effective
than Illusion Limited to Appearance.

The  default  Illusion  effect  is  perceptible  to  anyone  or
anything  (including  machines)  as  if  it  were  real.  Some
illusions exist solely in the mind, like projected psychic
hallucinations. This type of Illusion has the Resistible by
Will flaw and the Selective extra, since the illusionist can
choose whether or not to project the illusion into a par-
ticular subject’s mind, and therefore decides who can or
cannot perceive the illusion. This is a net +0 modifier, for
the same base cost.
MY ALLY, MY ENEMY

A common Illusion trick is to switch the appearances of
an  enemy  and  an  ally,  causing  a  foe’s  teammate  to  at-
tack  that  enemy  by  mistake. You  can  generally  handle
this with an opposed check of Illusion and Insight; if you
win, the tar

[... truncated ...]
```

**Chunk 19** (`5731b0e9cb2f`):

```
CHAPTER 6: POWERS

177

1-4 RANKS

Senses  in  MUTANTS  &  MASTERMINDS  are  broken  down  into
sense types, used as descriptors for sensory effects. Here
are  the  traits  of  normal  human  senses,  for  use  when
modifying them with the options from Senses:

VISUAL

Normal  vision  is  ranged  (with  a  –1/10  feet  modifier),
acute (able to distinguish fine details) and accurate (able
to pinpoint the locations of things).
AUDITORY

Normal hearing is ranged  (with  a –1/10  feet modifier),
acute  (able  to  pick  up  details  like  differences  in  tone),
and radius (able to pick up on sounds coming from any
direction). Normal hearing is not accurate.

OLFACTORY

Normal  human  olfactory  senses,  which  lump  together
smell  and  taste  for  descriptor  purposes,  are  fairly  lim-
ited. Ordinary human olfactory senses are neither acute
nor accurate. The sense of smell is a radius sense, how-
ever, able to pick up on scents coming from any direc-
tion. Its “range” is quite limited, however, effectively only
close, except for especially strong scents.

TACTILE

The normal sense of touch is, by definition, close range.
It is accurate (in that you know the location of anything
you  can  touch)  and  radius  (in  that  you  can  feel  things
from any surface of your body).

MENTAL

In MUTANTS & MASTERMINDS terms, the “sixth sense” or men-
tal  sense  type  is  fairly  crude  in  normal  humans,  lim-
ited essentially to interactions with the Insight skill and
awareness of mental effects used directly on you. Thus it
is close range and has none of the Sense qualities.

horizon and physical barriers between you and the sub-
ject, unless it also Penetrates Concealment.

1 RANK

You can see in the infrared portion of the spectrum, allow-
ing you to see heat patterns. Darkness does not provide
concealment  for  objects  differing  in  temperature  from
their  surroundings.  If  you  have  the Track  effect,  you  can
track warm creatures by the faint heat trails they leave be-
hind. The Gamemaster is the final judge on how long the
trail remains visible.
VISION

1 RANK

You can view extremely small things. You can make Per-
ception checks to see tiny things nearby. Cost is 1 rank for
dust-sized  objects,  2  ranks  for  cellular-sized,  3  ranks  for
DNA and complex molecules, 4 ranks for atomic-sized. The
GM  may  require  an  Expertise  skill  check  to  understand
and interpret what you see.

4 RANKS

A sense with this trait is unaffected by concealment from

[... truncated ...]
```

**Chunk 20** (`661dd344a1d2`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

the  round  in  which  the  duration  ends.  So,  for  example,
an instant duration Affliction only lasts one round, while
a  sustained  duration  Affliction  lasts  until  no  longer  sus-
tained. –1 cost per rank.

Limited Degree: Your Affliction is limited to no more than
two degrees of effect. With two applications of this modi-
fier, it is limited to no more than one degree of effect. –1
cost per rank.

BURROWING

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You can burrow through the ground, leaving a tunnel be-
hind if you choose. You move through soil and sand at a
speed rank equal to your Burrowing rank, minus 5. So Bur-
rowing 8, for example, lets you move through the ground
at speed rank 3 (around 16 MPH). Burrowing through hard
clay and packed earth reduces speed one additional rank.
Burrowing through solid rock reduces it by two additional
ranks. The tunnel you leave behind is either permanent or
collapses behind you immediately (your choice when you
begin burrowing each new tunnel).

Note  that  Burrowing  differs  from  the  Permeate  effect  of
Movement, which allows you to pass through an obstacle
like the ground at your normal speed without disturbing
it at all (see Movement for details).
EXTRAS

Penetrating:  Normally,  the  hardness  of  the  ground  af-
fects  only  the  speed  at  which  you  burrow.  At  the  GM’s
discretion, some super-hard materials may be considered
Impervious to Burrowing, in which case this extra allows
you to dig through them. 1 point per rank.

Ranged: This extra either allows you to create tunnels at a
greater distance (without having to be at the end-point of
the tunnel as it forms) or, in conjunction with Affects Oth-
ers, allows you to grant the Burrowing effect to someone
else at a distance. Doing both requires two applications of
the extra. +1 or 2 cost per rank.

FLAWS

Limited:  Burrowing  may  be  limited  to  certain  circum-
stances  or  materials,  such  as  only  loose  sand  and  soil

BLAST

Effect: Ranged Damage • 2 points per rank

You  can  make  a  damaging  ranged  attack.  It  might  be
a  blast  of  energy,  a  projectile  (arrow,  bullet,  throwing
blade, etc.), or some similar effect. You make a ranged
attack  check  against  the  target’s  Dodge  defense.  The
attack’s damage equals your power rank and the target
makes a Toughness resistance check against it.

(leaving  the  character  una

[... truncated ...]
```

**Chunk 21** (`685941d4ae65`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

The Elementals described here generally have traits such as Insubstantial default to Permanent. However, some elemen-
tals may be able to transform between their elemental and a flesh and blood form. Such elementals may have Sustained
powers and possibly the Activation Flaw if the transformation takes time or effort. In this case, the Activation Flaw can free
up a point that the player can spend on an additional Alternate Effect or Advantage.

Alternately, the elementals who are considered Embodiments (as rolled on the Abilities) may have Innate forms that can-
not be turned off even by nullification effects. Players may wish to take a point from another trait (such as an Alternate
Effect or Advantage) to buy the Innate Extra.

•  Earth Blast: Ranged Damage 10 • 1 point

5-10

•  Earthen Snare: Cumulative Affliction 10 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Immobile and Defenseless), Extra
Condition, Limited to Two Degrees • 1 point

11-14

Particulate Form: Elongation 7; Insubstantial 2;

Movement 2 (Slithering, Sure-Footed); Speed 2;
Visual Concealment 4, Partial • 23 points

Sandstorm: Environment 5 (Visibility -5; 500 feet

radius) • 10 points

Plant Form: Visual Concealment 4, Limited: in

vegetation; Immunity 2 (Plant Powers); Teleport 7,
Medium (Plants) • 13 points

Plant Control: Array (20 points + four Alternate Effects)

•  Plant Toxin: Cumulative Affliction 10 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated) 20 points

Take the Plant Control array and Plant Toxin (above)
and roll 1d20 four times (re-roll if you get the same
result) and add them to the array as Alternate Effects.

1-4

5-8

9-12

13-16

17-20

•  Animate Tree: Summon 10,

Controlled, Limited to Size and
Availability of tree • 1 point

•  Entanglement: Burst Area

Cumulative Affliction 10 (Resisted
by Dodge, Overcome by Damge;
Hindered and Vulnerable, Defenseless
and Immobile), Extra Condition,
Limited to Two Degrees, Limited:
Requires Ambient Plant-life • 1 point

•  Plant Perception: Remote Sensing 5
(All Senses), Medium (Plants) • 1 point

•  Wood Objects: Create 7, Innate,

Movable • 1 point

•  Transmit: Teleport 10, Extended,

Medium (Plants) • 1 point

Rock Form: Reaction Damage 7 (to being hit),

Limited to effect rank or Damage rank, whichever
is less; Enhanced Strength 2; Immunity 1 (Own
Powers); Impervious Protection 4 • 34 points

Plus add the fo

[... truncated ...]
```

**Chunk 22** (`72dc60c2e6cf`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

Affects Objects: Weaken with this modifier works on inani-
mate objects, although the effect can still only affect traits
the objects possess. This is most often applied to Weaken
Toughness  for  an  effect  that  can  weaken  both  creatures
and objects. +1 cost per rank, +0 for Affects Only Objects.

Broad: You can Weaken any of a broad set of traits, one at
a time suited to your effects descriptors. So you might be
able to Weaken Abilities, for example, or Weaken Mental
Effects. You choose which trait from the set is weakened
when you use the effect. +1 cost per rank.

Concentration: Once you have hit with a Concentration
Weaken, so long as you continue to take a standard action
each turn to maintain the effect, the target must make a
new resistance check against it, with no attack check re-
quired. +1 cost per rank.

Incurable: Weaken with this modifier cannot have its ef-
fects  countered  by  another  power  (such  as  Restorative
Healing) without the Persistent modifier; the target must
recover from the Weaken normally. Flat +1 point.

MODIFIERS

Precise: A Weaken effect capable of reducing more than one
trait at once can have this modifier, allowing you to choose
which traits are affected, while not affecting others. Note this
differs from the Selective extra (following). Flat +1 point.

Progressive:  A  Progressive  Weaken  effect  reduces  the
affected  traits  each  round  until  the  target  successfully
resists. Make a new resistance check for the target at the
end of each turn; failure weakens the affected trait(s) fur-
ther, while success stops the Progressive Weaken, but the
target must still recover ranks already lost (at the rate of 1
point per turn). +2 cost per rank.

Selective: This extra is applied to an Area Weaken so it only
affects some targets and not others. Combined with Precise
(previously), you can use an Area Weaken to selectively af-
fect only certain traits of certain targets. +1 cost per rank.

Simultaneous: If applied to a Broad Weaken, this extra al-
lows it to affect all of the traits in its set at the same time.
Each trait loses the difference between the resistance check
result and the DC in power points on a failed check. So a
Simultaneous Weaken Fire Effects subtracts points from ev-
ery fire effect the target possesses with a single attack. The
effect must be Broad to apply this modifier. +1 cost per rank.

Modifiers  enhance  or  limit  effects  in  v

[... truncated ...]
```

**Chunk 23** (`75f616f43b9d`):

```
CHAPTER 2: SECRET ORIGINS

97

6-10

11-15

Jinx: Selective Burst Area Luck Control
2 (negate hero or luck point, force
re-roll), Luck 5 • 15 points

Lucky Cat: Selective Burst Area Luck

Control 2 (grant re-roll, bestow luck
point), Luck 5 • 15 points

16-20

Nine Lives: Immortality 15, Limited:
only works eight times • 15 points

Thick Hide: Protection 4, Impervious 11 • 15 points

Roll 1d20 once and record the result.

ELEPHANT

Groundstrike (Alternate Effect of Strength Damage):

Burst Area Affliction 10 (Resisted by Dodge,
Overcome by Fortitude; Hindered and Vulnerable,
Stunned and Prone), Extra Condition, Limited to Two
Degrees, Limited to targets on the ground • 1 point

1-10

Immovable: Immunity 10 (being moved), Sustained

• 10 points

Power-Lifting: Enhanced Strength 4, Limited to

Lifting • 4 points

Trunk: Extra Limb 1, Elongation 1 • 2 points

Tusks: Strength-based Damage 2, Improved Critical 2

• 4 points

RHINO

Armored Plates: Immunity 4 (critical hits, self-

inflicted slam damage) • 4 points

11-20

Great Horn: Strength-based Damage 3, Improved

Critical 2 • 5 points

Unstoppable Charge: Penetrating 15 on Damage,

Limited to slam attacks; Speed 4 (30 MPH) • 12 points

Reptilian Movement: Movement 1 (Slithering) • 2 points

Heat Sensing Pits: Senses 1 (Infravision) • 1 points

Scaly Hide: Protection 2 • 2 points

Roll 1d20 once and record the result.

CROCODILE

Aquatic: Movement 1 (Environmental Adaptation—

Aquatic), Swimming 6 (30 MPH) • 8 points

1-6

Brute Strength: Enhanced Strength 2 • 4 points

Regrowth: Regeneration 2 • 2 points

Rending Bite: Strength-based Damage 2, Improved

Critical, Secondary Effect • 17 points

LIZARD

Paralyzing Spit: Affliction 10 (Resisted by Dodge,

Overcome by Fortitude; Dazed, Stunned,
Paralyzed), Accurate 2, Reach 3 • 15 points

Prehensile Tail: Elongation 1, Extra Limb 1 • 2 points

Regrowth: Regeneration 1, Persistent • 2 points

Speedy: Leaping 2 (30 feet); Movement 2 (Wall-

crawling 2); Speed 3 (16 MPH) • 9 points

Teeth and Claws: Strength-based Damage 2,

Accurate • 3 points

7-13

98

SNAKE

Tensile Strength: Elongation 4 (120 feet); Enhanced

14-20

Strength 4, Limited to Grabs • 8 points

Venomous Bite: Progressive Weaken Stamina 7
(Resisted by Fortitude), Accurate 2 • 23 points

DEFENSE

DODGE
+6

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

68

36

6

SKILLS

DEFENSES

TOTAL

20

20

150

•  Motivation—Acceptance: The Totem can be regard-
ed as a pariah or outcast in h

[... truncated ...]
```

**Chunk 24** (`765269f2e7c2`):

```
CHAPTER 6: POWERS

169

Subtle:  As  a  mental  sensory  effect,  Mind  Reading  has  a
degree  of  subtlety,  only  noticeable  to  the  subject  or  to
characters  with  an  appropriate  mental  sense,  such  as
Mental  Awareness  (see  the  Senses  effect).  Subtle  Mind
Reading is less detectable, requiring a DC 20 Perception
check  for  either  type  of  character  to  sense  it,  while  two
ranks  of  the  Subtle  modifier  makes  your  Mind  Reading
completely undetectable. Flat +1 or 2 points.

FLAWS

Close: Applied to Ranged Mind Reading, Close Mind Read-
ing requires a close attack check to touch an unwilling tar-
get and physical contact throughout the effect’s duration;
breaking contact ends the effect. –1 cost per rank.

Feedback: You suffer Feedback if a subject you are reading
is harmed, using your Mind Reading rank as the resistance
check  bonus  against  the  damage.  Additionally,  you  may
suffer Feedback at the GM’s discretion from reading or ex-
periencing  particularly  traumatic  or  emotionally-charged
thoughts of memories from the subject. –1 cost per rank.

Limited by Language: You can only understand the sub-
ject’s thoughts or memories if you share a common lan-
guage. –1 cost per rank.

Limited to Emotions: You can only read or probe for emo-
tions and emotional associations, not coherent thoughts
or memories. –1 cost per rank.

Limited to Sensory Link: If you have the Sensory Link extra
and this flaw, you can only tap into a subject’s senses, you
cannot read their thoughts or memories. –1 cost per rank.

Limited to Surface Thoughts: You can only read surface
thoughts and cannot achieve higher degrees of contact.
–1 cost per rank.

Ranged: Ranged Mind Reading requires a ranged attack
check in addition to the effect’s normal resistance check.
–1 cost per rank.

Sense-Dependent: Your Mind Reading is dependent on
a  sense  other  than  just  having  to  accurately  sense  the
target, such as needing to see his expressions (Sight-De-
pendent), hear him speak (Hearing-Dependent), smell his
changes in biochemistry (Scent-Dependent), and so forth.
Alternately, it may be dependent on first being in Mental
Communication with the target (see Communication). –1
cost per rank.

MORPH

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 5 points per rank

You can alter your appearance. Your traits do not change;
your new form is merely a cosmetic change. You gain a +20
bonus to Deception checks to disguise yourself as the fo

[... truncated ...]
```

**Chunk 25** (`80099a87d308`):

```
CHAPTER 7: GADGETS & GEAR

215

A  common  piece  of  equipment  for  crime  fighters  and
espionage agents is the utility belt (or bag, pouch, back-
pack, etc.): a collection of useful tools and equipment in
a compact carrying case. A utility belt is an array of Alter-
nate Equipment. Some characters may have a Removable
array of devices instead, allowing for far more unusual ef-
fects than run-of-the-mill equipment.

Note  that  equipment  with  a  cost  of  1  equipment  point
doesn’t  really  need  to  be  acquired  as  Alternate  Equip-
ment,  since  there’s  no  change  in  cost.  Still,  heroes  often
have 1-point items in their utility belts, like flashlights, re-
breathers, and so forth.

By spending hero points you can temporarily add Alter-
nate  Equipment  to  your  utility  belt,  for  those  one-time
items you may need in a pinch.

Feel  free  to  modify  this  example  (adding  or  omitting
items)  to  create  your  own  customized  utility  belts. The
tear gas, as the most expensive effect, has full cost. The
other items cost 1 point each for Alternate Equipment,
making the total equipment point cost of the utility belt
25  equipment  points,  or  5  power  points  (for  5  ranks  of
the Equipment advantage).

WEAPONS

•

Tear Gas Pellets: Ranged Cloud
Area Affliction 4 (Resisted by
Fortitude; Dazed and Vision
Impaired, Stunned and Vision
Disabled, Incapacitated) • 16 points.

•  Bolos: Ranged Cumulative

Affliction 3 (Resisted by Dodge, Overcome by
Damage; Hindered and   Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree  • 1 point.

•  Boomerangs: Ranged Damage 1, Strength-based

• 1 point.

•

Explosives: Ranged Burst Area Damage 5 • 1 point.

•  Cutting Torch: Damage 1 Linked to Weaken

Toughness 1 • 1 point.

•

Flash-Bangs: Ranged Burst Area Cumulative
Affliction 4 (Resisted and Overcome by Will; Visually
Impaired, Visually Disabled, Visually Unaware),
Limited to Vision  • 1 point.

•  Pepper Spray: see page 217 • 1 point.

•  Power Knuckles: Damage 4, Strength-based • 1 point.

•

•

Sleep Gas Pellets: Ranged Cloud Area Affliction 3
(Resisted and Overcome by Fortitude; Fatigued,
Exhausted, Asleep) • 1 point.

Smoke Pellets: Ranged Cloud Area Visual
Concealment Attack • 1 point.

Weapons of various sorts are common for both heroes and villains. They range from melee weapons to ranged weapons
like guns and bows and devices like shrink-rays, mind-control helmets and more. Characters who don’t have any offen-
sive pow

[... truncated ...]
```

**Chunk 26** (`81d16734de2e`):

```
CHAPTER 7: GADGETS & GEAR

217

Ranged  weapons  include  both  thrown  and  projectile
weapons.  Thrown  weapons  are  Strength-based,  adding
the wielder’s Strength rank to their Damage rank. Projec-
tile weapons include bows, crossbows, and guns as well
as energy weapons like lasers and blasters. Their Damage
is generally not Strength-based.

Like melee weapons, ranged weapons have category, ef-
fect,  critical,  and  cost  traits.  Ranged  weapon  categories
are  Projectile  Weapons,  Energy  Weapons,  Heavy  Weap-
ons, and Thrown Weapons.

Holdout  pistol:  A  low-caliber,  easily  concealed  pistol,
typically used as a back-up or secondary weapon.

Light pistol: A common handgun, found in the hands of
police officers and criminals alike.

Heavy  pistol:  A  high-caliber  handgun,  usually  used  by
those who want a lot of stopping power.

Machine pistol: A small automatic weapon, usable in one
hand.

Submachine gun: Compact automatic weapons that fire
pistol  ammunition,  submachine  guns  are  common  mili-
tary weapons, also used by criminals with access to more
serious firepower.

Shotgun: A shotgun can fire shot, which does Damage 5
with Accurate 1 due to the spread, but Limited to Dam-
age 3 against targets with Protection. It can also load solid
slugs, which inflict the same damage, but without the Ac-
curate bonus or the Limit on Damage.

Assault rifle: Rifles designed for military-use capable of
both single-fire and automatic fire.

Sniper rifle: Rifles designed for long-range use, typically
in conjunction with a powerful scope or targeting system.

Bow: Although outdated, some heroes and villains favor the
bow as a weapon and it can be quite effective in the right
hands. A bow-wielding character may have various “trick” ar-
rows with different powers, typically handled as devices.

Crossbow: Similar to a bow, and used for the same reasons.

Blaster pistol: A pistol that fires a coherent bolt of energy.

Blaster rifle: A larger rifle-sized weapon that fires a more
powerful bolt of energy.

Taser: A compressed-air weapon firing a pair of darts. On
impact  they  release  a  powerful  electrical  charge,  for  an
Affliction effect that can daze, stun, or incapacitate (For-
titude resistance, DC 15).

Flamethrower: A flamethrower shoots a stream or arc of
fire Damage as Cone or Line Area and can switch between
settings as an Alternate Effect.

Grenade  launcher:  A  grenade  launcher  fires  various
types of grenades out a greater distance, gener

[... truncated ...]
```

**Chunk 27** (`82504504b374`):

```
CHAPTER 6: POWERS

199

be “recovered” in some fashion, such as recharging, rest,
repair, reloading, and so forth. The GM decides when and
how a faded effect recovers, but it should generally occur
outside of combat and take at least an hour’s time. The GM
may  allow  a  hero  to  recover  a  faded  effect  immediately
and completely by spending a hero point.

usable only in certain situations and those usable only on
certain  things.  For  example  Only  While  Singing  Loudly,
Only While Flying, Only on Men (or Women), Only Against
Fire, Not Usable on Yellow Things, and so forth. As a gen-
eral rule, the effect must lose about half its usefulness to
qualify  for  this  modifier.  Anything  less  limiting  is  better
handled as an occasional complication.

FEEDBACK

-1 COST PER RANK

You suffer damage when a manifestation of your effect is
damaged. This  flaw  only  applies  to  effects  with  physical
(or  apparently  physical)  manifestations,  such  as  Create,
Illusion,  or  Summon,  for  example.  If  your  power’s  mani-
festation  is  damaged,  make  a  resistance  check  against
the attack’s damage rank, using your effect’s rank as the
resistance check bonus. For example, if a manifestation of
a rank 10 effect is attacked for damage 12, you must make
a resistance check against damage 12 with a +10 bonus
(the effect’s rank) in place of your normal Toughness.

GRAB-BASED

-1 COST PER RANK

An attack effect with this flaw requires you to successfully
grab a target before using the effect (see Grab, page 248).
This generally applies to an effect that is close range, since
you have to be in close combat to grab anyway. If the ef-
fect’s default range is not close, apply the Close modifier
as well. If you do not succeed on the grab, you cannot use
the effect. If your grab attempt succeeds, the effect occurs
automatically as a reaction.

Example: Lamprey has a draining touch that is a
Grab-Based  Weaken  Strength  effect.  So  the  mon-
strous  villain  has  to  take  a  standard  action  and
make a grab first in order to use it. If his close attack
check hits, the target makes a Dodge or Fortitude
resistance  check  against  Lamprey’s  Strength.  If  it
fails, the target then makes the Fortitude resistance
check against the villain’s Weaken effect to see how
much Strength Lamprey drains away.

This  flaw  is  essentially  a  form  of  Resistible,  with  a  grab
check rather than a regular resistance check (see the Re-
sistible flaw for more).

FLAT • -1

[... truncated ...]
```

**Chunk 28** (`8558df91a0a1`):

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

**Chunk 29** (`85cc7f979174`):

```
CHAPTER 2: SECRET ORIGINS

65

Water Control: Array (20 points + four Alternate

Effects)

•  Water Blast: Ranged Damage 10 • 20 points

Take the Water Control array and Water Blast
(above) and roll 1d20 four times (re-roll if you get the
same result) and add them to the array as Alternate
Effects.

1-4

•  Dehydrate: Cumulative Affliction
10 (Resisted by and Overcome by
Fortitude; Fatigued, Exhausted,
Incapacitated) • 1 point

1-10

5-8

9-12

13-16

17-20

•  Drown: Progressive Affliction
6 (Resisted and Overcome by
Fortitude; Dazed, Stunned,
Incapacitated) • 1 point

•  Hard Water Objects: Create 10

• 1 point

•  Move Water: Perception Ranged
Move Object 10, Limited to Water
• 1 point

•  Watery Snare: Ranged Affliction 10
(Resisted by Dodge, Overcome by
Strength; Hindered and Vulnerable,
Immobile and Defenseless), Extra
Condition, Limited to Two Degrees
• 1 point

11-15

Ice Form: Enhanced Strength 8; Immunity 7 (cold
damage, ice effects); Impervious Protection 8;
Senses 2 (Tracking, Infravision) • 45 points

Ice Slide: Flight 5 (60 MPH), Platform • 5 points

Ice Control: Array (20 points + four Alternate Effects)

•  Ice Blast: Ranged Damage 10 • 20 points

Take the Ice Control array and Ice Blast (above) and
roll 1d20 four times (re-roll if you get the same result)
and add them to the array as Alternate Effects.

1-4

5-8

9-12

13-16

•  Cold Blast: Ranged Affliction 10
(Resisted by and Overcome by
Fortitude; Fatigued, Exhausted,
Incapacitated) • 1 point

•  Cold Field: Environment 10 (Extreme

Cold) • 1 point

•  Ice Shapes: Create 6, Continuous,

Innate • 1 point

•  Icy Snare: Cumulative Affliction 10
(Resisted by Dodge, Overcome by
Damage; Hindered and Vulnerable,
Immobile and Defenseless), Extra
Condition, Limited to Two Degrees
• 1 point

17-20

•  Icy Surfaces: Environment 10
(Impede Movement) • 1 point

ABILITIES

POWERS

28

86

3

SKILLS

DEFENSES

TOTAL

14

19

150

•  Motivation—Acceptance: A transformed elemental
may lament his lost humanity and be isolated as a re-
sult of his new, inhuman form.

•

•

Accident:  Many  Elementals  have  difficulty  interact-
ing with others due to their nature. Fire Elementals, in
particular, are apt to inadvertently cause destruction
in their wake, but even Water Elementals may cause
property damage by just their presence.

Enemy: Elementals may have a rivalry or feel enmity
towards their diametric opposite (fire to water, earth
to air) and towards beings associated with their op-
posing element.

•

[... truncated ...]
```

**Chunk 30** (`872291c50bc3`):

```
CHAPTER 6: POWERS

205

things  like  air  (or  other  gases),  water  (or
other  liquids),  and  earth  (soil,  rock,  sand,
etc.)  through  to  biological  materials  like
acids, blood, and so forth. Energy mediums
are different forms of energy, from electro-
magnetic (electricity, light, radio, radiation,
etc.) to gravity, kinetic energy, or an exotic
source like divine, magical, psionic, or cos-
mic  energy  (given  under  Origin  descrip-
tors).
RESULT

Lastly,  a  power’s  result  is  what  happens
when  the  power  is  used  beyond  just
the game mechanics of its effect. For
example, the rules of the Affliction ef-
fect  describe  the  penalties  suffered  by  the
target,  but  they  don’t  describe  the  result,
the nature of the Affliction itself. Is it glow-
ing  bonds  of  energy,  sudden  fever  and
dizziness,  a  curse  of  misfortune,  a  life-
sapping  vapor,  or  any  number  of  other
things?

Result descriptors tend to be fairly broad,
given  the  potential  range  of  results  avail-
able to effects in the game. Some powers
may  not  have  or  need  result  descriptors;
after  all, “Mind  Control”  is  a  pretty  clear
description  of  a  result.  However, “an  in-
duced  trance  where  the  human  brain
becomes  capable  of  accepting  neurolin-
guistic programming inputs” is also a valid
descriptor for that same effect.

Like medium descriptors, result descriptors
may or may not match others the power al-
ready has. Take a taser-like weapon able to
stun the nervous system of its target:
it has an invented origin (someone
designed  and  built  it),  a  techno-
logical source (it’s a technological
device with a battery), uses
a  energy  medium  (an
electrical  shock),  and
results  in  an  electrical
overload  of  the  tar-
get’s  nervous  system
(the  result  descriptor
for its Affliction effect).
This  tells  us  a  lot  about
that  particular  power  and
ways  it  might  interact  with  other
effects.

Applying descriptors to a power is as simple as describing
what the power is and how it works: “The divinely-granted
ability to heal through a laying-on of hands,” for example,
“or the mutant power to control magnetic fields to move

ferrous metal objects.” Considerably more evocative and
descriptive than “Healing effect” or “Move Object, Limited
to Ferrous Metals,” aren’t they?

Generally, you should feel free to apply whatever descrip-
tors seem appropriate and necessary to describe your char-
acter’s powers, so long as they don’t sig

[... truncated ...]
```

**Chunk 31** (`8757660124bd`):

```
CHAPTER 2: SECRET ORIGINS

83

4-5

6-12

13-14

15-16

17-19

11-15

Induce Blindness: Perception Range

Cumulative Affliction 8 (Resisted and
Overcome by Will; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to one sense • 24 points

Mental Blast: Perception Range Damage

1-5

6, Resisted by Will • 24 points

Mental Illusions: Illusion 6 (All Senses),
Feedback, Resistible by Will, Selective
• 24 points

Mental Paralysis: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Stunned,
Paralyzed) • 24 points

Mind Control: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Compelled,
Controlled) • 24 points

20

Weaken Resolve: Perception Range

Weaken Will 8 • 24 points

Telekinetic: Take Telekinesis, listed immediately

below, then roll on the Telekinetic Table.

Telekinesis: Move Object 10, Accurate 4 • 24 points

Telekinetic Table: Roll 1d20 once and record the result
as the first power in an array, then roll 1d20 three times
and add each result as a 1-point Alternate Effect (re-roll
if you get the same result as your first roll).

1-3

4-7

8-12

Telekinetic Column: Line Area 2 (60

feet) Damage 8 • 24 points

Telekinetic Constructs: Create 8,

Movable • 24 points

Telekinetic Bolt: Ranged Damage 10,

Accurate 4 • 24 points

16-20

13-14

Telekinetic Grab: Ranged Concentration

Affliction 10 (Resisted by Dodge,
Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile),
Accurate 4, Extra Condition, Instant
Recovery, Limited Degree • 24 points

Roll 1d20 once and record the result.

Armored Costume and Combat Training: Protection 4,
Subtle, Removable (-1 point); Enhanced Advantages 8
(Defensive Attack, Defensive Roll 2, Evasion, Improved
Defense, Improved Initiative, Instant Up, Takedown);
Enhanced Defenses 8 (Dodge 4, Parry 4) • 20 points

Precognitive Reactions: Enhanced Advantages 8
(Defensive Roll 4, Evasion 2, Improved Defense,
Improved Initiative); Enhanced Defenses 12 (Dodge
6, Parry 6) • 20 points

Psychokinetic Shield: Protection 10, Impervious 5,

Sustained, Linked to Immunity 10 (Mental effects),
Limited to Half Effect • 20 points

Telekinetic Shield: Impervious Protection 10,

Sustained • 20 points

6-10

11-15

16-20

Roll 1d20 once and record the result.

1-2

Levitation: Flight 2 (8 MPH), Subtle • 5 points

3-6

7-8

Mental Awareness: Senses (Mental Awareness,

Acute, Detect, Radius, Range) • 5 points

Telekinetic Flight: Flight 5 (60 MPH), Distracting •

[... truncated ...]
```

**Chunk 32** (`9575430bef02`):

```
CHAPTER 2: SECRET ORIGINS

43

Power Point Totals:  Abilities 36 + Powers 84  + Advantages 1 + Skills  17 + Defenses 12  = 150

PL10PL10

STRENGTH
12
STAMINA
14

POWERS

AGILITY
1
DEXTERITY
1

FIGHTING
6
INTELLECT
0

AWARENESS
1
PRESENCE
1

Shockwave: Burst Area Damage 10, Limited: Both the

Powerhouse and its targets must be in contact with the ground
• 10 points

•  Groundstrike: Burst Area Affliction 10 (Resisted by Fortitude;
Vulnerable, Defenseless), Instant Recovery, Limited Degree,
Limited: Both the Powerhouse and its targets must be in
contact with the ground • 1 point

Leaping: Leaping 10 • 10 points

Super-Stamina: Enhanced Stamina 10, Immunity 12

(Cold and Heat Damage, Fatigue, Pressure), Impervious
Toughness 12 • 44 points

Super-Strength: Enhanced
Strength 8, plus Enhanced
Strength 4, Limited to
Lifting (Lifting Str16;
1,600 tons) • 20 points

All-out Attack, Power Attack,
 Ultimate Effort (Toughness
checks)

SKILLS

Close  Combat:  Unarmed  2  (+8),  Expertise:  Choose  One  6  (+6),
Insight  5  (+6),  Intimidation  7  (+8),  Perception  5  (+6),  Ranged
Combat: Throwing 7 (+8)

OFFENSE

INITIATIVE +1

Throw +8

Unarmed +8

Ranged, Damage 12

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

14

14

6

6

6

Power Point Totals:  Abilities 36 + Powers 85  + Advantages 3 + Skills  16 + Defenses 10  = 150

44

```

**Chunk 33** (`997bf2eca013`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PLAYER

Interpose

TOUGH

Ultimate Effort (Toughness checks)

QUICK

Improved Initiative

SKILLS

Close Combat: Unarmed 2

Take  the  skill  listed  above,  then  roll  1d20  twice  (re-roll  if
you get the same result twice) and record the results.

1-4

5-8

Athlete: You’re a trained athlete.

Ex-Military: You used to be in the armed forces.

9-12

Charmer: You have a way with people.

13-16

Rough Upbringing: You were raised on the streets
or have had a hard life.

17-20

Sharp Mind: You’re difficult to fool.

ATHLETE

Athletics 4, Perception 4, Ranged Combat: Throwing 4

Roll  1d20  once  and  record  the  result  as  the  first  power
in  an  array,  then  roll  1d20  once  and  add  the  result  as  a
1-point Alternate Effect (re-roll if you get the same result
as your first roll).

1-3

4-6

7-9

Energy Blast: Ranged Damage 10, Accurate 5,

Distracting, Tiring • 10 points

Foot Stomp: Line Area Damage 10, Powerhouse and
target must be in contact with the same surface
• 10 points

Groundstrike: Burst Area Affliction 10 (Resisted

and Overcome by Fortitude; Dazed and Hindered,
Stunned and Prone, Incapacitated), Extra
Condition, Instant Recovery, Powerhouse and
target must be in contact with the same surface
• 10 points

10-12

13-14

Shockwave: Burst Area Damage 10, Powerhouse
and targets must be in contact with the same
surface • 10 points

Super-Breath: Close Range Cone Area Move Object
5, Limited to moving toward and away, Linked
to Cone Area Damage 5, Unreliable (only the
Damage is Unreliable) • 10 points

15-17

Cut Loose!: Penetrating 10 on Strength • 10 points

18-20

Thunderclap: Cone Area Affliction 10 (Resisted and
Overcome by Fortitude; Dazed, Stunned), Limited
Degree • 10 points

EX-MILITARY

Expertise: Military 4, Perception 4, Ranged Combat: Throwing 4

CHARMER

Deception 4, Insight 4, Persuasion 4

UPBRINGING

Only if you rolled Solid Form or Super-Strength on the
Offensive  Powers  table,  take  Super-Stamina,  directly
below, then roll on the table below, as directed. Do not
take Super-Stamina if you rolled Density or Growth on
the  Offensive  Powers  table,  instead,  roll  on  the  table
below.

Expertise: Streetwise 4, Intimidation 6, Perception 2

Super-Stamina: Enhanced Stamina 10 • 20 points

MIND

Expertise: (Choose One) 4, Insight 4, Perception 4

POWERS

Roll 1d20 once and record the result.

Roll  1d20  four  times  (re-roll  if  you  get  the  s

[... truncated ...]
```

**Chunk 34** (`9b4ab26032fa`):

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

**Chunk 35** (`9c685bbd4830`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

NAME

COST

Activation

–1-2 flat points

Effect requires a move (1 point) or standard (2 points) action to activate.

Check Required

–1 flat per rank

Must succeed on a check to use effect.

Concentration

–1 per rank

Sustained effect becomes concentration duration.

Diminished Range

–1 flat per rank

Reduces short, medium, and long ranges for the effect.

Distracting

Fades

Feedback

Grab-Based

–1 per rank

–1 per rank

–1 per rank

–1 per rank

Increased Action

–1-3 per rank

Limited

Noticeable

Permanent

Quirk

–1 per rank

–1 flat point

–1 per rank

Vulnerable while using effect.

Effect loses 1 rank each time it is used.

Suffer damage when your effect’s manifestation is damaged.

Effect requires a successful grab attack to use.

Increases action required to use effect.

Effect loses about half its effectiveness.

Continuous or permanent effect is noticeable.

Effect cannot be turned off or improved with extra effort.

–1 flat per rank

A minor flaw attached to an effect. The opposite of a Feature.

Reduced Range

–1-2 per rank

Effect’s range decreases.

Removable

Resistible

Sense-Dependent

Side Effect

Tiring

Uncontrolled

Unreliable

–1-2/5 flat points

Effect can be taken away from the user.

–1 per rank

–1 per rank

–1-2 per rank

–1 per rank

–1 per rank

–1 per rank

Effect gains a resistance check.

Target must be able to perceive the effect for it to work.

Failing to use the effect causes a problematic side effect.

Effect causes a level of fatigue when used.

You have no control over the effect.

Effect only works about half the time (roll of 11 or more).

Example: A spellcaster has Senses 4 (Detect Magic,
Ranged,  Acute,  Analyze)  with  Expertise:  Magic
Check Required 4. The player needs to make a DC
13 skill check (10 + 3 additional ranks) to success-
fully cast the spell, followed by the normal Percep-
tion check to pick up on anything present, and per-
haps another Expertise check to interpret what the
character senses.

Skill checks an effect may require include:

Acrobatics: Suitable for effects requiring a measure
of coordination or complex maneuvering.

Deception:  Good  for  effects  intended  to  deceive,
particularly sensory effects like Concealment or Illu-
sion, and disguise or form-altering effects like Morph.

Expertise:  An  Expertise  skill  check  might  represent
having  to  know  something  about  the  subject  of  the
effect or having to kno

[... truncated ...]
```

**Chunk 36** (`9c7fcc5049c4`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

round, which limits its usefulness in responding to the ac-
tions of others. –1 cost per rank.

Ranged: Luck Control normally requires no attack check;
if Ranged, it does. –1 cost per rank.

Resistible: Targets  of  your  Luck  Control  get  a  resistance
check—usually Dodge or Will—to avoid its effects. –1 cost
per rank.

Side Effect: As a particular side effect of Luck Control, if
your  effort  to  alter  luck  fails,  you  suffer  a  setback  with-
out earning a hero point. Effectively the GM gains a “free”
complication against you. –1 or –2 cost per rank.

SENSORY

Effect:  Perception  Ranged,  Cumulative  Affliction,  Re-
sisted by Will • 4 points per rank

You  can  impose  your  will  on  others,  forcing  them  to
obey  your  commands. Targets  failing  a Will  resistance
check against your effect DC first become dazed, then
compelled, as they try to fight off your influence. Finally,
with  three  or  more  degrees  of  effect,  the  target  be-
comes controlled and obeys any commands you give.

Degrees  of  failure  on  resistance  checks  against  Mind
Control are cumulative. You can also apply the Progres-
sive modifier (see the Affliction effect) so your mental
hold  increases  each  time  the  target  fails  a  resistance
check against it!

Action: Standard • Range: Perception
Duration: Sustained • Cost: 2 point per rank

MIMIC

You can read another character’s mind. To use Mind Read-
ing,  make  an  opposed  effect  check  against  the  result  of
the target’s Will check. The degree of success determines
the degree of contact:

1

2

3

4

Surface  thoughts: You  can  read  what  the
target  is  presently  thinking.  Mind  Reading
transcends language; you comprehend the
target’s thoughts whether or not you share
a common language.

Personal thoughts: You can probe deeper
into  the  target’s  mind  for  information. You
can  essentially  ask  any  one  question  and
receive  the  answer  from  the  target’s  mind.
If the target doesn’t know the answer, then
you know that as well.

Memory: You can read the subject’s memo-
ries  and  recollections.  This  allows  you  to
perceive  them  exactly  as  the  target  recalls
them, one memory per round.

Subconscious:  You  can  read  memories
from the target’s subconscious, things even
the  target  does  not  consciously  know. This
might mean repressed or hidden memories,
deep-seated psychological traumas, or even
other personalities.

If  you 

[... truncated ...]
```

**Chunk 37** (`aa943c38ef67`):

```
CHAPTER 2: SECRET ORIGINS

89

d20 once on that table to determine if your base form and
duplicates are Energy Controllers, Martial Artists, or Pow-
erhouses. Your base form has the same abilities, powers,
advantages, skills, defenses, and totals as the summoned
characters, but with the addition of the Summon Twin or
Summon Triplets power.

Summon Twin: Summon 8 (One PL8, 120 point
duplicate), Heroic, Mental Link • 33 points

PL 8

STR
STA

1  AGL
2  DEX

2
4

FGT
INT

1  AWE
PRE
0

2
2

Powers: Energy Control (Array (16 points),
Energy Blast (Ranged Damage 8), AE: Energy
Explosion (Ranged Burst Area Damage
5), AE: Energy Bolts (Ranged Multiattack
Damage 5), AE: Dazzle (Cumulative Ranged
Affliction 8 (Resisted by Dodge and Overcome
by Fortitude; Impaired, Disabled, Unaware),
Limited to Vision); Energy Field (Sustained
Protection 6 Linked to Reaction Damage 2,
Precise); Energy Flight (Flight 6 (120 MPH));
Energy Immunity (Immunity 1 (Immune
to own powers)); Transform (Quick Change
(Feature 1, change into costume as a free
action))

Advantages: Accurate Attack, Power Attack,
Set-up, Teamwork

Skills: Acrobatics 4 (+8), Athletics 4 (+5),
Expertise (Choose One) 4 (+4), Perception 4
(+6), Ranged Combat: Energy Control 4 (+8)

Offense: Init +4, Energy Blast +8 (Ranged,
Damage 8 or other effects), Unarmed +1
(Close, Damage 1)

Defense: Dodge 8, Parry 8, Fort 8, Tou 8,
Will 8

1-6

1-10

Totals: Abilities 32 + Powers 50 + Advantages 2
+ Skills 10 + Defenses 23 = 117

1-6

Note: Roll on the Energy Controller
archetype’s Energy Descriptors table to
determine the type of energy you control.

PL 8

11-20

7-13

STR
STA

1  AGL
4  DEX

5
5

FGT
INT

10  AWE
PRE

1

2
0

Equipment: Smartphone, Flashlight,
Motorcycle, Restraints, Swingline (Movement
1 (Swinging)), Tonfa (Strength-based Damage
2, Reach 1), AE: Throwing Disks (Ranged,
Strength-based Damage 1)

Advantages: Chokehold, Daze (Deception),
Defensive Roll 2, Equipment 4, Evasion,
Improved Initiative, Instant Up, Power Attack,
Quick Draw, Set-up, Teamwork

Skills: Acrobatics 7 (+12), Athletics 6 (+10),
Deception 8 (+8), Expertise (Choose One)
7 (+8), Perception 6 (+8), Ranged Combat
(Throwing Disks) 5 (+10), Stealth 7 (+12),
Vehicles 4 (+9)

Offense: Init +9, Throwing Disks +10 (Ranged,
Damage 5), Tonfa +10 (Close, Damage 6),
Unarmed +10 (Close, Damage 4)

Defense: Dodge 10, Parry 10, Fort 8, Tou 6/4,
Will 8

Totals: Abilities 62 + Powers 0 + Advantages 15
+ Skills 25 + Defenses 15 = 117

14-20

PL 8

STR
STA

9  

[... truncated ...]
```

**Chunk 38** (`ac75d3f2b9e6`):

```
CHAPTER 2: SECRET ORIGINS

95

MYSTIC

MUTATION

Assessment, Ritualist, Trance

Expertise: (Choose one) 8, Investigation 6, Technology 6

PLAYFUL

Daze (Deception), Redirect, Taunt

SNEAKY

Evasion, Hide in Plain Sight, Improved Initiative

Roll 1d20 once and record the result.

1-5

Dominating: You are afforded respect by other
creatures.

6-10

Predator: You are on the top of the food chain.

11-15

Trickster: You are a cunning prankster.

16-20 Wise: You are astute and perceptive.

DOMINATING

1-5

Altruistic: You value the group over the individual.

Athletics 4, Intimidation 12, Perception 4

6-10

11-15

16-20

Cooperative: You are accustomed to a codependent
community.

Egoistic: You look out for yourself and your own
survival.

Vengeful: You go out of your way to spite others,
even at cost to yourself.

ALTRUISTIC

Inspire, Interpose, Leadership

COOPERATIVE

Animal Empathy, Set-up, Teamwork

EGOISTIC

Favored Environment (Choose One), Great Endurance,
Uncanny Dodge

VENGEFUL

Daze (Intimidation), Favored Foe (Choose One), Startle

SKILLS

Roll on the Origin Skills table and Disposition Skills tables.

Roll 1d20 once and record the result.

1-6

7-12

13-20

Awakened: You are an unusual member of your
species with a human intellect and perhaps even a
human form.

Invocation: You were granted your powers by
calling upon the animal spirits.

Mutation: You came upon your powers through a
freak accident.

AWAKENED

Athletics 6, Perception 6, Stealth 8

INVOCATION

Insight 8, Perception 6, Treatment 6

96

PREDATOR

Acrobatics 4, Athletics 4, Perception 6, Stealth 6

TRICKSTER

Acrobatics 6, Deception 6, Sleight of Hand 4, Stealth 4

WISE

Insight 8, Perception 8, Treatment 4

POWERS

Find the entry below for the type of Totem that matches
what you rolled for your Abilities.

Roll 1d20 once and record the result.

SCORPION

1-5

Climbing: Movement 2 (Wall-crawling 2) • 4 points

Sting: Progressive Weaken Stamina 10, Accurate 2

• 32 points

SPIDER

Spider-Movement: Leaping 2 (30 feet); Movement

3 (Swinging, Wall-crawling 2) • 8 points

Spider Senses: Senses 4 (Danger Sense, Darkvision,

Ranged Touch) • 4 points

6-10

Web Snare: Ranged Cumulative Affliction 6

(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobilized), Accurate 5, Extra Condition,
Limited to Two Degrees • 23 points

•  Web Tether: Move Object 7, Accurate 5 • 1 point

SWARM

Blinding Barrage: Burst Area Visual (All)

Concealment Attack 4 • 12 points

1

[... truncated ...]
```

**Chunk 39** (`b511fe78f53a`):

```
CHAPTER 2: SECRET ORIGINS

63

OVERSEER

Contacts, Leadership

UNOBTRUSIVE

Favored Environment (Choose One), Choose One: Evasion or
Improved Initiative

SKILLS

Ranged Combat: (Element) Control 6

Choose One: Acrobatics 4, or Athletics 4, or Close Combat:
Unarmed 4

Choose One: Deception 6 or Intimidation 6

Roll 1d20 once and record the result.

1-5

6-20

Android Host: Enhanced Strength 6, Reduced

Stamina 7 (Stamina —); Enhanced Defenses 8
(Dodge 4, Parry 4); Immunity 20 (upgrades Life
Support to all Fortitude effects); Protection 8
• 34 points

Gaseous Form: Visual Concealment 4, Partial;
Enhanced Advantages 2 (Defensive Roll 2);
Enhanced Defenses 18 (Dodge 9, Parry 9);
Insubstantial 2, Permanent • 34 points

Take the skills listed above, then roll 1d20 once and record
the result. If you rolled Embodiment for Abilities, take Na-
tive instead of rolling on this table.

Flight: Flight 7 (250 MPH) • 14 points

1-5

6-10

Native: You are well versed in or have researched
the properties of your element.

Pilot/Driver: You are proficient in the care and use
of planes or cars.

11-15

Scientist: You are knowledgeable in the sciences.

16-20

Soldier: You are a former military man.

Air Control: Array (24 points plus 2 Alternate Effects)

•  Air Blast: Ranged Damage 12 • 24 points

Take the Air Control Array and Air Blast (above) and roll
1d20  twice  (re-roll  if  you  get  the  same  result  twice)  and
add them to the Air Control array as Alternate Effects.

NATIVE

Expertise: Elements 8, Perception 4

PILOT/DRIVER

Expertise: Repair 4, Vehicles 8

SCIENTIST

Expertise: Science 8, Technology 4

SOLDIER

Athletics 4, Expertise: Military 8

POWERS

1-3

4-6

•  Fog: Environment 12 (Visibility -5; 8 mile radius)

• 1 point

•  Suffocation: Progressive Ranged Affliction 6
(Resisted and Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

7-10

•  Tornado: Cylinder Area Move Object 8,

Concentration Duration, Damaging • 1 point

11-13

•  Wind Binding: Ranged Affliction 12 (Resisted

by Dodge, Overcome by Strength; Hindered and
Vulnerable, Immobile and Defenseless), Extra
Condition, Limited Degree • 1 point

14-17

•  Wind Control: Move Object 12 • 1 point

18-20

•  Wind Screen: Deflect 12, Cylinder Area (×2),
Limited to Attacks Targeting Dodge • 1 point

Elemental Constitution: Immunity 12 (Critical Hits, Life

Support) • 12 points

Earthen Body: Enhanced Strength 8; Impervious Protection

8 • 32 points

Reconstitution: Regeneration 10, Source (El

[... truncated ...]
```

**Chunk 40** (`b60c97b07a3c`):

```
CHAPTER 6: POWERS

179

Effect: Variable (assumed forms), Move Action • 8 points
per rank

You  can  transform  into  different  forms,  gaining  the
physical  traits  (abilities,  skills,  advantages,  and  pow-
ers) of the assumed form. You gain (Shapeshift rank x 5)
power points worth of traits. You can also redistribute
points spent on your own physical traits (lowering your
Strength to apply those points elsewhere, for example).
You are limited to the inherent traits of the forms you
assume and do not gain new mental traits, even if that
form possesses them.

Shapeshift is often further Limited by the specific types
of forms the character can assume, such as Limited to
Animals or Limited to Machines.

ter’s perceptions are unreliable, the sense appears to work,
but the character gets the wrong information. For this rea-
son, the GM should make all reliability checks for Senses
in secret, just informing the player of what the character
does (or does not) notice. –1 cost per rank.

SHRINKING

GENERAL

Action: Free • Range: Personal
Duration: Sustained • Cost: 2 points per rank

You can temporarily decrease your size, becoming smaller,
harder to see — and hit — at the cost of losing Strength
and  speed.  Every  4  ranks  of  Shrinking  reduces  your  size
rank by 1 (normal humans are size rank –2 by default) and
each reduction in size rank subtracts 1 from your Strength
and every two reductions in size rank subtract 1 from your
ground speed rank. Add half your Shrinking rank (rounded
down)  to  your  active  defenses.  Add  your  Shrinking  rank
as a bonus to Stealth checks, since you are harder to spot,
but apply half your rank (rounded down) as a penalty to In-
timidation checks (hard to be imposing when you’re tiny).
Shrinking modifiers are restricted by power level limits.

So  at  Shrinking  12,  you  are  size  rank  –5  (about  6  inches
tall),  and  have  a  +6  bonus  to  active  defenses  and  +12
Stealth bonus, but –3 Strength, –1 speed, and –6 Intimida-
tion penalties.
EXTRAS

Atomic: At Shrinking 20 (and size rank –7), you can shrink
down to the molecular or even atomic level, allowing you
to pass through solid objects by slipping between their at-
oms. It takes at least a full turn to do so, possibly longer for
larger objects. You’re effectively immune to damage and
many effects at this scale, since you are essentially shifted
out of the ordinary universe. The GM decides if a particular
effect can reach you at the atomic level. If you have 

[... truncated ...]
```

**Chunk 41** (`b95c26d52ee0`):

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

**Chunk 42** (`ba29424008f5`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

Limited: You must specify a reasonably common effect
(or set of uncommon effects) that keeps you from recov-
ering from death, such as beheading, cremation, a stake
through the heart, and so forth. Even then, if the effect is
somehow removed or reversed (e.g. the stake is removed
from your corpse) you may still be able to come back. -1
cost per rank.

IMMUNITY

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You are immune to certain effects, automatically succeeding
on  any  resistance  check  against  them. You  assign  ranks  of
Immunity to various effects to gain immunity to them (with
more extensive effects requiring more ranks). These assign-
ments are permanent. Examples include the following:

•

•

•

•

•

•

1  rank:  aging,  disease,  poison,  one  environmental
condition  (cold,  heat,  high  pressure,  radiation,  or
vacuum), one type of suffocation (breathe normally
underwater or in an alien atmosphere, for example),
starvation and thirst, need for sleep, or a rare power
descriptor (such as your own powers, a close sibling’s
powers, etc.).

2 ranks: critical hits, suffocation effects (no need to
breathe  at  all),  or  an  uncommon  power  descriptor
(such as chemical, gravitic, necromantic, etc.).

5 ranks: alteration effects, sensory Affliction effects,
emotion  effects,  entrapment  (grabbing,  snares,  or
bonds), fatigue effects, interaction skills, or a particu-
lar  Damage  effect,  descriptor  (such  as  bullets,  cold,
electricity, falling, fire, magic, radiation, sonic, etc.)

10 ranks: a common power descriptor (such as all ef-
fects with cold, electricity, fire, radiation, or weather
descriptors,  for  example),  life  support  (includes  im-
munity  to  disease,  poison,  all  environmental  condi-
tions, suffocation, and starvation and thirst).

20  ranks:  a  very  common  power  descriptor  (blud-
geoning or energy, for example).

30 ranks: All effects resisted by Fortitude, All effects
resisted by Will.

•

80  ranks:  All  effects  resisted  by  Toughness  (the
equivalent of 40 ranks of Impervious Toughness).

Some Immunity effects are a matter of degree. For exam-
ple, “immunity to cold” can range from the environmen-
tal effects of cold (described under The Environment) to
cold damage, to complete immunity to all effects with the
“cold”  descriptor. The  first  requires  only  1  rank,  and  pro-
vides no resistance to othe

[... truncated ...]
```

**Chunk 43** (`bc6e8d2fe577`):

```
CHAPTER 2: SECRET ORIGINS

93

Supernatural Resistance: Roll 1d20 three times
(re-roll if you get the same result twice) and record
the results.

1-3

4-6

Immunity 5 (Cold, Heat, Pressure,
Radiation, Vacuum) • 5 points

Immunity 5 (Disease, Poison, Starvation

and Thirst, Suffocation) • 5 points

11-20

7-8

Immunity 5 (Alteration effects) • 5 points

9-10

Immunity 5 (Cold damage) • 5 points

11-12

Immunity 5 (Electricity damage) • 5 points

13-14

Immunity 5 (Emotion effects) • 5 points

15-17

Immunity 5 (Fire damage) • 5 points

18-20

Immunity 5 (Magic damage) • 5 points

Roll 1d20 once and record the result.

1-7

Eyes of Darkness: Senses 2 (Darkvision) • 2 points

8-14

15-20

Spider-Climb: Movement 1 (Wall-crawling)

• 2 points

Vampire Bite: Weaken Stamina 4, Grab-based

• 2 points

WEREWOLF

Thick Skin: Protection 3; Impervious Toughness 9, Lim-
ited—Not versus magical or silver weapons • 9 points

Roll 1d20 once and record the result.

Brother to Wolves: Summon 2 (Wolves and

1-10

Dogs), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Deathly Howl: Auditory Perception Area Affliction
10 (Resisted and Overcome by Will; Dazed and
Impaired, Disabled and Stunned), Extra Condition,
Limited Degree • 20 points

1-4

5-10

Demonic Cape: Flight 6 (120 MPH), Gliding,

11-20

Removable (-1 point) • 5 points

Demonic Movement: Leaping 2 (30 feet); Speed 3

(16 MPH) • 5 points

11-16 Giant Bat Wings: Flight 5 (60 MPH), Wings • 5 points

17-20

Hellrider: Movement 2 (Wall-crawling, Water

Walking), Limited to While Moving; Speed 6 (120
MPH), Activation (standard action, -2 points),
Removable (-1 point) • 5 points

VAMPIRE

Blood Drain: Regeneration 10, Source (Blood) • 5 points

Roll 1d20 once and record the result.

1-5

6-20

Living Vampire: Enhanced Stamina 13; Immunity

4 (aging, disease, need for sleep, poison);
Impervious Toughness 8 • 38 points

Undead Invulnerability: Immunity 30 (Fortitude
effects); Impervious Protection 8, Limited—Not
against blessed or magical weapons • 38 points

Roll 1d20 once and record the result.

1-6

7-12

13-20

Children of the Night: Summon 2 (Bats, Rats, and

Wolves), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Dominate: Perception Ranged Affliction 10 (Resisted

and Overcome by Will; Entranced, Compelled,
Controlled), Visually Sense-Dependent • 20 points

Mist Form: Insubstantial 2, Linked to Flight 5 (60

MPH) • 20 points

Roll 1d20 once and record the result.

[... truncated ...]
```

**Chunk 44** (`c1c422470246`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

TALENT

STRENGTH
1
STAMINA
1

AGILITY
2
DEXTERITY
2

FIGHTING
1
INTELLECT
3

AWARENESS
6
PRESENCE
2

Roll 1d20 once and record the result.

DABBLER

Expertise: (Choose One) 4, Insight 4, Perception 4

NINJA

Acrobatics 4, Perception 4, Stealth 4

SNEAK

Deception 4, Perception 4, Stealth 4

STUDENT

Expertise: (Choose One) 6, Insight 2, Perception 4

1-4

5-8

9-12

13-16

Charmed Life: You live a charmed life; maybe
you’re just lucky, but maybe it’s low-level psionic
influence... who can say?

POWERS

Contemplative: You are always calm and
controlled.

Perfect Mind: You use a greater percentage of
your mind.

Thought Leader: You use your abilities to help
others reach greater heights.

Roll  1d20  once  to  determine  if  you  should  roll  on  the
Psionic,  Mentalist,  or  Telekinetic  table,  then  roll  1d20
again on that table and record the result.

17-20

Trained Fighter: You know how to fight.

LIFE

Attractive, Fascinate (Persuasion), Luck

CONTEMPLATIVE

Fearless, Trance, Ultimate Effort (Will checks)

MIND

Eidetic Memory, Jack-of-all-trades, Ultimate Effort (Will checks),

LEADER

Choose either: Inspire, Leadership, and Teamwork, or Inspire 2
and Leadership or Teamwork

FIGHTER

Improved Initiative, Power Attack, Uncanny Dodge

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Charmer: You’re good with people.

Dabbler: You dabble in whatever interests you.

9-12

Ninja: You have been trained in the way of the ninja.

13-16

17-20

Sneak: You’re sneaky and underhanded when you
need to be.

11-15

Student: You’re a high-school, college, or post-
graduate student.

CHARMER

Deception 4, Insight 4, Persuasion 4

Psionic: Take Telepathy, listed immediately below,

then roll on the Psionic Table.

Telepathy: Mind Reading 5 Linked to Area Mental

Communication 3 • 25 points

Psionic Table: Roll 1d20 once and record the result
as the first power of an array, then roll 1d20 twice
and add each result as a 1-point Alternate Effect (re-
roll if you get the same result as your first roll).

1-3

4-7

ESP: Remote Sensing 6 (Normal Visual,
Normal Auditory, Mental) • 24 points

Mental Blast: Perception Range Damage

6, Resisted by Will • 24 points

1-10

8-11

Psi-Knife: Damage 8, Penetrating 4,

Accurate 4, Resisted by Will • 24 points

12-14

15-17

Psionic Invisibility: Concealment 10,

Affects Others, Limited—Concealme

[... truncated ...]
```

**Chunk 45** (`c53b199f9ade`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

OFFENSE

INITIATIVE +11

Mimic +11

Unarmed +81

Ranged, Mimic1

Close, Damage 11

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

81

11

81

81

81

STRENGTH
1
STAMINA
1

POWERS

AGILITY
1
DEXTERITY
1

FIGHTING
8
INTELLECT
1

AWARENESS
1
PRESENCE
2

Mimic: Variable 12 (60 points) for duplicating a subject’s traits,
Continuous, Move Action, Limited to One Subject, Resistible
(Dodge, DC 22) • 84 points.

Assessment

SKILLS

Deception 6 (+8), Expertise: (Choose One)
 4 (+5), Insight 8 (+9), Perception 6 (+7)

1 These bonuses will vary based
on the traits mimicked

```

**Chunk 46** (`c7946753c154`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

jects cannot have their selectivity changed once they are
created. +1 cost per rank.

Stationary:  Your  created  objects  can  hang  immobile
in  the  air. They  resist  being  moved  with  a  Strength  rank
equal to the modifier rank. Unless you have the Tether ex-
tra  or  the  Movable  extra,  you  cannot  move  a  stationary
created object once it’s placed any more than anyone else
can. +0 cost per rank.

Subtle:  This  modifier  either  makes  created  objects  not
noticeable as constructs for 1 rank (they look just like real
objects) or not noticeable at all for 2 ranks (such as objects
composed of invisible force). Flat +1or 2 points.

Tether: You  have  a  connection  to  your  created  objects,
allowing  you  to  exert  your  own  Strength  to  move  them
(provided you are strong enough to do so). Flat 1 point.
FLAWS

Feedback: You may suffer damage when your created ob-
jects are damaged (see the Feedback flaw description for
details). -1 cost per rank.

Permanent:  Permanent  created  objects  last  until  de-
stroyed or nullified. Unlike Continuous Create, you cannot
choose to dismiss such objects; they are truly permanent.
You  cannot  repair  permanent  created  objects  or  other-
wise alter them once they’re created. +0 cost per rank (for
a Sustained effect).

Proportional: Your  created  objects  have  a  total  volume
rank plus Toughness rank equal to your Create rank, rather

than both volume and Toughness up to your rank. So you
can create an object with volume rank 0 and Toughness
equal to your Create rank, vice versa, or anywhere in be-
tween, so long as the sum of the two ranks does not ex-
ceed your Create rank. –1 cost per rank.

DAZZLE

Effect:  Ranged,  Cumulative  Affliction,  Limited  to  One
Sense • 2 points per rank

You can overwhelm one of the target’s senses, chosen
when  you  take  this  effect.  The  target  makes  a  Forti-
tude  or  Will  resistance  check  against  your  effect  DC
(choose one when you acquire the effect). One degree
of failure leaves the sense impaired (–2 penalty). Two
degrees leave it disabled (–5 penalty) while three de-
grees  leave  the  sense  unaware: The  target  automati-
cally fails Perception checks involving the sense, and
everything effectively has total concealment from that
sense.

The target makes a new resistance check at the end of
each  turn  to  recover.  Success  removes  the  condition
imposed by the Dazzle power. Failure 

[... truncated ...]
```

**Chunk 47** (`c87ce883452a`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

Limited  to  One  Type:  Your  Quickness  applies  to  only
physical or mental tasks, not both. –1 cost per rank.

Limited to One Task: Your Quickness applies to only one
particular  task,  such  as  reading,  mathematical  calcula-
tions, and so forth. –2 cost per rank.

DEFENSE

Action: None • Range: Personal
Duration: Permanent • Cost: 1 point per rank

You recover quickly from damage. Remove penalties to
your  Toughness  checks  due  to  damage  equal  to  your
Regeneration rank each minute. You then recover other
damage  conditions  equal  to  your  Regeneration  rank
each minute, starting from your most severe condition.
Spread  this  recovery  out  evenly  over  a  minute  (10  ac-
tion  rounds).  So  with  Regeneration  5,  you  remove  a  –1
Toughness penalty every other round (every round with
Regeneration 10, and up to a –2 penalty per round with
Regeneration 20).

Characters  with  no  Stamina  do  not  heal  (see  Absent
Abilities in the Abilities chapter). One or more ranks of
Regeneration overcome this. An absent Stamina character
with Regeneration 1 recovers at a normal rate; additional
Regeneration ranks speed up that rate.
EXTRAS

Persistent:  You  can  regenerate  even  Incurable  damage
conditions (see the Incurable modifier). +1 cost per rank.
FLAWS

Source: Your Regeneration only works when you have ac-
cess  to  a  particular  source  to  replenish  yourself,  such  as
blood, electricity, sand, scrap metal, sunlight, and so forth.
–1 cost per rank.

SENSORY

Action: Free • Range: Rank
Duration: Sustained • Cost: 1–5 points per rank

You can displace one or more of your senses over a dis-
tance, perceiving as if you were at that location, up to 60
feet away. Each additional rank increases your range one
distance rank, so rank 2 is 120 feet, rank 3 is 250 feet, and
so  on.  Remote  Sensing  overrides  your  normal  sense(s)
while  you  are  using  it.  Subjects  observed  via  Remote
Sensing can “feel” it with an Insight check (DC 10 + rank).

You can make Perception checks normally using your dis-
placed senses, taking the normal action to do so. To search
a  large  area  for  someone  or  something,  use  the  search

Quickness,  like  many  power  effects,  is  not  especially
realistic;  it  allows  you  to  do  things  like  disassemble
an  entire  car  as  a  free  action  at  a  high  enough  rank
(around  rank  13-14),  but  doesn’t  have  any  effect  on
how  many 

[... truncated ...]
```

**Chunk 48** (`cf5b8ba8408b`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Effect: Damage, Reaction • 4 points per rank

Effect: Ranged Damage • 2 points per rank

You can surround your body with an aura of damaging
energy or some similar effect. Anyone you touch or that
touches you must make a Toughness resistance check
against your aura’s Damage rank. You can turn your aura
on and off at will as a free action. If your Aura damages
some targets but not others, apply the Selective or Lim-
ited modifiers (depending on whether or not the selec-
tivity is under your control).

Reduced Trait: One or more of your traits is lowered while
others  are  enhanced. This  flaw  is  worth  as  many  points
as  the  reduction  in  the  affected  trait(s).  So,  for  example,
if you lose Intellect while you gain in Strength, treat the
value  of  the  lost  Intellect  ranks  as  the  value  of  the  flaw.
As with all flaws, the effect must still cost at least 1 power
point. Flat –points equal to the lowered trait.

You can generate and project a type of energy, such as
cold, electricity, fire, kinetic force, magnetism, radiation,
or  even  cosmic  energy,  in  a  damaging  blast  (see  the
Blast power).

Energy Control is further defined by the addition of Alter-
nate Effects (see Alternate Effects, page 188), expand-
ing what you can do with your control. For example, Cold
Control  might  let  you  lower  the  surrounding  tempera-
ture (Environment – Cold) or trap targets in ice (Affliction,
see  the  Snare  version).  Magnetic  Control  could  let  you
manipulate metallic objects (Limited Move Object) while
Electrical Control lets you generate an electrical pulse to
overload electronics (Burst Area Nullify Electronics). Add
as many Alternate Effects to your Energy Control as you
can afford, and consider some additional ones as options
for power stunts (see Powers Stunts, page 20).

CONTROL

Action: Standard • Range: Rank
Duration: Sustained • Cost: 1–2 points per rank

You  can  change  the  environment  in  an  area:  raising  or
lowering  the  temperature,  creating  light,  causing  rain,
and so forth (see The Environment in the Action & Ad-
venture chapter for details).

Your  Environment  affects  a  30  foot  radius  around  you
at rank 1. Each additional rank moves the radius up one
distance rank, for a reach of approximately 2,000 miles at
rank  20,  sufficient  to  alter  the  environment  of  an  entire
continent!

Each of the following is a separate Environment effect. If
you 

[... truncated ...]
```

**Chunk 49** (`cfadcb33d64b`):

```
CHAPTER 2: SECRET ORIGINS

85

POWERS

Roll 1d20 once and record the result.

1-3

Shapeshifter: Variable 9 (45 points, for assuming

different shapes), Move Action • 72 points

Size-Changer: Roll 1d20 once or choose Giant Size
or Shrinking. You may take the other power as an
Alternate Effect by reducing Giant Size’s Power-
lifting to only 1 rank and dropping the Impervious
extra from Shrinking’s Protection 1. Also, only take
the Flight Belt supplied by the Giant Size power.

11-20

Density Decrease: Insubstantial 4
(Incorporeal, affected by magic),
Reaction, Linked to Flight 1 (4 MPH),
Limited to air-walking, and Immunity
10 (Life Support), Quirk: immunity to
suffocation requires holding breath, and
Concealment 1 (Hearing), Continuous;
Disruption Attacks: Array (24 points),
Incorporeal Weapon (Affects Corporeal
Damage 12, Resisted by Fortitude,
Limited to the Toughness of object used
as weapon), AE: Disrupt Electronics
(Close Range Affects Corporeal Nullify 12
(electronics), Simultaneous), AE: Disrupt
Synapses (Affects Corporeal Affliction
12 (Resisted and Overcome by Fortitude;
Dazed, Stunned, Incapacitated); Innate
Understanding of Powers (Enhanced
Advantages 13 (Close Attack 6, Defensive
Roll 2, Hide in Plain Sight, Redirect, Set-up
2, Teamwork), Enhanced Skill -4 (Close
Combat: Unarmed -8) (Note: the Innate
Understanding of Powers abilities only
work when no powers are active or when
Density Decrease is active) • 72 points

14-16

17-20

Specific Shapeshifter: Variable 9 (45 points, for

assuming different shapes), Continuous, Limited
(Choose one type of entity you can turn into:
Animals, Machines, Humanoids, Aliens, etc.), Move
Action • 72 points

Stretcher: Strength-based Damage 6; Elongation 8
(1,800 feet); Enhanced Advantages 14 (Accurate
Attack, Chokehold, Close Attack 2, Evasion, Fast
Grab, Improved Grab, Improved Hold, Improved
Trip, Interpose, Power Attack, Precise Attack
(Close; Cover), Takedown 2); Enhanced Skill 4
(Close Combat: Grab +8); Impervious Toughness 8,
Limited—Physical Impact Damage; Insubstantial
1 (Liquid), Precise; Morph 2 (Humanoid Forms),
Distracting; Movement 6 (Environmental
Adaptation - Tight Spaces, Safe Fall, Slithering,
Sure-footed, Swinging, Wall-crawling); Protection 7;
Speed 3 (16 MPH) • 72 points

DEFENSE

DODGE
+6

PARRY
+6

FORTITUDE
+6

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

32

72

6

SKILLS

DEFENSES

TOTAL

16

24

150

•

Fame:  Many  Shapeshifters  (especially  heroic  ones)
don’t worry about hiding their

[... truncated ...]
```

**Chunk 50** (`d329357e5091`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

GOLEM

STRENGTH
8
STAMINA
-

AGILITY
0
DEXTERITY
0

FIGHTING
6
INTELLECT
0

AWARENESS
4
PRESENCE
4

TECHNOLOGICAL

STRENGTH
8
STAMINA
-
UNDEAD

AGILITY
0
DEXTERITY
2

FIGHTING
6
INTELLECT
4

AWARENESS
1
PRESENCE
1

STRENGTH
6
STAMINA
-

AGILITY
2
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
2

Roll 1d20 once and record the result.

6-10

1-10

11-15

Brawler: You know how to use your strength to your
advantage.

Dabbler: You have some magical or technological
knowledge and can create useful devices or artifacts.

16-20

Perfect Recall: You have an uncanny memory.

BRUTE

Athletics 6, Intimidation 6

EXPERT

Perception 4, Choose One: Expertise: Magic 8 or Technology 8

SEEKER

Investigation 5, Perception 3, Persuasion 4

SNEAK

Deception 6, Stealth 6

POWERS

Find  the  entry  below  for  the  type  of  Construct  that
matches what you rolled for your Abilities.

GOLEM

Roll 1d20 once and record the result.

1-5

Blast: Ranged Damage 8, Accurate 6 • 22 points

Elemental Body: Enhanced Advantages 6 (Close

Attack 6); plus roll 1d20 once:

1-5

6-10

11-15

16-20

Damaging Aura: Reaction Damage 6

• 22 points

Gaseous Form: Flight 3 (16 MPH);

Insubstantial 2 (Gaseous) • 22 points

Liquid Form: Concealment 10 (All

Senses; Limited—In Liquid, Passive);
Insubstantial 1 (Liquid); Swimming 6
(30 MPH) • 22 points

Particulate Form: Elongation 2 (30
feet); Insubstantial 2 (Particulate);
Movement 2 (Permeate 2) • 22 points

BRAWLER

Improved Grab, Choose One: Power Attack or Accurate Attack

11-20

Unstoppable: Enhanced Strength 4; Enhanced Trait
2 (Close Attack 2); Immortality 5; Regeneration 2
• 22 points

DABBLER

Choose one set: Artificer, Skill Mastery (Expertise: Magic); or,
Inventor, Skill Mastery (Technology)

TECHNOLOGICAL

Roll 1d20 once and record the result.

RECALL

Eidetic Memory, Well-informed

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-5

Brute: You’re big and intimidating.

6-10

Expert: You know a lot about magic or technology.

11-15

Seeker: You’re looking for clues to your origin or past.

16-20

Sneak: You’re stealthy.

1-4

Blast: Ranged Damage 9, Accurate 4 • 22 points

5-8

Retractable Claws and Combat Computer: Strength-
based Damage 2, Penetrating 6; Enhanced Traits
14 (All-out Attack, Close Attack 4, Diehard, Evasion,
Fast Grab, Improved Critical (Claws), Improved
Initiative 2, Precise Atta

[... truncated ...]
```

**Chunk 51** (`d4cad3e10e05`):

```
CHAPTER 2:
ORIGINS .............. 23
HERO ARCHETYPES ......... 23
HERO DESIGN ................... 23
POINTS ................ 24
Starting Power Points .......... 24
Spending Power Points ...... 24
Power Level ............................. 24
Reallocating

Power Points ........................ 26
COMPLICATIONS .............. 27
Choosing Complications .... 27
Motivation ............................... 27
Other Complications ........... 28
BACKGROUND .................. 30
Name ......................................... 30
Origin ......................................... 30
Age ............................................. 31
Appearance ............................. 32
Personality ............................... 33
Goals .......................................... 33

IMPROVEMENT .............. 33
Increasing Power Level ....... 33
CHARACTER

ARCHETYPES .................. 34
Battlesuit .................................. 35
Construct ................................. 36
Crime Fighter .......................... 37
Energy Controller .................. 38
Gadgeteer ................................ 39
Martial Artist ........................... 40
Mimic ......................................... 41
Mystic ........................................ 42
Paragon .................................... 43
Powerhouse ............................ 44
Psychic ...................................... 45
Shapeshifter ............................ 46
Speedster ................................. 47
Warrior ...................................... 48
Weapon Master...................... 49
FIGHTER -

THE ROOK ....................... 50

POWERHOUSE -

PRINCESS ........................ 52

GENERATOR.................... 54

22

Quickness ...............................174
Regeneration ........................175
Remote Sensing ..................175
Senses .....................................176
Shrinking ................................180
Speed ......................................180
Summon .................................180
Swimming..............................183
Teleport ..................................183
Transform ...............................184
Variable ...................................184
Weaken ...................................186
MODIFIERS...................... 187
Applying Modifiers .............187
Extras .......................................188
Accurate ...............................188
Affects Corporeal ...............188
Affects Insubstantial .........188
Affects Obj

[... truncated ...]
```

**Chunk 52** (`daeb5804fb93`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

mimics  other’s  traits  is  limited  to  the  traits  its
subject(s)  possess;  a  Variable  effect  pro-
viding  you  with  traits  suitable  to  dif-
ferent shapes is limited by the form(s)
you  assume;  a  Variable  effect  pro-
viding  adaptations  is  limited  to  the
stimulus  to  which  it  adapts,  and
so  forth.  This  descriptor  does  not
reduce  the  effect’s  cost  unless  it’s
especially  narrow  or  limiting,  and
the GM is the final arbiter of what con-
stitutes  a  suitable  descriptor  and  which
descriptors are narrow enough to qualify
for a Limited flaw.

The  allocation  of  your  Variable  points  is
sustained,  so  if  you  stop  maintaining  your
Variable  effect  for  any  reason,  your  allo-
cated points “reset” to a “null” state: you lose
any temporary traits and must take the
action  necessary  to  reallocate  your
Variable  points  again  on  your  turn  to
regain  them.  Points  in  a  Continuous
Variable  effect  remain  where  you  set
them  without  maintenance,  unless  the
Variable  effect  itself  is  countered  or  nul-
lified.  Variable  effects  cannot  be  perma-
nent in duration by definition.

EXTRAS

Action: You can change the configuration of
your effect faster, although only a Reaction
Variable  can  change  more  often  than  once
per turn, and then only in response to its trig-
gering  circumstances.  Gamemasters  should
exercise  caution  with  Variable  effects  that
can be reconfigured as a free action or re-
action:  they  not  only  grant  tremendous
flexibility,  they  can  also  slow  down  game
play as the player considers virtually infinite
possibilities for each action using the Variable
effect. Move Action: +1 cost per rank . Free Action: +2 cost
per rank. Reaction: +3 cost per rank.

Affects Others: You can grant effects to someone
else. The subject granted the use of the effect con-
trols  its  configuration,  if  appropriate  for  its  descrip-
tors (although you retain the ability to withdraw use of the
effect altogether whenever you wish). Affects Others Only:
+0 cost per rank. Affects Others or yourself: +1 cost per rank.

Perception: Applied to a Ranged Affects Others Variable,
this extra allows you to grant the benefits of the effect to
any target you can accurately perceive. +1 cost per rank.

Ranged:  A Variable  effect  with  Affects  Others  may  have
the Ranged extra to improve the range at which you can
grant the effect to anoth

[... truncated ...]
```

**Chunk 53** (`db8b2bdf371a`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Energy Blast: Ranged Damage 12

Take the Gimmick Blaster and Energy Blast
(above), plus roll 1d20 three times (re-roll if you
get the same result twice) and add them to the
Gimmick Blaster array as Alternate Effects. Name
each of these Alternate Effects as appropriate for
your character’s gimmick.

1-3

4-5

6-8

9-11

12-14

Create 7, Continuous, Innate

Move Object 12

Ranged Affliction 12 (Resisted and
Overcome by Fortitude; Dazed,
Stunned, Incapacitated)

Ranged Affliction 12 (Resisted by
Dodge, Overcome by Damage;
Vulnerable, Defenseless,
Incapacitated)

Ranged Cloud Area Affliction 8

(Resisted and Overcome by Fortitude;
Dazed and Visually Impaired,
Stunned and Visually Disabled) Extra
Condition, Limited Degree

15-17

Ranged Burst Area Damage 8

18-20

Close Cone Area Damage 8, Penetrating 8

Personal Combat Enhancers: Enhanced Advantage

11 (All-out Attack, Defensive Attack, Evasion,
Extraordinary Effort, Diehard, Fearless, Great
Endurance, Improved Critical (Unarmed),
Improved Initiative, Takedown 2); Enhanced
Strength 3; Enhanced Trait 5 (Close Attack 5);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 points

8-12

13-14

15-16

Physical Boosters: Enhanced Strength 8; Leaping

2 (30 feet); Quickness 2; Speed 2 (8 MPH);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 point

17-20

High-tech Arsenal: Ray Gun (Ranged Damage 12,
AE: Power Truncheon (Strength-based Damage
8), AE: Stunner (Ranged Affliction 12 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated)), AE: Force Capsule Grenade
(Ranged Affliction 12 (Resisted by Dodge,
Overcome by Damage; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree); Easily Removable (-10 points)
• 17 points

Roll 1d20 once and record the result.

1-5

6-10

Combat Training and Armored Costume:
Enhanced Advantage 2 (Defensive Roll 2),
Enhanced Defenses (Dodge 4, Parry 4), Protection
4, Removable (-1 point) • 13 points

Displacer Field: Enhanced Defenses (Dodge 6, Parry
6) Linked to Protection 4, Sustained, Removable
(-3 points) • 13 points

11-15

Energy-Absorbing Body Suit: Protection 10,

Impervious 6, Removable (-3 points) • 13 points

16-20

Force Field: Immunity 6 (Critical Hits, Cold, Heat,

High Pressure, Radiation) Linked to Protection 10,
Sustained, Removable (-3 points) • 13 points

Roll 1d20 once and record the result.

1-4

5-8

9-16

17-20

Biologica

[... truncated ...]
```

**Chunk 54** (`dd5713402cfd`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL 7

STR
STA

8  AGL
8  DEX

0
0

FGT
INT

6  AWE
PRE
0

0
2

Powers: Foot Stomp (Line Area Damage 7,
Limited—Must be on same surface as target);
Super-Movement (Leaping 6 (500 feet));
Super-Tough (Immunity 10 (Life Support),
Impervious Toughness 4)

14-20

Advantages: Accurate Attack, All-out Attack,
Diehard, Fast Grab, Set-up 2, Takedown,
Teamwork

Skills: Athletics 3 (+11), Intimidation 4 (+6),
Perception 5 (+5)

Offense: Init +0, Unarmed +6 (Close, Damage 8)

Defense: Dodge 6, Parry 6, Fort 8, Tou 8, Will 6

Totals: Abilities 48 + Powers 26 + Advantages 8
+ Skills 6 + Defenses 12 = 100

SUMMONER

Roll 1d20 once on this table if you have the Summoner set
of Abilities and record the result.

15-20

Equipment: Bow (Ranged Damage 3),
Club (Strength-based Damage 2), Knife
(Strength-based Damage 1, Improved
Critical), Nunchaku (Strength-based
Damage 2, Improved Critical), Shuriken
(Ranged Multiattack Damage 1), Sword
(Strength-based Damage 3, Improved
Critical)

Advantages: Equipment 4, Evasion, Hide
in Plain Sight, Quick Draw

Skills: Acrobatics 6 (+10), Athletics 6 (+8),
Perception 3 (+5), Ranged Combat (Ninja
Weapons) 3 (+7), Sleight of Hand 4 (+8),
Stealth 10 (+14)

Offense: Init +4, Bow +7 (Ranged, Damage
3), Sword +7 (Close, Damage 5, Crit. 19-20),
Unarmed +7 (Close, Damage 2)

Defense: Dodge 10, Parry 10, Fort 6, Tou
2, Will 6

Totals: Abilities 42 + Powers 8 + Advantages
7 + Skills 16 + Defenses 17 = 90

ROBOTS

PL 6

8  AGL

STR
STA  —  DEX  0

2  FGT

2  AWE

0
INT  —  PRE  —

Imaginary Friend: Summon 10 (One PL10,

150-point character; Choose or roll up another
character using the tables in this book and use
that as your summoned creature. Note: the
summoned creature may not have minions, a
headquarters, or any other traits the GM decides
are outside the scope of the Summon power),
Controlled, Heroic, Mental Link • 51 points

Roll 1d20 once and record the result. (Only roll on
this table if you Summon the Imaginary Friend.)

1-4

5-8

Invisibility: Concealment 10 (All
senses), Blending • 10 points

Lucky: Luck Control 2 (Force a re-roll,
Negate luck), Luck 4 • 10 points

9-12

Mimic: Variable 2 (10 points),

Limited—Can only mimic a trait of
Imaginary Friend, Increased Action
(Standard), Tiring • 10 points

13-16

Shapechange: Morph 2 (Humanoids)

• 10 points

17-20

Projections: Create 5 • 10 points

Summon Animals: Summon 4 (Sixteen PL4,

60-point minions; You can s

[... truncated ...]
```

**Chunk 55** (`e17d1554782d`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Dense Fog: Visual (All) Concealment 4 Attack, Burst

1-8

Arc Riding: Leaping 10 • 10 points

Weather Control array as Dynamic Alternate Effects (re-
roll if you get the same result twice).

Arctic Freeze: Ranged Cumulative Affliction 10
(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree
• 30 points

Dazzling Strike: Ranged Cumulative Affliction 10

(Resisted and Overcome by Fortitude; Vision and
Auditory Impaired, Vision and Auditory Disabled,
Vision and Auditory Unaware) • 30 points

Area (×3), Selective • 28 points

Downdraft: Ranged Affliction 10 (Resisted and

Overcome by Strength; Hindered and Impaired,
Stunned and Prone, Incapacitated), Alternate
Resistance (Strength), Concentration Duration,
Extra Condition, Instant Recovery • 30 points

Glacier: Create 9, Continuous, Innate, Linked to
Environment 2 (Cold, Impede Movement 1)
• 30 points

Hailstorm: Ranged Cloud Area Damage 9, Indirect 2

(falling from above) • 30 points

Lightning Bolt: Ranged Damage 12, Accurate 3,
Indirect 3 (any point downwards) • 30 points

Stormy Weather: Environment 10 (2 miles; Cold,

Impede Movement, Visibility) • 30 points

Tornado: Cylinder Area Move Object 10,

Concentration Duration, Damaging • 30 points

Wind Screen: Deflect 10, Cylinder Area (×3), Limited

to Attacks Targeting Dodge • 30 points

1-2

3-4

5-6

7-8

9-10

11-12

13-14

15-16

17-18

19-20

Roll 1d20 once and record the result.

1-5

Aquatic: Immunity 3 (Cold, Drowning, Pressure),
Senses 5 (Darkvision, Accurate and Extended
Hearing); Swimming 2 (2 MPH), Stacks with other
Swimming • 10 points

6-10

Cold Immunity: Immunity 10 (Cold effects) • 10 points

11-20

Weather-Proof: Immunity 10 (Weather effects)

• 10 points

Roll 1d20 once and record the result.

1-7

8-14

15-20

Force Field: Impervious Protection 8, Sustained

• 16 points

Vigorous: Enhanced Stamina 3; Enhanced Defenses

10 (Dodge 5, Parry 5), Sustained • 16 points

Wind Shield: Enhanced Defenses 16 (Dodge 8, Parry

8), Sustained • 16 points

Roll 1d20 once and record the result.

Swimming: Movement 1 (Environmental

9-12

Adaptation—Aquatic); Swimming 8 (120 MPH),
Stacks with other Swimming • 10 points

13-20 Wind Riding: Flight 5 (60 MPH) • 10 points

DEFENSE

DODGE
+2

PARRY
+0

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

40

75

7

SKILLS

DEFENSES

TOTAL

16

12

150

•  Moti

[... truncated ...]
```

**Chunk 56** (`f1bc1ad153ee`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Example:  Lady  Liberty,  rescuing  people  from  a
tenement  fire,  is  hemmed-in  by  collapsed  debris.
Her player decides to simply punch a path through.
Since  she’s  going  for  maximum  damage,  she  de-
cides  to  make  the  attack  check  normally  (rather
than a routine check). Given her attack bonus, she’ll
only miss on a natural 1 anyway. She succeeds and
does her Strength in Damage, +5 for the automatic
critical. The GM decides the brick, mortar, and heavy
beams have a toughness of 9 and makes a Tough-
ness  check,  rolling  a  5,  against  a  DC  30  (Lady  Lib-
erty’s Damage +15). A 14 result is three degrees of
failure, so she easily smashes through the debris and
clears the building, carrying people to safety!

The  Toughness  ranks  of  some  common  materials  are
shown on the Material Toughness table. The listed ranks
are for about an inch (distance rank –7) thickness of the
material: apply a +1 per doubling of thickness or a –1 per
halving of it. So a foot of stone is Toughness 8. Equipment
has Toughness based on its material. Devices have a base
Toughness equal to the total points in the device divided
by 5 (rounded down, minimum of 1).

MATERIAL

TOUGHNESS

Paper

Soil

Glass

Ice

Rope

Wood

Stone

Iron

Reinforced Concrete

Steel

Titanium

Super-alloys

RECOVERY

0

0

1

1

1

3

5

7

8

9

15

20+

Living targets remove one damage condition per minute
of  rest,  starting  from  their  worst  condition  and  working
back. So a damaged character recovers from being inca-
pacitated, then staggered, dazed, and finally removes a –1
Toughness check penalty per minute until fully recovered.
The Healing and Regeneration effects can speed this pro-
cess. Lasting or more serious injuries are handled as com-
plications  (see  Lasting Injuries  in  the  Recovery section
of the Action & Adventure chapter).

Objects, having no Stamina, do not recover from damage
unless they have an effect like Regeneration. Instead, they
must be repaired. See the guidelines under the Technol-
ogy skill when repairing damaged objects.

DEFLECT

DEFENSE

Action: Standard • Range: Ranged
Duration: Instant • Cost: 1 point per rank

You can actively defend for characters other than yourself,
deflecting or diverting attacks against them at a distance,
and may be able to more effectively defend yourself, de-
pending on your rank. See the Defend action in the Ac-
tion  &  Adventure  chapter  for  details. You 

[... truncated ...]
```

**Chunk 57** (`f45e1af7c8dc`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Effect: Ranged, Progressive Affliction, Resisted by Forti-
tude • 4 points per rank

You  render  the  target  unable  to  breathe.  Targets  fail-
ing  the  Fortitude  resistance  check  against  your  effect
DC become dazed, stunned, and finally incapacitated,
passing out from the lack of oxygen. A failed attempt
to  resist  the  ongoing  effect  of  Suffocation  causes  the
target’s condition to worsen by one degree.

ent than “heat ray” is a descriptor for a Damage effect or
“sticky webbing” is a descriptor for a hindering Affliction;
in  neither  case  does  the  character  need  Summon  Heat
Ray or Summon Webbing to create the desired powers!

SWIMMING

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You can swim fast. You have a water speed equal to your
Swimming  rank  –2,  subject  to  the  usual  rules  for  swim-
ming (see the Athletics skill description for details). You
can make Athletics checks to swim as routine checks. This
power does not allow you to breathe underwater (for that
see Immunity, page 165).

TELEPORT

MOVEMENT

Action: Move • Range: Rank
Duration: Instant • Cost: 2 points per rank

You can move instantly from place to place without cross-
ing the distance in between. You can teleport yourself and
up  to  50  lbs.  (mass  rank  0)  of  additional  mass  a  distance
rank equal to your effect rank as a move action. Unwilling
passengers  get  a  Dodge  resistance  check  to  avoid  being
taken along.

You can only teleport to places you can accurately sense
or know especially well (in the GM’s judgment). You re-
tain  your  position  and  relative  velocity  when  you  tele-
port. So if you are falling when you teleport, you are still
falling at the same speed when you arrive at your desti-
nation.

Teleport is meant for use on or around a planet. For things
like traveling to distant planets or stars, apply the Space
Travel  effect  of  Movement  as  a  “hyperjump”  or  similar
power.
EXTRAS

Accurate: You don’t need to know or accurately sense your
destination to teleport there, just be able to generally de-
scribe it, such as “inside the capitol building lobby” or “atop
the  Emerald  Tower’s  roof.”  If  the  destination  isn’t  in  your
Teleport range, nothing happens. +1 cost per rank.

SUPER-SPEED

Effect: Enhanced Initiative, Quickness, Speed • 3 points
per rank

You are fast! Each rank of Super-Speed gives you the
effects  of  Imp

[... truncated ...]
```

**Chunk 58** (`f97fb5b16662`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

PARAGON
PARAGON

STRENGTH
12
STAMINA
12

POWERS

AGILITY
3
DEXTERITY
1

FIGHTING
8
INTELLECT
0

AWARENESS
1
PRESENCE
1

Flight: Flight 9 (1,000 MPH)• 18 points.

Invulnerability: Enhanced Stamina 10,

Immunity 10 (Life Support), Impervious
Toughness 12 • 42 points.

Super-Speed: Quickness 2 • 2 points.

Super-Strength: Enhanced Strength 10, plus
Enhanced Strength 2, Limited to Lifting
(Lifting Str 14; 400 tons)
• 22 points.

Power Attack

SKILLS

Expertise: (Choose One) 7 (+7), Insight 6 (+7),
Perception 8 (+9), Persuasion 6 (+7), Ranged
Combat: Throwing 7 (+8)

OFFENSE

INITIATIVE +3

Throw +8

Ranged, Damage 12

Unarmed +8

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

12

12

8

8

8

```

**Chunk 59** (`fc4ed8309dc8`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

Action: This extra reduces the action required for you to
use Healing. You cannot use Healing more than once per
turn  regardless. To  heal  multiple  subjects  at  once,  apply
the Area modifier. +1 cost per rank.

Affects Objects: Your Healing can also “heal” damage to
non-living  subjects.  You  make  a  Healing  check  against
the subject’s worst damage condition, as normal. +1 cost
per rank.

Area: Healing with this extra grants the same benefit to all
subjects in the affected area. Area Empathic Healing (see
this power’s Flaws) is an unwise combination, as the heal-
er takes on all of the damage conditions of the affected
subjects at once! +1 cost per rank.

Energizing: You can heal the fatigued and exhausted con-
ditions as well as damage conditions: DC 10, one degree of
success for fatigued, two degrees of success for exhausted.
However, you take on the removed conditions and cannot
use  Healing  to  eliminate  your  own  fatigue  (although  you
can still use hero points to recover from them). If the Heal-
ing check fails, you must wait the normal recovery time or
use extra effort to try again. +1 cost per rank.

Perception: Applied to Ranged Healing (following), Per-
ception Ranged Healing does not require an attack check
to “touch” the subject. +1 cost per rank.

Persistent: Your  Healing  can  remove  even  Incurable  ef-
fects (see the Incurable modifier). Flat +1 point.

Ranged:  Ranged  Healing  requires  an  attack  check  to
“touch” the subject with the Healing effect. The GM may
waive the check for a willing subject holding completely
still, but the subject is defenseless that round, making it an
unwise decision in the midst of combat. +1 cost per rank.

recover from it normally. You can use Healing and Regen-
eration to cure your own conditions. You can have the Res-
urrection modifier for Healing, but if you successfully use
it, you die! This may not be as bad as it seems if you have
Immortality, allowing you to return to life (see the Immor-
tality effect for details). –1 cost per rank.

Limited: Examples of ways in which Healing may be Lim-
ited include: One Type of Damage (such as energy or blud-
geoning  damage),  Objects  (in  conjunction  with  Affects
Objects), Others (you can’t use Healing on yourself), or Self
(you can only use Healing on yourself). –1 cost per rank.

Temporary:  The  benefits  of  your  Healing  are  temporary,
lasting for one hour. The subject the

[... truncated ...]
```

**Chunk 60** (`ffc525f7d497`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-14

Rapid Fire: Selective Ranged Multiattack Damage 4,

Accurate 4 • 20 points

15-18

Sonic Boom: Burst Area Damage 10 • 20 points

19-20

Vertigo Attack: Cumulative Affliction 9 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated), Accurate 2 • 20 points

Roll  1d20  once  and  add  the  power  to  the  Speedster
Stunts array as an Alternate Effect

1-4

5-6

Air Control: Cone Area Move Object 10, Close

Range • 1 point

Anchor: Simultaneous Nullify Movement Effects 10

• 1 point

7-8

Phase Shift: Insubstantial 4 • 1 point

9-10

11-20

Temporal/Dimensional Duplicate: Summon
Duplicate 10, Active, Feedback • 1 point

Roll on the table above instead (re-roll if you get

the same result as earlier) • 1 point

Roll 1d20 once and record the result.

Bullet: Enhanced Defenses 12 (Dodge 6, Parry 6);

Protection 8, Impervious • 28 points

Hard Target: Enhanced Advantages 6 (Defensive

Roll 3, Improved Initiative 3), Enhanced Defenses
22 (Dodge 11, Parry 11) • 28 points

Natural Selection: Enhanced Agility 2, Enhanced
Stamina 2, Enhanced Defenses 20 (Dodge 10,
Parry 10) • 28 points

1-4

5-12

13-16

17-20

SUMMONER

The Summoner is an archetype that covers a lot of ground,
from heroes who create duplicates of themselves to those
who animate images, summon otherworldly creatures, or
create minions out of thin air. In order to make the Sum-
moner fit into this book, these tables produce a duplicator
(who  summons  duplicates  of  him-  or  herself )  or  a  sum-
moner whose summoned creatures are minions with de-
cent combat abilities.

There are a few options for the duplicator: a Martial Artist,
and Energy Controller, and a Powerhouse. These are only
examples of the sorts of duplicators you can use and you
are free to swap points around to change your duplicating
Martial Artist into a duplicating Battlesuit, Crime Fighter,
Weapon Master or any other archetype, just be sure the
duplicates  remain  within  their  power  level  limits  (117
points and PL8 for Twin or 100 points and PL7 for Triplets,
plus the cost of the Summon power).

Note  that  on  the  tables  below,  things  are  a  bit  different
than for the other archetypes in this book. Follow the in-
structions and it should be clear. The change is necessary
because  the  Summon  power  your  character  has  influ-
ences the number of points available to spend on other
sections of the character.
ABILITIES

R

[... truncated ...]
```

---

## Concept: Limited Degree

Chunk count: 17
Receives actions: ['act_0179']

### Chunk texts

**Chunk 1** (`04f4880a6e63`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HIGHTECH GEAR

Advantage: Equipment 10 (Equipment listed
immediately below)

Smartphone, Restraints, Flashlight, Multi-tool,
Rebreather • 6 points

Headquarters—Size: Huge, Toughness: 10;
Features: Communications, Computer, Concealed,
Garage, Gym, Laboratory, Living Space, Power
System, Security System, Workshop • 15 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Swingline: Movement 1 (Swinging) • 2 points

Utility Belt • 17 points

11-20

•  Bolos: Ranged Cumulative Affliction 4 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobilized), Extra
Condition, Limited Degree • 12 points

•  Boomerangs: Strength-based Ranged Damage 1,

Accurate 2 • 1 point

ure. This motivation is especially appropriate for the
Dark Avenger.

•  Motivation—Thrills: You don’t have any powers, per
se, but why should that stop you from having fun?

•

Enemy: The Crime Fighter usually has at least one vil-
lain central to his or her existence who plagues the
hero consistently.

ELEMENTAL

The Elemental is a being composed of a pure element, usu-
ally one of the classical four elements of earth, air, fire, or
water. They have powers reflecting their elemental compo-
sition, as well as control and mastery over that element.
ABILITIES

•  Explosives: Ranged Burst Area Damage 4 • 1 point

Roll 1d20 once and record the result.

•  Power-Knuckles: Strength-based Damage 3,

Improved Critical, Inaccurate • 1 point

•  Taser: Ranged Cumulative Affliction 4 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated) • 1 point

•  Tear-Gas Pellets: Ranged Cloud Area Affliction 4
(Resisted and Overcome by Fortitude; Dazed and
Visually Impaired, Stunned and Visually Disabled),
Extra Condition, Limited Degree • 1 point

DEFENSES

DODGE
+7

PARRY
+5

FORTITUDE
+4

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

68

7/0*

SKILLS

DEFENSES

28/35*

TOTAL

23

24

150

*If you rolled Gadgeteer on the Powers/Equipment table,
then  you  have  Powers  7  and  Advantages  28,  otherwise
you have Powers 0 and Advantages 35.

•  Motivation—Patriotism:  You  strongly  believe  in  the
ideals your country was founded on and fight to uphold
them... especially from those who would twist them to
their own purposes. Patriotic Crime Fighters often have
a military background, but they don’t have to.

•  Motivation—Doing Good: Crime Fighters with this
motivation ar

[... truncated ...]
```

**Chunk 2** (`1081db3c43af`):

```
CHAPTER 2: SECRET ORIGINS

69

15-20

Scientist: At heart, you’re a scientist. You’re always
working on something in the lab, but you like to get
“out in the field” and test the practical applications
of your inventions. Plus, there are all sorts of unusual
things out in the world that you’d never get to
experience in the lab.

TINKERER

Accurate Attack, Luck, Power Attack

INVENTOR

Benefit 3 (Millionaire)

SKILLS

Close Combat: Unarmed or Gadgets 6, Expertise: Science 10,
Ranged Combat: Gadgets 6, Technology 10, Vehicles 4

Take the skills listed above, then roll 1d20 once and record
the result.

1-5

6-10

Businessman/woman: You know how to run a
business.

Explorer: You have the skills necessary to explore
new places.

11-15

Investigator: You’re a talented detective.

16-20

Infiltrator: You’re stealthy.

BUSINESSMAN/WOMAN

Expertise: Business 5, Insight 6, Persuasion 5

EXPLORER

Athletics 7, Perception 5, Stealth 4

INVESTIGATOR

Insight 4, Investigation 7, Perception 5

INFILTRATOR

Deception 6, Sleight of Hand 4, Stealth 6

POWERS

Roll 1d20 once and record the result.

ADVENTURER

STRENGTH
2
STAMINA
2
GIMMICK

AGILITY
2
DEXTERITY
2

STRENGTH
2
STAMINA
1

AGILITY
2
DEXTERITY
2
SCIENTIST

FIGHTING
4
INTELLECT
8

AWARENESS
3
PRESENCE
2

FIGHTING
4
INTELLECT
9

AWARENESS
4
PRESENCE
1

STRENGTH
1
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
4
INTELLECT
10

AWARENESS
4
PRESENCE
0

Beginner’s Luck, Eidetic Memory, Equipment 3 (Headquarters),
Improvised Tools, Inventor, Skill Mastery (Technology)

Headquarters—Size:  Large,  Toughness:  10;  Features:
Communications, Computer, Fire Prevention System, Infirmary,
Laboratory,  Library,  Living  Space,  Personnel,  Power  System,
Security System, Workshop • 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Athletic: You take care of yourself and are physically fit.

6-10

Natural Leader: You’re a natural leader.

11-15

Tinkerer: You’re constantly tinkering with your
inventions and are able to get the most out of them.

16-20

Well-to-do Inventor: You either inherited wealth or
have made money off some of your more mundane
inventions.

ATHLETIC

Evasion, Improved Initiative, Uncanny Dodge

LEADER

8-12

Inspire 2, Leadership

70

1-4

5-7

Energy Projector Device: Ranged Damage 8,
Accurate 2; AE: Ranged Affliction 8 (Resisted
and Overcome by Fortitude; Dazed Stunned,
Incapacitated), Accurate 2; AE: Ranged
Multiattack Damage 5, Accurate 3; AE: Close Cone
Area Dazzle 9

[... truncated ...]
```

**Chunk 3** (`301534069c2d`):

```
CHAPTER 2: SECRET ORIGINS

99

5-8

Cybernetic Implants: Enhanced Awareness

2; Enhanced Advantages 2 (Eidetic Memory,
Improved Initiative); Enhanced Defenses 4 (Parry
2, Dodge 2); Senses 6 (Accurate and Extended
Hearing, Analytical and Extended Vision,
Infravision) • 16 points

9-15

Healing Factor: Enhanced Stamina 2; Immunity 2
(disease, poison); Regeneration 10 • 16 points

16-20

Tactical Mastermind: Enhanced Intellect 2,

Enhanced Awareness 2; Enhanced Advantages
3 (Defensive Roll 2, Uncanny Dodge); Senses
5 (Danger Sense, Detect Weakness—Acute,
Analytical, Ranged) • 16 points

OTHERWORLDLY

Roll 1d20 once and record the result.

1-4

5-6

7-11

12-17

18-20

Alien: Enhanced Stamina 2; Immunity 7 (Cold, Heat,
Pressure, Radiation, Suffocation, Vacuum); Mental
Communication 1; Senses 1 (Mental Awareness)
• 16 points

Aquatic: Enhanced Stamina 2; Immunity 3 (Cold,

Drowning, Pressure); Movement 1 (Environmental
Adaptation—Aquatic); Senses 1 (Low-light Vision);
Swimming 6 (30 MPH) • 16 points

Exemplar: Enhanced Stamina 1, Enhanced

Awareness 1, Enhanced Defenses 2 (Dodge 1,
Parry 1); Immunity 2 (Aging, Disease); Quickness 4;
Speed 4 (30 MPH) • 16 points

Immortal: Enhanced Awareness 2; Immortality
5, Limited (choose effect); Immunity 3 (Aging,
Disease, Poison); Protection 2; Regeneration 2
• 16 points

Winged: Enhanced Awareness 2, Enhanced

Defenses 4 (Dodge 2, Parry 2); Flight 6 (120 MPH),
Wings; Immunity 1 (Cold); Senses 1 (Extended
Vision) • 16 points

HUMAN

Roll 1d20 once and record the result.

11-20

Unique Weapon: Strength-based Damage 3,

Accurate, Penetrating 10 plus roll 1d20 once:

1-5

6-10

Atom Slicer: Weaken Toughness 10,

Penetrating 2, Linked to Damage, Easily
Removable (-10 points) • 16 points

Boom Staff: Movement 3 (Space Travel

3), Portal; Easily Removable (-10
points) • 16  points

11-15

Dimension Cutter: Movement 3

(Dimension Travel 3), Portal; Easily
Removable (-10 points) • 16 points

16-20

Thundering Mallet: Cumulative
Affliction 10 (Resisted and
Overcome by Fortitude; Vulnerable,
Defenseless), Limited Degree, Linked
to Damage, Penetrating 2; Easily
Removable (-10 points) • 16 points

DEFENSE

DODGE
+4

PARRY
+2

ABILITIES

POWERS

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

78

32

9

SKILLS

DEFENSES

TOTAL

17

14

150

•  Motivation—Patriotism:  Duty  to  country  may  have
motivated the warrior to have undergone experiments
that transformed him or to visit the world outside his
home.

•  Motivation—Responsibility:  The  war

[... truncated ...]
```

**Chunk 4** (`373c8323a9b6`):

```
CHAPTER 6: POWERS

149

Spread throughout this section are boxes like this one,
providing  examples  of  some  of  the  most  common
powers  found  amongst  superhero  characters  to  give
you a “menu” of pre-fabricated powers to choose from
when  creating  your  own  heroes  (and  villains)  in  MU-
MASTERMINDS.  Sample  powers  are  presented  on
the Power Effects table in italics.

Each power is presented in the following format:

NAME

Effect(s): Modifier(s) • Cost

Name: What the power is called. Feel free to mod-
ify the name to suit how you’re using the power.

Effects: The power’s effect or effects are listed by
name.

Modifiers:  Any  modifiers  applying  to  the  effect
are  listed  with  it.  If  a  power  has  multiple  effects,
each is listed with its applicable modifiers.

Cost: Lastly, the power’s cost is given. This is a cost
per rank of the power if it has a ranked effect, oth-
erwise it is a flat cost in power points. Some pow-
ers may have a flat cost for the initial power, plus a
cost per rank for additional ranks.

Effect: Varies, Activation • effects total –1 or 2 points

isting degrees on the target. For example, if you hit a target
and impose a vulnerable condition (one degree), then at-
tack again and get one degree on the effect, you impose
the Affliction’s second degree condition. +1 cost per rank.

Extra  Condition:  Your  Affliction  imposes  an  additional
condition per degree of success. So with one application of
this extra, your Affliction imposes two conditions—such as
dazed  and  hindered,  or  impaired  and  vulnerable—rather
than just one. With two applications, it imposes three con-
ditions,  and  so  forth.  Since  mutually  incompatible  condi-
tions  are  largely  wasted,  Afflictions  with  this  extra  often
have the Limited Degree flaw as well. +1 cost per rank.

Progressive: This modifier causes an Affliction to increase
incrementally  without  any  effort  from  you.  If  the  target
fails  a  resistance  check  to  end  the  Affliction,  it  not  only
persists, but increases in effect by one degree! So a target
affected by the first degree of a Progressive Affliction who
fails to resist progresses to the second degree of the effect
at the start of his next round. A successful resistance check
still ends the Affliction, as usual. +2 cost per rank.

FLAWS

Instant Recovery: Similar to the Reversible extra (see p.
196),  the  target  of  an  Affliction  effect  with  this  modifier
recovers  automatically,  no  c

[... truncated ...]
```

**Chunk 5** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 6** (`43d5c758bf78`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WASP

Insect Senses: Senses 4 (Acute Smell, Darkvision,

Ranged Touch) • 4 points

16-20

Sting: Cumulative Affliction 8 (Resisted and Overcome
by Fortitude; Impaired, Disabled, Incapacitated),
Linked to Damage 8, Accurate 2 • 26 points

Roll 1d20 once and record the result.

CANINE

Bite: Strength-based Damage 3, Improved Critical,

Wings: Flight 6 (120 MPH), Wings • 6 points

Penetrating 3 • 7 points

Canine Senses: Senses 3 (Low-light Vision, Acute

and Tracking Olfactory) • 3 points

1-10

Canine Movement: Leaping 2 (30 feet); Speed 4 (30

Talons: Strength-based Damage 1, Accurate 2, Fast Grab

MPH) • 6 points

• 4 points

Roll 1d20 once and record the result.

FALCON

Flight: Flight 6 (120 MPH), Wings • 6 points

Keen Eyesight: Senses 3 (Extended 2 and Rapid

Vision) • 3 points

1-10

Sonic Scream: Cone Area Affliction 9 (Resisted

and Overcome by Fortitude; Dazed and Auditory
Impaired, Stunned and Auditory Disabled,
Incapacitated and Auditory Unaware), Extra
Condition, Quirk—Impaired, Disabled, Unaware
Limited to One Sense (-4 points) • 23 points

11-20

OWL

Nightvision: Senses 2 (Extended Vision, Low-light

Vision) • 2 points

11-20

Shriek: Cone Area Affliction 8 (Resisted and
Overcome by Will; Dazed and Vulnerable,
Stunned and Defenseless, Incapacitated)
• 24 points

Silent Flight: Flight 5 (60 MPH), Subtle, Wings • 6 points

Howl: Auditory Perception Area Affliction

10 (Resisted and Overcome by Will; Dazed
and Impaired, Disabled and Stunned), Extra
Condition, Limited Degree • 20 points

FELINE

Claws: Strength-based Damage 1, Accurate,

Improved Critical • 3 points

Feline Senses: Senses 3 (Low-light Vision, Acute and

Tracking Olfactory) • 3 points

Feline Movement: Leaping 3 (60 feet); Movement
3 (Safe Fall, Sure-footed, Trackless); Movement
1 (Water-walking), Limited to Solid Surfaces;
Movement 1 (Wall-crawling), Limited to One
Move Action; Speed 4 (30 MPH) • 15 points

Plus roll 1d20 once and record the result.

1-5

Black Cat: Reaction Visual Perception

Area Affliction 5 (Resisted by Dodge,
Overcome by Will; Vulnerable,
Defenseless, Incapacitated), Side-
effect (Always happens, chosen by
player) • 15 points

```

**Chunk 7** (`661dd344a1d2`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

the  round  in  which  the  duration  ends.  So,  for  example,
an instant duration Affliction only lasts one round, while
a  sustained  duration  Affliction  lasts  until  no  longer  sus-
tained. –1 cost per rank.

Limited Degree: Your Affliction is limited to no more than
two degrees of effect. With two applications of this modi-
fier, it is limited to no more than one degree of effect. –1
cost per rank.

BURROWING

MOVEMENT

Action: Free • Range: Personal
Duration: Sustained • Cost: 1 point per rank

You can burrow through the ground, leaving a tunnel be-
hind if you choose. You move through soil and sand at a
speed rank equal to your Burrowing rank, minus 5. So Bur-
rowing 8, for example, lets you move through the ground
at speed rank 3 (around 16 MPH). Burrowing through hard
clay and packed earth reduces speed one additional rank.
Burrowing through solid rock reduces it by two additional
ranks. The tunnel you leave behind is either permanent or
collapses behind you immediately (your choice when you
begin burrowing each new tunnel).

Note  that  Burrowing  differs  from  the  Permeate  effect  of
Movement, which allows you to pass through an obstacle
like the ground at your normal speed without disturbing
it at all (see Movement for details).
EXTRAS

Penetrating:  Normally,  the  hardness  of  the  ground  af-
fects  only  the  speed  at  which  you  burrow.  At  the  GM’s
discretion, some super-hard materials may be considered
Impervious to Burrowing, in which case this extra allows
you to dig through them. 1 point per rank.

Ranged: This extra either allows you to create tunnels at a
greater distance (without having to be at the end-point of
the tunnel as it forms) or, in conjunction with Affects Oth-
ers, allows you to grant the Burrowing effect to someone
else at a distance. Doing both requires two applications of
the extra. +1 or 2 cost per rank.

FLAWS

Limited:  Burrowing  may  be  limited  to  certain  circum-
stances  or  materials,  such  as  only  loose  sand  and  soil

BLAST

Effect: Ranged Damage • 2 points per rank

You  can  make  a  damaging  ranged  attack.  It  might  be
a  blast  of  energy,  a  projectile  (arrow,  bullet,  throwing
blade, etc.), or some similar effect. You make a ranged
attack  check  against  the  target’s  Dodge  defense.  The
attack’s damage equals your power rank and the target
makes a Toughness resistance check against it.

(leaving  the  character  una

[... truncated ...]
```

**Chunk 8** (`7b2254220623`):

```
CHAPTER 6: POWERS

181

SNARE

Effect:  Ranged,  Cumulative  Affliction,  Extra  Condition,
Resisted by Dodge, Limited Degree • 3 points per rank

You can restrain a target with bonds of ice, glue, web-
bing, bands of energy, and so forth (whatever suits your
descriptors). The target makes a Dodge resistance check
against your effect DC. One degree of failure leaves the
target hindered and vulnerable, while two results in the
target becoming defenseless and immobilized. There is
no additional effect for three or more degrees of failure.

The resistance check to break out of a Snare is based on
Damage (including Strength Damage) or Sleight of Hand,
either breaking the effect or slipping out of it. This is part of
the power’s Alternate Resistance, with no change in cost.

Mental Link: You  have  a  mental  link  with  your  minions,
allowing you to communicate with them and issue orders
telepathically like the Communication Link effect (see the
Senses effects in this chapter). Flat +1 point.

Multiple  Minions:  You  can  summon  more  than  one
minion. Each application of this extra doubles your total
number of minions. So, for example, with Summon 6, you
summon a single 90-point minion. With Multiple Minions
1, you can summon two 90-point minions, with Multiple
Minions  2,  four  minions,  and  so  forth.  It  requires  a  stan-
dard action to summon each minion unless you also have
the Horde extra (see previous). +2 cost per rank.

STRIKE

Effect: Damage • 1 point per rank

You  inflict  additional  damage  in  close  combat.  Your
Strike  either  substitutes  for  your  Strength  damage  or
adds  to  it,  if  it  is  Strength-based,  see  the  Damage  ef-
fect for details. It might be claws, energy fields, focused
striking  strength,  or  something  similar,  depending  on
your  descriptors.  Close  combat  weapons  are  either
equipment or this power with the Removable flaw. See
the Gadgets & Gear chapter (following) for more infor-
mation.

Sacrifice: When you are hit with an effect requiring a resis-
tance check, you can spend a hero point to shift it to one
of your minions instead. The minion must be within range
of the effect and a viable target. Needless to say, this is not
a particularly heroic ability. In fact, the GM may wish to re-
strict  it  to  villains  or  non-player  characters  (in  which  case
a hero earns a hero point when a villain uses this extra to
avoid an effect by sacrificing a minion). Flat +1 point.

Variable  Type:  Minions  a

[... truncated ...]
```

**Chunk 9** (`80099a87d308`):

```
CHAPTER 7: GADGETS & GEAR

215

A  common  piece  of  equipment  for  crime  fighters  and
espionage agents is the utility belt (or bag, pouch, back-
pack, etc.): a collection of useful tools and equipment in
a compact carrying case. A utility belt is an array of Alter-
nate Equipment. Some characters may have a Removable
array of devices instead, allowing for far more unusual ef-
fects than run-of-the-mill equipment.

Note  that  equipment  with  a  cost  of  1  equipment  point
doesn’t  really  need  to  be  acquired  as  Alternate  Equip-
ment,  since  there’s  no  change  in  cost.  Still,  heroes  often
have 1-point items in their utility belts, like flashlights, re-
breathers, and so forth.

By spending hero points you can temporarily add Alter-
nate  Equipment  to  your  utility  belt,  for  those  one-time
items you may need in a pinch.

Feel  free  to  modify  this  example  (adding  or  omitting
items)  to  create  your  own  customized  utility  belts. The
tear gas, as the most expensive effect, has full cost. The
other items cost 1 point each for Alternate Equipment,
making the total equipment point cost of the utility belt
25  equipment  points,  or  5  power  points  (for  5  ranks  of
the Equipment advantage).

WEAPONS

•

Tear Gas Pellets: Ranged Cloud
Area Affliction 4 (Resisted by
Fortitude; Dazed and Vision
Impaired, Stunned and Vision
Disabled, Incapacitated) • 16 points.

•  Bolos: Ranged Cumulative

Affliction 3 (Resisted by Dodge, Overcome by
Damage; Hindered and   Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree  • 1 point.

•  Boomerangs: Ranged Damage 1, Strength-based

• 1 point.

•

Explosives: Ranged Burst Area Damage 5 • 1 point.

•  Cutting Torch: Damage 1 Linked to Weaken

Toughness 1 • 1 point.

•

Flash-Bangs: Ranged Burst Area Cumulative
Affliction 4 (Resisted and Overcome by Will; Visually
Impaired, Visually Disabled, Visually Unaware),
Limited to Vision  • 1 point.

•  Pepper Spray: see page 217 • 1 point.

•  Power Knuckles: Damage 4, Strength-based • 1 point.

•

•

Sleep Gas Pellets: Ranged Cloud Area Affliction 3
(Resisted and Overcome by Fortitude; Fatigued,
Exhausted, Asleep) • 1 point.

Smoke Pellets: Ranged Cloud Area Visual
Concealment Attack • 1 point.

Weapons of various sorts are common for both heroes and villains. They range from melee weapons to ranged weapons
like guns and bows and devices like shrink-rays, mind-control helmets and more. Characters who don’t have any offen-
sive pow

[... truncated ...]
```

**Chunk 10** (`8757660124bd`):

```
CHAPTER 2: SECRET ORIGINS

83

4-5

6-12

13-14

15-16

17-19

11-15

Induce Blindness: Perception Range

Cumulative Affliction 8 (Resisted and
Overcome by Will; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to one sense • 24 points

Mental Blast: Perception Range Damage

1-5

6, Resisted by Will • 24 points

Mental Illusions: Illusion 6 (All Senses),
Feedback, Resistible by Will, Selective
• 24 points

Mental Paralysis: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Stunned,
Paralyzed) • 24 points

Mind Control: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Compelled,
Controlled) • 24 points

20

Weaken Resolve: Perception Range

Weaken Will 8 • 24 points

Telekinetic: Take Telekinesis, listed immediately

below, then roll on the Telekinetic Table.

Telekinesis: Move Object 10, Accurate 4 • 24 points

Telekinetic Table: Roll 1d20 once and record the result
as the first power in an array, then roll 1d20 three times
and add each result as a 1-point Alternate Effect (re-roll
if you get the same result as your first roll).

1-3

4-7

8-12

Telekinetic Column: Line Area 2 (60

feet) Damage 8 • 24 points

Telekinetic Constructs: Create 8,

Movable • 24 points

Telekinetic Bolt: Ranged Damage 10,

Accurate 4 • 24 points

16-20

13-14

Telekinetic Grab: Ranged Concentration

Affliction 10 (Resisted by Dodge,
Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile),
Accurate 4, Extra Condition, Instant
Recovery, Limited Degree • 24 points

Roll 1d20 once and record the result.

Armored Costume and Combat Training: Protection 4,
Subtle, Removable (-1 point); Enhanced Advantages 8
(Defensive Attack, Defensive Roll 2, Evasion, Improved
Defense, Improved Initiative, Instant Up, Takedown);
Enhanced Defenses 8 (Dodge 4, Parry 4) • 20 points

Precognitive Reactions: Enhanced Advantages 8
(Defensive Roll 4, Evasion 2, Improved Defense,
Improved Initiative); Enhanced Defenses 12 (Dodge
6, Parry 6) • 20 points

Psychokinetic Shield: Protection 10, Impervious 5,

Sustained, Linked to Immunity 10 (Mental effects),
Limited to Half Effect • 20 points

Telekinetic Shield: Impervious Protection 10,

Sustained • 20 points

6-10

11-15

16-20

Roll 1d20 once and record the result.

1-2

Levitation: Flight 2 (8 MPH), Subtle • 5 points

3-6

7-8

Mental Awareness: Senses (Mental Awareness,

Acute, Detect, Radius, Range) • 5 points

Telekinetic Flight: Flight 5 (60 MPH), Distracting •

[... truncated ...]
```

**Chunk 11** (`9575430bef02`):

```
CHAPTER 2: SECRET ORIGINS

43

Power Point Totals:  Abilities 36 + Powers 84  + Advantages 1 + Skills  17 + Defenses 12  = 150

PL10PL10

STRENGTH
12
STAMINA
14

POWERS

AGILITY
1
DEXTERITY
1

FIGHTING
6
INTELLECT
0

AWARENESS
1
PRESENCE
1

Shockwave: Burst Area Damage 10, Limited: Both the

Powerhouse and its targets must be in contact with the ground
• 10 points

•  Groundstrike: Burst Area Affliction 10 (Resisted by Fortitude;
Vulnerable, Defenseless), Instant Recovery, Limited Degree,
Limited: Both the Powerhouse and its targets must be in
contact with the ground • 1 point

Leaping: Leaping 10 • 10 points

Super-Stamina: Enhanced Stamina 10, Immunity 12

(Cold and Heat Damage, Fatigue, Pressure), Impervious
Toughness 12 • 44 points

Super-Strength: Enhanced
Strength 8, plus Enhanced
Strength 4, Limited to
Lifting (Lifting Str16;
1,600 tons) • 20 points

All-out Attack, Power Attack,
 Ultimate Effort (Toughness
checks)

SKILLS

Close  Combat:  Unarmed  2  (+8),  Expertise:  Choose  One  6  (+6),
Insight  5  (+6),  Intimidation  7  (+8),  Perception  5  (+6),  Ranged
Combat: Throwing 7 (+8)

OFFENSE

INITIATIVE +1

Throw +8

Unarmed +8

Ranged, Damage 12

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

14

14

6

6

6

Power Point Totals:  Abilities 36 + Powers 85  + Advantages 3 + Skills  16 + Defenses 10  = 150

44

```

**Chunk 12** (`b511fe78f53a`):

```
CHAPTER 2: SECRET ORIGINS

63

OVERSEER

Contacts, Leadership

UNOBTRUSIVE

Favored Environment (Choose One), Choose One: Evasion or
Improved Initiative

SKILLS

Ranged Combat: (Element) Control 6

Choose One: Acrobatics 4, or Athletics 4, or Close Combat:
Unarmed 4

Choose One: Deception 6 or Intimidation 6

Roll 1d20 once and record the result.

1-5

6-20

Android Host: Enhanced Strength 6, Reduced

Stamina 7 (Stamina —); Enhanced Defenses 8
(Dodge 4, Parry 4); Immunity 20 (upgrades Life
Support to all Fortitude effects); Protection 8
• 34 points

Gaseous Form: Visual Concealment 4, Partial;
Enhanced Advantages 2 (Defensive Roll 2);
Enhanced Defenses 18 (Dodge 9, Parry 9);
Insubstantial 2, Permanent • 34 points

Take the skills listed above, then roll 1d20 once and record
the result. If you rolled Embodiment for Abilities, take Na-
tive instead of rolling on this table.

Flight: Flight 7 (250 MPH) • 14 points

1-5

6-10

Native: You are well versed in or have researched
the properties of your element.

Pilot/Driver: You are proficient in the care and use
of planes or cars.

11-15

Scientist: You are knowledgeable in the sciences.

16-20

Soldier: You are a former military man.

Air Control: Array (24 points plus 2 Alternate Effects)

•  Air Blast: Ranged Damage 12 • 24 points

Take the Air Control Array and Air Blast (above) and roll
1d20  twice  (re-roll  if  you  get  the  same  result  twice)  and
add them to the Air Control array as Alternate Effects.

NATIVE

Expertise: Elements 8, Perception 4

PILOT/DRIVER

Expertise: Repair 4, Vehicles 8

SCIENTIST

Expertise: Science 8, Technology 4

SOLDIER

Athletics 4, Expertise: Military 8

POWERS

1-3

4-6

•  Fog: Environment 12 (Visibility -5; 8 mile radius)

• 1 point

•  Suffocation: Progressive Ranged Affliction 6
(Resisted and Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

7-10

•  Tornado: Cylinder Area Move Object 8,

Concentration Duration, Damaging • 1 point

11-13

•  Wind Binding: Ranged Affliction 12 (Resisted

by Dodge, Overcome by Strength; Hindered and
Vulnerable, Immobile and Defenseless), Extra
Condition, Limited Degree • 1 point

14-17

•  Wind Control: Move Object 12 • 1 point

18-20

•  Wind Screen: Deflect 12, Cylinder Area (×2),
Limited to Attacks Targeting Dodge • 1 point

Elemental Constitution: Immunity 12 (Critical Hits, Life

Support) • 12 points

Earthen Body: Enhanced Strength 8; Impervious Protection

8 • 32 points

Reconstitution: Regeneration 10, Source (El

[... truncated ...]
```

**Chunk 13** (`bc6e8d2fe577`):

```
CHAPTER 2: SECRET ORIGINS

93

Supernatural Resistance: Roll 1d20 three times
(re-roll if you get the same result twice) and record
the results.

1-3

4-6

Immunity 5 (Cold, Heat, Pressure,
Radiation, Vacuum) • 5 points

Immunity 5 (Disease, Poison, Starvation

and Thirst, Suffocation) • 5 points

11-20

7-8

Immunity 5 (Alteration effects) • 5 points

9-10

Immunity 5 (Cold damage) • 5 points

11-12

Immunity 5 (Electricity damage) • 5 points

13-14

Immunity 5 (Emotion effects) • 5 points

15-17

Immunity 5 (Fire damage) • 5 points

18-20

Immunity 5 (Magic damage) • 5 points

Roll 1d20 once and record the result.

1-7

Eyes of Darkness: Senses 2 (Darkvision) • 2 points

8-14

15-20

Spider-Climb: Movement 1 (Wall-crawling)

• 2 points

Vampire Bite: Weaken Stamina 4, Grab-based

• 2 points

WEREWOLF

Thick Skin: Protection 3; Impervious Toughness 9, Lim-
ited—Not versus magical or silver weapons • 9 points

Roll 1d20 once and record the result.

Brother to Wolves: Summon 2 (Wolves and

1-10

Dogs), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Deathly Howl: Auditory Perception Area Affliction
10 (Resisted and Overcome by Will; Dazed and
Impaired, Disabled and Stunned), Extra Condition,
Limited Degree • 20 points

1-4

5-10

Demonic Cape: Flight 6 (120 MPH), Gliding,

11-20

Removable (-1 point) • 5 points

Demonic Movement: Leaping 2 (30 feet); Speed 3

(16 MPH) • 5 points

11-16 Giant Bat Wings: Flight 5 (60 MPH), Wings • 5 points

17-20

Hellrider: Movement 2 (Wall-crawling, Water

Walking), Limited to While Moving; Speed 6 (120
MPH), Activation (standard action, -2 points),
Removable (-1 point) • 5 points

VAMPIRE

Blood Drain: Regeneration 10, Source (Blood) • 5 points

Roll 1d20 once and record the result.

1-5

6-20

Living Vampire: Enhanced Stamina 13; Immunity

4 (aging, disease, need for sleep, poison);
Impervious Toughness 8 • 38 points

Undead Invulnerability: Immunity 30 (Fortitude
effects); Impervious Protection 8, Limited—Not
against blessed or magical weapons • 38 points

Roll 1d20 once and record the result.

1-6

7-12

13-20

Children of the Night: Summon 2 (Bats, Rats, and

Wolves), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Dominate: Perception Ranged Affliction 10 (Resisted

and Overcome by Will; Entranced, Compelled,
Controlled), Visually Sense-Dependent • 20 points

Mist Form: Insubstantial 2, Linked to Flight 5 (60

MPH) • 20 points

Roll 1d20 once and record the result.

[... truncated ...]
```

**Chunk 14** (`db8b2bdf371a`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Energy Blast: Ranged Damage 12

Take the Gimmick Blaster and Energy Blast
(above), plus roll 1d20 three times (re-roll if you
get the same result twice) and add them to the
Gimmick Blaster array as Alternate Effects. Name
each of these Alternate Effects as appropriate for
your character’s gimmick.

1-3

4-5

6-8

9-11

12-14

Create 7, Continuous, Innate

Move Object 12

Ranged Affliction 12 (Resisted and
Overcome by Fortitude; Dazed,
Stunned, Incapacitated)

Ranged Affliction 12 (Resisted by
Dodge, Overcome by Damage;
Vulnerable, Defenseless,
Incapacitated)

Ranged Cloud Area Affliction 8

(Resisted and Overcome by Fortitude;
Dazed and Visually Impaired,
Stunned and Visually Disabled) Extra
Condition, Limited Degree

15-17

Ranged Burst Area Damage 8

18-20

Close Cone Area Damage 8, Penetrating 8

Personal Combat Enhancers: Enhanced Advantage

11 (All-out Attack, Defensive Attack, Evasion,
Extraordinary Effort, Diehard, Fearless, Great
Endurance, Improved Critical (Unarmed),
Improved Initiative, Takedown 2); Enhanced
Strength 3; Enhanced Trait 5 (Close Attack 5);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 points

8-12

13-14

15-16

Physical Boosters: Enhanced Strength 8; Leaping

2 (30 feet); Quickness 2; Speed 2 (8 MPH);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 point

17-20

High-tech Arsenal: Ray Gun (Ranged Damage 12,
AE: Power Truncheon (Strength-based Damage
8), AE: Stunner (Ranged Affliction 12 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated)), AE: Force Capsule Grenade
(Ranged Affliction 12 (Resisted by Dodge,
Overcome by Damage; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree); Easily Removable (-10 points)
• 17 points

Roll 1d20 once and record the result.

1-5

6-10

Combat Training and Armored Costume:
Enhanced Advantage 2 (Defensive Roll 2),
Enhanced Defenses (Dodge 4, Parry 4), Protection
4, Removable (-1 point) • 13 points

Displacer Field: Enhanced Defenses (Dodge 6, Parry
6) Linked to Protection 4, Sustained, Removable
(-3 points) • 13 points

11-15

Energy-Absorbing Body Suit: Protection 10,

Impervious 6, Removable (-3 points) • 13 points

16-20

Force Field: Immunity 6 (Critical Hits, Cold, Heat,

High Pressure, Radiation) Linked to Protection 10,
Sustained, Removable (-3 points) • 13 points

Roll 1d20 once and record the result.

1-4

5-8

9-16

17-20

Biologica

[... truncated ...]
```

**Chunk 15** (`dcdc4c459ab6`):

```
CHAPTER 2: SECRET ORIGINS

61

CRIMINOLOGIST

EXPERT

Assessment, Skill Mastery (Expertise: Streetwise)

Perception 6, Technology 8, Treatment 6

SCIENTIST

INVESTIGATOR

Inventor, Skill Mastery (Technology)

Expertise: Streetwise 4, Insight 5, Investigation 6, Perception 5

SLEUTH

SNEAK

Skill Mastery (Investigation), Tracking

Deception 6, Sleight of Hand 6, Stealth 8

POWERS/EQUIPMENT

Roll 1d20 once and record the result. If you rolled the In-
ventor set of Abilities, take Gadgets instead of rolling.

Roll 1d20 once and record the result.

1-10

Acrobat: You’re a trained acrobat, capable of
incredible feats of agility.

11-15 Martial Artist: You’re a trained fighter.

16-20

Thief: You’re a trained thief, able to disappear with a
moment’s notice.

ACROBAT

Evasion, Instant Up

1-4

ARTIST

Defensive Attack, Uncanny Dodge

THIEF

Hide in Plain Sight, Skill Mastery (Stealth)

SKILLS

Close Combat: Unarmed 6

Take the skill listed above, then if you rolled Dark Aveng-
er  for  your  Abilities,  take  Avenger  and  roll  once,  re-roll
if  you  get  Avenger  again.  If  you  rolled  the  Detective
for  your  Abilities,  take  Investigator  and  roll  once,  re-roll
if  you  get  Investigator  again.  If  you  rolled  Inventor  for
your Abilities, take Expert and roll once, re-roll if you get
Expert again.

1-4

Athlete: You’re physically capable and impressive.

5-8

Avenger: You’ve trained yourself in a number of
useful skills.

5-10

6-10

9-12

Expert: You know a lot about some subjects.

13-16

Investigator: You’ve studied investigation and other
forms of observation.

17-20

Sneak: You’re stealthy.

ATHLETE

Acrobatics 6, Athletics 8, Intimidation 6

AVENGER

Expertise: Streetwise 6, Intimidation 8, Vehicles 6

11-15

16-20

Advantage: Equipment 10 (Equipment listed
immediately below)
Smartphone • 2 points
Headquarters—Size: Medium, Toughness: 8;
Features: Communications, Computer, Concealed,
Garage, Gym, Living Space, Power System, Security
System • 10 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Knife: Strength-based Damage 1, Improved Critical

• 2 points

Customized Heavy Pistol with Laser Sight:
Ranged Damage 4, Accurate 2 • 10 points

Customized Assault Rifle: Ranged Multiattack

Damage 5, Accurate • 16 points

GADGETS

Advantage: Equipment 3 (Headquarters)
Headquarters—Size: Large, Toughness: 10;
Features: Communications, Computer, Concealed,
Fire Prevention System, Gym, Infirmary, Laboratory,
Living Space,

[... truncated ...]
```

**Chunk 16** (`e087f7a0b70b`):

```
CHAPTER 2: SECRET ORIGINS

57

Take  the  Weapon  Array  and  the  Plasma  Blast  (above),
plus roll 1d20 four times on the table below (re-roll if you
get the same result twice) and add them to the Weapon
Array as Alternate Effects.

1-2

•  Electrified Shell: Reaction Damage 6 • 1 point

3-4

5-7

8-9

10-12

13-15

16-18

19-20

•  Electro-Stunner: Ranged Affliction 10 (Resisted
by Dodge and Overcome by Fortitude; Dazed,
Stunned, Incapacitated), Accurate 4 • 1 point

•  Plasma Bolts: Ranged Multiattack Damage 6,

Accurate 6 • 1 point

•  Force Capsule: Ranged Affliction 10 (Resisted

by Dodge and Overcome by Damage; Hindered
and Vulnerable, Defenseless and Immobile), Extra
Condition, Limited Degree, Accurate 4 • 1 point

•  Micro Rockets: Ranged Burst Area Damage 8

• 1 point

•  Omni-Blaster: Cone Area Damage 10,

Penetrating 4 • 1 point

•  Strength and Accuracy Booster: Enhanced
Strength 8; Enhanced Trait 6 (Close Attack 6)
• 1 point

•  Tractor/Presser Beam: Move Object 10,

Accurate 4 • 1 point

Ability Amplifier: Enhanced Defenses 16 (Dodge 4,

Fortitude 4, Parry 4, Will 4), Removable (-3 points) • 13 points

Armored Shell: Impervious Protection 8, Removable (-3

points) • 13 points

Sealed Systems: Immunity 10 (Life Support), Removable (-2

points) • 8 points

Roll 1d20 once and record the result.

1-7

8-10

Gravity Drivers: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

•  Space Flight: Movement 2 (Environment

Adaptation—Zero-G , Space Travel 1) • 1 point

Locomotion Systems: Speed 7 (250 MPH); Leaping
4 (120 feet); Movement 2 (Choose two: Safe Fall,
Swinging, Wall-crawling 1, a second rank of
Wall-crawling), Removable (-3 points) • 12 points

Rocket Turbines: Flight 7 (250 MPH), Removable

(-3 points) • 11 points

11-17

•  Aquatic Turbines: Swimming 8 (120 MPH);

Movement 1 (Environment Adaptation—Aquatic)
• 1 point

18-20

Teleport-Tech: Teleport 3 (250 feet), Easy, Extended
(8 miles), Change Direction, Change Velocity,
Turnabout, Removable (-3 points) • 12 points

Communication Systems: Radio Communication 2,

Removable (-2 points) • 6 points

Sensors: Senses 2 (Extended Vision, Infravision), Removable

(-0 points) • 2 points

DEFENSES

DODGE
+4

PARRY
+2

FORTITUDE
+2

TOUGHNESS
+0

WILL
+4

ABILITIES

POWERS

36

76

10

SKILLS

DEFENSES

TOTAL

16

12

150

•

Identity: The Battlesuit often has a secret identity he
or she tries to protect.

•  Motivation—Responsibility:  Whether  an  inventor
of  military  weapons,  a  trained 

[... truncated ...]
```

**Chunk 17** (`e17d1554782d`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Dense Fog: Visual (All) Concealment 4 Attack, Burst

1-8

Arc Riding: Leaping 10 • 10 points

Weather Control array as Dynamic Alternate Effects (re-
roll if you get the same result twice).

Arctic Freeze: Ranged Cumulative Affliction 10
(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree
• 30 points

Dazzling Strike: Ranged Cumulative Affliction 10

(Resisted and Overcome by Fortitude; Vision and
Auditory Impaired, Vision and Auditory Disabled,
Vision and Auditory Unaware) • 30 points

Area (×3), Selective • 28 points

Downdraft: Ranged Affliction 10 (Resisted and

Overcome by Strength; Hindered and Impaired,
Stunned and Prone, Incapacitated), Alternate
Resistance (Strength), Concentration Duration,
Extra Condition, Instant Recovery • 30 points

Glacier: Create 9, Continuous, Innate, Linked to
Environment 2 (Cold, Impede Movement 1)
• 30 points

Hailstorm: Ranged Cloud Area Damage 9, Indirect 2

(falling from above) • 30 points

Lightning Bolt: Ranged Damage 12, Accurate 3,
Indirect 3 (any point downwards) • 30 points

Stormy Weather: Environment 10 (2 miles; Cold,

Impede Movement, Visibility) • 30 points

Tornado: Cylinder Area Move Object 10,

Concentration Duration, Damaging • 30 points

Wind Screen: Deflect 10, Cylinder Area (×3), Limited

to Attacks Targeting Dodge • 30 points

1-2

3-4

5-6

7-8

9-10

11-12

13-14

15-16

17-18

19-20

Roll 1d20 once and record the result.

1-5

Aquatic: Immunity 3 (Cold, Drowning, Pressure),
Senses 5 (Darkvision, Accurate and Extended
Hearing); Swimming 2 (2 MPH), Stacks with other
Swimming • 10 points

6-10

Cold Immunity: Immunity 10 (Cold effects) • 10 points

11-20

Weather-Proof: Immunity 10 (Weather effects)

• 10 points

Roll 1d20 once and record the result.

1-7

8-14

15-20

Force Field: Impervious Protection 8, Sustained

• 16 points

Vigorous: Enhanced Stamina 3; Enhanced Defenses

10 (Dodge 5, Parry 5), Sustained • 16 points

Wind Shield: Enhanced Defenses 16 (Dodge 8, Parry

8), Sustained • 16 points

Roll 1d20 once and record the result.

Swimming: Movement 1 (Environmental

9-12

Adaptation—Aquatic); Swimming 8 (120 MPH),
Stacks with other Swimming • 10 points

13-20 Wind Riding: Flight 5 (60 MPH) • 10 points

DEFENSE

DODGE
+2

PARRY
+0

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

40

75

7

SKILLS

DEFENSES

TOTAL

16

12

150

•  Moti

[... truncated ...]
```

---

## Concept: Linked

Chunk count: 22
Receives actions: ['act_0402']

### Chunk texts

**Chunk 1** (`068f6ea2c39b`):

```
CHAPTER 6: POWERS

191

•

•

ter of the burst. This immunity does not apply to other
effects, nor does it extend to anyone else: for that, ap-
ply the Selective extra. If the user wants to be affected
at the same time, increase cost per rank by +1. An ex-
ample would be a Close Burst Area Healing effect that
included the user along with everyone else in the area.
This is the equivalent of the +1 Affects Others modifier.

Ranged:  A  ranged  area  effect  can  be  placed  any-
where within the effect’s range, extending to fill the
area’s volume from the origin point.

Perception: A perception area effect can be placed
anywhere  the  user  can  accurately  perceive.  Percep-
tion area effects neither require an attack check nor
allow a Dodge resistance check, although targets still
get a normal resistance check against the effect. Per-
ception  area  effects  are  blocked  by  either  conceal-
ment or cover; choose one when acquiring the effect.
For concealment, if the attacker can’t accurately per-
ceive a target in the area, it is unaffected. Thus even
heavy smoke or darkness can block the effect. Effects
blocked by cover are much like conventional area ef-
fects:  solid  barriers  interfere  with  the  effect,  even  if
they are transparent, but the effect ignores conceal-
ment like darkness, shadows, or smoke. Only targets
behind total cover are unaffected.

Example: Mastermind has a Burst Area Affliction, al-
lowing him to seize control of the minds of everyone
in  the  affected  area.  He  must  be  able  to  accurately
perceive a target to control it; an invisible foe or one
out of his line of sight, for example, would be unaffect-
ed, even if they were within the area of the burst. On
the other hand, targets behind a glass wall or invisible
force field are affected, since Mastermind can perceive
them. Conversely, Fear-Master has a Burst Area Afflic-
tion as well—his fear-inducing gas. Targets behind a
solid barrier (such as on the other side of that glass
wall or invisible shield) are unaffected, but the unseen
or concealed target is, even though Fear-Master can’t
perceive him, since the gas still reaches them.

ATTACK

+0 COST PER RANK

This  extra  applies  to  personal  range  effects,  making
them into attack effects. Examples include Shrinking and
Teleport, causing a target to shrink or teleport away, re-
spectively.  Unlike  most  extras,  the  effect’s  cost  does  not
change, although it does work differently.

The  effect  no  longer  works

[... truncated ...]
```

**Chunk 2** (`0713e58acd4e`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

EXTRAS

NAME

COST

Accurate

1 flat per rank

+2 attack check bonus per rank

Affects Corporeal

1 flat per rank

Effect works on corporeal beings with rank equal to extra rank.

Affects Insubstantial

1-2 flat points

Effect works on insubstantial beings at half (1 rank) or full (2 ranks) effect.

Affects Objects

+0-1 per rank

Fortitude resisted effect works on objects.

Affects Others

+0-1 per rank

Personal effect works on others.

Alternate Effect

1-2 flat points

Substitute one effect for another in a power.

Alternate Resistance

+0-1 per rank

Effect uses a different resistance.

Area

Attack

Contagious

+1 per rank

+0 per rank

+1 per rank

Effect works on an area.

Personal effect works on others as an attack.

Effect works on anyone coming into contact with its target.

Dimensional

1-3 flat points

Effect works on targets in other dimensions.

Extended Range

1 flat per rank

Doubles ranged effect’s distances per rank.

Feature

Homing

1 flat per rank

1 flat per rank

Adds a minor capability or benefit to an effect.

Attack effect gains additional chances to hit.

Impervious

+1 per rank

Resistance ignores effects with difficulty modifier of half extra rank or less.

Increased Duration

+1 per rank

Improves effect’s duration.

Increased Mass

1 flat per rank

Effect can carry a greater amount of mass.

Increased Range

+1 per rank

Improves effect’s range.

Incurable

Indirect

Innate

Insidious

Linked

Multiattack

Penetrating

Precise

Reach

Reaction

Reversible

Ricochet

1 flat point

Effect cannot be countered or removed using Healing or Regeneration.

1 flat per rank

Effect can originate from a point other than the user.

1 flat point

1 flat point

0 flat points

+1 per rank

1 flat per rank

1 flat point

1 flat per rank

+1 or 3 per rank

1 flat point

1 flat per rank

Effect cannot be Nullified.

Result of the effect is more difficult to detect.

Two or more effects work together as one.

Effect can hit multiple targets or a single target multiple times.

Effect overcomes Impervious Resistance.

Effect can perform delicate and precise tasks.

Extend effect’s reach by 5 feet per rank.

Changes effect’s required action to reaction.

Effect can be removed at will as a free action.

Attacker can bounce effect to change direction.

Secondary Effect

+1 per rank

Instant effect works on the target twice.

Selective

Sleep

Split

Subtle

Sustained

Triggered

+1 per rank



[... truncated ...]
```

**Chunk 3** (`1094aa03eba1`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

Example:  Captain  Thunder  has  the  ability  to  hurl
thunderbolts  that  shock  their  targets  with  electric-
ity and deafen them with powerful claps of thunder.
This  is  a  Ranged  Damage  effect  (lightning),  cost-
ing 2 points per rank, Linked to a Ranged Affliction
(deafening thunder), costing 2 points per rank. The
combined effect costs 4 points per rank.Since both
effects  are  ranged  and  require  a  standard  action
to use, so does the combined effect. Since Damage
requires a Toughness check and Affliction requires a
Dodge check, the target checks against them sepa-
rately, making a Toughness resistance check against
the damage of the lightning and a Dodge check to
avoid being deafened by the thunder. Since the two
effects are Linked, Captain Thunder cannot throw a
lightning  bolt  without  the  deafening  thunderclap,
nor can he attempt to merely deafen a target with-
out  also  hitting  them  with  lightning!  (To  do  these
things,  Cap  might  take  the  stand-alone  effects  as
Alternate Effects.)

+1 COST PER RANK

A Multiattack effect allows you to hit multiple targets, or a
single target multiple times, in the same standard action.
Multiattack  can  apply  to  any  effect  requiring  an  attack
check. There are three ways in which a Multiattack effect
can be used:

To  use  a  Multiattack  against  a  single  target,  make  your
attack check normally. If successful, increase the attack’s
resistance check DC by +2 for two degrees of success, and
+5  for  three  or  more. This  circumstance  bonus  does  not
count against power level limits.

If  an  Impervious  Resistance  would  ignore  the  attack  be-
fore any increase in the DC, then the attack still has no ef-
fect as usual; a volley of multiple shots is no more likely to
penetrate Impervious Resistance than just one.

You can use Multiattack to hit multiple targets at once by
“walking” or “spraying” the Multiattack across an arc. Roll
one  attack  check  per  target  in  the  arc. You  suffer  a  pen-
alty to each check equal to the total number of targets. So
making a Multiattack against five targets is a –5 penalty
to each attack check. If you miss one target, you may still
attempt to hit the others.

by  your  covering  attack  at  the  cost  of  being  automati-
cally  attacked  by  it;  make  a  normal  attack  check  to  hit
that opponent.

FLAT • 1 POINT PER RANK

Your effect overcomes Impervious Resistance to a deg

[... truncated ...]
```

**Chunk 4** (`25d04efd242a`):

```
CHAPTER 6: POWERS

187

ply to at least one rank, and may apply to as many ranks as
the effect has. The change in cost and effect applies only
to the ranks with the modifier; the unmodified ranks have
their normal cost and effect.

Example:  Caliber’s  micro-rockets  are  a  Damage  7
effect. They also explode on impact, for a Burst Area
Damage  effect,  but  the  Area  Damage  is  only  rank
4. So the first 4 ranks of the Caliber’s Damage effect
have the Burst Area modifier, costing 1 point more (or
3 per rank). The remaining 3 ranks have their usual
cost (2 per rank). Caliber makes a normal ranged at-
tack check against the main target for his micro-rock-
et launcher; if he hits, the target has to resist Damage
7, and everyone within the area around the target re-
sists Damage 4 (the Area Damage). Even if he misses,
the main target has to resist the Area Damage 4, since
the micro-rocket explodes close by! In Caliber’s busi-
ness, it pays to cover your bases...

MODIFIERS

Some modifiers, rather than increasing or decreasing an ef-
fect’s cost per rank, have a flat value in power points, noted
as flat in the modifier’s header. For example, the Subtle extra
costs only 1 or 2 points, depending on how subtle the effect
is. Likewise, the Activation flaw has a flat value of –1 or –2
points, depending on how long the power takes to activate.

Flat-value modifiers are applied to the final cost of an effect,
after its cost per rank and total cost for its number of ranks
is determined. So, for example, if an effect costs 2 points per
rank, with +1 per rank for extras and –2 per rank for flaws.
It has a final adjusted cost of (2 + 1 – 2) or 1 point per rank.
With 8 ranks, it costs 8 power points. If the same effect also
has a flat-value extra costing 2 points and a flat-value flaw
worth –1 point, then you add 2 to the final cost and sub-
tract 1, for a total of (8 points for the effect + 2 points for the
flat extra – 1 point for the flat flaw) or 9 power points.
modified cost + flat extra value -
flat flaw value

tion). When  an  effect  is  used  against  a  corporeal  target,
the effect’s rank is equal to the rank of this extra, up to a
maximum of the effect’s full rank. Characters with lower
ranks  1–3  of  Insubstantial  do  not  require  this  extra  for
their effects to work on the physical world, although they
can apply it to their Strength rank to allow them to exert
some Strength while Insubstantial.

FLAT • 1 OR 2 POINTS

An  effect  with  this  extra  wo

[... truncated ...]
```

**Chunk 5** (`267bbd73af09`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

INNOCENT

Animal Empathy, Luck

INCISIVE

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

SUBTLE

Evasion, Hide in Plain Sight

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-3

Dynamic: You are a good all-around athlete.

4-7

Empathic: You understand what makes other
people tick.

8-10

Furtive: You don’t like to stand out.

11-14

Inscrutable: Your emotions are difficult to read.

15-18 Observant: Little escapes your notice.

19-20

Sponge: You possess an open and receptive mind.

DYNAMIC

Acrobatics 6, Athletics 6

EMPATHIC

Insight 8, Persuasion 4

FURTIVE

Deception 6, Stealth 6

INSCRUTABLE

Deception 8, Perception 4

OBSERVANT

Insight 6, Perception 6

SPONGE

Expertise: Current Events 4, Expertise: Popular Culture 4,
Investigation 4

POWERS

Roll 1d20 once and record the result.

1-2

Animal Mimicry: Variable 10 (50 points, to mimic
Traits of one animal at a time), Continuous
• 80 points

Mental Duplication: Mind Reading 10, Limited
to Duplicated mind; Variable 10 (50 points, for
duplicating a subject’s mental traits), Continuous,
Resistible by Will • 80 points

Nemesis: Variable 8 (40 points, for traits suitable for
confronting a particular opponent), Continuous,
Free Action • 80 points

Object Mimicry: Variable 8 (40 points, for traits of

object touched), Reaction • 80 points

3-4

5-6

7-9

10-13

Power Duplication: Variable 10 (50 points, for

duplicating one target’s powers), Continuous
• 80 points

14-15

Power Theft: Cumulative Affliction 12 (Resisted

and Overcome by Will; Powers Impaired, Powers
Disabled, Transformed—Powerless) Linked to
Variable 8 (40 points, for duplicating one target’s
powers), Move Action, Limited to Afflicted
subjects • 80 points

16-17

Reflex Memory: Variable 8 (40 points, for observed
Skills and Advantages), Continuous, Free Action
• 80 points

18-20

Android Body: Immunity 30 (Fortitude Effects),
Reduced Traits (Stamina —, Fortitude —);
Protection 5 • 16 points

Power Duplication: Variable 8 (40 points, for

duplicating a target’s powers), Continuous • 64 points

DEFENSES

DODGE
+5

PARRY
+5

FORTITUDE
+5

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

32

80

6

SKILLS

DEFENSES

TOTAL

12

20

150

•  Motivation—Acceptance: Due to the nature of their
powers, many Mimics feel as if they lack an identity of
their own. They may seek acceptance as unique indi-
v

[... truncated ...]
```

**Chunk 6** (`301534069c2d`):

```
CHAPTER 2: SECRET ORIGINS

99

5-8

Cybernetic Implants: Enhanced Awareness

2; Enhanced Advantages 2 (Eidetic Memory,
Improved Initiative); Enhanced Defenses 4 (Parry
2, Dodge 2); Senses 6 (Accurate and Extended
Hearing, Analytical and Extended Vision,
Infravision) • 16 points

9-15

Healing Factor: Enhanced Stamina 2; Immunity 2
(disease, poison); Regeneration 10 • 16 points

16-20

Tactical Mastermind: Enhanced Intellect 2,

Enhanced Awareness 2; Enhanced Advantages
3 (Defensive Roll 2, Uncanny Dodge); Senses
5 (Danger Sense, Detect Weakness—Acute,
Analytical, Ranged) • 16 points

OTHERWORLDLY

Roll 1d20 once and record the result.

1-4

5-6

7-11

12-17

18-20

Alien: Enhanced Stamina 2; Immunity 7 (Cold, Heat,
Pressure, Radiation, Suffocation, Vacuum); Mental
Communication 1; Senses 1 (Mental Awareness)
• 16 points

Aquatic: Enhanced Stamina 2; Immunity 3 (Cold,

Drowning, Pressure); Movement 1 (Environmental
Adaptation—Aquatic); Senses 1 (Low-light Vision);
Swimming 6 (30 MPH) • 16 points

Exemplar: Enhanced Stamina 1, Enhanced

Awareness 1, Enhanced Defenses 2 (Dodge 1,
Parry 1); Immunity 2 (Aging, Disease); Quickness 4;
Speed 4 (30 MPH) • 16 points

Immortal: Enhanced Awareness 2; Immortality
5, Limited (choose effect); Immunity 3 (Aging,
Disease, Poison); Protection 2; Regeneration 2
• 16 points

Winged: Enhanced Awareness 2, Enhanced

Defenses 4 (Dodge 2, Parry 2); Flight 6 (120 MPH),
Wings; Immunity 1 (Cold); Senses 1 (Extended
Vision) • 16 points

HUMAN

Roll 1d20 once and record the result.

11-20

Unique Weapon: Strength-based Damage 3,

Accurate, Penetrating 10 plus roll 1d20 once:

1-5

6-10

Atom Slicer: Weaken Toughness 10,

Penetrating 2, Linked to Damage, Easily
Removable (-10 points) • 16 points

Boom Staff: Movement 3 (Space Travel

3), Portal; Easily Removable (-10
points) • 16  points

11-15

Dimension Cutter: Movement 3

(Dimension Travel 3), Portal; Easily
Removable (-10 points) • 16 points

16-20

Thundering Mallet: Cumulative
Affliction 10 (Resisted and
Overcome by Fortitude; Vulnerable,
Defenseless), Limited Degree, Linked
to Damage, Penetrating 2; Easily
Removable (-10 points) • 16 points

DEFENSE

DODGE
+4

PARRY
+2

ABILITIES

POWERS

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

78

32

9

SKILLS

DEFENSES

TOTAL

17

14

150

•  Motivation—Patriotism:  Duty  to  country  may  have
motivated the warrior to have undergone experiments
that transformed him or to visit the world outside his
home.

•  Motivation—Responsibility:  The  war

[... truncated ...]
```

**Chunk 7** (`43d5c758bf78`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WASP

Insect Senses: Senses 4 (Acute Smell, Darkvision,

Ranged Touch) • 4 points

16-20

Sting: Cumulative Affliction 8 (Resisted and Overcome
by Fortitude; Impaired, Disabled, Incapacitated),
Linked to Damage 8, Accurate 2 • 26 points

Roll 1d20 once and record the result.

CANINE

Bite: Strength-based Damage 3, Improved Critical,

Wings: Flight 6 (120 MPH), Wings • 6 points

Penetrating 3 • 7 points

Canine Senses: Senses 3 (Low-light Vision, Acute

and Tracking Olfactory) • 3 points

1-10

Canine Movement: Leaping 2 (30 feet); Speed 4 (30

Talons: Strength-based Damage 1, Accurate 2, Fast Grab

MPH) • 6 points

• 4 points

Roll 1d20 once and record the result.

FALCON

Flight: Flight 6 (120 MPH), Wings • 6 points

Keen Eyesight: Senses 3 (Extended 2 and Rapid

Vision) • 3 points

1-10

Sonic Scream: Cone Area Affliction 9 (Resisted

and Overcome by Fortitude; Dazed and Auditory
Impaired, Stunned and Auditory Disabled,
Incapacitated and Auditory Unaware), Extra
Condition, Quirk—Impaired, Disabled, Unaware
Limited to One Sense (-4 points) • 23 points

11-20

OWL

Nightvision: Senses 2 (Extended Vision, Low-light

Vision) • 2 points

11-20

Shriek: Cone Area Affliction 8 (Resisted and
Overcome by Will; Dazed and Vulnerable,
Stunned and Defenseless, Incapacitated)
• 24 points

Silent Flight: Flight 5 (60 MPH), Subtle, Wings • 6 points

Howl: Auditory Perception Area Affliction

10 (Resisted and Overcome by Will; Dazed
and Impaired, Disabled and Stunned), Extra
Condition, Limited Degree • 20 points

FELINE

Claws: Strength-based Damage 1, Accurate,

Improved Critical • 3 points

Feline Senses: Senses 3 (Low-light Vision, Acute and

Tracking Olfactory) • 3 points

Feline Movement: Leaping 3 (60 feet); Movement
3 (Safe Fall, Sure-footed, Trackless); Movement
1 (Water-walking), Limited to Solid Surfaces;
Movement 1 (Wall-crawling), Limited to One
Move Action; Speed 4 (30 MPH) • 15 points

Plus roll 1d20 once and record the result.

1-5

Black Cat: Reaction Visual Perception

Area Affliction 5 (Resisted by Dodge,
Overcome by Will; Vulnerable,
Defenseless, Incapacitated), Side-
effect (Always happens, chosen by
player) • 15 points

```

**Chunk 8** (`44f0396c2518`):

```
CHAPTER 6: POWERS

163

Insight  check.  Senses  with  the  Counters  Illusion  effect
(see Senses) automatically detect illusions. If any viewer
successfully uncovers an illusion and communicates this
fact to others, they gain another Insight check with a +5
circumstance bonus. Circumstances may grant additional
modifiers to the Insight check to uncover an illusion, de-
pending on how convincing it is.

Maintaining an active illusion (such as a fighting creature)
requires a standard action each round, but maintaining a
static illusion (one that doesn’t move or interact) is only a
free action.

EXTRAS

Illusion is a broad-ranging effect, usable for a number of
different things. A few common considerations for Illu-
sion include the following.

Independent: Your active illusions only require a free action
to maintain, rather than a standard action. +1 cost per rank.

Selective:  You  choose  who  perceives  your  Illusion  and
who doesn’t. +1 cost per rank.

For illusions so realistic they are capable of inflicting dam-
age, add a Linked Perception Range Damage effect. At the
GM’s discretion, this effect can even be made into a Linked
Array  with  a  variety  of  alternate  attack  effects,  allowing
your illusionist to inflict conditions other than damage on
targets. Keep in mind the attack effects all need to be per-
ception range to match the range of Illusion.

Illusion  can  alter  a  subject’s  appearance,  providing  an
essentially impenetrable disguise—at least until some-
one  makes  a  successful  check  to  see  through  the  illu-
sion.  However,  for  just  the  ability  to  alter  appearance,
use the Morph effect, which is generally more effective
than Illusion Limited to Appearance.

The  default  Illusion  effect  is  perceptible  to  anyone  or
anything  (including  machines)  as  if  it  were  real.  Some
illusions exist solely in the mind, like projected psychic
hallucinations. This type of Illusion has the Resistible by
Will flaw and the Selective extra, since the illusionist can
choose whether or not to project the illusion into a par-
ticular subject’s mind, and therefore decides who can or
cannot perceive the illusion. This is a net +0 modifier, for
the same base cost.
MY ALLY, MY ENEMY

A common Illusion trick is to switch the appearances of
an  enemy  and  an  ally,  causing  a  foe’s  teammate  to  at-
tack  that  enemy  by  mistake. You  can  generally  handle
this with an opposed check of Illusion and Insight; if you
win, the tar

[... truncated ...]
```

**Chunk 9** (`634190f2dd84`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

PSYCHIC
PSYCHIC

STRENGTH
0
STAMINA
0

POWERS

AGILITY
1
DEXTERITY
2

FIGHTING
2
INTELLECT
2

AWARENESS
6
PRESENCE
3

Mental Awareness: Senses 2 (Mental Sense,

Radius) • 2 points.

Telekinesis: Move Object 8, Accurate 4 • 20 points.

Telekinetic Field: Protection 12, Impervious,

Sustained • 24 points.

Telekinetic Levitation: Flight 5 (60 MPH) • 10 points.

Telepathy: Mind Reading 5 Linked to Area
Mental Communication 2 • 20 points.

•  Telepathic Illusion: Illusion 4 (all senses),

Resisted by Will, Selective • 1 point.

•  Mental Blast: Perception Range Damage 5,

Resisted by Will • 1 point.

OPTIONS

To customize, you may choose the following option
with no change in point total:

•  Mind Control: Replace the Telepathic Illusion Alternate

Effect with Affliction 5 (Resisted by Will; Dazed, Compelled,
Controlled), Cumulative, Perception Range.

Ultimate Effort (Will defense)

SKILLS

Expertise: (Choose One) 6 (+8), Insight 6 (+12),
Perception 4 (+10), Persuasion 8 (+11)

OFFENSE

Mental Blast —

Telekinesis +10

Unarmed +2

DEFENSE

DODGE

PARRY

WILL

INITIATIVE +1

Perception Range, Damage 5,
Resisted by Will (DC 20)

Ranged, Str 8 Grab

Close, Damage 0

FORTITUDE

TOUGHNESS

6

12

8

8

14

```

**Chunk 10** (`80099a87d308`):

```
CHAPTER 7: GADGETS & GEAR

215

A  common  piece  of  equipment  for  crime  fighters  and
espionage agents is the utility belt (or bag, pouch, back-
pack, etc.): a collection of useful tools and equipment in
a compact carrying case. A utility belt is an array of Alter-
nate Equipment. Some characters may have a Removable
array of devices instead, allowing for far more unusual ef-
fects than run-of-the-mill equipment.

Note  that  equipment  with  a  cost  of  1  equipment  point
doesn’t  really  need  to  be  acquired  as  Alternate  Equip-
ment,  since  there’s  no  change  in  cost.  Still,  heroes  often
have 1-point items in their utility belts, like flashlights, re-
breathers, and so forth.

By spending hero points you can temporarily add Alter-
nate  Equipment  to  your  utility  belt,  for  those  one-time
items you may need in a pinch.

Feel  free  to  modify  this  example  (adding  or  omitting
items)  to  create  your  own  customized  utility  belts. The
tear gas, as the most expensive effect, has full cost. The
other items cost 1 point each for Alternate Equipment,
making the total equipment point cost of the utility belt
25  equipment  points,  or  5  power  points  (for  5  ranks  of
the Equipment advantage).

WEAPONS

•

Tear Gas Pellets: Ranged Cloud
Area Affliction 4 (Resisted by
Fortitude; Dazed and Vision
Impaired, Stunned and Vision
Disabled, Incapacitated) • 16 points.

•  Bolos: Ranged Cumulative

Affliction 3 (Resisted by Dodge, Overcome by
Damage; Hindered and   Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree  • 1 point.

•  Boomerangs: Ranged Damage 1, Strength-based

• 1 point.

•

Explosives: Ranged Burst Area Damage 5 • 1 point.

•  Cutting Torch: Damage 1 Linked to Weaken

Toughness 1 • 1 point.

•

Flash-Bangs: Ranged Burst Area Cumulative
Affliction 4 (Resisted and Overcome by Will; Visually
Impaired, Visually Disabled, Visually Unaware),
Limited to Vision  • 1 point.

•  Pepper Spray: see page 217 • 1 point.

•  Power Knuckles: Damage 4, Strength-based • 1 point.

•

•

Sleep Gas Pellets: Ranged Cloud Area Affliction 3
(Resisted and Overcome by Fortitude; Fatigued,
Exhausted, Asleep) • 1 point.

Smoke Pellets: Ranged Cloud Area Visual
Concealment Attack • 1 point.

Weapons of various sorts are common for both heroes and villains. They range from melee weapons to ranged weapons
like guns and bows and devices like shrink-rays, mind-control helmets and more. Characters who don’t have any offen-
sive pow

[... truncated ...]
```

**Chunk 11** (`800b98bbc634`):

```
CHAPTER 8: ACTION & ADVENTURE

237

less than ideal conditions. This section details some of the
hazards heroes may face.

FALLING

Criminals  often  lurk  in  the  darkness,  and  many  crimes
take  place  at  night.  Most  cities  are  lit  well  enough,  but
sometimes  heroes  run  into  areas  where  it’s  difficult  to
see. Poorly lit areas provide concealment. Characters with
Counters Concealment (Darkness) Senses or other appro-
priate Senses effects can ignore concealment penalties for
poor lighting.

Intense  heat  and  cold  wear  down  characters,  while  pro-
longed exposure to the elements can be extremely dan-
gerous.

Characters in hot or cold conditions must make Fortitude
checks (DC 10, +1 per previous check) to avoid becoming
fatigued.  Fatigued  characters  who  fail  a  check  become
exhausted, then incapacitated, at which point the charac-
ter’s condition becomes dying after another failed Forti-
tude check.

How  often  characters  have  to  make  Fortitude  checks  de-
pends on the conditions. Once an hour for uncomfortable
heat or cold (a hot summer day or cold winter day), once
per 10 minutes for intense heat or cold (a blazing desert or
arctic conditions), once a minute for extreme heat or cold
like the edge of a volcano or an arctic winter storm. Checks
are made at the end of each period of exposure. Truly in-
tense heat or cold—such as a blast furnace or touching liq-
uid nitrogen—inflicts direct damage like an attack.

Characters with the appropriate Immunity do not need to
make Fortitude checks for extreme temperatures.

Heroes  can  go  without  water  for  a  day.  After  this,  they
need to make a Fortitude check (DC 10, +1 per previous
check) each hour to avoid a level of fatigue. Heroes can go
without food for three days. After this, they must make a
Fortitude check (DC 10, +1 per previous check) each day
to  avoid  fatigue.  The  character  cannot  recover  until  he
gets  water  or  food.  Heroes  with  Immunity  to  Starvation
can go an unlimited time without food or water.

Characters can hold their breath for ten rounds (one min-
ute) plus a number of rounds equal to twice their Stamina.
After that time they must make a Fortitude check (DC 10)
each round to continue holding their breath. The DC in-
creases  by  +1  for  each  previous  success.  Failure  on  the
Fortitude  check  means  the  character  becomes  incapaci-
tated . On the following round the character is dying. A dy-
ing character cannot stabilize until

[... truncated ...]
```

**Chunk 12** (`8757660124bd`):

```
CHAPTER 2: SECRET ORIGINS

83

4-5

6-12

13-14

15-16

17-19

11-15

Induce Blindness: Perception Range

Cumulative Affliction 8 (Resisted and
Overcome by Will; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to one sense • 24 points

Mental Blast: Perception Range Damage

1-5

6, Resisted by Will • 24 points

Mental Illusions: Illusion 6 (All Senses),
Feedback, Resistible by Will, Selective
• 24 points

Mental Paralysis: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Stunned,
Paralyzed) • 24 points

Mind Control: Perception Range

Cumulative Affliction 6 (Resisted and
Overcome by Will; Dazed, Compelled,
Controlled) • 24 points

20

Weaken Resolve: Perception Range

Weaken Will 8 • 24 points

Telekinetic: Take Telekinesis, listed immediately

below, then roll on the Telekinetic Table.

Telekinesis: Move Object 10, Accurate 4 • 24 points

Telekinetic Table: Roll 1d20 once and record the result
as the first power in an array, then roll 1d20 three times
and add each result as a 1-point Alternate Effect (re-roll
if you get the same result as your first roll).

1-3

4-7

8-12

Telekinetic Column: Line Area 2 (60

feet) Damage 8 • 24 points

Telekinetic Constructs: Create 8,

Movable • 24 points

Telekinetic Bolt: Ranged Damage 10,

Accurate 4 • 24 points

16-20

13-14

Telekinetic Grab: Ranged Concentration

Affliction 10 (Resisted by Dodge,
Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobile),
Accurate 4, Extra Condition, Instant
Recovery, Limited Degree • 24 points

Roll 1d20 once and record the result.

Armored Costume and Combat Training: Protection 4,
Subtle, Removable (-1 point); Enhanced Advantages 8
(Defensive Attack, Defensive Roll 2, Evasion, Improved
Defense, Improved Initiative, Instant Up, Takedown);
Enhanced Defenses 8 (Dodge 4, Parry 4) • 20 points

Precognitive Reactions: Enhanced Advantages 8
(Defensive Roll 4, Evasion 2, Improved Defense,
Improved Initiative); Enhanced Defenses 12 (Dodge
6, Parry 6) • 20 points

Psychokinetic Shield: Protection 10, Impervious 5,

Sustained, Linked to Immunity 10 (Mental effects),
Limited to Half Effect • 20 points

Telekinetic Shield: Impervious Protection 10,

Sustained • 20 points

6-10

11-15

16-20

Roll 1d20 once and record the result.

1-2

Levitation: Flight 2 (8 MPH), Subtle • 5 points

3-6

7-8

Mental Awareness: Senses (Mental Awareness,

Acute, Detect, Radius, Range) • 5 points

Telekinetic Flight: Flight 5 (60 MPH), Distracting •

[... truncated ...]
```

**Chunk 13** (`885a404994e2`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

sponse to a particular danger, after a set amount of time,
in  response  to  a  particular  event,  and  so  forth—chosen
when  you  apply  the  modifier.  Once  chosen,  the  trigger
cannot be changed.

The  circumstances  must  be  detectable  by  your  senses.
You can acquire Senses Limited and Linked to Triggered
effects, if desired. Setting the effect requires the same ac-
tion as using it normally.

A Triggered  effect  lying  in  wait  may  be  detected  with  a
Perception check (DC 10 + effect rank) and in some cases
disarmed with a successful skill or power check (such as
Sleight  of  Hand, Technology,  Nullify  or  another  counter-
ing effect) with a DC of (10 + effect rank).

A  Triggered  effect  is  good  for  one  use  per  rank  in  this
modifier. After its last activation, it stops working.

You  can  apply  an  additional  rank  of Triggered  to  have  a
Variable Trigger, allowing you to change the effect’s trig-
ger each time you set it.

FLAT • 1-2 POINTS

You can change the descriptors of an effect with this modi-
fier, varying them as a free action once per round. With rank
1, you can apply any of a closely related group of descrip-
tors,  such  as  weather,  electromagnetic,  temperature,  and
so forth. With rank 2, you can apply any of a broad group,
such  as  any  mental,  magical,  or  technological  descriptor.
The GM decides if a given descriptor is appropriate in con-
junction with a particular effect and this modifier.

FLAWS

The  following  section  lists  available  flaws,  starting  with
the flaw’s name and the amount it reduces effect cost (in
power points per rank or flat value), along with a descrip-
tion of how the flaw modifies effects in game terms.

A flat-value flaw cannot have more ranks than the effect
itself.

FLAT • -1 OR -2 POINTS

A  power  with  this  flaw  requires  an  action  to  prepare  or
activate before any of its effects are usable. If the power
requires a move action to activate, the flaw is –1 point. If
it requires a standard action, it is –2 points. Activation tak-
ing  less  than  a  move  action  is  not  a  flaw,  although  may
qualify as a complication (see the Power Loss complica-
tion for details).

Activation has no effect other than making all of the pow-
er’s  effects  available  for  use. The  effects  themselves  still
require their normal actions to use. You can use a power’s
effects in the same turn as you activate it, provided y

[... truncated ...]
```

**Chunk 14** (`997bf2eca013`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PLAYER

Interpose

TOUGH

Ultimate Effort (Toughness checks)

QUICK

Improved Initiative

SKILLS

Close Combat: Unarmed 2

Take  the  skill  listed  above,  then  roll  1d20  twice  (re-roll  if
you get the same result twice) and record the results.

1-4

5-8

Athlete: You’re a trained athlete.

Ex-Military: You used to be in the armed forces.

9-12

Charmer: You have a way with people.

13-16

Rough Upbringing: You were raised on the streets
or have had a hard life.

17-20

Sharp Mind: You’re difficult to fool.

ATHLETE

Athletics 4, Perception 4, Ranged Combat: Throwing 4

Roll  1d20  once  and  record  the  result  as  the  first  power
in  an  array,  then  roll  1d20  once  and  add  the  result  as  a
1-point Alternate Effect (re-roll if you get the same result
as your first roll).

1-3

4-6

7-9

Energy Blast: Ranged Damage 10, Accurate 5,

Distracting, Tiring • 10 points

Foot Stomp: Line Area Damage 10, Powerhouse and
target must be in contact with the same surface
• 10 points

Groundstrike: Burst Area Affliction 10 (Resisted

and Overcome by Fortitude; Dazed and Hindered,
Stunned and Prone, Incapacitated), Extra
Condition, Instant Recovery, Powerhouse and
target must be in contact with the same surface
• 10 points

10-12

13-14

Shockwave: Burst Area Damage 10, Powerhouse
and targets must be in contact with the same
surface • 10 points

Super-Breath: Close Range Cone Area Move Object
5, Limited to moving toward and away, Linked
to Cone Area Damage 5, Unreliable (only the
Damage is Unreliable) • 10 points

15-17

Cut Loose!: Penetrating 10 on Strength • 10 points

18-20

Thunderclap: Cone Area Affliction 10 (Resisted and
Overcome by Fortitude; Dazed, Stunned), Limited
Degree • 10 points

EX-MILITARY

Expertise: Military 4, Perception 4, Ranged Combat: Throwing 4

CHARMER

Deception 4, Insight 4, Persuasion 4

UPBRINGING

Only if you rolled Solid Form or Super-Strength on the
Offensive  Powers  table,  take  Super-Stamina,  directly
below, then roll on the table below, as directed. Do not
take Super-Stamina if you rolled Density or Growth on
the  Offensive  Powers  table,  instead,  roll  on  the  table
below.

Expertise: Streetwise 4, Intimidation 6, Perception 2

Super-Stamina: Enhanced Stamina 10 • 20 points

MIND

Expertise: (Choose One) 4, Insight 4, Perception 4

POWERS

Roll 1d20 once and record the result.

Roll  1d20  four  times  (re-roll  if  you  get  the  s

[... truncated ...]
```

**Chunk 15** (`aa943c38ef67`):

```
CHAPTER 2: SECRET ORIGINS

89

d20 once on that table to determine if your base form and
duplicates are Energy Controllers, Martial Artists, or Pow-
erhouses. Your base form has the same abilities, powers,
advantages, skills, defenses, and totals as the summoned
characters, but with the addition of the Summon Twin or
Summon Triplets power.

Summon Twin: Summon 8 (One PL8, 120 point
duplicate), Heroic, Mental Link • 33 points

PL 8

STR
STA

1  AGL
2  DEX

2
4

FGT
INT

1  AWE
PRE
0

2
2

Powers: Energy Control (Array (16 points),
Energy Blast (Ranged Damage 8), AE: Energy
Explosion (Ranged Burst Area Damage
5), AE: Energy Bolts (Ranged Multiattack
Damage 5), AE: Dazzle (Cumulative Ranged
Affliction 8 (Resisted by Dodge and Overcome
by Fortitude; Impaired, Disabled, Unaware),
Limited to Vision); Energy Field (Sustained
Protection 6 Linked to Reaction Damage 2,
Precise); Energy Flight (Flight 6 (120 MPH));
Energy Immunity (Immunity 1 (Immune
to own powers)); Transform (Quick Change
(Feature 1, change into costume as a free
action))

Advantages: Accurate Attack, Power Attack,
Set-up, Teamwork

Skills: Acrobatics 4 (+8), Athletics 4 (+5),
Expertise (Choose One) 4 (+4), Perception 4
(+6), Ranged Combat: Energy Control 4 (+8)

Offense: Init +4, Energy Blast +8 (Ranged,
Damage 8 or other effects), Unarmed +1
(Close, Damage 1)

Defense: Dodge 8, Parry 8, Fort 8, Tou 8,
Will 8

1-6

1-10

Totals: Abilities 32 + Powers 50 + Advantages 2
+ Skills 10 + Defenses 23 = 117

1-6

Note: Roll on the Energy Controller
archetype’s Energy Descriptors table to
determine the type of energy you control.

PL 8

11-20

7-13

STR
STA

1  AGL
4  DEX

5
5

FGT
INT

10  AWE
PRE

1

2
0

Equipment: Smartphone, Flashlight,
Motorcycle, Restraints, Swingline (Movement
1 (Swinging)), Tonfa (Strength-based Damage
2, Reach 1), AE: Throwing Disks (Ranged,
Strength-based Damage 1)

Advantages: Chokehold, Daze (Deception),
Defensive Roll 2, Equipment 4, Evasion,
Improved Initiative, Instant Up, Power Attack,
Quick Draw, Set-up, Teamwork

Skills: Acrobatics 7 (+12), Athletics 6 (+10),
Deception 8 (+8), Expertise (Choose One)
7 (+8), Perception 6 (+8), Ranged Combat
(Throwing Disks) 5 (+10), Stealth 7 (+12),
Vehicles 4 (+9)

Offense: Init +9, Throwing Disks +10 (Ranged,
Damage 5), Tonfa +10 (Close, Damage 6),
Unarmed +10 (Close, Damage 4)

Defense: Dodge 10, Parry 10, Fort 8, Tou 6/4,
Will 8

Totals: Abilities 62 + Powers 0 + Advantages 15
+ Skills 25 + Defenses 15 = 117

14-20

PL 8

STR
STA

9  

[... truncated ...]
```

**Chunk 16** (`b53c348dec5d`):

```
CHAPTER 6: POWERS

193

•

Indirect  4:  The  effect  can  originate  from  any  point
and aim in any direction, including towards you
(hitting a target in front of you from behind, for ex-
ample).

INNATE

FLAT • 1 POINT

An effect with this modifier is an innate part of your na-
ture  and  unaffected  by  Nullify  (see  the  Nullify  effect  in
this  chapter).  Gamemasters  should  exercise  caution  in
allowing  the  application  of  Innate;  the  effect  must  be  a
truly inborn or essential trait, such as an elephant’s size or
a ghost’s incorporeal nature. If the effect is not something
normal to the character’s species or type, it probably isn’t
innate.

INSIDIOUS

FLAT • 1 POINT

This  modifier  is  similar  to  the  Subtle  modifier  (later  in
this  section),  except  Insidious  makes  the  result  of  an
effect  harder  to  detect  rather  than  the  effect  itself.  For
example, a target suffering from Insidious Damage isn’t
even aware he’s been damaged. Someone affected by an
Insidious Weaken feels fine until some deficiency makes
it obvious that he’s weaker, and so forth. A target of an
Insidious effect may remain unaware of the danger until
it’s too late!

An  Insidious  effect  is  detectable  either  by  a  DC  20  skill
check  (usually  Perception,  although  skills  like  Expertise,
Insight, or Treatment may apply in other cases) or a par-
ticular unusual sense, such as an Insidious magical effect
noticeable by Detect Magic or Magical Awareness.

Note that Insidious does not make the effect itself harder
to notice; apply the Subtle modifier for that. So it is pos-
sible for an active Insidious effect to be noticeable: the tar-
get can perceive the use of the effect, but not its results:
the effect appears “harmless” or doesn’t seem to “do any-
thing” since the target cannot detect the results.

LINKED

FLAT • 0 POINTS

This modifier applies to two or more effects, linking them
together so they only work in conjunction as one.

The  Linked  effects  must  operate  at  the  same  range.
The  action  required  to  use  the  combined  effects  is  the
longest of its components and they use a single attack
check  (if  one  is  required)  and  resistance  check  (if  both
effects  use  the  same  type  of  check).  If  the  effects  have
different  resistances,  targets  check  against  each  effect
separately.  Different  Alternate  Effects  cannot be  Linked
since they can’t be used at the same time by definition.
Generally, the same effect c

[... truncated ...]
```

**Chunk 17** (`bc6e8d2fe577`):

```
CHAPTER 2: SECRET ORIGINS

93

Supernatural Resistance: Roll 1d20 three times
(re-roll if you get the same result twice) and record
the results.

1-3

4-6

Immunity 5 (Cold, Heat, Pressure,
Radiation, Vacuum) • 5 points

Immunity 5 (Disease, Poison, Starvation

and Thirst, Suffocation) • 5 points

11-20

7-8

Immunity 5 (Alteration effects) • 5 points

9-10

Immunity 5 (Cold damage) • 5 points

11-12

Immunity 5 (Electricity damage) • 5 points

13-14

Immunity 5 (Emotion effects) • 5 points

15-17

Immunity 5 (Fire damage) • 5 points

18-20

Immunity 5 (Magic damage) • 5 points

Roll 1d20 once and record the result.

1-7

Eyes of Darkness: Senses 2 (Darkvision) • 2 points

8-14

15-20

Spider-Climb: Movement 1 (Wall-crawling)

• 2 points

Vampire Bite: Weaken Stamina 4, Grab-based

• 2 points

WEREWOLF

Thick Skin: Protection 3; Impervious Toughness 9, Lim-
ited—Not versus magical or silver weapons • 9 points

Roll 1d20 once and record the result.

Brother to Wolves: Summon 2 (Wolves and

1-10

Dogs), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Deathly Howl: Auditory Perception Area Affliction
10 (Resisted and Overcome by Will; Dazed and
Impaired, Disabled and Stunned), Extra Condition,
Limited Degree • 20 points

1-4

5-10

Demonic Cape: Flight 6 (120 MPH), Gliding,

11-20

Removable (-1 point) • 5 points

Demonic Movement: Leaping 2 (30 feet); Speed 3

(16 MPH) • 5 points

11-16 Giant Bat Wings: Flight 5 (60 MPH), Wings • 5 points

17-20

Hellrider: Movement 2 (Wall-crawling, Water

Walking), Limited to While Moving; Speed 6 (120
MPH), Activation (standard action, -2 points),
Removable (-1 point) • 5 points

VAMPIRE

Blood Drain: Regeneration 10, Source (Blood) • 5 points

Roll 1d20 once and record the result.

1-5

6-20

Living Vampire: Enhanced Stamina 13; Immunity

4 (aging, disease, need for sleep, poison);
Impervious Toughness 8 • 38 points

Undead Invulnerability: Immunity 30 (Fortitude
effects); Impervious Protection 8, Limited—Not
against blessed or magical weapons • 38 points

Roll 1d20 once and record the result.

1-6

7-12

13-20

Children of the Night: Summon 2 (Bats, Rats, and

Wolves), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Dominate: Perception Ranged Affliction 10 (Resisted

and Overcome by Will; Entranced, Compelled,
Controlled), Visually Sense-Dependent • 20 points

Mist Form: Insubstantial 2, Linked to Flight 5 (60

MPH) • 20 points

Roll 1d20 once and record the result.

[... truncated ...]
```

**Chunk 18** (`c1c422470246`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

TALENT

STRENGTH
1
STAMINA
1

AGILITY
2
DEXTERITY
2

FIGHTING
1
INTELLECT
3

AWARENESS
6
PRESENCE
2

Roll 1d20 once and record the result.

DABBLER

Expertise: (Choose One) 4, Insight 4, Perception 4

NINJA

Acrobatics 4, Perception 4, Stealth 4

SNEAK

Deception 4, Perception 4, Stealth 4

STUDENT

Expertise: (Choose One) 6, Insight 2, Perception 4

1-4

5-8

9-12

13-16

Charmed Life: You live a charmed life; maybe
you’re just lucky, but maybe it’s low-level psionic
influence... who can say?

POWERS

Contemplative: You are always calm and
controlled.

Perfect Mind: You use a greater percentage of
your mind.

Thought Leader: You use your abilities to help
others reach greater heights.

Roll  1d20  once  to  determine  if  you  should  roll  on  the
Psionic,  Mentalist,  or  Telekinetic  table,  then  roll  1d20
again on that table and record the result.

17-20

Trained Fighter: You know how to fight.

LIFE

Attractive, Fascinate (Persuasion), Luck

CONTEMPLATIVE

Fearless, Trance, Ultimate Effort (Will checks)

MIND

Eidetic Memory, Jack-of-all-trades, Ultimate Effort (Will checks),

LEADER

Choose either: Inspire, Leadership, and Teamwork, or Inspire 2
and Leadership or Teamwork

FIGHTER

Improved Initiative, Power Attack, Uncanny Dodge

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Charmer: You’re good with people.

Dabbler: You dabble in whatever interests you.

9-12

Ninja: You have been trained in the way of the ninja.

13-16

17-20

Sneak: You’re sneaky and underhanded when you
need to be.

11-15

Student: You’re a high-school, college, or post-
graduate student.

CHARMER

Deception 4, Insight 4, Persuasion 4

Psionic: Take Telepathy, listed immediately below,

then roll on the Psionic Table.

Telepathy: Mind Reading 5 Linked to Area Mental

Communication 3 • 25 points

Psionic Table: Roll 1d20 once and record the result
as the first power of an array, then roll 1d20 twice
and add each result as a 1-point Alternate Effect (re-
roll if you get the same result as your first roll).

1-3

4-7

ESP: Remote Sensing 6 (Normal Visual,
Normal Auditory, Mental) • 24 points

Mental Blast: Perception Range Damage

6, Resisted by Will • 24 points

1-10

8-11

Psi-Knife: Damage 8, Penetrating 4,

Accurate 4, Resisted by Will • 24 points

12-14

15-17

Psionic Invisibility: Concealment 10,

Affects Others, Limited—Concealme

[... truncated ...]
```

**Chunk 19** (`cfadcb33d64b`):

```
CHAPTER 2: SECRET ORIGINS

85

POWERS

Roll 1d20 once and record the result.

1-3

Shapeshifter: Variable 9 (45 points, for assuming

different shapes), Move Action • 72 points

Size-Changer: Roll 1d20 once or choose Giant Size
or Shrinking. You may take the other power as an
Alternate Effect by reducing Giant Size’s Power-
lifting to only 1 rank and dropping the Impervious
extra from Shrinking’s Protection 1. Also, only take
the Flight Belt supplied by the Giant Size power.

11-20

Density Decrease: Insubstantial 4
(Incorporeal, affected by magic),
Reaction, Linked to Flight 1 (4 MPH),
Limited to air-walking, and Immunity
10 (Life Support), Quirk: immunity to
suffocation requires holding breath, and
Concealment 1 (Hearing), Continuous;
Disruption Attacks: Array (24 points),
Incorporeal Weapon (Affects Corporeal
Damage 12, Resisted by Fortitude,
Limited to the Toughness of object used
as weapon), AE: Disrupt Electronics
(Close Range Affects Corporeal Nullify 12
(electronics), Simultaneous), AE: Disrupt
Synapses (Affects Corporeal Affliction
12 (Resisted and Overcome by Fortitude;
Dazed, Stunned, Incapacitated); Innate
Understanding of Powers (Enhanced
Advantages 13 (Close Attack 6, Defensive
Roll 2, Hide in Plain Sight, Redirect, Set-up
2, Teamwork), Enhanced Skill -4 (Close
Combat: Unarmed -8) (Note: the Innate
Understanding of Powers abilities only
work when no powers are active or when
Density Decrease is active) • 72 points

14-16

17-20

Specific Shapeshifter: Variable 9 (45 points, for

assuming different shapes), Continuous, Limited
(Choose one type of entity you can turn into:
Animals, Machines, Humanoids, Aliens, etc.), Move
Action • 72 points

Stretcher: Strength-based Damage 6; Elongation 8
(1,800 feet); Enhanced Advantages 14 (Accurate
Attack, Chokehold, Close Attack 2, Evasion, Fast
Grab, Improved Grab, Improved Hold, Improved
Trip, Interpose, Power Attack, Precise Attack
(Close; Cover), Takedown 2); Enhanced Skill 4
(Close Combat: Grab +8); Impervious Toughness 8,
Limited—Physical Impact Damage; Insubstantial
1 (Liquid), Precise; Morph 2 (Humanoid Forms),
Distracting; Movement 6 (Environmental
Adaptation - Tight Spaces, Safe Fall, Slithering,
Sure-footed, Swinging, Wall-crawling); Protection 7;
Speed 3 (16 MPH) • 72 points

DEFENSE

DODGE
+6

PARRY
+6

FORTITUDE
+6

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

32

72

6

SKILLS

DEFENSES

TOTAL

16

24

150

•

Fame:  Many  Shapeshifters  (especially  heroic  ones)
don’t worry about hiding their

[... truncated ...]
```

**Chunk 20** (`d4cad3e10e05`):

```
CHAPTER 2:
ORIGINS .............. 23
HERO ARCHETYPES ......... 23
HERO DESIGN ................... 23
POINTS ................ 24
Starting Power Points .......... 24
Spending Power Points ...... 24
Power Level ............................. 24
Reallocating

Power Points ........................ 26
COMPLICATIONS .............. 27
Choosing Complications .... 27
Motivation ............................... 27
Other Complications ........... 28
BACKGROUND .................. 30
Name ......................................... 30
Origin ......................................... 30
Age ............................................. 31
Appearance ............................. 32
Personality ............................... 33
Goals .......................................... 33

IMPROVEMENT .............. 33
Increasing Power Level ....... 33
CHARACTER

ARCHETYPES .................. 34
Battlesuit .................................. 35
Construct ................................. 36
Crime Fighter .......................... 37
Energy Controller .................. 38
Gadgeteer ................................ 39
Martial Artist ........................... 40
Mimic ......................................... 41
Mystic ........................................ 42
Paragon .................................... 43
Powerhouse ............................ 44
Psychic ...................................... 45
Shapeshifter ............................ 46
Speedster ................................. 47
Warrior ...................................... 48
Weapon Master...................... 49
FIGHTER -

THE ROOK ....................... 50

POWERHOUSE -

PRINCESS ........................ 52

GENERATOR.................... 54

22

Quickness ...............................174
Regeneration ........................175
Remote Sensing ..................175
Senses .....................................176
Shrinking ................................180
Speed ......................................180
Summon .................................180
Swimming..............................183
Teleport ..................................183
Transform ...............................184
Variable ...................................184
Weaken ...................................186
MODIFIERS...................... 187
Applying Modifiers .............187
Extras .......................................188
Accurate ...............................188
Affects Corporeal ...............188
Affects Insubstantial .........188
Affects Obj

[... truncated ...]
```

**Chunk 21** (`db8b2bdf371a`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Energy Blast: Ranged Damage 12

Take the Gimmick Blaster and Energy Blast
(above), plus roll 1d20 three times (re-roll if you
get the same result twice) and add them to the
Gimmick Blaster array as Alternate Effects. Name
each of these Alternate Effects as appropriate for
your character’s gimmick.

1-3

4-5

6-8

9-11

12-14

Create 7, Continuous, Innate

Move Object 12

Ranged Affliction 12 (Resisted and
Overcome by Fortitude; Dazed,
Stunned, Incapacitated)

Ranged Affliction 12 (Resisted by
Dodge, Overcome by Damage;
Vulnerable, Defenseless,
Incapacitated)

Ranged Cloud Area Affliction 8

(Resisted and Overcome by Fortitude;
Dazed and Visually Impaired,
Stunned and Visually Disabled) Extra
Condition, Limited Degree

15-17

Ranged Burst Area Damage 8

18-20

Close Cone Area Damage 8, Penetrating 8

Personal Combat Enhancers: Enhanced Advantage

11 (All-out Attack, Defensive Attack, Evasion,
Extraordinary Effort, Diehard, Fearless, Great
Endurance, Improved Critical (Unarmed),
Improved Initiative, Takedown 2); Enhanced
Strength 3; Enhanced Trait 5 (Close Attack 5);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 points

8-12

13-14

15-16

Physical Boosters: Enhanced Strength 8; Leaping

2 (30 feet); Quickness 2; Speed 2 (8 MPH);
Activation—Move Action (-1 point), Removable
(-4 points) • 17 point

17-20

High-tech Arsenal: Ray Gun (Ranged Damage 12,
AE: Power Truncheon (Strength-based Damage
8), AE: Stunner (Ranged Affliction 12 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated)), AE: Force Capsule Grenade
(Ranged Affliction 12 (Resisted by Dodge,
Overcome by Damage; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree); Easily Removable (-10 points)
• 17 points

Roll 1d20 once and record the result.

1-5

6-10

Combat Training and Armored Costume:
Enhanced Advantage 2 (Defensive Roll 2),
Enhanced Defenses (Dodge 4, Parry 4), Protection
4, Removable (-1 point) • 13 points

Displacer Field: Enhanced Defenses (Dodge 6, Parry
6) Linked to Protection 4, Sustained, Removable
(-3 points) • 13 points

11-15

Energy-Absorbing Body Suit: Protection 10,

Impervious 6, Removable (-3 points) • 13 points

16-20

Force Field: Immunity 6 (Critical Hits, Cold, Heat,

High Pressure, Radiation) Linked to Protection 10,
Sustained, Removable (-3 points) • 13 points

Roll 1d20 once and record the result.

1-4

5-8

9-16

17-20

Biologica

[... truncated ...]
```

**Chunk 22** (`e17d1554782d`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Dense Fog: Visual (All) Concealment 4 Attack, Burst

1-8

Arc Riding: Leaping 10 • 10 points

Weather Control array as Dynamic Alternate Effects (re-
roll if you get the same result twice).

Arctic Freeze: Ranged Cumulative Affliction 10
(Resisted by Dodge, Overcome by Damage;
Hindered and Vulnerable, Defenseless and
Immobile), Extra Condition, Limited Degree
• 30 points

Dazzling Strike: Ranged Cumulative Affliction 10

(Resisted and Overcome by Fortitude; Vision and
Auditory Impaired, Vision and Auditory Disabled,
Vision and Auditory Unaware) • 30 points

Area (×3), Selective • 28 points

Downdraft: Ranged Affliction 10 (Resisted and

Overcome by Strength; Hindered and Impaired,
Stunned and Prone, Incapacitated), Alternate
Resistance (Strength), Concentration Duration,
Extra Condition, Instant Recovery • 30 points

Glacier: Create 9, Continuous, Innate, Linked to
Environment 2 (Cold, Impede Movement 1)
• 30 points

Hailstorm: Ranged Cloud Area Damage 9, Indirect 2

(falling from above) • 30 points

Lightning Bolt: Ranged Damage 12, Accurate 3,
Indirect 3 (any point downwards) • 30 points

Stormy Weather: Environment 10 (2 miles; Cold,

Impede Movement, Visibility) • 30 points

Tornado: Cylinder Area Move Object 10,

Concentration Duration, Damaging • 30 points

Wind Screen: Deflect 10, Cylinder Area (×3), Limited

to Attacks Targeting Dodge • 30 points

1-2

3-4

5-6

7-8

9-10

11-12

13-14

15-16

17-18

19-20

Roll 1d20 once and record the result.

1-5

Aquatic: Immunity 3 (Cold, Drowning, Pressure),
Senses 5 (Darkvision, Accurate and Extended
Hearing); Swimming 2 (2 MPH), Stacks with other
Swimming • 10 points

6-10

Cold Immunity: Immunity 10 (Cold effects) • 10 points

11-20

Weather-Proof: Immunity 10 (Weather effects)

• 10 points

Roll 1d20 once and record the result.

1-7

8-14

15-20

Force Field: Impervious Protection 8, Sustained

• 16 points

Vigorous: Enhanced Stamina 3; Enhanced Defenses

10 (Dodge 5, Parry 5), Sustained • 16 points

Wind Shield: Enhanced Defenses 16 (Dodge 8, Parry

8), Sustained • 16 points

Roll 1d20 once and record the result.

Swimming: Movement 1 (Environmental

9-12

Adaptation—Aquatic); Swimming 8 (120 MPH),
Stacks with other Swimming • 10 points

13-20 Wind Riding: Flight 5 (60 MPH) • 10 points

DEFENSE

DODGE
+2

PARRY
+0

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

40

75

7

SKILLS

DEFENSES

TOTAL

16

12

150

•  Moti

[... truncated ...]
```

---

## Concept: Living Space

Chunk count: 9

### Chunk texts

**Chunk 1** (`04f4880a6e63`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HIGHTECH GEAR

Advantage: Equipment 10 (Equipment listed
immediately below)

Smartphone, Restraints, Flashlight, Multi-tool,
Rebreather • 6 points

Headquarters—Size: Huge, Toughness: 10;
Features: Communications, Computer, Concealed,
Garage, Gym, Laboratory, Living Space, Power
System, Security System, Workshop • 15 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Swingline: Movement 1 (Swinging) • 2 points

Utility Belt • 17 points

11-20

•  Bolos: Ranged Cumulative Affliction 4 (Resisted
by Dodge, Overcome by Damage; Hindered and
Vulnerable, Defenseless and Immobilized), Extra
Condition, Limited Degree • 12 points

•  Boomerangs: Strength-based Ranged Damage 1,

Accurate 2 • 1 point

ure. This motivation is especially appropriate for the
Dark Avenger.

•  Motivation—Thrills: You don’t have any powers, per
se, but why should that stop you from having fun?

•

Enemy: The Crime Fighter usually has at least one vil-
lain central to his or her existence who plagues the
hero consistently.

ELEMENTAL

The Elemental is a being composed of a pure element, usu-
ally one of the classical four elements of earth, air, fire, or
water. They have powers reflecting their elemental compo-
sition, as well as control and mastery over that element.
ABILITIES

•  Explosives: Ranged Burst Area Damage 4 • 1 point

Roll 1d20 once and record the result.

•  Power-Knuckles: Strength-based Damage 3,

Improved Critical, Inaccurate • 1 point

•  Taser: Ranged Cumulative Affliction 4 (Resisted
and Overcome by Fortitude; Dazed, Stunned,
Incapacitated) • 1 point

•  Tear-Gas Pellets: Ranged Cloud Area Affliction 4
(Resisted and Overcome by Fortitude; Dazed and
Visually Impaired, Stunned and Visually Disabled),
Extra Condition, Limited Degree • 1 point

DEFENSES

DODGE
+7

PARRY
+5

FORTITUDE
+4

TOUGHNESS
+0

WILL
+8

ABILITIES

POWERS

68

7/0*

SKILLS

DEFENSES

28/35*

TOTAL

23

24

150

*If you rolled Gadgeteer on the Powers/Equipment table,
then  you  have  Powers  7  and  Advantages  28,  otherwise
you have Powers 0 and Advantages 35.

•  Motivation—Patriotism:  You  strongly  believe  in  the
ideals your country was founded on and fight to uphold
them... especially from those who would twist them to
their own purposes. Patriotic Crime Fighters often have
a military background, but they don’t have to.

•  Motivation—Doing Good: Crime Fighters with this
motivation ar

[... truncated ...]
```

**Chunk 2** (`1081db3c43af`):

```
CHAPTER 2: SECRET ORIGINS

69

15-20

Scientist: At heart, you’re a scientist. You’re always
working on something in the lab, but you like to get
“out in the field” and test the practical applications
of your inventions. Plus, there are all sorts of unusual
things out in the world that you’d never get to
experience in the lab.

TINKERER

Accurate Attack, Luck, Power Attack

INVENTOR

Benefit 3 (Millionaire)

SKILLS

Close Combat: Unarmed or Gadgets 6, Expertise: Science 10,
Ranged Combat: Gadgets 6, Technology 10, Vehicles 4

Take the skills listed above, then roll 1d20 once and record
the result.

1-5

6-10

Businessman/woman: You know how to run a
business.

Explorer: You have the skills necessary to explore
new places.

11-15

Investigator: You’re a talented detective.

16-20

Infiltrator: You’re stealthy.

BUSINESSMAN/WOMAN

Expertise: Business 5, Insight 6, Persuasion 5

EXPLORER

Athletics 7, Perception 5, Stealth 4

INVESTIGATOR

Insight 4, Investigation 7, Perception 5

INFILTRATOR

Deception 6, Sleight of Hand 4, Stealth 6

POWERS

Roll 1d20 once and record the result.

ADVENTURER

STRENGTH
2
STAMINA
2
GIMMICK

AGILITY
2
DEXTERITY
2

STRENGTH
2
STAMINA
1

AGILITY
2
DEXTERITY
2
SCIENTIST

FIGHTING
4
INTELLECT
8

AWARENESS
3
PRESENCE
2

FIGHTING
4
INTELLECT
9

AWARENESS
4
PRESENCE
1

STRENGTH
1
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
4
INTELLECT
10

AWARENESS
4
PRESENCE
0

Beginner’s Luck, Eidetic Memory, Equipment 3 (Headquarters),
Improvised Tools, Inventor, Skill Mastery (Technology)

Headquarters—Size:  Large,  Toughness:  10;  Features:
Communications, Computer, Fire Prevention System, Infirmary,
Laboratory,  Library,  Living  Space,  Personnel,  Power  System,
Security System, Workshop • 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Athletic: You take care of yourself and are physically fit.

6-10

Natural Leader: You’re a natural leader.

11-15

Tinkerer: You’re constantly tinkering with your
inventions and are able to get the most out of them.

16-20

Well-to-do Inventor: You either inherited wealth or
have made money off some of your more mundane
inventions.

ATHLETIC

Evasion, Improved Initiative, Uncanny Dodge

LEADER

8-12

Inspire 2, Leadership

70

1-4

5-7

Energy Projector Device: Ranged Damage 8,
Accurate 2; AE: Ranged Affliction 8 (Resisted
and Overcome by Fortitude; Dazed Stunned,
Incapacitated), Accurate 2; AE: Ranged
Multiattack Damage 5, Accurate 3; AE: Close Cone
Area Dazzle 9

[... truncated ...]
```

**Chunk 3** (`1af862ab5396`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Battlesuits  typically  fall  into  one  of  three  categories:
they’re either ranged combatants, melee powerhouses, or
a mix of the two. No matter what role the Battlesuit fills,
the  person  inside  the  armor  tends  to  be  a  fairly  normal
person, possibly highly trained or highly intelligent, who
relies on the armor to provide his or her powers.
ABILITIES

Roll 1d20 once and record the result.

13-16

17-20

Scientist: You work as a scientist and/or have
natural talent in that area.

Wealthy: Whether you inherited or earned it, you’re
a part of the upper-crust of society.

COMBATANT

Accurate Attack, All-out Attack, Improved Initiative, Interpose,
Move-by Action

INVENTOR

Eidetic Memory, Improvised Tools, Inventor, Ultimate Effort
(Technology), Well-informed

1-12

Genius: You’re incredibly intelligent and likely had a
hand in creating your battlesuit.

LUCKY

13-18

19-20

Military: You were trained by the military as a
soldier or scientist and may have received or stolen
your battlesuit from them.

Accidental: You chanced upon your armor
somehow, either the armor’s creation was a one-
time fluke, it was found by you, or it was given to
you by an organization or aliens.

GENIUS

STRENGTH
0
STAMINA
1

AGILITY
1
DEXTERITY
2

FIGHTING
2
INTELLECT
8

AWARENESS
2
PRESENCE
2

MILITARY

STRENGTH
3
STAMINA
3

AGILITY
1
DEXTERITY
2
ACCIDENTAL

FIGHTING
3
INTELLECT
2

AWARENESS
2
PRESENCE
2

STRENGTH
2
STAMINA
1

AGILITY
3
DEXTERITY
2

FIGHTING
2
INTELLECT
3

AWARENESS
3
PRESENCE
2

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

5-8

Combatant: You have natural talent or you’ve been
trained in combat, both in armor and out.

Inventor: You know your way around technology, have
a headquarters, and can build gadgets given time.

9-12

Lucky: Things are easy for you.

Beginner’s Luck, Luck 2, Redirect, Teamwork

SCIENTIST

Equipment 3 (Headquarters), Skill Mastery (Expertise:
Science), Skill Mastery (Technology)

Headquarters—Size: Large, Toughness: 10; Features:
Communications, Computer, Fire Prevention System, Hangar,
Infirmary, Laboratory, Library, Living Space, Power System,
Security System, Workshop • 15 points)

WEALTHY

Attractive, Benefit 4 (Multi-millionaire)
SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

People Person: You’re good with people and in
business.

5-16


[... truncated ...]
```

**Chunk 4** (`75c6a0d7757a`):

```
CHAPTER 2: SECRET ORIGINS

75

MYSTIC

The  Mystic  commands  vast  magical  powers  and  uses
them  to  defend  the  Earth  from  otherworldly  threats  as
well  as  to  combat  the  evils  found  just  down  the  street.
The  Mystic  typically  has  extensive  knowledge  of  magic
and other realms, but few real-world skills to speak of. The
magical powers the Mystic commands are nearly limitless,
allowing  the  Mystic  to  fire  blasts  of  magical  energy,  fly,
create  illusions,  heal  others,  travel  to  other  dimensions,
and reproduce virtually any other power imaginable.
ABILITIES

Roll 1d20 once and record the result.

1-6

Host: You’re the host of a mystical being which gives
you access to supernatural powers.

7-13

Magical Heritage: Your family has a long history of
being blessed with magical powers... or perhaps it’s
cursed.

14-20

Mystic Master: You’ve trained long and hard to
master the mystic arts.

HOST

STRENGTH
1
STAMINA
0

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
2

AWARENESS
5
PRESENCE
5

HERITAGE

STRENGTH
0
STAMINA
0

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
2

AWARENESS
7
PRESENCE
4

MASTER

AGILITY
1
DEXTERITY
3

STRENGTH
0
STAMINA
0

FIGHTING
4
INTELLECT
3

AWARENESS
6
PRESENCE
4

Equipment 3 (Headquarters), Ranged Attack 5, Trance

Headquarters—Size: Medium, Toughness: 10; Features:
Concealed, Dual-size (Huge), Laboratory, Library, Living Space,
Personnel, Sealed, Security System, Self-repairing, Workshop
• 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Centered: You’ve trained yourself to remain calm
and centered, no matter what.

6-10

Enchanter: You can create magical artifacts.

76

```

**Chunk 5** (`8ad0833a1563`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

WEREWOLF

STRENGTH
7
STAMINA
6

AGILITY
4
DEXTERITY
1

FIGHTING
9
INTELLECT
0

AWARENESS
3
PRESENCE
1

Roll 1d20 once and record the result.

REFINED

Expertise (Choose One) 4, Insight 4, Perception 6, Persuasion 10

TEEN

Deception 8, Expertise: Popular Culture 4, Expertise:
Streetwise 4, Perception 4, Technology 4

TEMPTER

Deception 12, Insight 6, Perception 6

POWERS

Aristocrat: You used your powers to gain wealth
and social status.

1-5

6-10

Heartthrob: People are attracted to your dark and
handsome looks.

11-15

Savage: You delight in your strength and power.

16-20

Wilder: You are comfortable in the wild and possibly
more bestial or feral than others of your kind.

ARISTOCRAT

Benefit 2 (Wealthy), Equipment 2 (Lair Headquarters)

Lair Headquarters—Size: Large, Toughness: 10; Features:
Concealed or Secret, Defense Systems or Deathtraps, Laboratory
or Workshop, Library, Living Space, Security System • 10 points

HEARTTHROB

Attractive, Daze (Deception), Fascinate (Choose One:
Deception or Persuasion), Inspire

SAVAGE

Agile Feint, Evasion, Great Endurance, Power Attack

WILDER

Animal Empathy, Great Endurance, Favored Environment
(Choose One), Track

SKILLS

Roll 1d20 once and record the result.

1-4

5-8

9-12

Bestial: You are feral and powerful.

Mysterious: You are enigmatic and secretive.

Refined: You are experienced with the finer things
in… life.

13-16

Teen: You are young and exploring your newfound
powers.

17-20

Tempter: You are cunning and deceitful.

BESTIAL

Athletics 6, Intimidation 12, Perception 6

MYSTERIOUS

Deception 8, Perception 8, Stealth 8

Roll 1d20 once and record the result, then roll on the De-
mon, Vampire, or Werewolf table below depending on
which set of Abilities you rolled.

1-6

Brutish Strength: Enhanced Strength 4 • 8 points

7-12

13-20

Devilish Speed: Enhanced Advantages 6 (Close
Attack 4, Improved Initiative 2); Quickness 2
• 8 points

Supernatural Might: Enhanced Strength 2; Power-
lifting 2; Enhanced Advantages 2 (Close Attack 2)
• 8 points

DEMON

Demonic Physiology: Protection 3 • 3 points

Hellfire Control: Array (20 points plus 1 Alternate Effect) • 21

points total

Roll 1d20 once and record the result as the first power in
the Hellfire Control array, then roll again (re-roll if you get
the same result on the second roll) and add the result to
the Hellfire Control array as a 1-point Alternate Effect.

1-3

4-6

7-11

12

[... truncated ...]
```

**Chunk 6** (`ab446868e7fe`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

SEA-BASE

Gamemasters can use the following sample headquarters
as ready-made lairs for supervillains while players can use
them as bases for their heroes.

Size: Gargantuan Toughness: 14 Features: Communications,
Computer, Concealed, Dock, Fire Prevention System, Isolated,
Living Space, Power System, Security System • 16 points.

SKYSCRAPER (5 FLOORS)

Size:  Medium  Toughness:  8  Features:  Communications,
Computer,  Concealed,  Garage,  Gym,  Living  Space,  Power
System, Security System • 10 points.

Size:  Large  Toughness:  10  Features:  Communications,
Computer,  Defense  System,  Fire  Prevention  System,  Gym,
Hangar,  Infirmary,  Laboratory,  Library,  Living  Space,  Power
System, Security System, Workshop • 17 points.

MOON-BASE

Size:  Awesome Toughness:  20  Features:  Combat  Simulator,
Communications, Computer, Defense System, Fire Prevention
Isolated,
System,  Gym,  Hangar,  Holding  Cells,
Laboratory, Living Space, Power System, Security System (DC
25), Teleport (Affects Others), Workshop • 28 points.

Infirmary,

Size:  Huge  Toughness:  10  Features:  Communications,
Computer,  Concealed,  Dock,  Garage,  Gym,  Hangar,  Infirmary,
Laboratory,  Library,  Living  Space,  Power  System,  Security
System, Workshop • 19 points.

Size:  Colossal  Toughness:  20  Features:  Combat  Simulator,
Communications, Computer, Defense System, Fire Prevention
System,  Gym,  Hangar,  Holding  Cells,
Isolated,
Laboratory,  Living  Space,  Power  System,  Security  System,
Teleport (Affects Others) • 25 points.

Infirmary,

Size:  Huge  Toughness:  14  Features:  Communications,
Computer, Concealed, Defense System, Garage, Holding Cells,
Isolated,  Laboratory,  Library,  Living  Space,  Power  System,
Security System • 19 points.

Size: Medium Toughness: 10 Features: Concealed, Dual-Size
(Huge),  Laboratory,  Library,  Living  Space,  Security  System,
Workshop • 12 points.

Size:  Large  Toughness:  12  Features:  Combat  Simulator,
Communications,  Computer,  Concealed,  Defense  System,  Fire
Prevention System, Garage, Gym, Holding Cells, Infirmary, Living
Space, Power System, Security System, Workshop • 22 points.

Armored robots, humanlike androids, even magically-animated golems or zombies are all examples of constructs, non-
living things capable of acting on their own to one degree or another, carrying out pre-programmed instructions, or
even possessing independent th

[... truncated ...]
```

**Chunk 7** (`d5fc086574e9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

LUCKY

Beginner’s Luck, Luck 2, Redirect

RESOURCES

Equipment 4 (Headquarters)

8-14

Super-strength: Enhanced Strength 4 • 8 points

15-20

Soldier: Enhanced Trait 4 (Close Attack 4); Power-

lifting 4 • 8 points

Headquarters—Size: Gargantuan, Toughness: 12; Features:
Communications, Computer, Gym, Infirmary, Isolated,
Laboratory, Library, Living Space, Personnel, Power System,
Security System, Teleport (Affects Others), Workshop • 20 points

WARRIOR

All-out Attack, Improved Initiative, Interpose, Move-by Action

Immunities: Immunity 10 (Life Support) • 10 points

Invulnerability: Protection 4 • 4 points

Roll 1d20 once and record the result.

WEALTHY

Benefit 4 (Multi-millionaire)

SKILLS

1-15

Flight: Flight 8 (500 MPH) • 16 points

16-20

Super Movement: Speed 3 (16 MPH); Leaping 7

(900 feet); Movement 3 (Swinging, Wall-crawling
2) • 16 points

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

If you have the Superhuman or Vessel set of abilities, role
once on this table. Do not roll on this table otherwise.

1-5

Athlete: You’re a trained athlete.

6-10

Broad Training: You have a broad set of skills from
your education or experiences.

11-15

Charismatic: You’re good with people.

16-20

Learned: You’re well educated, with some
technological training.

ATHLETE

Acrobatics 6, Athletics 6, Perception 4

TRAINING

1-4

5-7

8-11

Improved Invulnerability: Impervious Toughness 6

• 6 points

Inhuman Physiology: Enhanced Advantage 1

(Diehard); Immunity 2 (Critical Hits); Regeneration 3
• 6 points

Enhanced Senses: Senses 6 (Extended Auditory
2, Extended Vision 2, Microscopic Vision, Ultra-
Hearing) • 6 points

12-15 Quickness: Quickness 6 • 6 points

16-18

Telepathy: Mental Communication 1, Subtle 2

• 6 points

19-20

Traveler: Movement 3 (Dimension Travel 3) • 6 points

Expertise: (Choose One) 4, Insight 2, Perception 2, Persuasion
4, Ranged Combat: Throwing 4

CHARISMATIC

Expertise: (Choose One) 4, Insight 4, Perception 4, Persuasion 4

DEFENSE

LEARNED

Expertise: (Choose One) 6, Perception 4, Technology 6

POWERS

DODGE
+4

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

SUPERHUMAN/VESSEL

DODGE
+4

PARRY
+0

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

WILL
+6

If you have the Man of Action Abilities, don’t roll for your
Offensive Power, instead, take Find Weakness:

Find Weakness: Strength-based Damage 4; Enhanced

Advantage 4 (Close At

[... truncated ...]
```

**Chunk 8** (`dcdc4c459ab6`):

```
CHAPTER 2: SECRET ORIGINS

61

CRIMINOLOGIST

EXPERT

Assessment, Skill Mastery (Expertise: Streetwise)

Perception 6, Technology 8, Treatment 6

SCIENTIST

INVESTIGATOR

Inventor, Skill Mastery (Technology)

Expertise: Streetwise 4, Insight 5, Investigation 6, Perception 5

SLEUTH

SNEAK

Skill Mastery (Investigation), Tracking

Deception 6, Sleight of Hand 6, Stealth 8

POWERS/EQUIPMENT

Roll 1d20 once and record the result. If you rolled the In-
ventor set of Abilities, take Gadgets instead of rolling.

Roll 1d20 once and record the result.

1-10

Acrobat: You’re a trained acrobat, capable of
incredible feats of agility.

11-15 Martial Artist: You’re a trained fighter.

16-20

Thief: You’re a trained thief, able to disappear with a
moment’s notice.

ACROBAT

Evasion, Instant Up

1-4

ARTIST

Defensive Attack, Uncanny Dodge

THIEF

Hide in Plain Sight, Skill Mastery (Stealth)

SKILLS

Close Combat: Unarmed 6

Take the skill listed above, then if you rolled Dark Aveng-
er  for  your  Abilities,  take  Avenger  and  roll  once,  re-roll
if  you  get  Avenger  again.  If  you  rolled  the  Detective
for  your  Abilities,  take  Investigator  and  roll  once,  re-roll
if  you  get  Investigator  again.  If  you  rolled  Inventor  for
your Abilities, take Expert and roll once, re-roll if you get
Expert again.

1-4

Athlete: You’re physically capable and impressive.

5-8

Avenger: You’ve trained yourself in a number of
useful skills.

5-10

6-10

9-12

Expert: You know a lot about some subjects.

13-16

Investigator: You’ve studied investigation and other
forms of observation.

17-20

Sneak: You’re stealthy.

ATHLETE

Acrobatics 6, Athletics 8, Intimidation 6

AVENGER

Expertise: Streetwise 6, Intimidation 8, Vehicles 6

11-15

16-20

Advantage: Equipment 10 (Equipment listed
immediately below)
Smartphone • 2 points
Headquarters—Size: Medium, Toughness: 8;
Features: Communications, Computer, Concealed,
Garage, Gym, Living Space, Power System, Security
System • 10 points

Motorcycle: Medium; Str 1; Speed 6; Defense 10;

Toughness 8 • 10 points

Knife: Strength-based Damage 1, Improved Critical

• 2 points

Customized Heavy Pistol with Laser Sight:
Ranged Damage 4, Accurate 2 • 10 points

Customized Assault Rifle: Ranged Multiattack

Damage 5, Accurate • 16 points

GADGETS

Advantage: Equipment 3 (Headquarters)
Headquarters—Size: Large, Toughness: 10;
Features: Communications, Computer, Concealed,
Fire Prevention System, Gym, Infirmary, Laboratory,
Living Space,

[... truncated ...]
```

**Chunk 9** (`eab98ce0e1fc`):

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

## Concept: Looking Glass

Chunk count: 0

### Chunk texts

---

## Concept: Lord

Chunk count: 1

### Chunk texts

**Chunk 1** (`6890e166bca9`):

```
CHAPTER 2: SECRET ORIGINS

29

A lot of background details go into making your hero more than just a collection of numbers. Take a moment (if you
haven’t already) to consider some of the following things about your character:

NAME

What is your character’s name? That is to say, what is the
name  the  hero  uses  in  public,  that  appears  in  one-inch
type  in  the  newspaper  headlines?  Most  heroes  adopt
unique  and  distinctive “code  names,”  so  consider  a  suit-
able name for yours. Code names are often based on pow-
ers, theme, or style. Here are some options to consider:
ORIGIN

A name may be based on the hero’s origin, power source,
nation (or even world) of birth, and such.
POWERS

Choose a name based on the hero’s powers: Firestarter or
Blaze for a flame-controlling character, Thunder or Spark
for an electrical character, and so forth.

THEME

Maybe  the  character  has  a  theme  or  style  suggesting  a
name: Paladin might be a medieval knight displaced into
the present day, with a magical sword and armor. Madame
Macabre may be all about magic and the occult.

TITLES

Names  may  include  various  titles  like  Mister,  Miss,  Ms.,
Doctor,  Sir,  Lord,  Lady,  and  Madam  or  even  royal  titles
like  King,  Queen,  Prince,  Princess,  Duke,  Baron,  Emperor
and so forth. Military ranks are also popular parts of hero
names, especially General, Major, and Captain.
GENDER

Names often include gender designations like Man/Wom-
an, Boy/Girl, Lad/Lass, and so forth.
SOUND

Some  code-names  don’t  really  have  anything  to  do  with  a
character’s powers or background—they just sound cool: Kis-
met, Scion, Animus, Damask, and so forth. They may hint at
the hero’s powers or origin, or have nothing to do with them.

REAL NAME

Some heroes go by their given name, not using a code-
name at all. Oftentimes these names still sound like code-

names,  however.  They  may  also  be  nicknames,  such  as
“Dash” for someone with the name Dashell, or “Buzz” for
someone  with  the  name  Buzcinski,  or  whatever  other
nickname a character may have, such as “Stretch” or “Tiny”.

ORIGIN

What’s  the  origin  of  your  hero’s  powers?  It  can  be  any-
thing from a character born with the potential for powers
to someone granted them by an accident—exposure to a
strange meteor, radiation, genetic engineering, or any of
countless similar encounters. Here are some of the more
common superhero origins:
ACCIDENT

Perhaps  the  most  common  origin. The  hero  

[... truncated ...]
```

---

## Concept: Luck

Chunk count: 18
Receives actions: ['act_0245']

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

**Chunk 2** (`1081db3c43af`):

```
CHAPTER 2: SECRET ORIGINS

69

15-20

Scientist: At heart, you’re a scientist. You’re always
working on something in the lab, but you like to get
“out in the field” and test the practical applications
of your inventions. Plus, there are all sorts of unusual
things out in the world that you’d never get to
experience in the lab.

TINKERER

Accurate Attack, Luck, Power Attack

INVENTOR

Benefit 3 (Millionaire)

SKILLS

Close Combat: Unarmed or Gadgets 6, Expertise: Science 10,
Ranged Combat: Gadgets 6, Technology 10, Vehicles 4

Take the skills listed above, then roll 1d20 once and record
the result.

1-5

6-10

Businessman/woman: You know how to run a
business.

Explorer: You have the skills necessary to explore
new places.

11-15

Investigator: You’re a talented detective.

16-20

Infiltrator: You’re stealthy.

BUSINESSMAN/WOMAN

Expertise: Business 5, Insight 6, Persuasion 5

EXPLORER

Athletics 7, Perception 5, Stealth 4

INVESTIGATOR

Insight 4, Investigation 7, Perception 5

INFILTRATOR

Deception 6, Sleight of Hand 4, Stealth 6

POWERS

Roll 1d20 once and record the result.

ADVENTURER

STRENGTH
2
STAMINA
2
GIMMICK

AGILITY
2
DEXTERITY
2

STRENGTH
2
STAMINA
1

AGILITY
2
DEXTERITY
2
SCIENTIST

FIGHTING
4
INTELLECT
8

AWARENESS
3
PRESENCE
2

FIGHTING
4
INTELLECT
9

AWARENESS
4
PRESENCE
1

STRENGTH
1
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
4
INTELLECT
10

AWARENESS
4
PRESENCE
0

Beginner’s Luck, Eidetic Memory, Equipment 3 (Headquarters),
Improvised Tools, Inventor, Skill Mastery (Technology)

Headquarters—Size:  Large,  Toughness:  10;  Features:
Communications, Computer, Fire Prevention System, Infirmary,
Laboratory,  Library,  Living  Space,  Personnel,  Power  System,
Security System, Workshop • 15 points

Take the advantages listed above, then roll 1d20 once and
record the result.

1-5

Athletic: You take care of yourself and are physically fit.

6-10

Natural Leader: You’re a natural leader.

11-15

Tinkerer: You’re constantly tinkering with your
inventions and are able to get the most out of them.

16-20

Well-to-do Inventor: You either inherited wealth or
have made money off some of your more mundane
inventions.

ATHLETIC

Evasion, Improved Initiative, Uncanny Dodge

LEADER

8-12

Inspire 2, Leadership

70

1-4

5-7

Energy Projector Device: Ranged Damage 8,
Accurate 2; AE: Ranged Affliction 8 (Resisted
and Overcome by Fortitude; Dazed Stunned,
Incapacitated), Accurate 2; AE: Ranged
Multiattack Damage 5, Accurate 3; AE: Close Cone
Area Dazzle 9

[... truncated ...]
```

**Chunk 3** (`17270869c240`):

```
CHAPTER 2: SECRET ORIGINS

87

Roll 1d20 once and record the result.

1-5

Fighter: You were trained in combat.

6-10

Nimble: You are quick-footed.

11-15

Prodigy: You have learned a little bit of everything.

16-20

Team-Player: You have experience working as part
of a super-team.

FIGHTER

Close Attack 2, Equipment (Sword or other melee weapon)

NIMBLE

Evasion, Instant Up, Move-by Action

PRODIGY

Beginner’s Luck, Eidetic Memory, Well-informed

TEAM-PLAYER

Interpose, Set-up, Teamwork

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Athlete: You are a trained athlete.

Charmer: People like you.

9-12

Police: You work in law enforcement.

13-16

Scientist: You are an expert in a field of science.

17-20

Thief: You’ve operated outside the law.

16-20

ATHLETE

Acrobatics 4, Athletics 8, Perception 4

CHARMER

Deception 6, Insight 4, Persuasion 6

POLICE

Insight 4, Investigation 6, Perception 6

SCIENTIST

Expertise: (Choose One) 6, Technology 6, Vehicles 4

THIEF

Deception 4, Stealth 6, Technology 6

POWERS

Roll 1d20 once and record the result.

Running: Roll 1d20 once:

1-10

Gravity-Defying Runner: Movement
3 (Wall-crawling 2, Water Walking),
Limited to While Moving; Quickness 10;
Speed 15 (64,000 MPH) • 28 points

1-10

11-15

16-20

Rapid Metabolism: Immunity 1 (Poison);
Quickness 11; Regeneration 5; Speed
11 (4,000 MPH) • 28 points

Time-Traveler: Movement 3 (Time

Travel—any time); Quickness 10; Senses
4 (Precognition), Check Required
(Intellect or Expertise: History); Speed
10 (2,000 MPH) • 28 points

11-15

Flying: Roll 1d20 once:

Cosmic Speedster: Flight 9 (1,000 MPH);

Immunity 6 (cold, heat, radiation,
suffocation, vacuum); Movement 2
(Environmental Adaptation—Zero-G;
Space Travel 1) • 28 points

Hypersonic: Flight 14 (32,000 MPH) • 28

points

Hyper-Speed: Flight 10 (2,000 MPH);

Quickness 8 • 28 points

1-5

6-15

16-20

Teleporting: Roll 1d20 once:

1-5

6-10

Dimensional Walker: Movement 3

(Dimension Travel—any dimension);
Teleport 11 (8 miles) • 28 points

Proximal: Teleport 9 (2 miles), Accurate,

Turnabout • 28 points

Transmit: Teleport 9 (2 miles), Easy,

11-15

Extended (500 miles), Medium (Choose
One), Turnabout • 28 points

16-20

World-Walker: Teleport 9 (2 miles),
Extended (500 miles), Turnabout
• 28 points

Speedster Stunts: Array (20 points plus 1 point of Al-
ternate Effect)

Roll 1d20 once and record the result as the first power in
the  Speedster  Stunts  a

[... truncated ...]
```

**Chunk 4** (`1af862ab5396`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

Battlesuits  typically  fall  into  one  of  three  categories:
they’re either ranged combatants, melee powerhouses, or
a mix of the two. No matter what role the Battlesuit fills,
the  person  inside  the  armor  tends  to  be  a  fairly  normal
person, possibly highly trained or highly intelligent, who
relies on the armor to provide his or her powers.
ABILITIES

Roll 1d20 once and record the result.

13-16

17-20

Scientist: You work as a scientist and/or have
natural talent in that area.

Wealthy: Whether you inherited or earned it, you’re
a part of the upper-crust of society.

COMBATANT

Accurate Attack, All-out Attack, Improved Initiative, Interpose,
Move-by Action

INVENTOR

Eidetic Memory, Improvised Tools, Inventor, Ultimate Effort
(Technology), Well-informed

1-12

Genius: You’re incredibly intelligent and likely had a
hand in creating your battlesuit.

LUCKY

13-18

19-20

Military: You were trained by the military as a
soldier or scientist and may have received or stolen
your battlesuit from them.

Accidental: You chanced upon your armor
somehow, either the armor’s creation was a one-
time fluke, it was found by you, or it was given to
you by an organization or aliens.

GENIUS

STRENGTH
0
STAMINA
1

AGILITY
1
DEXTERITY
2

FIGHTING
2
INTELLECT
8

AWARENESS
2
PRESENCE
2

MILITARY

STRENGTH
3
STAMINA
3

AGILITY
1
DEXTERITY
2
ACCIDENTAL

FIGHTING
3
INTELLECT
2

AWARENESS
2
PRESENCE
2

STRENGTH
2
STAMINA
1

AGILITY
3
DEXTERITY
2

FIGHTING
2
INTELLECT
3

AWARENESS
3
PRESENCE
2

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

1-4

5-8

Combatant: You have natural talent or you’ve been
trained in combat, both in armor and out.

Inventor: You know your way around technology, have
a headquarters, and can build gadgets given time.

9-12

Lucky: Things are easy for you.

Beginner’s Luck, Luck 2, Redirect, Teamwork

SCIENTIST

Equipment 3 (Headquarters), Skill Mastery (Expertise:
Science), Skill Mastery (Technology)

Headquarters—Size: Large, Toughness: 10; Features:
Communications, Computer, Fire Prevention System, Hangar,
Infirmary, Laboratory, Library, Living Space, Power System,
Security System, Workshop • 15 points)

WEALTHY

Attractive, Benefit 4 (Multi-millionaire)
SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

People Person: You’re good with people and in
business.

5-16


[... truncated ...]
```

**Chunk 5** (`267bbd73af09`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

INNOCENT

Animal Empathy, Luck

INCISIVE

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

SUBTLE

Evasion, Hide in Plain Sight

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-3

Dynamic: You are a good all-around athlete.

4-7

Empathic: You understand what makes other
people tick.

8-10

Furtive: You don’t like to stand out.

11-14

Inscrutable: Your emotions are difficult to read.

15-18 Observant: Little escapes your notice.

19-20

Sponge: You possess an open and receptive mind.

DYNAMIC

Acrobatics 6, Athletics 6

EMPATHIC

Insight 8, Persuasion 4

FURTIVE

Deception 6, Stealth 6

INSCRUTABLE

Deception 8, Perception 4

OBSERVANT

Insight 6, Perception 6

SPONGE

Expertise: Current Events 4, Expertise: Popular Culture 4,
Investigation 4

POWERS

Roll 1d20 once and record the result.

1-2

Animal Mimicry: Variable 10 (50 points, to mimic
Traits of one animal at a time), Continuous
• 80 points

Mental Duplication: Mind Reading 10, Limited
to Duplicated mind; Variable 10 (50 points, for
duplicating a subject’s mental traits), Continuous,
Resistible by Will • 80 points

Nemesis: Variable 8 (40 points, for traits suitable for
confronting a particular opponent), Continuous,
Free Action • 80 points

Object Mimicry: Variable 8 (40 points, for traits of

object touched), Reaction • 80 points

3-4

5-6

7-9

10-13

Power Duplication: Variable 10 (50 points, for

duplicating one target’s powers), Continuous
• 80 points

14-15

Power Theft: Cumulative Affliction 12 (Resisted

and Overcome by Will; Powers Impaired, Powers
Disabled, Transformed—Powerless) Linked to
Variable 8 (40 points, for duplicating one target’s
powers), Move Action, Limited to Afflicted
subjects • 80 points

16-17

Reflex Memory: Variable 8 (40 points, for observed
Skills and Advantages), Continuous, Free Action
• 80 points

18-20

Android Body: Immunity 30 (Fortitude Effects),
Reduced Traits (Stamina —, Fortitude —);
Protection 5 • 16 points

Power Duplication: Variable 8 (40 points, for

duplicating a target’s powers), Continuous • 64 points

DEFENSES

DODGE
+5

PARRY
+5

FORTITUDE
+5

TOUGHNESS
+0

WILL
+5

ABILITIES

POWERS

32

80

6

SKILLS

DEFENSES

TOTAL

12

20

150

•  Motivation—Acceptance: Due to the nature of their
powers, many Mimics feel as if they lack an identity of
their own. They may seek acceptance as unique indi-
v

[... truncated ...]
```

**Chunk 6** (`2b979f00a098`):

```
CHAPTER 5: ADVANTAGES .... 131
ACQUIRING

ADVANTAGES ............... 131

ADVANTAGE

DESCRIPTIONS ............. 131
Types of Advantages .........131
Accurate Attack ...................131
Agile Feint ..............................131
All-out Attack .......................131
Animal Empathy ..................131
Artificer ...................................131
Assessment ...........................132
Attractive................................132
Beginner’s Luck ....................134
Benefit, Ranked ....................134
Chokehold .............................134
Close Attack, Ranked .........134
Connected .............................134
Contacts .................................134
Daze .........................................134
Defensive Attack .................134
Defensive Roll .......................135
Diehard ...................................135
Eidetic Memory ...................135
Equipment,  ...........................135
Evasion ....................................135
Extraordinary Effort ............135
Fascinate ................................136
Fast Grab ................................136
Favored Environment ........136
Favored Foe ...........................136
Fearless ...................................136
Grabbing Finesse ................136
Great Endurance .................136
Hide in Plain Sight ..............136
Improved Aim ......................136
Improved Critical .................136
Improved Defense ..............136
Improved Disarm ................136
Improved Grab .....................137
Improved Hold .....................137
Improved Initiative .............137
Improved Smash .................137
Improved Trip .......................137
Improvised Tools .................137
Improvised Weapon ...........137
Inspire......................................137
Instant Up ..............................138
Interpose ................................138
Inventor ..................................138
Jack-of-All-Trades ................138
Languages, Ranked ............138
Leadership .............................138
Luck ..........................................139
Minion .....................................139
Move-by Action ...................139
Power Attack .........................139
Precise Attack .......................139
Prone Fighting .....................139

Quick Draw ............................139
Ranged Attack ......................139
Redirect ..................................139
Ritualist ................

[... truncated ...]
```

**Chunk 7** (`3a7f34326ad9`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

move  one  of  the  following  conditions  from  an  ally  with
whom you can interact: dazed, fatigued, or stunned.

LUCK

FORTUNE, RANKED (1/2 PL)

Once per round, you can choose to re-roll a die roll, like
spending a hero point (see Hero Points, page 20), includ-
ing adding 10 to re-rolls of 10 or less. You can do this a
number  of  times  per  game  session  equal  to  your  Luck
rank, with a maximum rank of half the series power level
(rounded down). Your Luck ranks refresh when your hero
points “reset”  at  the  start  of  an  adventure. The  GM  may
choose to set a different limit on ranks in this advantage,
depending on the series.

Generally speaking, languages are not terribly important
in comic book superhero stories except as background col-
or or occasional plot complications. Gamemasters should
allow  players  with  characters  fluent  in  other  languages
the occasional opportunity to show them off or put them
to good use. If you specifically set up the language barrier
as an obstacle by confronting the heroes with a language
they cannot possibly understand, that should count as a
complication and be worth a hero point.

COMBAT

MINION

GENERAL, RANKED

You can draw a weapon from a holster or sheath as a free
action, rather than a move action.

You have a follower or minion. This minion is an indepen-
dent  character  with  a  power  point  total  of  (advantage
rank x 15). Minions are subject to the normal power level
limits, and cannot have minions themselves. Your minions
(if capable of independent thought) automatically have a
helpful attitude toward you. They are subject to the nor-
mal rules for minions (see page 245).

Minions do not earn power points. Instead, you must spend
earned  power  points  to  increase  your  rank  in  this  advan-
tage to improve the minion’s power point total and traits.
Minions also do not have hero points. Any lost minions are
replaced in between adventures with other followers with
similar abilities at the Gamemaster’s discretion.

ACTION

COMBAT

When taking a standard action and a move action you can
move both before and after your standard action, provid-
ed the total distance moved isn’t greater than your normal
movement speed.

COMBAT

When  you  make  a  power  attack  (see  Maneuvers,  page
250)  you  can  take  a  penalty  of  up  to  –5  on  your  attack
bonus and add the same number (up to +5) to the effect
bonus of your attack.

[... truncated ...]
```

**Chunk 8** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 9** (`6717e2899e27`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

METAL

Beginner’s Luck, Eidetic Memory, Luck, Taunt

WATER

Assessment, Evasion, Trance, Uncanny Dodge

WOOD

Favored Environment (Choose One), Hide in Plain Sight, Precise
Attack (Close, Concealment), Teamwork

Roll 1d20 once and record the result.

1-4

Crane: You avoid direct confrontation, countering
and pinpointing weaknesses.

5-8

Dragon: Your style emphasizes versatility and balance.

9-12

13-16

Monastic: You learned your martial arts from a
temple or mystical city.

Ninja: You are skilled in the arts of stealth and
assassination.

17-20

Soldier: You were trained by the military.

AGENT

Acrobatics 4, Athletics 4, Close Combat: Unarmed 2, Insight 4,
Investigation 4, Perception 4, Stealth 6, Technology 4

MERCENARY

Acrobatics 4, Athletics 6, Close Combat: Unarmed 2, Expertise:
Streetwise 6, Insight 4, Intimidation 6, Perception 4

MONASTIC

Acrobatics 4, Athletics 4, Close Combat: Unarmed 2, Expertise:
Philosophy 6, Insight 6, Perception 6, Treatment  4

9-12

Leopard: You rely on sheer speed and eschew defense.

NINJA

13-16

Snake: You fight from unusual stances and positions
to catch your opponent off-guard.

17-20

Tiger: You strike with great strength and ferocity.

CRANE

Defensive Attack, Evasion, Grabbing Finesse, Improved
Defense, Improved Disarm, Instant Up, Move-by Action,
Redirect, Set-up

DRAGON

Accurate Attack, All-out Attack, Defensive Attack, Evasion,
Fast Grab, Grabbing Finesse, Improved Disarm, Improved Trip,
Move-by Action

LEOPARD

All-out Attack, Improved Critical (Unarmed), Improved
Initiative, Improved Trip, Move-by Action, Seize Initiative, Skill
Mastery (Acrobatics), Startle, Takedown

SNAKE

Chokehold, Defensive Attack, Fast Grab, Grabbing Finesse,
Improved Disarm, Improved Grab, Improved Hold, Prone
Fighting, Weapon Bind

TIGER

1-12

All-out Attack, Defensive Attack, Improved Critical (Unarmed),
Improved Smash, Move-by Action, Skill Mastery (Athletics),
Startle, Takedown, Weapon Break

SKILLS

If you rolled Mystic Endowment for Abilities, roll 1d20 once
and record the result. Otherwise, roll 1d20 twice (do not re-
roll if you get the same result twice) and record the results.

1-4

Agent: You work with a government or private spy
agency.

5-8

Mercenary: You contract out your fighting skills.

Acrobatics 6, Athletics 4, Close Combat: Unarmed 2,
Deception 4, Perception 4, Sleight of Hand 6, Stealth 6

SOLDIER

Acrobatics 4, Athletics 6, Cl

[... truncated ...]
```

**Chunk 10** (`6e58428e1e90`):

```
CHAPTER 6: POWERS

167

EXTRAS

Area: Your Luck Control effect works equally on all targets
in the affected area. You spend only one hero point, but
the subjects are each affected individually. You must ap-
ply the same effect to all subjects at once. +1 cost per rank.

Luck: Each rank in this extra gives you the benefit of a rank
in the Luck advantage (see Luck in the Advantages chap-
ter). It is subject to the same limits as the Luck advantage
set by the GM. Flat +1 point per rank of Luck.

Selective: This extra, applied to Area Luck Control, allows
you to choose who in the area is or is not affected by it. +1
cost per rank.

FLAWS

Action: If the action required for Luck Control is increased
beyond a reaction, it is only usable during your turn each

Effect:  Perception  Ranged  Damage,  Resisted  by  Will  •
4 points per rank

You can strike targets’ minds with “mental force,” inflict-
ing  Damage  resisted  by  the  target’s  Will  rather  than
Toughness, but having no effect on targets immune to
effects resisted by Will, such as inanimate objects. Men-
tal Blasts are often, but not always, Subtle as well, which
costs a flat 1 point.

MAGIC

Effect: Ranged Damage • 2 points per rank

You are a sorcerer, witch, or wizard, able to cast a variety
of magical spells. Your basic default effect is a Blast of
eldritch  force,  able  to  inflict  Ranged  Damage  (see  the
Blast power, previously).

However,  like  the  Energy  Control  power,  Magic  can
have a wide range of Alternate Effects, each a separate
spell you have mastered. The possibilities are virtually
limitless, within the bounds of your hero’s descriptors
and  the  Gamemaster’s  approval.  Examples  include
mystic  bindings  (Affliction,  see  the  Snare  version),
dispelling  magical  effects  (Nullify  Magic),  conjuring
clouds of mist or fog (an Area Visual Concealment At-
tack), scrying distant places (Remote Sensing), or slip-
ping  between  the  dimensions  to  appear  elsewhere
(Teleport), to name just a few.

All Magic effects have the “magic” descriptor regardless
of their other descriptors, so a Blast of flames conjured
with magic has both the “magic” and “fire” descriptors,
for example.

Magicians  often  have  a  Power  Loss  complication  (see
Complications  in  The  Basics  chapter):  if  they  are  un-
able to freely speak and gesture to cast their spells, they
cannot  use  Magic  (or  any  related  magical  powers  reli-
ant on spellcasting). Certain styles of Magic may impose
ot

[... truncated ...]
```

**Chunk 11** (`706d511e685d`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

both be Insubstantial and make an attack to make others
Insubstantial. +0 or +1 cost per rank.

suffer any damage from landing after a jump, so long as it
is within your maximum distance.

Continuous:  Extending  the  effect’s  duration  to  continu-
ous allows you to remain Insubstantial until you choose to
return to your corporeal form. +1 cost per rank.

Innate: Use this modifier if your character’s form is natu-
rally  or  innately  Insubstantial,  particularly  if  the  effect  is
permanent in duration. Flat +1 point.

Precise: This modifier allows you to selectively make some
portions of your body insubstantial while keeping others
substantial (or vice versa). This allows you to do things like
reach through a wall, solidify your hand to pick up an ob-
ject  or  tap  someone  on  the  shoulder  (or  punch  them  in
the face), and become incorporeal again to withdraw it on
the following round. Flat +1 point.

Progressive:  You  can  assume  lower  ranked  forms  of  In-
substantial, but you must progress through them in order
to reach the higher-ranked ones. For example if you have
Progressive Insubstantial 3, you can assume fluid, gaseous,
or energy forms, but to assume energy form, you must first
progress through fluid and gaseous, becoming less and less
substantial. Since you can only activate the effect once per
turn, it takes you three turns to get there. +0 cost per rank.

Reaction: Becoming Insubstantial is normally a free action,
meaning  you  can’t  switch  to  an  Insubstantial  form  when
surprised or otherwise unable to take action. At the GM’s
option, applying the Action extra to use Insubstantial as a
reaction allows you to switch forms “reflexively” in response
to such hazards, even if it is not your turn. +1 cost per rank.

Subtle:  This  extra  makes  your  Insubstantial  nature  less
noticeable  to  observers.  Rank  1  requires  a  Perception
check (DC 20) to detect that you are Insubstantial, while 2
ranks mean you look entirely normal in Insubstantial form
(which may cause opponents to waste effort on you, not
knowing  you  are  immune  to  their  attacks,  for  example).
Flat +1 or 2 points.

FLAWS

Absent Strength: This flaw applies only to rank 1 Insub-
stantial and removes your effective Strength while in that
form, leaving you with limited ability to affect the physical
world like the higher ranks of the effect. Flat –1 point.

Permanent: You are always Insubstantial; you

[... truncated ...]
```

**Chunk 12** (`75f616f43b9d`):

```
CHAPTER 2: SECRET ORIGINS

97

6-10

11-15

Jinx: Selective Burst Area Luck Control
2 (negate hero or luck point, force
re-roll), Luck 5 • 15 points

Lucky Cat: Selective Burst Area Luck

Control 2 (grant re-roll, bestow luck
point), Luck 5 • 15 points

16-20

Nine Lives: Immortality 15, Limited:
only works eight times • 15 points

Thick Hide: Protection 4, Impervious 11 • 15 points

Roll 1d20 once and record the result.

ELEPHANT

Groundstrike (Alternate Effect of Strength Damage):

Burst Area Affliction 10 (Resisted by Dodge,
Overcome by Fortitude; Hindered and Vulnerable,
Stunned and Prone), Extra Condition, Limited to Two
Degrees, Limited to targets on the ground • 1 point

1-10

Immovable: Immunity 10 (being moved), Sustained

• 10 points

Power-Lifting: Enhanced Strength 4, Limited to

Lifting • 4 points

Trunk: Extra Limb 1, Elongation 1 • 2 points

Tusks: Strength-based Damage 2, Improved Critical 2

• 4 points

RHINO

Armored Plates: Immunity 4 (critical hits, self-

inflicted slam damage) • 4 points

11-20

Great Horn: Strength-based Damage 3, Improved

Critical 2 • 5 points

Unstoppable Charge: Penetrating 15 on Damage,

Limited to slam attacks; Speed 4 (30 MPH) • 12 points

Reptilian Movement: Movement 1 (Slithering) • 2 points

Heat Sensing Pits: Senses 1 (Infravision) • 1 points

Scaly Hide: Protection 2 • 2 points

Roll 1d20 once and record the result.

CROCODILE

Aquatic: Movement 1 (Environmental Adaptation—

Aquatic), Swimming 6 (30 MPH) • 8 points

1-6

Brute Strength: Enhanced Strength 2 • 4 points

Regrowth: Regeneration 2 • 2 points

Rending Bite: Strength-based Damage 2, Improved

Critical, Secondary Effect • 17 points

LIZARD

Paralyzing Spit: Affliction 10 (Resisted by Dodge,

Overcome by Fortitude; Dazed, Stunned,
Paralyzed), Accurate 2, Reach 3 • 15 points

Prehensile Tail: Elongation 1, Extra Limb 1 • 2 points

Regrowth: Regeneration 1, Persistent • 2 points

Speedy: Leaping 2 (30 feet); Movement 2 (Wall-

crawling 2); Speed 3 (16 MPH) • 9 points

Teeth and Claws: Strength-based Damage 2,

Accurate • 3 points

7-13

98

SNAKE

Tensile Strength: Elongation 4 (120 feet); Enhanced

14-20

Strength 4, Limited to Grabs • 8 points

Venomous Bite: Progressive Weaken Stamina 7
(Resisted by Fortitude), Accurate 2 • 23 points

DEFENSE

DODGE
+6

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

WILL
+6

ABILITIES

POWERS

68

36

6

SKILLS

DEFENSES

TOTAL

20

20

150

•  Motivation—Acceptance: The Totem can be regard-
ed as a pariah or outcast in h

[... truncated ...]
```

**Chunk 13** (`8558df91a0a1`):

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

**Chunk 14** (`872471930ea9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HUMAN

STRENGTH
5
STAMINA
6

AGILITY
6
DEXTERITY
6

FIGHTING
10
INTELLECT
1

AWARENESS
4
PRESENCE
1

OTHERWORLDLY

STRENGTH
7
STAMINA
8

AGILITY
6
DEXTERITY
4

FIGHTING
8
INTELLECT
1

AWARENESS
2
PRESENCE
3

Agile Feint, Power Attack, Takedown

Take the advantages listed above, then roll 1d20 once on
both  the  Background  Advantages  table  and  the  Com-
bat Advantages table and record the results.

1-5

Field General: You know how to lead in battle.

6-10

Hunter: You honed your talents hunting the most
dangerous game or bounties.

11-15

Mysterious Past: Your memories are lost or
implanted but you demonstrate competence in
unexpected areas.

16-20

Survivor: You are always the last one standing.

ADVANTAGES—FIELD GENERAL

Inspire, Leadership, Teamwork

ADVANTAGES—HUNTER

Skill Mastery (Perception), Tracking, and Choose One: Favored
Environment or Favored Foe

ADVANTAGES—AGILE

Evasion, Grabbing Finesse, Improved Defense

ADVANTAGES—DARING

All-out Attack, Fearless, Improved Critical (Choose One Attack)

ADVANTAGES—GRAPPLER

Chokehold, Improved Grab, Improved Hold

ADVANTAGES—SKILLFUL

Accurate Attack, Defensive Attack, Precise Attack (Close;
Concealment)

SKILLS

Acrobatics 6, Athletics 6, Insight 4, Perception 6

Take the skills listed above, then roll 1d20 once and record
the result.

1-4

Advanced: You come from a society more highly
developed than our own.

5-8

Charismatic: You have a way with people.

9-12

Cultured: You are well learned and articulate.

13-16 Military: You are experienced in the ways of war.

17-20 Mystical: You are familiar with myth and magic.

ADVANCED

Technology 6, Vehicles 6

CHARISMATIC

Insight 6, Persuasion 6

CULTURED

Expertise: History 6, Persuasion 6

MILITARY

Expertise: Tactics 6, Intimidation 6

ADVANTAGES—MYSTERIOUS PAST

MYSTICAL

Beginner’s Luck, Benefit (Cipher), Language (Choose One)

Expertise: (Choose One: Magic or Mythology) 6, Insight 6

SURVIVOR

POWERS

Diehard, Great Endurance, Ultimate Effort (Toughness checks)

HUMAN

Roll 1d20 once and record the result.

1-5

Agile: You seldom suffer a solid hit.

6-10

Daring: You fight with a devil-may-care attitude.

11-15

Grappler: You like to keep your opponents right in
front of you.

16-20

Skillful: You fight with flair and precision.

1-4

Animalistic: Comprehend Animals 2; Enhanced

Stamina 2; Enhanced Skill 2 (Perception 4); Senses
6 (Acute and Tracking Smell, Danger Sense,

[... truncated ...]
```

**Chunk 15** (`9ab4a1de72d2`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

ADVANTAGE

Beginner’s Luck
Inspire
Leadership
Luck
Seize Initiative
Ultimate Effort

ADVANTAGE

Assessment
Benefit
Diehard
Eidetic Memory
Equipment
Extraordinary Effort
Fearless
Great Endurance
Instant Up
Interpose
Minion
Second Chance
Sidekick
Teamwork
Trance

ADVANTAGE

Agile Feint
Animal Empathy
Artificer
Attractive
Connected
Contacts
Daze
Fascinate
Favored Foe
Hide in Plain Sight
Improvised Tools
Inventor
Jack-of-all-trades
Languages
Ritualist
Skill Mastery
Startle
Taunt
Tracking
Well-informed

EFFECT

Spend a hero point to gain 5 temporary ranks in a skill.
Spend a hero point to grant allies a +1 circumstance bonus per rank.
Spend a hero point to remove a condition from an ally.
Re-roll a die roll once per rank.
Spend a hero point to go first in the initiative order.
Spend a hero point to get an effective 20 on a specific check.

EFFECT

Use Insight to learn an opponent’s combat capabilities.
Gain a significant perquisite or fringe benefit.
Automatically stabilize when dying.
Total recall, +5 circumstance bonus to remember things.
5 points of equipment per rank.
Gain two benefits when using extra effort.
Immune to fear effects.
+5 on checks involving endurance.
Stand from prone as a free action.
Take an attack meant for an ally.
Gain a follower or minion with (15 x rank) power points.
Re-roll a failed check against a hazard once.
Gain a sidekick with (5 x rank) power points.
+5 bonus to support team checks.
Go into a deathlike trance that slows bodily functions.

EFFECT

Feint using Acrobatics skill or movement speed.
Use interaction skills normally with animals.
Use Expertise: Magic to create temporary magical devices.
Circumstance bonus to interaction based on your looks.
Call in assistance or favors with a Persuasion check.
Make an initial Investigation check in one minute.
Use Deception or Intimidation to daze an opponent.
Use an interaction skill to entrance others.
Circumstance bonus to checks against a type of opponent.
Hide while observed without need for a diversion.
No penalty for using skills without tools.
Use Technology to create temporary devices.
Use any skill untrained.
Speak and understand additional languages.
Use Expertise: Magic to create and perform rituals.
Make routine checks with one skill under any conditions.
Use Intimidation to feint in combat.
Use Deception to demoralize in combat.
Use Perception to follow tracks.
Immediate Investigation or Persuasion check

[... truncated ...]
```

**Chunk 16** (`c1c422470246`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

TALENT

STRENGTH
1
STAMINA
1

AGILITY
2
DEXTERITY
2

FIGHTING
1
INTELLECT
3

AWARENESS
6
PRESENCE
2

Roll 1d20 once and record the result.

DABBLER

Expertise: (Choose One) 4, Insight 4, Perception 4

NINJA

Acrobatics 4, Perception 4, Stealth 4

SNEAK

Deception 4, Perception 4, Stealth 4

STUDENT

Expertise: (Choose One) 6, Insight 2, Perception 4

1-4

5-8

9-12

13-16

Charmed Life: You live a charmed life; maybe
you’re just lucky, but maybe it’s low-level psionic
influence... who can say?

POWERS

Contemplative: You are always calm and
controlled.

Perfect Mind: You use a greater percentage of
your mind.

Thought Leader: You use your abilities to help
others reach greater heights.

Roll  1d20  once  to  determine  if  you  should  roll  on  the
Psionic,  Mentalist,  or  Telekinetic  table,  then  roll  1d20
again on that table and record the result.

17-20

Trained Fighter: You know how to fight.

LIFE

Attractive, Fascinate (Persuasion), Luck

CONTEMPLATIVE

Fearless, Trance, Ultimate Effort (Will checks)

MIND

Eidetic Memory, Jack-of-all-trades, Ultimate Effort (Will checks),

LEADER

Choose either: Inspire, Leadership, and Teamwork, or Inspire 2
and Leadership or Teamwork

FIGHTER

Improved Initiative, Power Attack, Uncanny Dodge

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-4

5-8

Charmer: You’re good with people.

Dabbler: You dabble in whatever interests you.

9-12

Ninja: You have been trained in the way of the ninja.

13-16

17-20

Sneak: You’re sneaky and underhanded when you
need to be.

11-15

Student: You’re a high-school, college, or post-
graduate student.

CHARMER

Deception 4, Insight 4, Persuasion 4

Psionic: Take Telepathy, listed immediately below,

then roll on the Psionic Table.

Telepathy: Mind Reading 5 Linked to Area Mental

Communication 3 • 25 points

Psionic Table: Roll 1d20 once and record the result
as the first power of an array, then roll 1d20 twice
and add each result as a 1-point Alternate Effect (re-
roll if you get the same result as your first roll).

1-3

4-7

ESP: Remote Sensing 6 (Normal Visual,
Normal Auditory, Mental) • 24 points

Mental Blast: Perception Range Damage

6, Resisted by Will • 24 points

1-10

8-11

Psi-Knife: Damage 8, Penetrating 4,

Accurate 4, Resisted by Will • 24 points

12-14

15-17

Psionic Invisibility: Concealment 10,

Affects Others, Limited—Concealme

[... truncated ...]
```

**Chunk 17** (`d5fc086574e9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

LUCKY

Beginner’s Luck, Luck 2, Redirect

RESOURCES

Equipment 4 (Headquarters)

8-14

Super-strength: Enhanced Strength 4 • 8 points

15-20

Soldier: Enhanced Trait 4 (Close Attack 4); Power-

lifting 4 • 8 points

Headquarters—Size: Gargantuan, Toughness: 12; Features:
Communications, Computer, Gym, Infirmary, Isolated,
Laboratory, Library, Living Space, Personnel, Power System,
Security System, Teleport (Affects Others), Workshop • 20 points

WARRIOR

All-out Attack, Improved Initiative, Interpose, Move-by Action

Immunities: Immunity 10 (Life Support) • 10 points

Invulnerability: Protection 4 • 4 points

Roll 1d20 once and record the result.

WEALTHY

Benefit 4 (Multi-millionaire)

SKILLS

1-15

Flight: Flight 8 (500 MPH) • 16 points

16-20

Super Movement: Speed 3 (16 MPH); Leaping 7

(900 feet); Movement 3 (Swinging, Wall-crawling
2) • 16 points

Roll  1d20  twice  (re-roll  if  you  get  the  same  result  twice)
and record the results.

If you have the Superhuman or Vessel set of abilities, role
once on this table. Do not roll on this table otherwise.

1-5

Athlete: You’re a trained athlete.

6-10

Broad Training: You have a broad set of skills from
your education or experiences.

11-15

Charismatic: You’re good with people.

16-20

Learned: You’re well educated, with some
technological training.

ATHLETE

Acrobatics 6, Athletics 6, Perception 4

TRAINING

1-4

5-7

8-11

Improved Invulnerability: Impervious Toughness 6

• 6 points

Inhuman Physiology: Enhanced Advantage 1

(Diehard); Immunity 2 (Critical Hits); Regeneration 3
• 6 points

Enhanced Senses: Senses 6 (Extended Auditory
2, Extended Vision 2, Microscopic Vision, Ultra-
Hearing) • 6 points

12-15 Quickness: Quickness 6 • 6 points

16-18

Telepathy: Mental Communication 1, Subtle 2

• 6 points

19-20

Traveler: Movement 3 (Dimension Travel 3) • 6 points

Expertise: (Choose One) 4, Insight 2, Perception 2, Persuasion
4, Ranged Combat: Throwing 4

CHARISMATIC

Expertise: (Choose One) 4, Insight 4, Perception 4, Persuasion 4

DEFENSE

LEARNED

Expertise: (Choose One) 6, Perception 4, Technology 6

POWERS

DODGE
+4

PARRY
+4

FORTITUDE
+4

TOUGHNESS
+0

SUPERHUMAN/VESSEL

DODGE
+4

PARRY
+0

FORTITUDE
+2

TOUGHNESS
+0

WILL
+6

WILL
+6

If you have the Man of Action Abilities, don’t roll for your
Offensive Power, instead, take Find Weakness:

Find Weakness: Strength-based Damage 4; Enhanced

Advantage 4 (Close At

[... truncated ...]
```

**Chunk 18** (`dd5713402cfd`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL 7

STR
STA

8  AGL
8  DEX

0
0

FGT
INT

6  AWE
PRE
0

0
2

Powers: Foot Stomp (Line Area Damage 7,
Limited—Must be on same surface as target);
Super-Movement (Leaping 6 (500 feet));
Super-Tough (Immunity 10 (Life Support),
Impervious Toughness 4)

14-20

Advantages: Accurate Attack, All-out Attack,
Diehard, Fast Grab, Set-up 2, Takedown,
Teamwork

Skills: Athletics 3 (+11), Intimidation 4 (+6),
Perception 5 (+5)

Offense: Init +0, Unarmed +6 (Close, Damage 8)

Defense: Dodge 6, Parry 6, Fort 8, Tou 8, Will 6

Totals: Abilities 48 + Powers 26 + Advantages 8
+ Skills 6 + Defenses 12 = 100

SUMMONER

Roll 1d20 once on this table if you have the Summoner set
of Abilities and record the result.

15-20

Equipment: Bow (Ranged Damage 3),
Club (Strength-based Damage 2), Knife
(Strength-based Damage 1, Improved
Critical), Nunchaku (Strength-based
Damage 2, Improved Critical), Shuriken
(Ranged Multiattack Damage 1), Sword
(Strength-based Damage 3, Improved
Critical)

Advantages: Equipment 4, Evasion, Hide
in Plain Sight, Quick Draw

Skills: Acrobatics 6 (+10), Athletics 6 (+8),
Perception 3 (+5), Ranged Combat (Ninja
Weapons) 3 (+7), Sleight of Hand 4 (+8),
Stealth 10 (+14)

Offense: Init +4, Bow +7 (Ranged, Damage
3), Sword +7 (Close, Damage 5, Crit. 19-20),
Unarmed +7 (Close, Damage 2)

Defense: Dodge 10, Parry 10, Fort 6, Tou
2, Will 6

Totals: Abilities 42 + Powers 8 + Advantages
7 + Skills 16 + Defenses 17 = 90

ROBOTS

PL 6

8  AGL

STR
STA  —  DEX  0

2  FGT

2  AWE

0
INT  —  PRE  —

Imaginary Friend: Summon 10 (One PL10,

150-point character; Choose or roll up another
character using the tables in this book and use
that as your summoned creature. Note: the
summoned creature may not have minions, a
headquarters, or any other traits the GM decides
are outside the scope of the Summon power),
Controlled, Heroic, Mental Link • 51 points

Roll 1d20 once and record the result. (Only roll on
this table if you Summon the Imaginary Friend.)

1-4

5-8

Invisibility: Concealment 10 (All
senses), Blending • 10 points

Lucky: Luck Control 2 (Force a re-roll,
Negate luck), Luck 4 • 10 points

9-12

Mimic: Variable 2 (10 points),

Limited—Can only mimic a trait of
Imaginary Friend, Increased Action
(Standard), Tiring • 10 points

13-16

Shapechange: Morph 2 (Humanoids)

• 10 points

17-20

Projections: Create 5 • 10 points

Summon Animals: Summon 4 (Sixteen PL4,

60-point minions; You can s

[... truncated ...]
```

---

## Concept: Luck Control

Chunk count: 6
Receives actions: ['act_0016', 'act_0250']

### Chunk texts

**Chunk 1** (`27cd3f53557a`):

```
CHAPTER 6: POWERS ........ 143
POWERS ..... 143
Power Costs ...........................143
Power Descriptors...............143
TYPES ................. 144
WORK ..... 145
Effect Checks ........................145
Effect Parameters ................145
Countering Effects ..............147
EFFECTS ............ 149
Affliction .................................149
Burrowing ..............................151
Communication ...................151
Comprehend.........................152
Concealment ........................153
Create ......................................154
Damage ..................................156
Deflect .....................................157
Elongation .............................158
Enhanced Trait .....................158
Environment .........................159
Extra Limbs ............................160
Feature ....................................160
Flight ........................................161
Growth ....................................162
Healing ....................................162
Illusion .....................................163
Immortality ...........................164
Immunity ...............................165
Insubstantial .........................166
Leaping ...................................167
Luck Control ..........................167
Mind Reading .......................169
Morph......................................170
Move Object .........................171
Movement .............................172
Nullify ......................................173
Protection ..............................174

INTRODUCTION .....................5
```

**Chunk 2** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 3** (`6e58428e1e90`):

```
CHAPTER 6: POWERS

167

EXTRAS

Area: Your Luck Control effect works equally on all targets
in the affected area. You spend only one hero point, but
the subjects are each affected individually. You must ap-
ply the same effect to all subjects at once. +1 cost per rank.

Luck: Each rank in this extra gives you the benefit of a rank
in the Luck advantage (see Luck in the Advantages chap-
ter). It is subject to the same limits as the Luck advantage
set by the GM. Flat +1 point per rank of Luck.

Selective: This extra, applied to Area Luck Control, allows
you to choose who in the area is or is not affected by it. +1
cost per rank.

FLAWS

Action: If the action required for Luck Control is increased
beyond a reaction, it is only usable during your turn each

Effect:  Perception  Ranged  Damage,  Resisted  by  Will  •
4 points per rank

You can strike targets’ minds with “mental force,” inflict-
ing  Damage  resisted  by  the  target’s  Will  rather  than
Toughness, but having no effect on targets immune to
effects resisted by Will, such as inanimate objects. Men-
tal Blasts are often, but not always, Subtle as well, which
costs a flat 1 point.

MAGIC

Effect: Ranged Damage • 2 points per rank

You are a sorcerer, witch, or wizard, able to cast a variety
of magical spells. Your basic default effect is a Blast of
eldritch  force,  able  to  inflict  Ranged  Damage  (see  the
Blast power, previously).

However,  like  the  Energy  Control  power,  Magic  can
have a wide range of Alternate Effects, each a separate
spell you have mastered. The possibilities are virtually
limitless, within the bounds of your hero’s descriptors
and  the  Gamemaster’s  approval.  Examples  include
mystic  bindings  (Affliction,  see  the  Snare  version),
dispelling  magical  effects  (Nullify  Magic),  conjuring
clouds of mist or fog (an Area Visual Concealment At-
tack), scrying distant places (Remote Sensing), or slip-
ping  between  the  dimensions  to  appear  elsewhere
(Teleport), to name just a few.

All Magic effects have the “magic” descriptor regardless
of their other descriptors, so a Blast of flames conjured
with magic has both the “magic” and “fire” descriptors,
for example.

Magicians  often  have  a  Power  Loss  complication  (see
Complications  in  The  Basics  chapter):  if  they  are  un-
able to freely speak and gesture to cast their spells, they
cannot  use  Magic  (or  any  related  magical  powers  reli-
ant on spellcasting). Certain styles of Magic may impose
ot

[... truncated ...]
```

**Chunk 4** (`792ccb4b72a0`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

be capable of using the advantage and cannot gain the
benefits  of  fortune  advantages,  only  other  types.  If  the
advantage has any prerequisites, you must have them to
gain the benefits of the advantage as a heroic feat.

One hero point allows you to re-roll any die roll you make
and take the better of the two rolls. On a result of 1 through
10 on the second roll, add 10 to the result, an 11 or higher
remains as-is (so the re-roll is always a result of 11-20). You
must spend the hero point to improve a roll before the GM
announces the outcome of your initial roll. You cannot spend
hero  points  on  die  rolls  made  by  the  GM  or  other  players
without the Luck Control effect (see the Powers chapter).

You can spend a hero point to get sudden inspiration in
the form of a hint, clue, or bit of help from the GM. It might
be a way out of the villain’s fiendish deathtrap, a vital clue
for solving a mystery, or an idea about the villain’s weak-
ness. It’s up to the GM exactly how much help the players
get from inspiration and how it manifests, but since hero
points are a very limited resource, the help should be in
some way significant.

You can spend a hero point to attempt to counter an ef-
fect  used  against  you  as  a  reaction.  See  Countering  Ef-
fects in the Powers chapter for details.

RECOVER

You can spend a hero point to recover faster. A hero point
allows  you  to  immediately  remove  a  dazed,  fatigued,  or
stunned condition, without taking an action. Among oth-
er things, this option allows you to use extra effort (pre-
viously)  without  suffering  any  fatigue.  Spending  a  hero
point to recover also lets you convert an exhausted condi-
tion into a fatigued condition.

In  comic  book  stories,  heroes  often  confront  the  villain(s)
and deal with various setbacks. Perhaps the villain defeats or
outwits them in the first couple scenes. Maybe one or more
of  the  heroes  have  to  overcome  a  personal  problem. The
villain may have a secret the heroes need to discover, and
so forth. By the end of the story, the heroes have overcome
these challenges and they’re ready to take on the villain.

reflects this kind of story structure
through the awarding of hero points. The heroes gain ad-
ditional hero points as an adventure progresses. When the
going gets tough, the heroes get tougher, because they
get hero points to help them overcome future challenges.

Heroes ge

[... truncated ...]
```

**Chunk 5** (`9c7fcc5049c4`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

round, which limits its usefulness in responding to the ac-
tions of others. –1 cost per rank.

Ranged: Luck Control normally requires no attack check;
if Ranged, it does. –1 cost per rank.

Resistible: Targets  of  your  Luck  Control  get  a  resistance
check—usually Dodge or Will—to avoid its effects. –1 cost
per rank.

Side Effect: As a particular side effect of Luck Control, if
your  effort  to  alter  luck  fails,  you  suffer  a  setback  with-
out earning a hero point. Effectively the GM gains a “free”
complication against you. –1 or –2 cost per rank.

SENSORY

Effect:  Perception  Ranged,  Cumulative  Affliction,  Re-
sisted by Will • 4 points per rank

You  can  impose  your  will  on  others,  forcing  them  to
obey  your  commands. Targets  failing  a Will  resistance
check against your effect DC first become dazed, then
compelled, as they try to fight off your influence. Finally,
with  three  or  more  degrees  of  effect,  the  target  be-
comes controlled and obeys any commands you give.

Degrees  of  failure  on  resistance  checks  against  Mind
Control are cumulative. You can also apply the Progres-
sive modifier (see the Affliction effect) so your mental
hold  increases  each  time  the  target  fails  a  resistance
check against it!

Action: Standard • Range: Perception
Duration: Sustained • Cost: 2 point per rank

MIMIC

You can read another character’s mind. To use Mind Read-
ing,  make  an  opposed  effect  check  against  the  result  of
the target’s Will check. The degree of success determines
the degree of contact:

1

2

3

4

Surface  thoughts: You  can  read  what  the
target  is  presently  thinking.  Mind  Reading
transcends language; you comprehend the
target’s thoughts whether or not you share
a common language.

Personal thoughts: You can probe deeper
into  the  target’s  mind  for  information. You
can  essentially  ask  any  one  question  and
receive  the  answer  from  the  target’s  mind.
If the target doesn’t know the answer, then
you know that as well.

Memory: You can read the subject’s memo-
ries  and  recollections.  This  allows  you  to
perceive  them  exactly  as  the  target  recalls
them, one memory per round.

Subconscious:  You  can  read  memories
from the target’s subconscious, things even
the  target  does  not  consciously  know. This
might mean repressed or hidden memories,
deep-seated psychological traumas, or even
other personalities.

If  you 

[... truncated ...]
```

**Chunk 6** (`dd5713402cfd`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL 7

STR
STA

8  AGL
8  DEX

0
0

FGT
INT

6  AWE
PRE
0

0
2

Powers: Foot Stomp (Line Area Damage 7,
Limited—Must be on same surface as target);
Super-Movement (Leaping 6 (500 feet));
Super-Tough (Immunity 10 (Life Support),
Impervious Toughness 4)

14-20

Advantages: Accurate Attack, All-out Attack,
Diehard, Fast Grab, Set-up 2, Takedown,
Teamwork

Skills: Athletics 3 (+11), Intimidation 4 (+6),
Perception 5 (+5)

Offense: Init +0, Unarmed +6 (Close, Damage 8)

Defense: Dodge 6, Parry 6, Fort 8, Tou 8, Will 6

Totals: Abilities 48 + Powers 26 + Advantages 8
+ Skills 6 + Defenses 12 = 100

SUMMONER

Roll 1d20 once on this table if you have the Summoner set
of Abilities and record the result.

15-20

Equipment: Bow (Ranged Damage 3),
Club (Strength-based Damage 2), Knife
(Strength-based Damage 1, Improved
Critical), Nunchaku (Strength-based
Damage 2, Improved Critical), Shuriken
(Ranged Multiattack Damage 1), Sword
(Strength-based Damage 3, Improved
Critical)

Advantages: Equipment 4, Evasion, Hide
in Plain Sight, Quick Draw

Skills: Acrobatics 6 (+10), Athletics 6 (+8),
Perception 3 (+5), Ranged Combat (Ninja
Weapons) 3 (+7), Sleight of Hand 4 (+8),
Stealth 10 (+14)

Offense: Init +4, Bow +7 (Ranged, Damage
3), Sword +7 (Close, Damage 5, Crit. 19-20),
Unarmed +7 (Close, Damage 2)

Defense: Dodge 10, Parry 10, Fort 6, Tou
2, Will 6

Totals: Abilities 42 + Powers 8 + Advantages
7 + Skills 16 + Defenses 17 = 90

ROBOTS

PL 6

8  AGL

STR
STA  —  DEX  0

2  FGT

2  AWE

0
INT  —  PRE  —

Imaginary Friend: Summon 10 (One PL10,

150-point character; Choose or roll up another
character using the tables in this book and use
that as your summoned creature. Note: the
summoned creature may not have minions, a
headquarters, or any other traits the GM decides
are outside the scope of the Summon power),
Controlled, Heroic, Mental Link • 51 points

Roll 1d20 once and record the result. (Only roll on
this table if you Summon the Imaginary Friend.)

1-4

5-8

Invisibility: Concealment 10 (All
senses), Blending • 10 points

Lucky: Luck Control 2 (Force a re-roll,
Negate luck), Luck 4 • 10 points

9-12

Mimic: Variable 2 (10 points),

Limited—Can only mimic a trait of
Imaginary Friend, Increased Action
(Standard), Tiring • 10 points

13-16

Shapechange: Morph 2 (Humanoids)

• 10 points

17-20

Projections: Create 5 • 10 points

Summon Animals: Summon 4 (Sixteen PL4,

60-point minions; You can s

[... truncated ...]
```

---

## Concept: Macabre

Chunk count: 1

### Chunk texts

**Chunk 1** (`6890e166bca9`):

```
CHAPTER 2: SECRET ORIGINS

29

A lot of background details go into making your hero more than just a collection of numbers. Take a moment (if you
haven’t already) to consider some of the following things about your character:

NAME

What is your character’s name? That is to say, what is the
name  the  hero  uses  in  public,  that  appears  in  one-inch
type  in  the  newspaper  headlines?  Most  heroes  adopt
unique  and  distinctive “code  names,”  so  consider  a  suit-
able name for yours. Code names are often based on pow-
ers, theme, or style. Here are some options to consider:
ORIGIN

A name may be based on the hero’s origin, power source,
nation (or even world) of birth, and such.
POWERS

Choose a name based on the hero’s powers: Firestarter or
Blaze for a flame-controlling character, Thunder or Spark
for an electrical character, and so forth.

THEME

Maybe  the  character  has  a  theme  or  style  suggesting  a
name: Paladin might be a medieval knight displaced into
the present day, with a magical sword and armor. Madame
Macabre may be all about magic and the occult.

TITLES

Names  may  include  various  titles  like  Mister,  Miss,  Ms.,
Doctor,  Sir,  Lord,  Lady,  and  Madam  or  even  royal  titles
like  King,  Queen,  Prince,  Princess,  Duke,  Baron,  Emperor
and so forth. Military ranks are also popular parts of hero
names, especially General, Major, and Captain.
GENDER

Names often include gender designations like Man/Wom-
an, Boy/Girl, Lad/Lass, and so forth.
SOUND

Some  code-names  don’t  really  have  anything  to  do  with  a
character’s powers or background—they just sound cool: Kis-
met, Scion, Animus, Damask, and so forth. They may hint at
the hero’s powers or origin, or have nothing to do with them.

REAL NAME

Some heroes go by their given name, not using a code-
name at all. Oftentimes these names still sound like code-

names,  however.  They  may  also  be  nicknames,  such  as
“Dash” for someone with the name Dashell, or “Buzz” for
someone  with  the  name  Buzcinski,  or  whatever  other
nickname a character may have, such as “Stretch” or “Tiny”.

ORIGIN

What’s  the  origin  of  your  hero’s  powers?  It  can  be  any-
thing from a character born with the potential for powers
to someone granted them by an accident—exposure to a
strange meteor, radiation, genetic engineering, or any of
countless similar encounters. Here are some of the more
common superhero origins:
ACCIDENT

Perhaps  the  most  common  origin. The  hero  

[... truncated ...]
```

---

## Concept: Magic

Chunk count: 18
Performs actions: ['act_0247', 'act_0248', 'act_0454']
Receives actions: ['act_0302']

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

**Chunk 2** (`1b8011530852`):

```
CHAPTER 2: SECRET ORIGINS

101

11-15

16-20

Vigilante: You use your weapons to fight crime and
injustice.

Weaponsmith: You craft your own weapons and
even augment them with the latest technology.

SOLDIER

Expertise: Military 6, Vehicles 6

TIME-DISPLACED

PERSONALITY

Deception 8, Intimidation 8, Persuasion 8

TALKER

Deception 10, Insight 4, Persuasion 10

POWERS

Expertise: History 6, Choose One: Expertise: Magic 6 or
Technology 6

VIGILANTE

Roll 1d20 once and record the result.

Expertise: Streetwise 6, Investigation 6

WEAPONSMITH

Expertise: Weapons 6, Technology 6

Roll 1d20 once and record the result.

1-6

Flamboyant: You fight with great flair.

7-14

Instinctive: You let your well-honed reflexes take over.

15-20

Sneaky: You prefer to avoid a direct confrontation.

FLAMBOYANT

Acrobatics 8, Athletics 4, Sleight of Hand 4

INSTINCTIVE

Acrobatics 6, Athletics 6, Stealth 4

SNEAKY

Acrobatics 6, Athletics 4, Stealth 6

Roll 1d20 once and record the result.

1-4

5-8

Assertive: You know how and when to take charge.

Cunning: You are good at manipulating others.

9-12

Empathic: You seem to understand others.

13-16

Forceful Personality: Others seem to instinctively
respect you.

17-20

Smooth Talker: You know how to get your way.

ASSERTIVE

Insight 8, Intimidation 8, Persuasion 8

CUNNING

Deception 10, Insight 8, Perception 6

EMPATHIC

Insight 10, Perception 6, Persuasion 8

Bow and Trick Arrows: Array (10 points plus five

Alternate Effects), Easily Removable (-6 points) • 9
points total

Standard Arrow: Ranged Damage 5 • 10 points

Roll 1d20 five times (re-roll if you get the same result
twice) and add them to the Bow and Trick Arrows
array as Alternate Effects.

1-2

3-4

5-6

7-8

1-5

9-10

11-12

13-14

15-16

17-18

19-20

•  Boomerang Arrow: Ranged Damage

4, Homing, Subtle • 1 point

•  Boxing Glove Arrow: Ranged
Affliction 5 (Resisted by Dodge,
Overcome by Fortitude; Dazed,
Stunned, Incapacitated) • 1 point

•  Cable Arrow: Movement 1

(Swinging) • 1 point (if you get this
result twice, place the Cable Arrow
outside the array instead for 2
points): Cable Arrow: Movement 1
(Swinging) • 2 points

•  Explosive Arrow: Burst Area Ranged
Damage 5, Unreliable (five uses)
• 1 point

•  Flare Arrow: Ranged Cumulative

Affliction 5 (Resisted and Overcome
by Fortitude; Visually Impaired,
Visually Disabled, Visually Unaware),
Limited to One Sense • 1 point

•  Knockout Gas Arrow: Burst Area
Ranged Affliction 5 (Resisted and
Overcome by Fort

[... truncated ...]
```

**Chunk 3** (`3788ea99174b`):

```
CHAPTER 7: GADGETS & GEAR

211

Example:  Makeshift  needs  to  whip  up  a  mind-
shielding  device  to  confront  Gepetto,  who  has
seized control of his teammates. Immunity to Mind
Control (a common Affliction effect) cost 5 power
points, so the Technology check is DC 15 (10 + 5)
and takes 5 hours. Makeshift’s skill bonus is +15, so
he succeeds automatically. The construction check
is  also  DC  15  (10  +  the  device’s  cost).  It  takes  20
hours. Makeshift again succeeds automatically on
the  check.  However,  that’s  25  hours  total  to  build
the  mind-shield,  and  Gepetto  plans  to  send  his
new “puppets” into action in just a few hours. Even
taking a –15 check penalty to cut the time to one-
eighth only takes it down to just over three hours.
Makeshift needs that device right now, so he’s go-
ing to need to speed things up....

you speed up the process any further by taking a check
penalty.  You  can  use  a  jury-rigged  invention  again  by
spending another hero point.

Example:  Needing  to  get  the  mind  shield  device
ready  right  away,  Makeshift’s  player  decides  to
spend a hero point to jury-rig it. He skips the design
step  altogether  and  reduces  construction  time  to
5 rounds (just under a minute). The DC of the con-
struction check increases to 20, but still well within
Makeshift’s skill; the player only needs to roll a 5 or
better. He rolls a 25 result on the check and, a min-
ute later, Makeshift has a makeshift mind-shield he
hopes will protect him from Gepetto’s power long
enough to try and free his teammates from the vil-
lain’s influence.

DEVICES

MISHAPS

An inventor can choose to spend a hero point to jury-rig a
device; ideal for when a particular device is needed right
now.  When  jury-rigging  a  device,  skip  the  design  check
and  reduce  the  time  of  the  construction  check  to  one
round  per  power  point  of  the  device’s  cost,  but  increase
the DC of the check by +5. The inventor makes the check
and, if successful, has use of the device for one scene be-
fore it burns out, falls apart, blows up, or otherwise fails.
You can’t jury-rig an invention as a routine check, nor can

At  the  GM’s  discretion,  three  or  more  degrees  of  failure,
or a natural roll of 1, on any required inventing skill check
may result in some unexpected side-effect or mishap. Ex-
actly  what  depends  heavily  on  the  invention.  Inventing
mishaps can become a source of adventure ideas and put
the heroes in some diff

[... truncated ...]
```

**Chunk 4** (`3a7f34326ad9`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

move  one  of  the  following  conditions  from  an  ally  with
whom you can interact: dazed, fatigued, or stunned.

LUCK

FORTUNE, RANKED (1/2 PL)

Once per round, you can choose to re-roll a die roll, like
spending a hero point (see Hero Points, page 20), includ-
ing adding 10 to re-rolls of 10 or less. You can do this a
number  of  times  per  game  session  equal  to  your  Luck
rank, with a maximum rank of half the series power level
(rounded down). Your Luck ranks refresh when your hero
points “reset”  at  the  start  of  an  adventure. The  GM  may
choose to set a different limit on ranks in this advantage,
depending on the series.

Generally speaking, languages are not terribly important
in comic book superhero stories except as background col-
or or occasional plot complications. Gamemasters should
allow  players  with  characters  fluent  in  other  languages
the occasional opportunity to show them off or put them
to good use. If you specifically set up the language barrier
as an obstacle by confronting the heroes with a language
they cannot possibly understand, that should count as a
complication and be worth a hero point.

COMBAT

MINION

GENERAL, RANKED

You can draw a weapon from a holster or sheath as a free
action, rather than a move action.

You have a follower or minion. This minion is an indepen-
dent  character  with  a  power  point  total  of  (advantage
rank x 15). Minions are subject to the normal power level
limits, and cannot have minions themselves. Your minions
(if capable of independent thought) automatically have a
helpful attitude toward you. They are subject to the nor-
mal rules for minions (see page 245).

Minions do not earn power points. Instead, you must spend
earned  power  points  to  increase  your  rank  in  this  advan-
tage to improve the minion’s power point total and traits.
Minions also do not have hero points. Any lost minions are
replaced in between adventures with other followers with
similar abilities at the Gamemaster’s discretion.

ACTION

COMBAT

When taking a standard action and a move action you can
move both before and after your standard action, provid-
ed the total distance moved isn’t greater than your normal
movement speed.

COMBAT

When  you  make  a  power  attack  (see  Maneuvers,  page
250)  you  can  take  a  penalty  of  up  to  –5  on  your  attack
bonus and add the same number (up to +5) to the effect
bonus of your attack.

[... truncated ...]
```

**Chunk 5** (`3c75d5b04a0e`):

```
CHAPTER 2: SECRET ORIGINS

41

Power Point Totals:  Abilities 32 + Powers 84  + Advantages 1 + Skills  12 + Defenses 21  = 150

PL10PL10

MYSTIC
MYSTIC

STRENGTH
0
STAMINA
0

POWERS

AGILITY
1
DEXTERITY
3

FIGHTING
4
INTELLECT
3

AWARENESS
6
PRESENCE
4

Astral Projection: Remote Sensing 10 (visual,

auditory, mental), physical body is defenseless,
Subtle 2 • 32 points.

•  Levitation: Flight 4 (30 MPH) and

Mystic Shield: Protection 12, Impervious,
Sustained • 1 point.

Mystic Senses: Senses 2 (Magical
Awareness, Radius) • 2 points.

Spellcasting: Ranged Damage 12

(mystic blast) • 24 points.

•  Choose five Alternate Effects • 5 points.

Fearless, Ranged Attack 5, Ritualist, Trance

SKILLS

Expertise: Magic 10 (+13), Insight 6 (+12),
Intimidation 4 (+8), Perception 4 (+10), Sleight of Hand 4 (+7)

OFFENSE

INITIATIVE +1

Spellcasting +8

Ranged, Damage 12 plus others

Unarmed +4

Close, Damage 0

DEFENSE

DODGE

PARRY

WILL

FORTITUDE

TOUGHNESS

6

12

8

6

13

Power Point Totals:  Abilities 42 + Powers 64  + Advantages 8 + Skills  14 + Defenses 22  = 150

42

```

**Chunk 6** (`3e277f7add29`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

11-15

Powerful Connection: You have a strong
connection or mastery over the magic at your
command.

16-20

Student of the Arts: You study and research
constantly in order to keep informed.

CENTERED

Fearless, Ultimate Effort (Will checks)

ENCHANTER

Artificer, Skill Mastery (Expertise: Magic)

3-4

5-6

7-8

9-10

11-12

13-14

CONNECTION

15-16

Accurate Attack, Power Attack

ARTS

Ritualist, Well-informed

SKILLS

17-18

19-20

•  Dispel Magic: Nullify 8, Broad (Magic),

Simultaneous • 1 point

•  Enervation: Ranged Weaken 8, Broad (Physical

Abilities (one at a time)) • 1 point

•  Enhanced Strength: Enhanced Strength 9;
Enhanced Trait 6 (Close Attack 6) • 1 point

•  Ghost Hands: Perception Move Object 7, Precise,

Subtle 2 • 1 point

•  Healing Hand: Healing 5, Energizing, Persistent,

Restorative, Stabilize • 1 point

•  Maddening Blast: Ranged Damage 8, Resisted by

Will • 1 point

•  Mystic Bindings: Ranged Affliction 12 (Resisted
and Overcome by Will; Hindered and Vulnerable,
Defenseless and Immobile), Extra Condition,
Limited Degree • 1 point

•  Mystic Constructs: Create 7, Continuous, Innate,

Precise, Subtle • 1 point

•  Phantasms: Illusion 4 vs. All Senses, Area (30

cubic feet), Resistible by Will, Selective • 1 point

Expertise: Magic 10, Insight 6, Perception 4

Take the skills listed above, then roll 1d20 once and record
the result.

Astral Projection (Remote Sensing 8 (Visual, Auditory,

Mental), Limited—Physical body is defenseless, Subtle
2), AE: Levitation and Mystic Shield (Flight 4 (30 MPH);
Sustained Protection 12, Impervious 6) • 27 points

1-8

Affecting Presence: You have the skills necessary to
explore new places.

9-14

Occult Investigator: You make it a point to
investigate unusual crimes. You may even consult for
the police.

15-20

Prestidigitator: You’ve studied the art of deception.

PRESENCE

Intimidation 4, Persuasion 4

INVESTIGATOR

Investigation 4, Sleight of Hand 4

PRESTIDIGITATOR

Deception 4, Sleight of Hand 4

POWERS

Magic Spells: Array (24 points, plus 5 points of Alternate

Effects)

•  Magical Blast: Ranged Damage 12 • 24 points

Take the Magic Spells and Magical Blast (above), plus roll
1d20 five times (re-roll if you get the same result twice) and
add them to the Magic Spells array as Alternate Effects.

1-2

•  Billowing Darkness: Ranged Burst Area
Concealment 4 Attack (All Visual) • 1 point

Roll 1d20 once and record the 

[... truncated ...]
```

**Chunk 7** (`44458c4fcb7e`):

```
CHAPTER 6: POWERS

185

Powers  based  off  the Variable  effect  are  obviously  very  flexible,  capable  of  duplicating  a  wide  range  of  other  effects.
Responsibility for controlling Variable effects in the game is placed largely in the hands of both the Gamemaster and
responsible players. To do otherwise would require weighing the effect down with numerous game-system limitations
that would keep it from doing what it is supposed to do: create a wide range of effects.

Keep in mind a Variable effect is not supposed to be “any effect I want.” That kind of unlimited power doesn’t belong in the
hands of player characters, and is better reserved as a plot device for NPCs. A Variable effect can be “any effect within a
given set of parameters,” but it’s up to you and the GM to define those parameters. The limits of power flexibility in MUTANTS
& MASTERMINDS are deliberately set by Variable effects, the use of extra effort, and hero points.

Many  comic  book  heroes  who  appear  to  have  the  power  to “do  anything”  are  actually  using  one  of  these  options  in
terms.  For  example,  a  super-wizard  can  do  practically  anything  with  magic.  However,  generally
speaking, these characters have certain abilities they use all the time (powers they have acquired with power points) and
“stunts” they only do from time to time, essentially power stunts performed with extra effort (and possibly hero points).
This is why the Magic power given later in this chapter, for example, is not a Variable effect: most powers in the game
have the potential to do “stunts” via extra effort, so the “variability” of Magic seen in the comics is already built-in to the
system, with some costs to control it, without having to give players carte blanche to duplicate any effect in the game at
will (which is just likely to slow things down and cause game balance issues).

Variable effects are better reserved for things where it is difficult to cost-out and define everything about a given power in
advance. For example, the ability to shapechange into any animal could be an application of the Morph effect with a long
list of Metamorph options, but listing out every single possible animal form, one at a time, would be tedious to say the
least, especially when a good number of those forms would be superfluous. A Variable effect, with the descriptor “animal
forms” is easier to manage. The player can pre-build certain commonly used animal forms for use during play, but also ha

[... truncated ...]
```

**Chunk 8** (`6e58428e1e90`):

```
CHAPTER 6: POWERS

167

EXTRAS

Area: Your Luck Control effect works equally on all targets
in the affected area. You spend only one hero point, but
the subjects are each affected individually. You must ap-
ply the same effect to all subjects at once. +1 cost per rank.

Luck: Each rank in this extra gives you the benefit of a rank
in the Luck advantage (see Luck in the Advantages chap-
ter). It is subject to the same limits as the Luck advantage
set by the GM. Flat +1 point per rank of Luck.

Selective: This extra, applied to Area Luck Control, allows
you to choose who in the area is or is not affected by it. +1
cost per rank.

FLAWS

Action: If the action required for Luck Control is increased
beyond a reaction, it is only usable during your turn each

Effect:  Perception  Ranged  Damage,  Resisted  by  Will  •
4 points per rank

You can strike targets’ minds with “mental force,” inflict-
ing  Damage  resisted  by  the  target’s  Will  rather  than
Toughness, but having no effect on targets immune to
effects resisted by Will, such as inanimate objects. Men-
tal Blasts are often, but not always, Subtle as well, which
costs a flat 1 point.

MAGIC

Effect: Ranged Damage • 2 points per rank

You are a sorcerer, witch, or wizard, able to cast a variety
of magical spells. Your basic default effect is a Blast of
eldritch  force,  able  to  inflict  Ranged  Damage  (see  the
Blast power, previously).

However,  like  the  Energy  Control  power,  Magic  can
have a wide range of Alternate Effects, each a separate
spell you have mastered. The possibilities are virtually
limitless, within the bounds of your hero’s descriptors
and  the  Gamemaster’s  approval.  Examples  include
mystic  bindings  (Affliction,  see  the  Snare  version),
dispelling  magical  effects  (Nullify  Magic),  conjuring
clouds of mist or fog (an Area Visual Concealment At-
tack), scrying distant places (Remote Sensing), or slip-
ping  between  the  dimensions  to  appear  elsewhere
(Teleport), to name just a few.

All Magic effects have the “magic” descriptor regardless
of their other descriptors, so a Blast of flames conjured
with magic has both the “magic” and “fire” descriptors,
for example.

Magicians  often  have  a  Power  Loss  complication  (see
Complications  in  The  Basics  chapter):  if  they  are  un-
able to freely speak and gesture to cast their spells, they
cannot  use  Magic  (or  any  related  magical  powers  reli-
ant on spellcasting). Certain styles of Magic may impose
ot

[... truncated ...]
```

**Chunk 9** (`872471930ea9`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

HUMAN

STRENGTH
5
STAMINA
6

AGILITY
6
DEXTERITY
6

FIGHTING
10
INTELLECT
1

AWARENESS
4
PRESENCE
1

OTHERWORLDLY

STRENGTH
7
STAMINA
8

AGILITY
6
DEXTERITY
4

FIGHTING
8
INTELLECT
1

AWARENESS
2
PRESENCE
3

Agile Feint, Power Attack, Takedown

Take the advantages listed above, then roll 1d20 once on
both  the  Background  Advantages  table  and  the  Com-
bat Advantages table and record the results.

1-5

Field General: You know how to lead in battle.

6-10

Hunter: You honed your talents hunting the most
dangerous game or bounties.

11-15

Mysterious Past: Your memories are lost or
implanted but you demonstrate competence in
unexpected areas.

16-20

Survivor: You are always the last one standing.

ADVANTAGES—FIELD GENERAL

Inspire, Leadership, Teamwork

ADVANTAGES—HUNTER

Skill Mastery (Perception), Tracking, and Choose One: Favored
Environment or Favored Foe

ADVANTAGES—AGILE

Evasion, Grabbing Finesse, Improved Defense

ADVANTAGES—DARING

All-out Attack, Fearless, Improved Critical (Choose One Attack)

ADVANTAGES—GRAPPLER

Chokehold, Improved Grab, Improved Hold

ADVANTAGES—SKILLFUL

Accurate Attack, Defensive Attack, Precise Attack (Close;
Concealment)

SKILLS

Acrobatics 6, Athletics 6, Insight 4, Perception 6

Take the skills listed above, then roll 1d20 once and record
the result.

1-4

Advanced: You come from a society more highly
developed than our own.

5-8

Charismatic: You have a way with people.

9-12

Cultured: You are well learned and articulate.

13-16 Military: You are experienced in the ways of war.

17-20 Mystical: You are familiar with myth and magic.

ADVANCED

Technology 6, Vehicles 6

CHARISMATIC

Insight 6, Persuasion 6

CULTURED

Expertise: History 6, Persuasion 6

MILITARY

Expertise: Tactics 6, Intimidation 6

ADVANTAGES—MYSTERIOUS PAST

MYSTICAL

Beginner’s Luck, Benefit (Cipher), Language (Choose One)

Expertise: (Choose One: Magic or Mythology) 6, Insight 6

SURVIVOR

POWERS

Diehard, Great Endurance, Ultimate Effort (Toughness checks)

HUMAN

Roll 1d20 once and record the result.

1-5

Agile: You seldom suffer a solid hit.

6-10

Daring: You fight with a devil-may-care attitude.

11-15

Grappler: You like to keep your opponents right in
front of you.

16-20

Skillful: You fight with flair and precision.

1-4

Animalistic: Comprehend Animals 2; Enhanced

Stamina 2; Enhanced Skill 2 (Perception 4); Senses
6 (Acute and Tracking Smell, Danger Sense,

[... truncated ...]
```

**Chunk 10** (`997bf2eca013`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PLAYER

Interpose

TOUGH

Ultimate Effort (Toughness checks)

QUICK

Improved Initiative

SKILLS

Close Combat: Unarmed 2

Take  the  skill  listed  above,  then  roll  1d20  twice  (re-roll  if
you get the same result twice) and record the results.

1-4

5-8

Athlete: You’re a trained athlete.

Ex-Military: You used to be in the armed forces.

9-12

Charmer: You have a way with people.

13-16

Rough Upbringing: You were raised on the streets
or have had a hard life.

17-20

Sharp Mind: You’re difficult to fool.

ATHLETE

Athletics 4, Perception 4, Ranged Combat: Throwing 4

Roll  1d20  once  and  record  the  result  as  the  first  power
in  an  array,  then  roll  1d20  once  and  add  the  result  as  a
1-point Alternate Effect (re-roll if you get the same result
as your first roll).

1-3

4-6

7-9

Energy Blast: Ranged Damage 10, Accurate 5,

Distracting, Tiring • 10 points

Foot Stomp: Line Area Damage 10, Powerhouse and
target must be in contact with the same surface
• 10 points

Groundstrike: Burst Area Affliction 10 (Resisted

and Overcome by Fortitude; Dazed and Hindered,
Stunned and Prone, Incapacitated), Extra
Condition, Instant Recovery, Powerhouse and
target must be in contact with the same surface
• 10 points

10-12

13-14

Shockwave: Burst Area Damage 10, Powerhouse
and targets must be in contact with the same
surface • 10 points

Super-Breath: Close Range Cone Area Move Object
5, Limited to moving toward and away, Linked
to Cone Area Damage 5, Unreliable (only the
Damage is Unreliable) • 10 points

15-17

Cut Loose!: Penetrating 10 on Strength • 10 points

18-20

Thunderclap: Cone Area Affliction 10 (Resisted and
Overcome by Fortitude; Dazed, Stunned), Limited
Degree • 10 points

EX-MILITARY

Expertise: Military 4, Perception 4, Ranged Combat: Throwing 4

CHARMER

Deception 4, Insight 4, Persuasion 4

UPBRINGING

Only if you rolled Solid Form or Super-Strength on the
Offensive  Powers  table,  take  Super-Stamina,  directly
below, then roll on the table below, as directed. Do not
take Super-Stamina if you rolled Density or Growth on
the  Offensive  Powers  table,  instead,  roll  on  the  table
below.

Expertise: Streetwise 4, Intimidation 6, Perception 2

Super-Stamina: Enhanced Stamina 10 • 20 points

MIND

Expertise: (Choose One) 4, Insight 4, Perception 4

POWERS

Roll 1d20 once and record the result.

Roll  1d20  four  times  (re-roll  if  you  get  the  s

[... truncated ...]
```

**Chunk 11** (`9ab4a1de72d2`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

CHAPTER 5: ADVANTAGES

ADVANTAGE

Beginner’s Luck
Inspire
Leadership
Luck
Seize Initiative
Ultimate Effort

ADVANTAGE

Assessment
Benefit
Diehard
Eidetic Memory
Equipment
Extraordinary Effort
Fearless
Great Endurance
Instant Up
Interpose
Minion
Second Chance
Sidekick
Teamwork
Trance

ADVANTAGE

Agile Feint
Animal Empathy
Artificer
Attractive
Connected
Contacts
Daze
Fascinate
Favored Foe
Hide in Plain Sight
Improvised Tools
Inventor
Jack-of-all-trades
Languages
Ritualist
Skill Mastery
Startle
Taunt
Tracking
Well-informed

EFFECT

Spend a hero point to gain 5 temporary ranks in a skill.
Spend a hero point to grant allies a +1 circumstance bonus per rank.
Spend a hero point to remove a condition from an ally.
Re-roll a die roll once per rank.
Spend a hero point to go first in the initiative order.
Spend a hero point to get an effective 20 on a specific check.

EFFECT

Use Insight to learn an opponent’s combat capabilities.
Gain a significant perquisite or fringe benefit.
Automatically stabilize when dying.
Total recall, +5 circumstance bonus to remember things.
5 points of equipment per rank.
Gain two benefits when using extra effort.
Immune to fear effects.
+5 on checks involving endurance.
Stand from prone as a free action.
Take an attack meant for an ally.
Gain a follower or minion with (15 x rank) power points.
Re-roll a failed check against a hazard once.
Gain a sidekick with (5 x rank) power points.
+5 bonus to support team checks.
Go into a deathlike trance that slows bodily functions.

EFFECT

Feint using Acrobatics skill or movement speed.
Use interaction skills normally with animals.
Use Expertise: Magic to create temporary magical devices.
Circumstance bonus to interaction based on your looks.
Call in assistance or favors with a Persuasion check.
Make an initial Investigation check in one minute.
Use Deception or Intimidation to daze an opponent.
Use an interaction skill to entrance others.
Circumstance bonus to checks against a type of opponent.
Hide while observed without need for a diversion.
No penalty for using skills without tools.
Use Technology to create temporary devices.
Use any skill untrained.
Speak and understand additional languages.
Use Expertise: Magic to create and perform rituals.
Make routine checks with one skill under any conditions.
Use Intimidation to feint in combat.
Use Deception to demoralize in combat.
Use Perception to follow tracks.
Immediate Investigation or Persuasion check

[... truncated ...]
```

**Chunk 12** (`9c685bbd4830`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

FLAWS

NAME

COST

Activation

–1-2 flat points

Effect requires a move (1 point) or standard (2 points) action to activate.

Check Required

–1 flat per rank

Must succeed on a check to use effect.

Concentration

–1 per rank

Sustained effect becomes concentration duration.

Diminished Range

–1 flat per rank

Reduces short, medium, and long ranges for the effect.

Distracting

Fades

Feedback

Grab-Based

–1 per rank

–1 per rank

–1 per rank

–1 per rank

Increased Action

–1-3 per rank

Limited

Noticeable

Permanent

Quirk

–1 per rank

–1 flat point

–1 per rank

Vulnerable while using effect.

Effect loses 1 rank each time it is used.

Suffer damage when your effect’s manifestation is damaged.

Effect requires a successful grab attack to use.

Increases action required to use effect.

Effect loses about half its effectiveness.

Continuous or permanent effect is noticeable.

Effect cannot be turned off or improved with extra effort.

–1 flat per rank

A minor flaw attached to an effect. The opposite of a Feature.

Reduced Range

–1-2 per rank

Effect’s range decreases.

Removable

Resistible

Sense-Dependent

Side Effect

Tiring

Uncontrolled

Unreliable

–1-2/5 flat points

Effect can be taken away from the user.

–1 per rank

–1 per rank

–1-2 per rank

–1 per rank

–1 per rank

–1 per rank

Effect gains a resistance check.

Target must be able to perceive the effect for it to work.

Failing to use the effect causes a problematic side effect.

Effect causes a level of fatigue when used.

You have no control over the effect.

Effect only works about half the time (roll of 11 or more).

Example: A spellcaster has Senses 4 (Detect Magic,
Ranged,  Acute,  Analyze)  with  Expertise:  Magic
Check Required 4. The player needs to make a DC
13 skill check (10 + 3 additional ranks) to success-
fully cast the spell, followed by the normal Percep-
tion check to pick up on anything present, and per-
haps another Expertise check to interpret what the
character senses.

Skill checks an effect may require include:

Acrobatics: Suitable for effects requiring a measure
of coordination or complex maneuvering.

Deception:  Good  for  effects  intended  to  deceive,
particularly sensory effects like Concealment or Illu-
sion, and disguise or form-altering effects like Morph.

Expertise:  An  Expertise  skill  check  might  represent
having  to  know  something  about  the  subject  of  the
effect or having to kno

[... truncated ...]
```

**Chunk 13** (`a92e401b2501`):

```
CHAPTER 5: ADVANTAGES
CHAPTER 5: ADVANTAGES

Heroes are more than just skilled, they often have amazing advantages, beyond the abilities of ordinary people. In MU-
MASTERMINDS, advantages often allow heroes to “break the rules,” gaining access to and doing things most people
cannot, or simply doing them better.

Advantages are rated in ranks and bought with power points, just like abilities and skills. Advantages cost 1 power point
per rank. Some advantages have no ranks and are acquired only once, effectively at rank 1.
Advantage Cost = 1 power point per advantage rank

Each advantage’s description explains the benefit it provides. It also says if the advantage can be acquired in ranks and
the effects of doing so. Such advantages are listed as “Ranked” alongside the advantage name. Ranks in a advantage are
noted with a number after the advantage’s name, such as “Defensive Roll 2” (for a character who has taken two ranks
in the Defensive Roll advantage), just like skill and power ranks. If there is a maximum number of ranks a character can
take, it’s listed in parentheses after the word “Ranked” in the advantage’s heading.

Advantages are categorized as one of four types:

•

•

•

•

Combat  Advantages  are  useful  in  combat  and  of-
ten modify how various combat maneuvers are per-
formed.

Fortune  Advantages  require  and  enhance  the  use
of hero points.

General Advantages provide special abilities or bo-
nuses not covered by the other categories.

Skill Advantages offer bonuses or modifications to
skill use.

Each advantage is listed by name, type, and if the advan-
tage is available in multiple ranks, followed by a descrip-
tion of the advantage’s benefits. The effects of additional
ranks  of  the  advantage  (if  any)  are  noted  in  the  text  of
each advantage. In some cases a advantage’s description
mentions  the  normal  conditions  for  characters  who  do
not have the advantage for comparison.

COMBAT

When you make an accurate attack (see Maneuvers, page
249) you can take a penalty of up to –5 on the effect modi-
fier of the attack and add the same number (up to +5) to
your attack bonus.

SKILL

You can use your Acrobatics bonus or movement speed
rank in place of Deception to feint and trick in combat as if
your skill bonus or speed rank were your Deception bonus
(see the Deception skill description). Your opponent op-
poses the attempt with Acrobatics or Insight (whichever
is better).

ATTACK

COMBAT

When you make an all-out attack (s

[... truncated ...]
```

**Chunk 14** (`bc6e8d2fe577`):

```
CHAPTER 2: SECRET ORIGINS

93

Supernatural Resistance: Roll 1d20 three times
(re-roll if you get the same result twice) and record
the results.

1-3

4-6

Immunity 5 (Cold, Heat, Pressure,
Radiation, Vacuum) • 5 points

Immunity 5 (Disease, Poison, Starvation

and Thirst, Suffocation) • 5 points

11-20

7-8

Immunity 5 (Alteration effects) • 5 points

9-10

Immunity 5 (Cold damage) • 5 points

11-12

Immunity 5 (Electricity damage) • 5 points

13-14

Immunity 5 (Emotion effects) • 5 points

15-17

Immunity 5 (Fire damage) • 5 points

18-20

Immunity 5 (Magic damage) • 5 points

Roll 1d20 once and record the result.

1-7

Eyes of Darkness: Senses 2 (Darkvision) • 2 points

8-14

15-20

Spider-Climb: Movement 1 (Wall-crawling)

• 2 points

Vampire Bite: Weaken Stamina 4, Grab-based

• 2 points

WEREWOLF

Thick Skin: Protection 3; Impervious Toughness 9, Lim-
ited—Not versus magical or silver weapons • 9 points

Roll 1d20 once and record the result.

Brother to Wolves: Summon 2 (Wolves and

1-10

Dogs), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Deathly Howl: Auditory Perception Area Affliction
10 (Resisted and Overcome by Will; Dazed and
Impaired, Disabled and Stunned), Extra Condition,
Limited Degree • 20 points

1-4

5-10

Demonic Cape: Flight 6 (120 MPH), Gliding,

11-20

Removable (-1 point) • 5 points

Demonic Movement: Leaping 2 (30 feet); Speed 3

(16 MPH) • 5 points

11-16 Giant Bat Wings: Flight 5 (60 MPH), Wings • 5 points

17-20

Hellrider: Movement 2 (Wall-crawling, Water

Walking), Limited to While Moving; Speed 6 (120
MPH), Activation (standard action, -2 points),
Removable (-1 point) • 5 points

VAMPIRE

Blood Drain: Regeneration 10, Source (Blood) • 5 points

Roll 1d20 once and record the result.

1-5

6-20

Living Vampire: Enhanced Stamina 13; Immunity

4 (aging, disease, need for sleep, poison);
Impervious Toughness 8 • 38 points

Undead Invulnerability: Immunity 30 (Fortitude
effects); Impervious Protection 8, Limited—Not
against blessed or magical weapons • 38 points

Roll 1d20 once and record the result.

1-6

7-12

13-20

Children of the Night: Summon 2 (Bats, Rats, and

Wolves), Horde, Mental Link, Multiple Minions 3 (8
minions), Sacrifice • 20 points

Dominate: Perception Ranged Affliction 10 (Resisted

and Overcome by Will; Entranced, Compelled,
Controlled), Visually Sense-Dependent • 20 points

Mist Form: Insubstantial 2, Linked to Flight 5 (60

MPH) • 20 points

Roll 1d20 once and record the result.

[... truncated ...]
```

**Chunk 15** (`c8f8dadd6203`):

```
CHAPTER 2: SECRET ORIGINS

91

SHADOWS

PL 6

4  AGL

STR
STA  —  DEX

0  FGT
INT

0

6  AWE
0  PRE

0
0

Powers: Claws (Strength-based Damage 2,
Affects Corporeal), Float (Flight 1 (4 MPH),
Shadow Form (Immunity 30 (Fortitude
Effects), Insubstantial 4 (Incorporeal;
Innate; Permanent), Protection 4, Strength
Affects Corporeal)

Skills: Perception 4 (+4), Stealth 12 (+12)

Offense: Init +0, Claws +6 (Close, Damage 6)

Defense: Dodge 6, Parry 6, Fort Immune,
Tou 4, Will 5

Totals: Abilities 10 + Powers 61 +
Advantages 0 + Skills 8 + Defenses 11 = 90

15-20

15-20

SUMMONER

Defensive Roll 4 and Choose One: Artificer, Ritualist, or Inventor

SKILLS

SUMMONER

Perception 4, Stealth 4, and Choose One Expertise: Magic 6 or
Technology 6

DEFENSE

SUMMONER

DODGE
+10

PARRY
+8

FORTITUDE
+4

TOUGHNESS
+0

WILL
+7

POINTS*

ABILITIES

POWERS

48

61

5

SKILLS

DEFENSES

TOTAL

7

29

150

*These numbers are for the Summoner only; for the Du-
plicator,  use  the  totals  listed  for  the  appropriate Twin  or
Triplets, then add the points for the Summon power.

•  Motivation—Acceptance:  The  Summoner  has  un-
usual abilities that make him or her an outsider. He or
she uses those powers to gain acceptance.

•  Motivation—Doing  Good:  Some  Summoners  are
heroes because they believe it’s the right thing to do.

•  Motivation—Responsibility:  With

the  powers
they’ve  been  given,  some  Summoners  believe  it’s
their responsibility to help others.

•  Motivation—Thrills:  Outside  of  their  Summon
ability, many Summoners don’t have a lot of powers.
Some may find the constant threat of danger to be a
bit much, but not this Summoner! The more danger,
the better!

•

•

•

Power Loss: Summoners may need to speak or move
their  hands  in  order  to  summon  their  minion(s).
When these Summoners are bound and/or gagged,
they lose their powers.

Relationship: A Summoner may have friends or fam-
ily to whom he’s responsible—but it may be that the
Summoner needs to keep his summoned creature(s)
happy as well. The Summoner may have Controlled
minions,  but  that  doesn’t  mean  he  can  be  mean  to
them and still expect them to show up!

Secret: The Summoner’s minions and abilities come
from  somewhere;  what  if  their  origin  is  particularly
dark or dangerous? The Summoner would certainly
want to keep that secret private as long as possible.

Supernatural Creatures are fantastical beings out of folk-
tales and scary stories. They’re generally regarded as ur-
ban  l

[... truncated ...]
```

**Chunk 16** (`d329357e5091`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

GOLEM

STRENGTH
8
STAMINA
-

AGILITY
0
DEXTERITY
0

FIGHTING
6
INTELLECT
0

AWARENESS
4
PRESENCE
4

TECHNOLOGICAL

STRENGTH
8
STAMINA
-
UNDEAD

AGILITY
0
DEXTERITY
2

FIGHTING
6
INTELLECT
4

AWARENESS
1
PRESENCE
1

STRENGTH
6
STAMINA
-

AGILITY
2
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
2

Roll 1d20 once and record the result.

6-10

1-10

11-15

Brawler: You know how to use your strength to your
advantage.

Dabbler: You have some magical or technological
knowledge and can create useful devices or artifacts.

16-20

Perfect Recall: You have an uncanny memory.

BRUTE

Athletics 6, Intimidation 6

EXPERT

Perception 4, Choose One: Expertise: Magic 8 or Technology 8

SEEKER

Investigation 5, Perception 3, Persuasion 4

SNEAK

Deception 6, Stealth 6

POWERS

Find  the  entry  below  for  the  type  of  Construct  that
matches what you rolled for your Abilities.

GOLEM

Roll 1d20 once and record the result.

1-5

Blast: Ranged Damage 8, Accurate 6 • 22 points

Elemental Body: Enhanced Advantages 6 (Close

Attack 6); plus roll 1d20 once:

1-5

6-10

11-15

16-20

Damaging Aura: Reaction Damage 6

• 22 points

Gaseous Form: Flight 3 (16 MPH);

Insubstantial 2 (Gaseous) • 22 points

Liquid Form: Concealment 10 (All

Senses; Limited—In Liquid, Passive);
Insubstantial 1 (Liquid); Swimming 6
(30 MPH) • 22 points

Particulate Form: Elongation 2 (30
feet); Insubstantial 2 (Particulate);
Movement 2 (Permeate 2) • 22 points

BRAWLER

Improved Grab, Choose One: Power Attack or Accurate Attack

11-20

Unstoppable: Enhanced Strength 4; Enhanced Trait
2 (Close Attack 2); Immortality 5; Regeneration 2
• 22 points

DABBLER

Choose one set: Artificer, Skill Mastery (Expertise: Magic); or,
Inventor, Skill Mastery (Technology)

TECHNOLOGICAL

Roll 1d20 once and record the result.

RECALL

Eidetic Memory, Well-informed

SKILLS

Roll 1d20 twice (do not re-roll if you get the same result
twice) and record the results.

1-5

Brute: You’re big and intimidating.

6-10

Expert: You know a lot about magic or technology.

11-15

Seeker: You’re looking for clues to your origin or past.

16-20

Sneak: You’re stealthy.

1-4

Blast: Ranged Damage 9, Accurate 4 • 22 points

5-8

Retractable Claws and Combat Computer: Strength-
based Damage 2, Penetrating 6; Enhanced Traits
14 (All-out Attack, Close Attack 4, Diehard, Evasion,
Fast Grab, Improved Critical (Claws), Improved
Initiative 2, Precise Atta

[... truncated ...]
```

**Chunk 17** (`e05fc680a484`):

```
CHAPTER 2: SECRET ORIGINS

33

The following archetypes are ready to play for a power level 10 series. Some require a few simple choices or offer options
for customization. Gamemasters can also use these archetypes as ready-made villains, if desired.

The Gadgeteer and Martial Artist rely a great deal on their
advantages (as do other archetypes like the Crime Fighter
and Weapon Master). You’ll want to read the descriptions
of all of the character’s advantages from the Advantages
chapter so you know the benefits they provide. Remem-
ber to make use of them during play to give your charac-
ter every appropriate, well, advantage.

In particular, note how some advantages and even pow-
ers work together. The Gadgeteer can use Quick-Thinking
to speed up the process of inventing (see Inventing, page
211) and Skill Mastery (Technology) to make some invent-
ing  checks  as  routine.  Similarly,  note  the  Martial  Artist’s
Power Attack advantage, good for doing extra damage to
slow, tough, opponents, and the Skill Mastery (Acrobatics)
advantage  for  pulling  off  formidable  (DC  25)  Acrobatics
checks as routine!

The  Mimic  and  Mystic  archetypes  are  both  very  flexible,
although in different ways, and it pays to know what your
character is capable of doing before you are immersed in
the midst of a game.

In the case of the Mimic, the GM may wish to put together
note cards or some other quick reference to the powers of
other characters whom the Mimic might wish to duplicate.
That way, you can see at a glance what traits the character
can copy, and simply hand the card to the player for refer-
ence.  Experienced  Mimics  may  even  build  up  a “hand”  of
such cards they reference often.

For  the  Mystic,  in  addition  to  choosing  your  charac-
ter’s  five  set  Alternate  Effects  (see  Alternate  Effect  on
page  188),  read  the  Magic  sample  power  on  page  168
of the Powers chapter and give some thought to power
stunts your character can do; spur of the moment spells
whipped up to fit a particular need. Mytics are very effec-
tive at power stunts and you might want to reserve a hero
point (or two) for that purpose.

The  Paragon  and  Powerhouse  are  among  the  strongest
archetypes,  able  to  lift  and  carry  a  lot  of  weight.  Just  to
give you an idea, the Paragon can lift a loaded 747 aircraft,
whereas the Powerhouse can lift four times that amount.
Both can easily smash through stone or bend steel.

Both archetypes are pretty tough, to

[... truncated ...]
```

**Chunk 18** (`e6cd24549519`):

```
CHAPTER 6: POWERS

145

ACTION

RANGE

DURATION

COST

Instant

Varies

Instant

Sustained

Sustained

Permanent

Sustained

Sustained

Instant

Instant

Instant

Sustained

Sustained

Sustained

Sustained

Instant

Instant

Sustained

Sustained

Permanent

Permanent

Sustained

Sustained

Sustained

Instant

Fort. or Will

1 per rank

—

See description

Toughness

—

—

—

—

—

Toughness

Fort. or Will

—

—

Strength

—

—

Toughness

Toughness

—

—

—

—

—

—

—

—

2 per rank

1 per rank

4 per rank

2 per rank

2 per rank

2 per rank

1 per rank

2 per rank

1 per rank

3 per rank

2 per rank

1 per rank

See description

4 per rank

2 per rank

As base trait

1-2 per rank

1 per rank

1 per rank

2 per rank

1 per rank

2 per rank

2 per rank

Standard

Varies

Standard

Free

Free

None

Free

Standard

Standard

Standard

Standard

Standard

Standard

Free

Free

Reaction

Standard

Free

Close

Varies

Ranged

Personal

Rank

Personal

Personal

Ranged

Close

Ranged

Ranged

Close

Perception

Personal

Personal

Close

Ranged

Personal

Standard

Rank

Personal

Personal

Personal

Personal

Personal

Close

Personal

Personal

Personal

Personal

Personal

None

None

Free

Free

Free

Standard

Standard

None

None

Free

Free

Free

Standard

Standard

Free

Standard

NAME

Affliction

Alternate Form

Blast

TYPE

Attack

Varies

Attack

Burrowing

Movement

Sensory

Sensory

Sensory

Control

Attack

Attack

Defense

Control

Control

General

General

Attack

Attack

General

Control

General

General

Movement

Defense

General

General

Control

Defense

Defense

General

Sensory

Movement

Control

Attack

Attack

General

Attack

Sensory

General

Control

Communication

Comprehend

Concealment

Create

Damage

Dazzle

Deflect

Duplication

Element Control

Elongation

Energy Absorption

Energy Aura

Energy Control

Enhanced Trait

Environment

Extra Limbs

Feature

Flight

Force Field

Growth

Healing

Illusion

Immortality

Immunity

Insubstantial

Invisibility

Leaping

Luck Control

Magic

Mental Blast

Mimic

Mind Control

Mind Reading

Morph

Move Object

Movement

Nullify

Power-Lifting

Protection

Quickness

Regeneration

Remote Sensing

Perception

Sustained

Awareness

1-5 per rank

Permanent

Permanent

Sustained

Sustained

Instant

Instant

Instant

Instant

Reaction

Standard

Standard

Perception

Ranged

Perception

Move

Personal

Sustained

Perception

Instant

Perception

Sustained

Personal

Ranged

Personal

Ra

[... truncated ...]
```

---

## Concept: Magical

Chunk count: 1

### Chunk texts

**Chunk 1** (`872291c50bc3`):

```
CHAPTER 6: POWERS

205

things  like  air  (or  other  gases),  water  (or
other  liquids),  and  earth  (soil,  rock,  sand,
etc.)  through  to  biological  materials  like
acids, blood, and so forth. Energy mediums
are different forms of energy, from electro-
magnetic (electricity, light, radio, radiation,
etc.) to gravity, kinetic energy, or an exotic
source like divine, magical, psionic, or cos-
mic  energy  (given  under  Origin  descrip-
tors).
RESULT

Lastly,  a  power’s  result  is  what  happens
when  the  power  is  used  beyond  just
the game mechanics of its effect. For
example, the rules of the Affliction ef-
fect  describe  the  penalties  suffered  by  the
target,  but  they  don’t  describe  the  result,
the nature of the Affliction itself. Is it glow-
ing  bonds  of  energy,  sudden  fever  and
dizziness,  a  curse  of  misfortune,  a  life-
sapping  vapor,  or  any  number  of  other
things?

Result descriptors tend to be fairly broad,
given  the  potential  range  of  results  avail-
able to effects in the game. Some powers
may  not  have  or  need  result  descriptors;
after  all, “Mind  Control”  is  a  pretty  clear
description  of  a  result.  However, “an  in-
duced  trance  where  the  human  brain
becomes  capable  of  accepting  neurolin-
guistic programming inputs” is also a valid
descriptor for that same effect.

Like medium descriptors, result descriptors
may or may not match others the power al-
ready has. Take a taser-like weapon able to
stun the nervous system of its target:
it has an invented origin (someone
designed  and  built  it),  a  techno-
logical source (it’s a technological
device with a battery), uses
a  energy  medium  (an
electrical  shock),  and
results  in  an  electrical
overload  of  the  tar-
get’s  nervous  system
(the  result  descriptor
for its Affliction effect).
This  tells  us  a  lot  about
that  particular  power  and
ways  it  might  interact  with  other
effects.

Applying descriptors to a power is as simple as describing
what the power is and how it works: “The divinely-granted
ability to heal through a laying-on of hands,” for example,
“or the mutant power to control magnetic fields to move

ferrous metal objects.” Considerably more evocative and
descriptive than “Healing effect” or “Move Object, Limited
to Ferrous Metals,” aren’t they?

Generally, you should feel free to apply whatever descrip-
tors seem appropriate and necessary to describe your char-
acter’s powers, so long as they don’t sig

[... truncated ...]
```

---

## Concept: Magicians

Chunk count: 1
Performs actions: ['act_0249']

### Chunk texts

**Chunk 1** (`6e58428e1e90`):

```
CHAPTER 6: POWERS

167

EXTRAS

Area: Your Luck Control effect works equally on all targets
in the affected area. You spend only one hero point, but
the subjects are each affected individually. You must ap-
ply the same effect to all subjects at once. +1 cost per rank.

Luck: Each rank in this extra gives you the benefit of a rank
in the Luck advantage (see Luck in the Advantages chap-
ter). It is subject to the same limits as the Luck advantage
set by the GM. Flat +1 point per rank of Luck.

Selective: This extra, applied to Area Luck Control, allows
you to choose who in the area is or is not affected by it. +1
cost per rank.

FLAWS

Action: If the action required for Luck Control is increased
beyond a reaction, it is only usable during your turn each

Effect:  Perception  Ranged  Damage,  Resisted  by  Will  •
4 points per rank

You can strike targets’ minds with “mental force,” inflict-
ing  Damage  resisted  by  the  target’s  Will  rather  than
Toughness, but having no effect on targets immune to
effects resisted by Will, such as inanimate objects. Men-
tal Blasts are often, but not always, Subtle as well, which
costs a flat 1 point.

MAGIC

Effect: Ranged Damage • 2 points per rank

You are a sorcerer, witch, or wizard, able to cast a variety
of magical spells. Your basic default effect is a Blast of
eldritch  force,  able  to  inflict  Ranged  Damage  (see  the
Blast power, previously).

However,  like  the  Energy  Control  power,  Magic  can
have a wide range of Alternate Effects, each a separate
spell you have mastered. The possibilities are virtually
limitless, within the bounds of your hero’s descriptors
and  the  Gamemaster’s  approval.  Examples  include
mystic  bindings  (Affliction,  see  the  Snare  version),
dispelling  magical  effects  (Nullify  Magic),  conjuring
clouds of mist or fog (an Area Visual Concealment At-
tack), scrying distant places (Remote Sensing), or slip-
ping  between  the  dimensions  to  appear  elsewhere
(Teleport), to name just a few.

All Magic effects have the “magic” descriptor regardless
of their other descriptors, so a Blast of flames conjured
with magic has both the “magic” and “fire” descriptors,
for example.

Magicians  often  have  a  Power  Loss  complication  (see
Complications  in  The  Basics  chapter):  if  they  are  un-
able to freely speak and gesture to cast their spells, they
cannot  use  Magic  (or  any  related  magical  powers  reli-
ant on spellcasting). Certain styles of Magic may impose
ot

[... truncated ...]
```

---

# Hypothesis concept review – batch 41

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

## Concept: Team Checks

Chunk count: 2
Receives actions: ['act_0123', 'act_0284']

### Chunk texts

**Chunk 1** (`7db012c9a682`):

```
CHAPTER 4: SKILLS

113

You can get a general idea of just how good a particu-
lar character’s skill bonus is using the general difficulty
class  guidelines  given  in  The  Basics  along  with  the
rules  for  routine  checks  (see  Routine  Checks  in  that
chapter).

For  example,  a  +5  total  skill  modifier  means  the  char-
acter can routinely achieve a result of 15 (a tough task).
Safe to say the character is a pro, able to routinely han-
dle tasks that would prove too much for someone less
skilled.  A  character  with  a  +10  skill  modifier  achieve  a
DC 20 (challenging task) on a routine basis, a real level of
expertise, while a +15 modifier can routinely complete
DC  25  (formidable)  tasks.  At  the  high  end,  a  +30  skill
modifier  can  routinely  accomplishing  the  nigh  impos-
sible (DC 40 tasks)!

Certain skills, called interaction skills, are aimed at deal-
ing  with  others  through  social  interaction.  Interaction
skills allow you to influence the attitudes of others and get
them to cooperate with you in one way or another. Since
interaction skills are intended for dealing with others so-
cially, they have certain requirements.

First,  you  must  be  able  to  interact  with  the  subject(s)  of
the  skill. They  must  be  aware  of  you  and  able  to  under-
stand you. If they can’t hear or understand you for some
reason, you have a –5 circumstance penalty to your skill
check (see Circumstance Modifiers in The Basics).

Interaction  skills  work  best  on  intelligent  subjects,  ones
with  an  Intellect  rank  of  –4  or  better. You  can  use  them
on creatures with Int –5, but again with a –5 circumstance
penalty;  they’re  just  too  dumb  to  get  the  subtleties  of
your  point. You  can’t  use  interaction  skills  at  all  on  sub-
jects lacking one or more mental abilities. (Try convincing
a  rock  to  be  your  friend—or  afraid  of  you—sometime.)

If you don’t find a particular skill on the list, like climbing,
bluffing, or search, remember that each skill in MUTANTS &
covers a lot of ground. So, you’ll find climbing
isn’t its own skill, but is listed as part of Athletics, while
bluffing and search are under Deception and Investiga-
tion, respectively. When in doubt, read through the skill
you think is most similar to what you’re looking for.

The  Immunity  effect  (see  the  Powers  chapter)  can  also
render characters immune to interaction skills.

You  can  use  interaction  skills  on  groups  of  subjects

[... truncated ...]
```

**Chunk 2** (`b60c97b07a3c`):

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

---

## Concept: Technological Powers

Chunk count: 1

### Chunk texts

**Chunk 1** (`c73e4c4738ad`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

•

•

Divine powers come from a higher being, essentially
a  god  or  gods.  Divine  power  is  generally  limited  to
the  god(s)  areas  of  influence  and  may  be  morally
aligned, available only to wielders with an allegiance
to that divinity.

Extradimensional  powers  originate  outside  the
home  dimension  of  the  setting,  from  other  planes
or dimensions of existence. Some extradimensional
powers  are  scientific  while  others  are  downright
mystical,  or  even  beyond  into  realms “man  was  not
meant to know.”

•

•

•  Magical powers draw upon magical energies, how-
ever they might be defined in the setting. Typically,
there  is  some  sort  of “magical  energy”  in  existence
that magicians and magical creatures draw upon for
their  powers  and  effects.  Note  that  powers  with  a
magical source are not necessarily “spells,” although
they might be; a dragon’s breath might use magic to
power it, or it might be biological, depending on the
descriptors applied to it (in other words, how it’s de-
fined in terms of the setting).

•  Moral  powers  come  from  an  abstract  morality  or
ideal,  essentially  from  an  allegiance  to  that  ideal.
Whether or not the moral power is aware and capa-
ble of interaction is up to the GM and the specifica-
tions of the setting; it’s the character’s belief in that
ideal that matters so far as the power is concerned.
“Good” and “evil” are common abstract moral sourc-
es of powers, but others may include chaos, law, an-
archy, order, justice, balance, neutrality, reason, and
so forth.

Psionic powers are powers of the mind, coming from
the psyche of the wielder (or perhaps from the Col-
lective  Unconscious,  which  acts  as  a “wellspring”  of
psionic power). This power source is associated with
classic “mental” powers like telepathy and telekinesis,
although effects like Mind Reading and Move Object
can also come from other sources.

Technological powers are the result of technology,
machines and technological devices. Although tech-
nological  power  sources  often  involve  Devices  or
Equipment, they don’t necessary have to; a techno-
logical  power  may  be  a  permanent  implant,  for  ex-
ample,  without  the  limitations  of  a  Device,  but  still
technological  (and  affected  by  things  keyed  to  the
technological descriptor).

MEDIUM

A power’s medium is what the power uses to accomplish its
effect(s). Often, a power’s source and me

[... truncated ...]
```

---

## Concept: Technology

Chunk count: 50
Performs actions: ['act_0030']
Receives actions: ['act_0129', 'act_0145', 'act_0147', 'act_0361', 'act_0386']

### Chunk texts

**Chunk 1** (`03bc5d87aec7`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

The headquarters is equipped with an automatic system
for  detecting  and  extinguishing  fires.  Any  large  open
flame  sets  the  system  off  (beware,  fire-using  heroes!).  It
functions as a Nullify Fire 5 effect. A computer-controlled
fire prevention system can be programmed to ignore cer-
tain sources of fire or the system can be placed on manual
control (requiring someone to throw a switch in order to
activate it).

GARAGE

A garage houses ground vehicles and includes a ramp, el-
evator, or other access to move vehicles in and out, facili-
ties for repairing and maintaining vehicles, and a sliding
access door.
GROUNDS

In addition to the actual building(s) of the headquarters, it
has a considerable area of land surrounding it. An HQ can
have  surrounding  land  of  one  size  category  larger  than
the structure at no cost, without having this feature. Hav-
ing it allows for grounds up to three size categories larger
than the structure, so a large mansion headquarters could
have a colossal area of land.

If the headquarters has features like Defense System and
Security System, they also extend over the grounds (with
fences, sensors, weapon emplacements, and so forth).

GYM

A  gym  consists  of  weight-training  and  other  exercise
machines,  space  for  working  out,  stretching,  and  similar
exercises, and all the necessary amenities (lockers, show-
ers, etc.). Some HQs may incorporate the gym feature into
the combat simulator, for a multi-purpose training room.
A gym may also include a pool (heated or unheated, good
for  aquatic  characters),  possibly  even  connected  to  an
outside  body  of  water,  to  the  base’s  dock,  or  both  at  no
additional cost.

HANGAR

A hangar houses air and space vehicles. It includes a hatch
and/or runway for the vehicles to launch and facilities for
repairing and maintaining flying vehicles. For some HQs
the launch facilities of the hangar may require a long tun-
nel or other access to the outside.

These are cells for holding prisoners, usually temporarily,
although  some  headquarters  might  have  more  perma-
nent holding facilities. The cells are equipped with Nul-
lify devices (ranked at the HQ power level) or their basic
Toughness is increased by 50%, which option should be
agreed  upon  by  both  player  and  GM  (both  options  for
two  features).  Heroes  use  holding  cells  to  contain  cap-
tured villains until th

[... truncated ...]
```

**Chunk 2** (`087066c7a800`):

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

**Chunk 3** (`0b483461d2f8`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

SKILL

Acrobatics

Athletics

Close Combat

Deception

Expertise

Insight

Intimidation

Investigation

Perception

Persuasion

Ranged Combat

Sleight of Hand

Stealth

Technology

Treatment

Vehicles

SKILLS

ABILITY

UNTRAINED?

Agl

Str

Fgt

Pre

Int

Awe

Pre

Int

Awe

Pre

Dex

Dex

Agl

Int

Int

Dex

No

Yes

Yes

Yes

No*

Yes

Yes

No

Yes

Yes

Yes

No

Yes

No

No

No

ACTION

move or free

move

standard

standard

—

free

standard

—

free

—

standard

standard

move

standard

standard

move

A “—” entry in the Action column means using the skill typically takes longer than a standard action. See the skill description for details.
* Some areas of Expertise can be used Untrained. See the entry on Expertise for more information.

Interaction: If “Interaction” is included on the line below
the skill’s name, it is an interaction skill.

Manipulation:  If “Manipulation”  is  included  on  the  line
below the skill’s name, it is a manipulation skill.

Requires Tools: If “Requires Tools” is included on the line
below the skill’s name, you need to have the proper tools
to use the skill. Not having the proper tools is a –5 circum-
stance penalty to the skill check (see Circumstance Modi-
fiers, page 15).

The skill name line is followed by a description of the skill
and how it is used.

Agility • Trained Only

Use Acrobatics to flip, dive, roll, tumble, and perform other
acrobatic maneuvers, as well as keeping your balance un-
der difficult circumstances.
BALANCING

You  can  keep  your  balance  and  move  along  a  precari-
ous  surface  at  your  ground  speed  minus  1  rank  with  a
successful  Acrobatics  check  against  the  surface’s  DC.  A
degree of failure indicates you spend your move action
just maintaining your balance and do not actually move,
while  two  or  more  degrees  of  failure  means  you  lose
your balance and fall.

A yard or more wide

Wide ledge (1-3 ft.)

Narrow ledge (less than 1 ft.)

Balance beam

Tightrope

Surface slightly slippery

Surface very slippery

Surface slightly uneven

Surface very uneven or angled

Move at your normal speed rank

Not vulnerable while balancing

DC

0

5

10

15

20

+2

+5

+2

+5

+5

+5

You are vulnerable while balancing. If you accept a +5 in-
crease to the Acrobatics DC, you are not vulnerable.

If  you  fail  a  resistance  check  while  balancing,  make  an-
other immediate Acrobatics check against the original DC
to avoid 

[... truncated ...]
```

**Chunk 4** (`1081db3c43af`):

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

**Chunk 5** (`115dd3a349cb`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

EQUIPMENT

In addition to their amazing devices, characters often make use of various mundane equipment—ordinary things found
in the real world—ranging from a simple set of tools to cell phones, laptop computers, and even common appliances.
These items are known as equipment to differentiate them from devices.

EQUIPMENT

Equipment  is  acquired  with  points  from  the  Equipment
advantage. Each piece of equipment has a cost in points,
just  like  other  traits.  The  character  pays  the  item’s  cost
out of the points from the Equipment advantage and can
thereafter have and use that item.

An  item’s  cost  is  based  on  its  effects  and  features,  just
like a power (see the Powers chapter for more informa-
tion), so a ranged weapon has a cost based on its Ranged
Damage  rank.  Equipment  often  provides  the  Features
effect,  including  some  specific  equipment  Features  de-
scribed in this chapter. Indeed, some items of equipment
provide only Features.

Just as with power effects, there is a diminishing value in
having multiple items with a similar function, or a single
piece of equipment with multiple functions, usable only
one at a time. Equipment can have the Alternate Effect
modifier (see the Extras section of the Powers chapter),
such as a weapon capable of different modes of opera-
tion, or a reconfigurable tool.

Characters can also have Alternate Equipment, an array of
items usable only one at a time. This is typically a multi-
function  item,  or  a  kit  or  collection  of  various  smaller
items. The  classic  example  is  the  utility  belt  (see  its  de-
scription  later  in  this  chapter).  Alternate  Equipment  can
also  include  things  like  an  arsenal  of  weapons  the  char-
acter can swap out, providing different sets of weapons,
with only a limited number usable at once.

Characters may not necessarily carry all their equipment
with them at all times. The GM may allow players to spend
a hero point in order to have a particular item of equip-
ment “on-hand” at a particular time. This is essentially an
equipment  “power  stunt”—a  one-time  use  of  the  item
for  one  scene—and  the  Gamemaster  rules  whether  or
not having a particular item on-hand is even possible. For
example, a hero out for an evening in his secret identity
might have something like a concealed weapon or other
small item on-hand, but it’s unlikely the character is carry-
i

[... truncated ...]
```

**Chunk 6** (`13ce58f9b33f`):

```
CHAPTER 2: SECRET ORIGINS

67

SKILLS

Ranged Combat: Energy Control 5, Choose One: Deception 7
or Intimidation 7

Take the skills listed above, then roll 1d20 twice (re-roll if
you get the same result twice) and record the results.

1-4

Athlete: You have undergone intensive physical
training.

5-8

Cool: You’re young and trendy

9-10

Observant: You are alert and watchful.

11-14

Popular: You know how to deal with people.

15-18

Pilot/Driver: You are a skilled race car driver or
hotshot pilot.

19-20

Sly: You’re sneaky and low-key.

ATHLETE

Acrobatics 4, Athletics 4

COOL

Expertise: Popular Culture 4, Perception 4

As a descriptor, substitute any one energy type on the
list  below  (or  one  you  come  up  with)  in  place  of  the
word, “Energy,” or “Energy Control type,” above.

An  Energy  Controller’s  personality  often  reflect  the
energy type he or she controls, so the descriptions for
Abilities, Advantages, and Skills can help narrow down
which energy type fits your character if you prefer to as-
sign one to your hero.

Alternatively, you might decide to randomly determine
your  Energy  Controller’s  descriptor  by  rolling  on  the
table below.

Roll 1d20 once and record the result.

1-3

4-5

6-7

Cold: You emit cold or remove heat.

Cosmic: You wield the very versatile and
primal cosmic energy.

Darkness: You control darkness—be it
shadow, void, or some other-dimensional
force—or else subtract light.

8-9

Electrical: You generate electricity.

10-12

Fire: You produce flame and heat.

13

14

15-16

17-18

19

20

Hellfire: You control an extra-dimensional,
flame-like energy.

Light: You generate intense light and heat.

Magnetic: You generate magnetic fields and
manipulate ferrous metals.

Plasma: You project super-heated gas, or
plasma.

Sonic: You manipulate and generate sound.

Vibration: You produce and control vibration
and resonant frequencies.

OBSERVANT

Investigation 4, Perception 4

POPULAR

Insight 4, Persuasion 4

PILOT/DRIVER

Technology 4, Vehicles 4

SLY

Sleight of Hand 4, Stealth 4

POWERS

Roll 1d20 once and record the result.

Energy Control: Array (24 points, plus 3 points of

Alternate Effects)

•  Energy Blast: Ranged Damage 12 • 24 points

Quick Change: Feature 1 (transform into costume as

1-10

a free action) • 1 point

11-15

16-20

Take the Energy Control array and Energy Blast
(above), then roll 1d20 three times on the Alternate
Effects sidebar (re-roll if you get the same result
twice) and add them to the E

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

**Chunk 8** (`1a59d1dc4a9a`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

267

On this and the following two pages, are a collection of twenty-one characters for use in all MUTANTS & MASTERMINDS games.
The characters range from the average man-on-the-street (Bystander) to highly trained soldiers and criminals. Many
of these characters fit into support roles, scientists, reporters, and street informants the heroes may go to in order to
get questions answered, while others are combatants. None of these characters will be a threat to PL10 characters, but
they’re often encountered in groups, which makes them more of a threat.

These characters are intended to be used when the GM needs a fairly common type of character that’s either around
to help or harm the character in some way depending on your series. They’re also meant to represent a wide range of
characters of that type. So, you can use the Police Officer to represent an actual police officer, but it could also be used
as the basis for a detective, highly-trained security professional, or bodyguard.

If you don’t see exactly the archetype you need, find something close and make a few changes. That should get you
close enough to keep the game moving quickly.

CIVILIANS

BYSTANDER

Scientists are specialists in their chosen field. This arche-
type  can  be  used  as  anything  from  an  archaeologist  to
zoologist, or for anything with a lot of knowledge about a
particular subject, such as a professor.

PL0

STR  0,  STA  0,  AGL  0,  DEX  0,  FGT  0,  INT  0,  AWE  0,  PRE  0.
Equipment:  cell  phone.  Advantages:  Equipment  1.  Skills:
Expertise:  Choose  One  4  (+4),  Expertise:  Current  Events  2  (+2),
Expertise:  Pop  Culture  2  (+2).  Offense:  Init  +0,  Unarmed  +0
(Damage 0). Defense: Dodge 0, Parry 0, Fort 0, Tou 0, Will 0. Totals:
Abilities 0 + Powers 0 + Advantages 1 + Skills 4 + Defenses 0 = 5

The bystander represents the everyday people that popu-
late the world. The sort of character a supervillain or other
criminal might take hostage or otherwise endanger. Cus-
tomize the bystander by choosing an expertise such as a
profession or trade skill.

REPORTER

PL1

STR  0,  STA  0,  AGL  0,  DEX  0,  FGT  0,  INT  2,  AWE  2,  PRE  1
Equipment: Camera, computer, digital recorder, smart-phone.
Advantages:  Contacts,  Equipment  1.  Skills:  Deception  4
(+5),  Expertise:  Current  Events  4  (+6),  Expertise:  Pop  Culture
2  (+4),  Expertise:  Streetwise  2  (+4),  Expertise:  Writing  4  (+6),
Investigation  2  (

[... truncated ...]
```

**Chunk 9** (`1af862ab5396`):

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

**Chunk 10** (`1b8011530852`):

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

**Chunk 11** (`1d151f074127`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

feature and require characters to pay for it if their charac-
ters have such a costume. Otherwise characters have to
make do with ordinary clothing (which may be damaged
or destroyed when they use their powers).

Some devices are otherwise normal equipment with spe-
cial properties. Magical items, normal equipment imbued
with  magical  properties,  are  examples.  Magical  weap-
ons  may  have  greater  damage  bonuses  or  grant  attack
bonuses  while  magical  armor  imposes  no  penalties  and
provides  greater  protection.  Such  enchantments  move
archaic weapons and armor from the realm of mundane
equipment to devices. The same is true of equipment us-
ing super-alloys, bulletproof cloth, and other wonders of
super-science.

WEAPONS

Weapons are common devices, ranging from super-pow-
ered versions of ordinary weapons like swords, bows, or
guns  (see  Enhanced  Equipment)  to  more  exotic  weap-
ons  like  magic  wands  or  alien  power  rings.  A  weapon
device  usually  has  one  or  more  attack  effects  but  may
provide  virtually  any  effect  the  player  wants  to  include.
Weapons often have several different attacks as Alternate
Effects. One example is an array of magic rings, each with
its own effect, but only usable one at a time.

The full range of devices MUTANTS & MASTERMINDS characters
can create and use is limited solely by your imagination.
Essentially any item with a power is considered a device.
Players and GMs may well come up with devices beyond
those  described  here.  Use  the  guidelines  in  this  chapter
and in the Powers chapter to handle any new devices and
their capabilities.

INVENTING

Characters with the Inventor advantage can create inven-
tions,  temporary  devices. To  create  an  invention,  the  in-
ventor defines its effects and its cost in power points. This
cost is used for the necessary skill checks, and determines
the time required to create the invention. Inventions are
subject to the same power level limits as other effects in
the series.

First,  the  inventor  must  design  the  invention.  This  is  a
Technology skill check the GM should make in secret. The
DC is 10 + the invention’s total power point cost, including
all modifiers except Removable, which does not apply to
inventions, as they are temporary by nature.

Designing an invention requires an hour’s work per power
point of the invention’s cost. You can make a routi

[... truncated ...]
```

**Chunk 12** (`238fc7bd4809`):

```
CHAPTER 3: ABILITIES

107

Here are descriptions of the eight abilities and what they represent.

STRENGTH (STR)

INTELLECT (INT)

Strength measures sheer muscle power and the ability to
apply it. Your Strength rank applies to:

•

Damage dealt by your unarmed and strength-based
attacks.
How far you can jump (based on an Athletics skill check).
The amount of weight you can lift, carry, and throw.
Athletics skill checks.

•
•
•
STAMINA (STA)

Stamina  is  health,  endurance,  and  overall  physical  resil-
ience.  Stamina  is  important  because  it  affects  a  charac-
ter’s ability to resist most forms of damage. Your Stamina
modifier applies to:

•
•

•

Toughness defense, for resisting damage.
Fortitude defense, for resisting effects targeting your
character’s health.
Stamina  checks  to  resist  or  recover  from  things  af-
fecting  your  character’s  health  when  a  specific  de-
fense doesn’t apply.

AGILITY (AGL)

Agility is balance, grace, speed, and overall physical coor-
dination. Your Agility rank applies to:

•

•
•
•

Dodge defense, for avoiding ranged attacks and oth-
er hazards.
Initiative bonus, for acting first in combat.
Acrobatics and Stealth skill checks.
Agility  checks  for  feats  of  coordination,  gross  move-
ment, and quickness when a specific skill doesn’t apply.

DEXTERITY (DEX)

Dexterity  is  a  measure  of  hand-eye  coordination,  preci-
sion, and manual dexterity. Your Dexterity rank applies to:

•
•
•

Attack checks for ranged attacks.
Sleight of Hand and Vehicles skill checks.
Dexterity  checks  for  feats  of  fine  control  and  preci-
sion when a specific skill doesn’t apply.

FIGHTING (FGT)

Fighting  measures  your  character’s  ability  in  close  com-
bat, from hitting a target to ducking and weaving around
any counter-attacks. Your Fighting rank applies to:

•
•

Attack checks for close attacks.
Parry defense, for avoiding close attacks.

Intellect covers reasoning ability and learning. A character
with a high Intellect rank tends to be knowledgeable and
well-educated. Your Intellect modifier applies to:

•

•

Expertise,  Investigation, Technology,  and Treatment
skill checks.
Intellect checks to solve problems using sheer brain-
power when a specific skill doesn’t apply.

AWARENESS (AWE)

While  Intellect  covers  reasoning,  Awareness  describes
common sense and intuition, what some might call “wis-
dom.” A character with a high Intellect and a low Aware-
ness may be an “absent-minded professor” type, smart

[... truncated ...]
```

**Chunk 13** (`2ec68f50f56a`):

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

**Chunk 14** (`3788ea99174b`):

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

**Chunk 15** (`4e205a3c2745`):

```
CHAPTER 4: SKILLS

117

The  bonus  from  a  Close  Combat  skill  applies  only  to  at-
tack checks with the particular attack, not to defenses. For
a broader bonus to attack checks that is less than simply
raising  Fighting  rank,  see  the  Close  Attack  advantage  in
the Advantages chapter.

DECEPTION

Presence • Interaction

Deception is the skill of getting others to believe what you
want them to believe. It covers things like acting, bluffing,
fast-talk, trickery, and subterfuge.

Deception takes as long as it takes to spin-out your story.
Uses of Deception in action rounds are generally standard
actions, although you can attempt to deceive as a move
action by taking a –5 penalty to your check.

BLUFFING

Make  a  Deception  check  to  tell  a  believable  lie  or  get
someone do go along with you.

A  bluff  is  usually  opposed  by  the  target’s  Deception  or
Insight  check.  Favorable  and  unfavorable  circumstances
weigh  heavily  on  the  outcome.  Two  circumstances  can
work against you: the deception is hard to believe, or what
you  ask  goes  against  the  target’s  self-interest,  nature,  or
personality.

If it’s important, you can distinguish between a deception
that  fails  because  the  target  doesn’t  believe  it  and  one
that fails because it asks too much. For instance, if the tar-
get gets a +10 bonus to resistance because the deception
demands serious risk, and the resistance check succeeds
by 10 or less, then the target doesn’t so much see through
the deception as prove reluctant to go along with it. If the
target’s Insight check succeeds by 11 or more, he has seen
through  the  deception,  and  would  have  refused  even  if
it had not placed unusual demands on him (that is, even
without the +10 modifier).

MODIFIER

The target wants
to believe you.

The deception is believable
and doesn’t affect the target
much either way.

The deception is a little hard
to believe or puts the target at
some kind of risk.

The deception is difficult
to believe or entails
a serious risk.

The deception is way
out there, almost too
incredible to consider.

–5

+0

+5

+10

+20

There are a number of factors to consider when choosing skills for your MUTANTS & MASTERMINDS character.

VS. TALENT

In game terms there’s no difference between a character who has ranks in a skill because of extensive training and an-
other whose skill ranks represent a natural talent or aptitude for the skill. Both are considered “trained” in the skill in
game te

[... truncated ...]
```

**Chunk 16** (`60fdef9305c6`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

PL4

STR  2,  STA  2,  AGL  1,  DEX  1,  FGT  3,  INT  0,  AWE  1,  PRE  1
Equipment: Bulletproof vest (+4 Toughness vs. Ballistic), light
pistol,  tonfa,  cell  phone,  handcuffs.  Advantages:  Equipment
3.  Skills:  Athletics  3  (+5),  Expertise:  Current  Events  2  (+2),
Expertise:  Streetwise  3  (+3),  Expertise:  Police  Officer  4  (+4),
Insight  4  (+5),  Intimidation  2  (+3),  Investigation  2  (+2),
Perception 4 (+5), Ranged Combat: Pistols 4 (+5), Treatment 2
(+2), Vehicles 4 (+5). Offense: Init +1, Unarmed +3 (Damage 2),
Tonfa +3 (Damage 3), Pistol +5 (Ranged Damage 3). Defense:
Dodge  2,  Parry  4,  Fort  4, Tou  6/2, Will  2.  Totals:  Abilities 22 +
Powers 0 + Advantages 3 + Skills 17 + Defenses 5 = 47

This archetype focuses primarily on uniformed beat cops.
Detectives,  undercover.  and  plainclothes  officers  have
more  ranks  in  Investigate  and  often  in  other  social  skills
like Persuasion and Intimidation.

PL5

STR  2,  STA  2,  AGL  2,  DEX  2,  FGT  4,  INT  0,  AWE  1,  PRE  1
Equipment:  Submachine  gun,  riot  gear  (+4  Toughness),
tonfa,  cell  phone,  handcuffs.  Advantages:  Close  Attack  2,
Equipment 4. Skills: Athletics 3 (+5), Expertise: Current Events
2  (+2),  Expertise:  Streetwise  4  (+4),  Expertise:  Police  Officer  5
(+5), Expertise: Tactics 5 (+5), Intimidation 4 (+5), Perception 2
(+3),  Ranged  Combat:  Submachine  Gun  4  (+6),  Stealth  4  (+6),
Treatment  3  (+3).  Offense:  Init  +2,  Unarmed  +6  (Damage  2),
Tonfa +6 (Damage 3), SMG +6 (Ranged Damage 4, Multiattack).
Defense: Dodge 4, Parry 4, Fort 6, Tou 6/2, Will 3. Totals: Abilities
28 + Powers 0 + Advantages 6 + Skills 18 + Defenses 8 = 60

SWAT  (Special  Weapons  And  Tactics)  squads  are  made
up  of  police  officers  with  special  training  in  squad-level
tactics  and  weapon-use. They  deal  with  serious  criminal
threats, including mutant criminals.

MILITANT

PL4

STR  1,  STA  1,  AGL  1,  DEX  1,  FGT  1,  INT  1,  AWE  1,  PRE  1
Equipment:  Light  pistol,  9  points  of  equipment  as  needed.
Advantages: Equipment 3. Skills: Close Combat: Unarmed 4
(+5), Deception 4 (+5), Expertise: Choose One 3 (+4), Expertise:
Demolitions  6  (+7),  Intimidation  3  (+4),  Ranged  Combat:
Pistol 4 (+5), Technology 4 (+5), Vehicles 4 (+5). Offense: Init
+1,  Unarmed  +5  (Damage  1),  Pistol  +5  (Ranged  Damage  3).
Defense: Dodge 4, Parry 4, Fort 4, Tou 1, Will 2. Totals: Abilities
16 + P

[... truncated ...]
```

**Chunk 17** (`6717e2899e27`):

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

**Chunk 18** (`6805431193d6`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

1), Assault Rifle +5 (Ranged Damage 5, Multiattack). Defense:
Dodge  5,  Parry  5,  Fort  5, Tou  5/2, Will  1.  Totals:  Abilities 20 +
Powers 0 + Advantages 11 + Skills 9 + Defenses 8 = 48

This archetype covers the typical infantryman or enlisted
soldier. Specialists and officers have appropriate addition-
al training (and skills).

PL4

STR  0,  STA  1,  AGL  1,  DEX  0,  FGT  2,  INT  3,  AWE  2,  PRE  4
Equipment: Bulletproof vest (+4 Toughness vs. Ballistic), heavy
pistol,  cell  phone.  Advantages:  Benefit  5  (Millionaire,  Status:
Crime  Lord),  Connected,  Equipment  3,  Well-informed.  Skills:
Expertise: Criminal 8 (+11), Expertise: Streetwise 6 (+9), Expertise:
Current  Events  2  (+5),  Intimidation  6  (+10),  Perception  2  (+4),
Persuasion 4 (+8), Ranged Combat: Pistols 4 (+4). Offense: Init
+1, Unarmed +2 (Damage 0), heavy pistol +4 (Ranged Damage
4).  Defense:  Dodge  3,  Parry  3,  Fort  3,  Tou  5/1,  Will  5.  Totals:
Abilities 26 + Powers 0 + Advantages 10 + Skills 16 + Defenses 8 = 60

Sitting  on  top  of  the  criminal  underworld  are  the  crime
lords. These are men and women who’ve come up through
the ranks and now run the show. Physically a crime lord
is  no  match  for  a  hero,  but  their  connections,  resources,
and  knowledge  of  the  underworld  can  be  problematic.
The crime lord presented here is a fairly small fish; Game-
masters should make any changes needed to increase the
crime lord’s power and influence for the series.

CRIMINAL

PL2

STR  1,  STA  0,  AGL  2,  DEX  1,  FGT  1,  INT  1,  AWE  0,  PRE  1
Equipment: Leather jacket (+1 Toughness), light pistol, knife,
cell phone. Advantages: Equipment 2. Skills: Athletics 4 (+5),
Expertise:  Choose  One  4  (+5),  Expertise:  Streetwise  4  (+5),
Expertise:  Current  Events  2  (+3),  Perception  4  (+4),  Stealth
6  (+8),  Technology  4  (+5),  Vehicles  4  (+5).  Offense:  Init  +2,
Unarmed  +1  (Damage  1),  Knife  +1  (Damage  2,  Crit.  19-20),
Pistol +1 (Ranged Damage 3). Defense: Dodge 3, Parry 3, Fort
2, Tou 1/0, Will 0. Totals: Abilities 14 + Powers 0 + Advantages 2 +
Skills 16 + Defenses 5 = 37

This  archetype  represents  run-of-the-mill  career  crimi-
nals. Gamemasters should shuffle the criminal’s skill ranks
around to specialize as needed.

PL2

STR  1,  STA  0,  AGL  2,  DEX  1,  FGT  1,  INT  1,  AWE  0,  PRE  1
Equipment: Leather jacket (+1 Toughness), light pistol, knife,
cell phone. Advantag

[... truncated ...]
```

**Chunk 19** (`6be13e770e51`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

Constructs  suffer  damage  like  inanimate  objects  (see
the  Damage  effect  in  the  Powers  chapter  for  details).
Constructs  do  not  recover  from  damage.  Instead,  they
must be repaired. See the Technology skill description for
guidelines on repairing damaged objects.

ZOMBIE

STR
2

STA
-

AGL
-1

DEX
-1

FGT
1

INT
-

AWE
-1

POWERS

Undead: Immunity 30 (Fortitude effects), Protection 3

OFFENSE

PL2

PRE
-

Constructs  with  Regeneration  are  self-repairing  (see  the
Regeneration effect in the Powers chapter).

INITIATIVE –1

Attack +1

Close, Damage 2

The  following  are  some  typical  constructs  for  MUTANTS  &
MASTERMINDS,  most  likely  to  show  up  as  a  villain’s  minions
. Individually, they’re no match for most heroes, but large
numbers of them can keep characters busy and even wear
them down with a lucky attack or two.

PL5

PRE
-

ROBOT

STR
5

STA
-

AGL
-1

DEX
-1

FGT
0

INT
-

AWE
0

SKILLS

Close Combat (Unarmed)  4 (+4)

POWERS

Armor: Protection 10, Impervious 6 • 16 points

Robot: Immunity 30 (Fortitude effects) • 30 points

DEFENSE

DODGE

PARRY

WILL

0

1

Immune

FORTITUDE

Immune

TOUGHNESS

ABILITIES

POWERS

–30

33

0

SKILLS

DEFENSES

TOTAL

STR
16

STA
-

AGL
0

DEX
0

FGT
0

INT
-

AWE
0

POWERS

Armor: Protection 12, Impervious  • 24 points

Giant: Growth 16, Continuous, Permanent, Innate  • 33 points

Robot: Immunity 30 (Fortitude) • 30 points

3

0

1

4

PL8

PRE
-

OFFENSE

OFFENSE

INITIATIVE –1

INITIATIVE +0

Attack +4

Close, Damage 5

Attack +0

Close, Damage 16

DEFENSE

DODGE

PARRY

WILL

0

0

FORTITUDE

Immune

TOUGHNESS

10

Immune

DEFENSE

DODGE

PARRY

WILL

–5

–5

Immune

FORTITUDE

Immune

TOUGHNESS

16

ABILITIES

POWERS

–24

46

0

SKILLS

DEFENSES

TOTAL

2

1

25

ABILITIES

POWERS

–30

87

0

SKILLS

DEFENSES

TOTAL

0

0

57

```

**Chunk 20** (`6c8715df5e97`):

```
CHAPTER 2: SECRET ORIGINS

35

Power Point Totals:  Abilities 30 + Powers 84  + Advantages 8 + Skills  12 + Defenses 16  = 150

PL10PL10

CONSTRUCT
CONSTRUCT

STRENGTH
11
STAMINA
-

POWERS

AGILITY
3
DEXTERITY
3

FIGHTING
9
INTELLECT
5

AWARENESS
1
PRESENCE
0

Armored: Protection 11, Impervious 6 • 17 points.

Unliving: Immunity to Fortitude Effects • 30 points.

OPTIONS

Choose one of the following • 20 points.

Elemental: Ranged Damage 10 (See Elemental Control in the

Powers chapter.)

Soldier: Ranged Damage 10 (built-in weapon)

Undead Revenant: Immortality 5, Regeneration 10

Wraith: Insubstantial 4

Eidetic Memory, Ranged Attack 5

SKILLS

Investigation 2 (+7), Perception 5 (+6), Persuasion 4 (+4), Technology
5 (+10), Vehicles 2 (+5)

OFFENSE

INITIATIVE +3

Ranged +8

Unarmed +9

Ranged, Damage *

Close, Damage 11

* Damage bonus depends on the option chosen under Powers.

DEFENSE

DODGE

PARRY

WILL

9

9

9

FORTITUDE

Immune

TOUGHNESS

11

Power Point Totals:  Abilities 54 + Powers 67  + Advantages 6 + Skills  9 + Defenses 14  = 150

36

```

**Chunk 21** (`7420eccba7af`):

```
CHAPTER 1: THE BASICS

13

TASK

SKILL

Sneak up on
someone

Stealth

Perception

Con someone

Deception

Win a car race

Vehicles

Insight

Vehicles

Pretend to be
someone else

Steal a key chain
unnoticed

Deception

Perception

Sleight of Hand

Perception

Win a trivia contest

Expertise

Expertise

Break computer
security

Technology

Technology

OR

DEGREE

OR
THAN ...
(DC 20)

DC+15

DC+10

DC+5

DC

DC–5

DC–10

DC–15

DC–20

Four (Success)

Three (Success)

Two (Success)

One (Success)

One (Failure)

Two (Failure)

Three (Failure)

Four (Failure)

35

30

25

20

15

10

5

0

Some  checks  are  opposed.  They  are  made  against  an-
other character’s check result as the DC. Whoever gets the
higher result wins. An example is trying to bluff someone.
You roll a Deception check, while the GM rolls an Insight
check for your target. If you beat the target’s Insight check
result, you succeed.

For ties on opposed checks, the character with the higher
bonus  wins.  If  the  bonuses  are  the  same,  roll  d20.  On  a
1–10, one character wins, and on an 11–20, victory goes to
the other character; decide which character is “high” and
which is “low” before rolling.

Opposed checks offer the Gamemaster a useful tool for
comparing the efforts of two characters quickly and eas-
ily. This applies not only to skills, but also powers and, in
some cases, abilities. If two or more characters compete
at a particular task, you can resolve it with an opposed
check. The character with the highest check result wins.
Of  course,  you  can  play  things  out  if  you  want,  but
sometimes it’s good to be able to resolve things with a
quick opposed check and move on.

As Gamemaster, if you find yourself without a particular
rule to resolve a conflict or contest between characters,
the opposed check is your friend. Pick the appropriate
skill,  power,  or  ability,  make  checks  for  the  characters
and compare the results to see how they did.

opposing character’s modifier +10, just like the result of
a routine check (previously).

Active defenses in combat, where characters are focusing
on other actions, are generally routine opposition, which
is why attack checks are made against a DC of 10 + the ap-
propriate defense. Active opposed checks in combat are
an  option  when  a  character  goes  on  the  defensive.  See
Defend in the Action & Adventure chapter for details.

In cases where a check is a simple test of one character’s
capability  against  another,  with  no  

[... truncated ...]
```

**Chunk 22** (`818544ba2429`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

do in the hope of gaining acceptance for him- or her-
self as well as other psychics.

•  Motivation—Responsibility:  Some  Psychics  use
their powers for good, because they feel they must
have been given their powers to help others.

•

•

Power  Loss:  Because  mental  powers  often  require
some  amount  of  focus;  drugs,  disorientation  of  any
kind, or noisy settings may prevent a Psychic from us-
ing his or her powers.

Quirk—Impressionable:  Psychic’s  with  telepathy
may  pick  up  personality  traits  and  attitudes  from
people they’ve interacted with using their powers.

Shapeshifters include characters who actually change their
shape to become animals, machines, mythic creatures, or hu-
manoid monsters, as well as characters who can change their
density, grow, shrink (or both!), or stretch to fantastic lengths.

ABILITIES

Roll 1d20 once and record the result.

1-10

Everyman: You’re an ordinary, everyday Joe. Or
you’re an alien being or construct made to look and
behave just like you’re an ordinary, everyday Joe.

11-20 Whiz: You’re an inventor, scientist, or incredibly smart.
EVERYMAN

STRENGTH
2
STAMINA
2

AGILITY
2
DEXTERITY
2

FIGHTING
2
INTELLECT
2

AWARENESS
2
PRESENCE
2

WHIZ

STRENGTH
2
STAMINA
2

AGILITY
2
DEXTERITY
0

FIGHTING
2
INTELLECT
7

AWARENESS
1
PRESENCE
0

Defensive Roll 3, Move-by Action

9-12

13-16

Smart Alec: You never stop talking. Sometimes
people want to hit you.

Spontaneous: You have poor impulse control,
which is actually a blessing in combat.

17-20 Wealthy: You inherited or have money of your own

somehow.

SPEED

Evasion, Improved Initiative

INVENTOR

Inventor, Skill Mastery (Choose One)

ALEC

Daze (Deception), Taunt

SPONTANEOUS

Improved Initiative, Uncanny Dodge

WEALTHY

Benefit 2 (Independently Wealthy)

SKILLS

Close Combat: Unarmed 8

Take the skill listed above, then roll 1d20 twice and record
the result (do not re-roll if you get the same result).

1-4

5-8

Adventurer: You like action and adventure and you
have the skills to keep you alive while pursuing them.

Explorer: You’re well traveled and know how to
blaze your own trails.

9-12

Infiltrator: You’re a trained deceiver and infiltrator.

13-16

Investigator: You’re a talented detective.

17-20

Researcher: You’ve been educated in technology
and a field of interest.

ADVENTURER

Athletics 4, Expertise: (Choose One) 4, Perception 4

EXPLORER

Athletics 4, Perception

[... truncated ...]
```

**Chunk 23** (`8558df91a0a1`):

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

**Chunk 24** (`86e82163c6b8`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

HIDING

OPERATING

If you have cover or concealment, make a Stealth check,
opposed by an observer’s Perception check, to hide and
go unnoticed.

If  others  are  aware  of  your  presence,  you  can’t  use
Stealth  to  remain  undetected.  You  can  run  around  a
corner so you are out of sight and then use Stealth, but
others know which way you went. You can’t hide at all if
you have absolutely no cover or concealment, since that
means you are standing out in plain sight. Of course, if
someone isn’t looking directly at you (you’re sneaking up
from behind, for example), then you have concealment
relative to that person.

A  successful  Deception  or  Intimidation  check  can  give
you the momentary distraction needed to make a Stealth
check  while  people  are  aware  of  you. When  others  turn
their attention from you, make a Stealth check if you can
reach  cover  or  concealment  of  some  kind.  (As  a  general
guideline, any such cover has to be within 1 foot for every
rank you have in Stealth.) This check, however, is at a –5
penalty because you have to move quickly.
TAILING

You  can  use  Stealth  to  tail  someone  at  your  normal
speed.  This  assumes  you  have  some  cover  or  conceal-
ment (crowds of people, shadows, fog, etc.). If the subject
is worried about being followed, he can make a Percep-
tion  check  (opposed  by  your  Stealth  check)  every  time
he  changes  course  (goes  around  a  street  corner,  exits  a
building,  and  so  on).  If  he  is  unsuspecting,  he  only  gets
one Perception check for the scene. If the subject notices
you, make a Deception check, opposed by Insight. If you
succeed, you manage to pass off your presence as coinci-
dence and can continue tailing. A failed Deception check,
or being noticed a second time, means the subject knows
something is up and reacts accordingly.

Most  routine  operations  of  technological  equipment
don’t require a skill check and can be done untrained. Us-
ing an unfamiliar device does require a check, with the DC
determined by how foreign or unusual the device is, from
simple (DC 10) to highly advanced (DC 25 or more).
BUILDING

The difficulty and time required to make an item depends
on its complexity, as shown on the Building Items table. If
your Technology check succeeds, you have made the item
after the necessary time. If the check fails, you did not pro-
duce a usable end result, and any time and materials are
wast

[... truncated ...]
```

**Chunk 25** (`872471930ea9`):

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

**Chunk 26** (`885a404994e2`):

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

**Chunk 27** (`8ad0833a1563`):

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

**Chunk 28** (`903a8c445c1a`):

```
CHAPTER 1: THE BASICS

11

Time Rank = Distance Rank - Speed Rank

Reversing  the  previous  formula,  we  can  also  figure  out
how long it takes someone at a particular speed to cov-
er  a  given  distance,  by  subtracting  the  speed  rank  from
the distance rank to get a time rank. So a normal human
(speed  0)  walking  30  miles  (distance  13)  takes  about  16
hours. A hero with Speed 14 covers the same distance in
(13 – 14 = –1) just 3 seconds!

Throwing Distance Rank =
Strength Rank - Mass Rank

As  another  example,  the  distance  rank  a  hero  can  throw
something equals the hero’s Strength rank minus the mass
rank of the object. So a hero with Strength 10 (able to lift 25
tons), picks up a 10-ton truck (mass rank 9). Since 10-9=1,
the hero can then toss the truck rank 1 distance (60 feet)!

GAME PLAY

A session of the MUTANTS & MASTERMINDS game resembles an issue of a comic book or an episode of an animated series.
The Gamemaster and the players get together and tell a story through the process of playing the game. The length of
the game session can vary, from just a couple hours to several hours or more. Some adventures may be completed in a
single session while others may take multiple sessions, just as some comic book stories are told in one issue while others
span multiple issues, forming a story arc or mini-series. The episodic nature of the game allows you to choose when to
stop playing and allows you to start up again at any time you and your friends want.

Also like a comic book, a M&M game consists of a series of interrelated scenes. Some scenes are fairly straightforward,
with the heroes interacting with each other and the supporting cast. In these cases the GM generally just asks the play-
ers to describe what their heroes are doing and in turn describes how the other characters react and what they do. There
may be some improvisational acting as everyone plays out the roles of their characters. When the action starts hap-
pening, such as when the heroes are staving off a disaster or fighting villains, time becomes more crucial and is broken
down into action rounds, and the players generally have to make die rolls to see how their heroes do.

CHECKS

Your hero stands perched on the rooftop, looking down
through the skylight. In the abandoned warehouse below,
the  villain  throws  the  switch  that  begins  lowering  your
hero’s friends into the vat of boiling acid! You turn to the
Gamemaster and say:

“I leap down, smashing throug

[... truncated ...]
```

**Chunk 29** (`94d3158e4b6b`):

```
CHAPTER 4: SKILLS ........... 113
BASICS .................. 113
Acquiring Skills ....................113
WORK ........ 113
Untrained Skill Checks ......113
Interaction Skills ..................114
Manipulation Skills .............114
DESCRIPTIONS..... 114
Acrobatics ..............................115
Athletics ..................................116
Close Combat .......................117
Deception ..............................118
Expertise .................................119
Insight .....................................120
Intimidation ..........................121
Investigation .........................122
Perception .............................123
Persuasion .............................124
Ranged Combat ..................125
Sleight of Hand ....................125
Stealth .....................................126
Technology ............................127
Treatment ..............................129
Vehicles ...................................129

```

**Chunk 30** (`952d6212a75a`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

Audio  Recorder: These  tiny  digital  recorders  (about  the
size  of  a  deck  of  playing  cards)  can  record  up  to  eight
hours  of  audio  and  can  be  connected  to  a  computer  to
download the digital recording.

Video  Camera:  A  hand-held  camera  that  records  video
and audio on tape or digitally, with a capacity of about 6
hours of footage. Video cameras cost 2 points, since they
effectively double as audio recorders as well.

sion goggles must have at least a little light to operate. A
cloudy night provides sufficient ambient light, but a pitch-
black cave or a sealed room doesn’t. For situations of total
darkness, the goggles come with an infrared illuminator
that, when switched on, operates like a flashlight visible
only to the wearer (or anyone else with IR vision).

Parabolic Microphone: This apparatus has a gun-like mi-
crophone with an attached set of headphones. A parabol-
ic mike provides a +5 equipment bonus to listening Per-
ception checks that overcomes some or all of the penalty
for listening to sounds at a distance, through walls, etc.

This equipment is most often used by criminals or to catch
criminals.

Handcuffs: Handcuffs are restraints designed to lock two
limbs—normally the wrists—of a prisoner together. They
fit any medium or small humanoid. Handcuffs can only be
placed on a defenseless or unresisting target. Steel cuffs
have Toughness 9 and are DC 20 to escape using Sleight
of Hand (or Technology to pick the lock).

Lock Release Gun: This small, pistol-like device automati-
cally disables and opens cheap and average mechanical
locks operated by standard keys as a routine check. It does
not affect other locks.

Restraints: Similar to handcuffs are plastic restraints, used in
cases where authorities need to restrain a large number of
people and cuffs are impractical. They are generally Tough-
ness 5 or so and DC 20 to escape with Sleight of Hand but
cannot be removed except by cutting or breaking them.

Heroes often use surveillance gear to keep tabs on crimi-
nals and their activities.

Binoculars: Standard binoculars allow the user to make visu-
al Perception checks at a greater distance, or with a reduced
penalty  for  distance,  effectively  providing  a  +5  equipment
bonus that overcomes some or all of the distance penalty.

Concealable Microphone: A tiny receiver usable as a lis-
tening device. It has a broadcast range of about a mi

[... truncated ...]
```

**Chunk 31** (`9b4ab26032fa`):

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

**Chunk 32** (`9b8b75c1b5e7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

PL10PL10

STRENGTH
12
STAMINA
1

POWERS

AGILITY
1
DEXTERITY
2

FIGHTING
8
INTELLECT
5

AWARENESS
2
PRESENCE
0

Battlesuit: Removable (–21 points)

Armor: Protection 11, Impervious

 • 22 points.

Boot Jets: Flight 8 (500 MPH) • 16 points.

Comm System: Radio Communication 2

 • 8 points.

Life Support System: Immunity 10 • 10 points.

Sensors: Senses 12 (Accurate Radio Extended 3 [radar], Darkvision,
Direction Sense, Distance Sense, Infravision, Time Sense, Ultra-
Hearing) • 12 points.

Servo Motors: Enhanced Strength 12 • 24 points.

•  Force Beams: Ranged Damage 12 • 1 point.

Tactical Computer: Enhanced Dodge 2, Enhanced Fighting 4,

Enhanced Ranged Attack 2 • 12 points.

Accurate Attack, Improvised Tools, Inventor, Ranged Attack 2, Ranged
Attack 4, Second Chance (Technology checks)

SKILLS

Expertise: (Choose one of Business, Engineering, or Science) 5 (+10),
Insight  4  (+6),  Perception  3  (+5),  Persuasion  4  (+4), Technology  8
(+13)

OFFENSE

INITIATIVE +1

Force Beam +8

Unarmed +8

Ranged, Damage 12

Close, Damage 12

DEFENSE

DODGE

PARRY

WILL

8

8

8

FORTITUDE

TOUGHNESS

6

12

```

**Chunk 33** (`9c685bbd4830`):

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

**Chunk 34** (`ac75d3f2b9e6`):

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

**Chunk 35** (`ae82f9b088df`):

```
CHAPTER 5: ADVANTAGES

137

LITERACY

Characters are assumed to be literate in their native language and any other language they know. At the GM’s discretion,
characters may have to spend an additional Languages rank to be literate in a language with a different alphabet or style
of writing from the character’s native language (such as Arabic, Japanese kanji or Russian Cyrillic for an English speaker).
Completely illiterate characters are faced with a potential Disability complication during the game.

level limits, like other uses of hero points. Multiple uses of
Inspire do not stack, only the highest bonus applies.

JACK-OF-ALL-TRADES

SKILL

GENERAL

You can go from prone to standing as a free action with-
out the need for an Acrobatics skill check.

INTERPOSE

GENERAL

Once  per  round,  when  an  ally  within  range  of  your  nor-
mal movement is hit by an attack, you can choose to place
yourself between the attacker and your ally as a reaction,
making  you  the  target  of  the  attack  instead. The  attack
hits  you  rather  than  your  ally,  and  you  suffer  the  effects
normally. You cannot use this advantage against area ef-
fects or perception range attacks, only those requiring an
attack check.

INVENTOR

SKILL

You can use the Technology skill to create inventions. See
Inventing, page 211, for details.

You can use any skill untrained, even skills or aspects of
skills  that  normally  cannot  be  used  untrained,  although
you must still have proper tools if the skill requires them.

LANGUAGES

SKILL, RANKED

You  can  speak  and  understand  additional  languages.
With one rank in this advantage, you know an additional
language. For each additional rank, you double your ad-
ditional  known  languages:  two  at  rank  2,  four  at  rank  3,
eight at rank 4, etc. So a character with Languages 7 is flu-
ent in 64 languages! Characters are assumed to be fluent
in any languages they know, including being able to read
and write in them.

For the ability to understand any language, see the Com-
prehend effect in the Powers chapter.

FORTUNE

Your presence reassures and lends courage to your allies.
As  a  standard  action,  you  can  spend  a  hero  point  to  re-

138

```

**Chunk 36** (`b511fe78f53a`):

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

**Chunk 37** (`bf47e9f3d3ae`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

The  communications  feature  allows  the  headquarters
to receive and transmit on a wide range of radio and TV
bands,  monitor  police  and  emergency  channels,  coor-
dinate  communications  between  members  of  a  team,
and  so  forth.  It  includes  communications  equipment,
consoles, and monitors. The system’s access to restricted
communication  bands  depends  on  the  clearance  and
skills  of  the  user.  Heroes  often  have  access  to  special
government  channels,  while  a  successful  Technology
skill check (DC 25) can grant a user illegal access to re-
stricted systems.

COMPUTER

A  state-of-the-art  computer  system  serves  the  entire
headquarters.  This  allows  characters  to  make  full  use
of  the  Technology  skill  and  the  computer  can  be  pro-
grammed  to  handle  routine  base  functions  (including
monitoring  communications  channels  and  controlling
defensive  systems).  An  artificially  intelligent  computer
system should be created as a Minion or Sidekick, perhaps
with the cost shared among members of a team. See the
Constructs section for more.

CONCEALED

The  headquarters  is  hidden  from  the  outside  world  in
some way. It may be camouflaged behind a false façade,
buried underground, or something similar. Note this is in

addition to the Isolated feature, if any. An isolated head-
quarters is difficult to reach, while a concealed headquar-
ters  is  difficult  to  find  in  the  first  place.  Skill  checks  to
locate the headquarters have their DC increased by +10.
Each  additional  feature  applied  to  this  increases  the  DC
+5, to a maximum of +30.

A  defense  system  consists  of  various  weapon  emplace-
ments  defending  the  exterior  and  interior  of  the  head-
quarters.  A  defense  system  can  have  any  attack  effect
with  a  cost  no  greater  than  twice  the  HQ  power  level.
Their attack bonus is equal to the power level.

A  villainous  version  of  the  Defense  System  feature  is
deathtraps: the villain’s lair has one or more fiendish traps
suitable for disposing of those pesky heroes. Some death-
traps are designed as security systems to keep heroes out:
concealed auto-guns, walls of flames, sealing rooms that
fill with water or sand, and so forth. Others are intended
for the slow elimination of captured heroes.

Note that not having this feature does not mean a villain
cannot jury-rig a deathtrap wit

[... truncated ...]
```

**Chunk 38** (`c0c1858f03fe`):

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

**Chunk 39** (`c8f8dadd6203`):

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

**Chunk 40** (`d329357e5091`):

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

**Chunk 41** (`d5fc086574e9`):

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

**Chunk 42** (`d7e831fa5f41`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

In many instances, players come up with creative uses for their characters’ descriptors. This should be encouraged and,
generally speaking, allowed freely so long as those uses don’t spoil the game. So if a fire-using character wants to use
a tiny amount of his flame blast power to light some candles, or the electrical-controlling character wants to use some
of his power output to act as a living battery to jump-start a car, go for it. In the latter case you might want to call for a
Technology skill check to make sure the character gets the terminals and the voltage right, but most of the time it’s bet-
ter to just let the trick go through and give the character a chance to shine.

Creative uses of descriptors with no real game effect are freebies: no extra effort or hero points needed. Situations
where creative uses of descriptors have a significant game effect can be handled as power stunts: pick the effect that
best suits the desired outcome and treat it as an Alternate Effect of the power the hero wants to use, with descrip-
tors assigned as appropriate. If an electrical-controlling hero wants to use his power like a living defibrillator to save
a heart-attack victim, for example, that can be a Healing power stunt. The hero uses extra effort (and possibly a hero
point) and gets a one-shot use of Healing to stabilize the dying victim.

While  descriptors  are  generally  applied  to  powers  when
those  powers  are  defined  (that  is,  when  a  character  is
created),  in  some  cases,  certain  descriptors  may  be  left
unspecified  and  defined  during  play.  This  can  either  be
because nobody thought to define the descriptor in ad-
vance, or it was deliberately left vague, to be filled-in later.

So, for example, a particular heroine might not know the
origin or source of her powers, and her player doesn’t want
to know, leaving them a mystery for later development in
the game. The GM agrees and so the heroine’s powers have
no  origin  or  source  descriptors.  Instead,  the  GM  chooses
them, which isn’t known until the heroine is subject to an
anti-magical field and discovers her powers don’t work! The
GM awards the player a hero point for the unexpected set-
back and now the source of the heroine’s powers is known,
although their origin still remains a mystery….

Applying descriptors in play gives you a lot of flexibility,
letting you handle certain things “on the fly” rather than
having 

[... truncated ...]
```

**Chunk 43** (`dcdc4c459ab6`):

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

**Chunk 44** (`dd71074ce318`):

```
CHAPTER 1: THE BASICS
CHAPTER 1: THE BASICS

CHAPTER 1: THE BASICS

As you can see, once you break it down, checks are actual-
ly fairly simple. All the Gamemaster has to say in response
to the player’s declaration is: “Okay, roll a Fighting check
to hit the villain,” letting the rest of the description stand
as what happens. Whether or not the hero is successful in
stopping the trap depends on the outcome of the attack
against the bad guy.

Of course, if the villain is expecting the hero, there might be
another trap, such as part of the catwalk rigged to fall away
under him, leaving him dangling above the acid vat and at
the villain’s mercy! In that case, the GM would respond to
the  player’s  description: “You  smash  through  the  skylight
and swing over to the catwalk, but when you do...” and go
on to describe what follows. The rest of the hero’s intended
action(s) are null and void, because things don’t always go
as planned when you’re dealing with cunning supervillains!

Checks are used to resolve all outcomes in MUTANTS & MAS-
TERMINDS,  so  once  you  understand  the  basic  concept,  the
rest is easy. For detailed examples of how to use checks in
the game and their effects, see the Action & Adventure
chapter.

If  you  roll  a  20  on  the  die  when  making  a  check  you’ve
scored a critical success. Determine the degree of success
normally and then increase it by one degree. This can turn
a low-level success into something more significant, but
more importantly, it can turn a failure into a full-fledged
success! A critical success with an attack check is called a
critical hit, discussed later in this chapter and in the Ac-
tion & Adventure chapter.

Checks are made against a difficulty class or DC, a num-
ber set by the GM, which your check must equal or exceed
to achieve success. So for a task with a DC of 15 you must
roll a check total of 15 or greater to succeed. In some cas-
es, the results of a check vary based on how much higher
or lower the result is than the DC, known as its degree of
success or failure.

DIFFICULTY (DC)

EXAMPLE (SKILL USED)

Very easy (0)

Notice something in plain sight
(Perception)

Easy (5)

Climb a knotted rope (Athletics)

Average (10)

Tough (15)

Challenging (20)

Formidable (25)

Heroic (30)

Super-heroic (35)

Nigh-impossible (40)

Hear an approaching security
guard (Perception)

Disarm an explosive
(Technology)

Swim against a strong current
(Athletics)

Climb a wet, slippery rock-face
(Athletics)

Overcome 

[... truncated ...]
```

**Chunk 45** (`de3a74af09d1`):

```
CHAPTER 7: GADGETS & GEAR

227

Also  note  that,  in  spite  of  the  name,  not  all “deathtraps”
are  necessarily  lethal.  Some  may  be  intended  to  merely
incapacitate and capture intruders (more along the lines
of  a  nonlethal  Defense  System),  allowing  the  villain  to
interrogate them...and then perhaps put them into a real
deathtrap!

The  headquarters  has  a  portal  or  gateway  to  another
dimension or dimensions. This can range from an other-
wise  innocuous-looking  door  to  a  humming  high-tech
portal  surrounded  by  support  equipment  and  monitors.
The portal provides two-way travel to and from the other
dimension,  and  it  may  even  reach  a  number  of  related
dimensions.  At  the  GM’s  discretion,  an  appropriate  skill
check—typically  Expertise  or  Technology—may  be  re-
quired to operate the portal.

DOCK

A  dock  houses  water  vehicles  and  includes  access  to  a
nearby waterway, an airlock or lock system for moving ve-
hicles in and out of the dock, and dry-dock facilities for re-
pairing and maintaining water vehicles. The headquarters
should be located within reasonable distance of a body of
water to have this feature.
DUAL SIZE

The  headquarters  has  two  separate  Size  categories:  its
inside category (purchased normally), which determines
the  structure’s  interior  space,  and  an  outside  category,
one or more size categories smaller. In essence, the head-
quarters is larger on the inside than on the outside! So
a  small  house,  for  example,  might  contain  the  space
of a huge castle on the inside. The GM may even allow
size  categories  beyond  Awesome,  with  each  additional
category doubling size; expensive HQs could be pocket
universes!  Pay  the  cost  of  the  larger  size,  plus  this  fea-
ture,  which  lets  you  set  the  exterior  size  at  any  smaller
category.

In general, the exterior dimensions of the HQ cannot be
smaller than a miniscule structure, about the size of a clos-
et or phone booth (or, say, a wardrobe or police box), large
enough  for  an  adult  human  to  pass  through  whatever
serves as the base’s entrance. Headquarters that have no
“exterior” structure, such as an extra-dimensional fortress
accessed by a magical talisman, do not have this feature,
but instead have things like Dimensional Portal, Isolated,
Sealed, and the like.

EFFECT

A  headquarters  can  be  given  any  appropriate  power  ef-
fect as a feature with the Gamemaster’s approval. The ef-
fect  c

[... truncated ...]
```

**Chunk 46** (`e05fc680a484`):

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

**Chunk 47** (`eab98ce0e1fc`):

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

**Chunk 48** (`f41e7b13c82a`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

DISGUISE

You can use makeup, costumes, and other props to change
your appearance. Your Deception check result determines
the effectiveness of the disguise, opposed by others’ Per-
ception check results. The GM makes the Deception check
secretly so you are not sure exactly how well your disguise
holds up under scrutiny.

Disguise  is  heavily  dependent  on  circumstances:  favor-
able ones include appropriate costuming and a subject
resembling your normal appearance, while unfavorable
circumstances include disguising yourself as a member
of a different race or sex, or not having sufficient props
(which can be up to a –5 modifier). If you are imperson-
ating  a  particular  individual,  anyone  who  knows  that
individual gets a circumstance bonus to the Perception
check: regular associates get a +2, while friends get a +5
and intimate loved ones a +10.

Successfully  acting  like  who  you  appear  to  be  may  also
require a Deception check with a DC equal to the observ-
er’s Insight check, modified by familiarity if the observer
knows the subject well, as mentioned previously.

A disguise normally requires at least 10 minutes of prepa-
ration.  The  GM  makes  Perception  checks  for  those  who
encounter you immediately upon meeting you and each
hour or day thereafter, depending on circumstances.

FEINTING

You can use Deception as a standard action to mislead an
opponent in combat. Make a Deception check as a stan-
dard action opposed by the better of your target’s Decep-
tion or Insight. If your Deception check succeeds, the tar-
get is vulnerable against your next attack, until the end of
your next round (see Vulnerable in the Conditions sec-
tion of The Basics chapter).
INNUENDO

You  can  use  Deception  to  send  covert  messages  using
word-play and double-meanings while apparently talking
about other things. The DC for a basic message is 10. Com-
plex messages or messages trying to communicate new
information have DCs of 15 or 20, respectively. The recipi-
ent of the message must make a Insight check against the
same DC to understand it.

DC

10

15

20

TASK

Basic message

Complex message

Message containing new or detailed information

Anyone listening in on your innuendo can attempt a In-
sight  check  against  the  message  DC.  If  successful,  the
eavesdropper notices a message hidden in your conversa-

tion. If the eavesdropper gets at least two degrees of suc-
cess, he also unders

[... truncated ...]
```

**Chunk 49** (`f47cb1a00aa5`):

```
CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

CHAPTER 9: GAMEMASTERING
CHAPTER 9: GAMEMASTERING

One player—the Gamemaster or “GM”—takes responsibility for running a MUTANTS & MASTERMINDS game. The Game-
master  creates  the  adventure,  runs  the  players  through  it,  takes  on  the  roles  of  the  various  other  characters  the
heroes encounter, and handles any questions about the rules as they arise. The Gamemaster also adjudicates the
process of character creation, deciding what traits, modifiers, and so forth are appropriate for the particular game,
along with the best way to express certain concepts in game terms. While Gamemastering is a big responsibility, it’s
not as hard as it might seem, and providing a fun and entertaining game for your friends can be quite rewarding.

While the players are responsible for keeping track of their characters and deciding on their actions, the Gamemaster is
responsible for everything else that happens in the game. A good GM tries to make sure the game runs as smoothly as
possible and is enjoyable for all of the players. Many components go into creating a good MUTANTS & MASTERMINDS game.
The following sections give you the basics, but experience is the best tool to help you become a better Gamemaster.

can  be  broken  down  into  a  series
of tasks the heroes must perform, from piecing together
clues  about  a  villain’s  latest  scheme  to  blasting  said  vil-
lain through a wall and disarming his doomsday device in
the nick of time. It’s up to the Gamemaster to assign the
difficulty of these and numerous other tasks in the game
and to determine the outcome of the heroes’ efforts. This
section  offers  some  general  guidelines  on  assigning  the
difficulty of a task.

THE 55% RULE

tract 10 from the DC. So a DC 25 action (a formidable task)
requires a bonus of +15 in order to have a 55% chance of
success (on a roll of 10 or higher).

Keep in mind that this chance of success on a task allows
a character to automatically succeed at that task as a rou-
tine  check  (see  Routine  Checks,  following,  and  in  The
Basics chapter). This is intentional; the average character
only really fails at an average task when hurried or under
stress. A 55% chance also allows a player to spend a hero
point to automatically succeed, since a hero point ensures
a die roll of at least 11. (See Hero Points, page 20.)

A good guideline to keep in mind is the chance of an aver-
age character (with a modifier of 0) succeeding

[... truncated ...]
```

**Chunk 50** (`f6ef830f7b6b`):

```
CHAPTER 4: SKILLS

127

goes off. For every two full degrees of success, the explo-
sive deals +5 damage to the structure. Failure means the
explosive does not go off as planned, while more than one
degree of failure means the charge goes off while you are
setting it! In all cases, the explosive deals normal damage
to all other targets.

You  can  make  an  explosive  device  more  difficult  to  dis-
arm. To do so, choose a disarm difficulty class before mak-
ing  your  check  to  set  the  detonator. Your  DC  to  set  the
detonator  is  the  desired  disarm  DC.  Failure  means  the
explosive fails to go off as planned. Two or more degrees
of failure mean the explosive goes off as the detonator is
being installed!

Disarming an explosive also requires a Technology check.
The DC is usually 10, unless the person who set the deto-
nator chose a higher disarm DC (previously). If you fail the
check, you do not disarm the explosive. With more than a
degree of failure, the explosive goes off. Setting or disarm-
ing a detonator is a standard action.
INVENTING

If you have the Inventor advantage (see the Advantages
chapter),  you  can  use  Technology  to  create  inventions,
temporary devices. See Inventing, page 211, for details.

SECURITY

You  can  use  Technology  to  disarm  or  sabotage  various
security devices, including locks, traps, and sensors. This
takes  at  least  a  minute,  possibly  longer,  at  the  GM’s  dis-
cretion.  The  GM  makes  your  Technology  check  secretly
so you don’t necessarily know right away if you have suc-
ceeded. The Gamemaster sets the DC of the check based
on the level of security:

Simple lock or home alarm system

Quality lock or home alarm system

Business and corporate security

High security: branch bank vault, museum

Very high security: bank headquarters
vault, medium prison

Maximum security: highly secure prison

Super-max security: super-prison

MODIFIERS

Preventing your tampering
 from being noticed.

DC

10

15

20

25

30

35

40

+5

Failure  on  your  skill  check  means  nothing  happens,  but
you can keep trying. More than one degree of failure sets
off the security or trap, if it is possible to do so.

128

```

---

## Concept: Teleport

Chunk count: 17
Performs actions: ['act_0069', 'act_0390', 'act_0391']

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

**Chunk 2** (`14dd371ce972`):

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

**Chunk 4** (`2b9b77a24290`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

TYPE

ACTION

RANGE

DURATION

COST

Sensory

General

General

Attack

Attack

None

Move

Free

Standard

Standard

Personal

Personal

Personal

Ranged

Ranged

Permanent

Sustained

Sustained

Instant

Instant

—

—

—

Fortitude

Dodge

Movement

Free

Personal

Sustained

—

Standard

Standard

Standard

Free

Free

Move

Standard

Standard

Standard

Close

Ranged

Close

Instant

Instant

Sustained

Personal

See description

Personal

Sustained

Rank

Close

Personal

Close

Instant

Sustained

Sustained

Toughness

Fortitude

—

—

—

—

—

—

Instant

Fort. or Will

1 per rank

8 per rank

2 per rank

2 per rank

3 per rank

1 per rank

1 per rank

4 per rank

2 per rank

3 per rank

1 per rank

2 per rank

2-5 per rank

7 per rank

1 per rank

NAME

Senses

Shapeshift

Shrinking

Sleep

Snare

Speed

Strike

Suffocation

Summon

Attack

Attack

Control

Super-Speed

See description

Movement

Movement

Control

General

Attack

Swimming

Teleport

Transform

Variable

Weaken

RANGE

Each  effect  has  a  default  range,  which  may  be  changed
by modifiers.

•

•

•

•

•

Personal: The effect works only on you, the user.

Close: The effect can target anyone or anything you
touch. Touching an unwilling subject requires an un-
armed attack check against the subject’s Parry.

Ranged:  The  effect  works  at  a  distance,  limited  by
perception  and  path  and  requiring  a  ranged  attack
check against the subject’s Dodge defense. A ranged
effect has a short range of (rank x 25 feet), a medium
range  of  (rank  x  50  feet)  and  a  long  range  of  (rank
x 100 feet). Ranged attack checks at medium range
suffer  a  –2  circumstance  penalty,  while  ranged  at-
tacks at long range suffer a –5 circumstance penalty.
See the Action & Adventure chapter for details.

Perception: The effect works on any target you can
perceive  with  an  accurate  sense,  without  any  need
for an attack check. If you cannot accurately perceive
the target, you cannot affect it.

Rank:  The  effect’s  range  or  area  of  effect  is  deter-
mined by its rank, as given in its description.

DURATION

so.  If  you  are  incapable  of  taking  the  necessary  ac-
tion, or simply choose not to, the effect ends.

Sustained: You can keep a sustained effect going by
taking  a  free  action  each  round  to  do  so.  If  you  are
incapable  of  taking  the  necessary  action,  or  simply
choose not to, the effect ends.

C

[... truncated ...]
```

**Chunk 5** (`373c8323a9b6`):

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

**Chunk 7** (`685941d4ae65`):

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

**Chunk 9** (`8757660124bd`):

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

**Chunk 10** (`9f103da0da38`):

```
CHAPTER 7: GADGETS & GEAR

229

the headquarters. As such, they shouldn’t be considered
all-purpose Minions of the occupant(s). A base’s person-
nel may help defend it in case of attack, but they’re not
going to go out on missions or otherwise assist outside
of their duties. This feature simply ensures there’s some-
one  taking  care  of  the  place  while  the  owner  isn’t  at
home.

Note that an HQ’s personnel do not have to be ordinary
humans.  They  could  be  service  robots,  magical  golems,
animated skeletons, enslaved aliens, trained apes, or just
about anything else the GM chooses to fit with the theme
of the base and its owner(s).

A  power  system  makes  the  headquarters  completely
independent  of  outside  power.  It  has  its  own  genera-
tors  (which  may  be  solar,  geothermal,  nuclear,  cosmic,
or  anything  else  the  designer  wants). They  provide  the
base’s  entire  power  needs.  The  headquarters  also  has
emergency  back-up  power  should  the  generators  fail.
This  generally  lasts  for  a  number  of  hours  equal  to  the
HQ’s power level.

SEALED

This  is  similar  to  the  Isolated  feature,  except  the  lair  is
sealed off from the outside world rather than isolated by
geographic location. It may be a structure with no doors,
windows,  or  other  outside  access,  or  behind  some  sort
of  barrier.  Only  the  lair’s  owner  and  designated  guests
may enter, although the GM should determine means by
which  trespassers  might  do  so,  including  effects  like  Di-
mensional Travel, Insubstantial, Permeate, and Teleport.

SECRET

does. If this feature is taken twice, the structure will even
rebuild itself in a week if it is destroyed! If it cannot rebuild
in its original location, it reappears in the nearest suitable
place.

Time within the headquarters actually moves at a differ-
ent  rate  than  that  of  the  world  outside! Time  within  the
structure is either slowed or sped up compared to the nor-
mal passage of time, passing at half or twice the normal
rate.  Each  additional  application  of  this  feature  doubles
the ratio of time passage: one-quarter or four times, one-
eighth or eight times, and so forth.

This  time  differential  allows  a  character  within  an  accel-
erated  Temporal  Limbo  to  spend  additional  time  plan-
ning, building, or recovering while little or no time passes
outside,  for  example.  Conversely,  it  allows  characters  in
a slowed Temporal Limbo to pass great amounts o

[... truncated ...]
```

**Chunk 11** (`aa5babc5f423`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

As with the Feature effect, a Feature extra should be sig-
nificant  enough  to  be  worth  at  least  1  power  point  and
not solely based on the power’s descriptors. So, for exam-
ple, a fiery Ranged Damage effect does not need a Feature
to ignite fires; doing so is part of its “fire” descriptor and
can be equally advantageous and problematic. A Ranged
Damage effect that consistently “brands” its target with a
visible and traceable mark, on the other hand, is an effect
with an added Feature.

HOMING

FLAT • 1 POINT PER RANK

This modifier grants a ranged effect an additional oppor-
tunity to hit. If an attack check with a Homing effect fails, it
attempts to hit again on the start of your next turn, requir-
ing only a free action to maintain and allowing you to take
other actions, including making another attack. Each rank
in Homing grants the effect one additional attack check,
but it still only gets one check per round.

The  Homing  effect  uses  the  same  accurate  sense  as  the
original attack to “track” its target, so concealment effec-
tive against that sense may confuse the effect and cause
it to miss. If a Homing attack misses due to concealment,
it  has  lost  its “lock”  on  the  target  and  does  not  get  any
further  chances  to  hit.  You  can  take  Senses  Linked  to
the Homing effect, if desired (to create things like radar-
guided or heat-seeking missiles, for example). If a Homing
attack  is  countered  before  it  hits,  it  loses  any  remaining
chances to hit. The same is true if it hits a different target.

+1 COST PER RANK

A defense with this modifier is highly resistant. Any effect
with a resistance difficulty modifier equal to or less than
half the Impervious rank (rounded up) has no effect. So,
for  example,  Impervious Toughness  9  ignores  any  Dam-
age with a rank of 5 or less. Penetrating effects can over-
come  Impervious  Resistance  (see  the  Penetrating  extra
description).

Impervious is primarily intended for Toughness resistance
checks, to handle characters immune to a certain thresh-
old  of  damage,  but  it  can  be  applied  to  other  defenses
with  the  GM’s  permission,  to  reflect  characters  with  cer-
tain reliable capabilities in terms of resisting particular ef-
fects or hazards.

+1 COST PER RANK

Effects have a standard duration: instant, sustained, con-
tinuous,  or  permanent.  See  Duration  at  the  start  of  this
chapter for details.

[... truncated ...]
```

**Chunk 12** (`ab446868e7fe`):

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

**Chunk 13** (`d4cad3e10e05`):

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

**Chunk 14** (`d5fc086574e9`):

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

**Chunk 15** (`db8b2bdf371a`):

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

**Chunk 17** (`f45e1af7c8dc`):

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

---

## Concept: Tether

Chunk count: 1
Receives actions: ['act_0191']

### Chunk texts

**Chunk 1** (`c7946753c154`):

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

---

## Concept: Thieves

Chunk count: 0
Receives actions: ['act_0510']

### Chunk texts

---

## Concept: Throwing

Chunk count: 1

### Chunk texts

**Chunk 1** (`bb3e97c13b71`):

```
CHAPTER 4: SKILLS
CHAPTER 4: SKILLS

CHAPTER 4: SKILLS

people are favorable or indifferent toward heroes, but a
specific circumstance or complication may call for a dif-
ferent attitude.

You  can  improve  others’  attitudes  with  a  DC  15  Persua-
sion  check.  Success  improves  the  subject’s  attitude  by
one  step,  while  every  two  additional  degrees  of  success
improve it by another step (so two steps at three degrees,
three  steps  at  five  degrees,  and  so  forth).  Failure  means
no change, and more than a degree of failure worsens the
subject’s attitude by one step! In the case of a hostile sub-
ject, they may outright attack or otherwise interfere with
you if their attitude worsens.

ATTITUDES

ATTITUDE

EFFECT

Hostile

Will take risks to attack
or interfere with you.

Unfavorable

Will insult, mislead,
or otherwise cause you trouble.

Indifferent

Favorable

Helpful

Acts as socially expected
towards you.

Will chat, advise,
and offer limited help.

Will take risks to
help or protect you.

Persuading someone is at least a standard action, usually
quite a bit longer. The GM decides if you can persuade at
all once a conflict has broken out! Even if the initial check
succeeds,  the  other  character  can  only  be  persuaded  so
far;  you  can  try  again  in  the  same  scene,  but  you  check
against the subject’s initial attitude, and may end up wors-
ening it rather than improving it!

Example:  The  heroes  must  convince  the  imperi-
ous King of Atlantis that the surface world is not
responsible  for  recent  attacks  against  his  king-
dom  in  order  to  avert  a  war.  The  king’s  attitude
is  unfavorable  towards  these  surface-world  in-
terlopers  to begin with. The team’s spokesperson
makes  a  Persuasion  attempt  and  gets  a  check
result  of  22,  a  success  with  two  degrees  total.
That  shifts  the  king’s  attitude  one  step,  to  indif-
ferent. He’s inclined to continue negotiating with
the heroes and willing to place the assault on the
surface world on-hold for the time-being. The he-
roes try to convince the king further, but any ad-
ditional checks need at least the same degree of
success as the first to get his attitude to favorable,
where he is willing to call off the attack, and more
than one degree of failure on any check moves his
attitude to hostile, where he orders the intruders
arrested and the attack to begin at once!

way:  you  find  a  new  approach  to  your  argument,  new
evidence appears,

[... truncated ...]
```

---

## Concept: Thugs

Chunk count: 1
Performs actions: ['act_0134']

### Chunk texts

**Chunk 1** (`9a2865ac841b`):

```
CHAPTER 4: SKILLS

121

ceed or fail, a target’s true attitude towards you generally
becomes hostile after you attempt an Intimidation check,
even if they go along with you for the moment.

You can use Intimidation in combat as a standard action
to undermine an opponent’s confidence. Make an Intimi-
dation check as a standard action. If it succeeds, your tar-
get is impaired (a –2 circumstance penalty on checks) un-
til the end of your next round. With four or more degrees
of success, the target is disabled (a –5 penalty) until the
end of your next round.

You can intimidate a whole group of minions—who can
all see and hear you—with a single check. If the group has
you at a disadvantage, you suffer the usual circumstance
penalty on your check. Compare your check result against
a single resistance check made by the GM for the entire
group. Your Intimidation check must have the same effect
on every member of the group (that is, you cannot demor-
alize some and coerce others, for example).

Example:  Rocky  is  facing  down  Pack-Rat  in  one
of his many bolt holes around Emerald City when
the big rat commands a pack of his street thieves
to keep Rocky from following him. The gang of kids
steps forward to get in Rocky’s way. Rocky has no
interest in hurting a bunch of kids, so he bellows,
“Get  outta  the  way  or  I’ll  knock  your  blocks  off!”
and his player decides to use Rocky’s routine Intimi-
dation check of 18 to attempt to coerce the entire
group of minions into moving out of his way. The
street kids are all Thugs, so they have a resistance
rank  of  0  (their  Insight  and  Will  ranks  are  tied).
Since Rocky is attempting the same effect on every
member of the group, he makes a single opposed
check. Unfortunately, the GM rolls a 13, which isn’t
enough  to  beat  Rocky’s  18.  The  street  kids  know
Rocky won’t actually hurt them, but they dive out
of the way anyway as Rocky bulls past.”

Intellect • Trained Only

You  know  how  to  search  for  and  study  clues,  gather  in-
formation through interviews and surveillance, and ana-
lyze evidence to help solve crimes. The GM may make In-
vestigation checks for you in secret, so you do not know
exactly what you have found, or if you may have missed
something.

SEARCH

You can search an area for clues, hidden items, traps, and
other details. Perception allows you to immediately notice
things, while an Investigation check allows you to pick up
on details with some effort.

122

```

---

## Concept: Thunder

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

## Concept: Tiring

Chunk count: 1

### Chunk texts

**Chunk 1** (`7ade13289c0f`):

```
CHAPTER 6: POWERS
CHAPTER 6: POWERS

CHAPTER 6: POWERS

use of a tiring effect. In essence, the power requires extra
effort  in  order  to  use  it  (see  Extra  Effort,  page  19). This
makes Tiring a useful flaw for creating an effect you can
only use with extra effort.

Tiring is often applied to just some ranks of an effect to rep-
resent a higher level of the effect, usable only through extra
effort. For example, a hero might have a rank 12 Damage
effect, but routinely use only 8 ranks of it. The remaining
4 ranks are Tiring, so using them quickly fatigues the hero.

A Tiring effect can be combined with extra effort, but the
fatigue stacks, causing a minimum of two levels of fatigue
per use.

-1 COST PER RANK

You have no control over an effect with this flaw. Instead,
the Gamemaster decides when and how it works (essen-
tially  making  it  a  plot  device). This  flaw  is  best  suited  for
mysterious powers out of the characters’ direct control or
effects the GM feels more comfortable having under direct,
rather than player, control.

-1 COST PER RANK

An Unreliable effect doesn’t work all the time. Roll a die
each round before you use or maintain the effect. On a
10 or less, it doesn’t work this round, but you’ve still used
the action the effect requires. You can roll again on the
following  round  to  see  if  it  works,  although  you  must
take  the  normal  action  needed  to  activate  the  effect
again. Spending a hero point on your reliability roll al-

lows you to succeed automatically (since the roll is then
at least an 11).

Alternately,  instead  of  having  a  reliability  roll,  you  can
choose to have five uses where your effect works normal-
ly, then it stops working altogether until you can “recover”
it in some way (see the Fades flaw for more on this). The
GM may allow you to spend a hero point to automatically
recover a spent Unreliable power.

Powers  that  are  only  occasionally  unreliable  (less  than
about 50% of the time) are better handled as complica-
tions (see Complications, page 30).

One possible application of the Unreliable flaw is to re-
flect weapons or equipment that occasionally run out of
ammunition or “jam” or “crash” and must be reloaded or
reset in some way. It really only applies to effects where
this happens fairly often, as given in the Unreliable flaw
description. Large ammo or fuel capacities, which only
occasionally run out or inconvenience the character, are
better handled as descriptors and occasiona

[... truncated ...]
```

---

## Concept: Totem

Chunk count: 2
Performs actions: ['act_0094']
Receives actions: ['act_0094']

### Chunk texts

**Chunk 1** (`75f616f43b9d`):

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

**Chunk 2** (`f8e903dbf3d7`):

```
CHAPTER 2: SECRET ORIGINS
CHAPTER 2: SECRET ORIGINS

CHAPTER 2: SECRET ORIGINS

*If you rolled Vampire for Abilities, then you have Abilities
44, Powers 73, and Defenses 17; otherwise, you have Abili-
ties 62, Powers 52, and Defenses 20.

•  Motivation—Acceptance:  The  Supernatural  Crea-

ture is usually an outcast.

•  Motivation—Doing  Good:  Some  Supernatural
Creatures  attempt  to  go  against  the  grain  and  use
their powers for good.

•

•

•

Power Loss: Some Supernatural Creatures only have
their powers at night, or lose their powers when on
holy  ground  or  when  they  assume  human  form...  if
they have one.

Quirk—Angst:  The  Supernatural  Creature  often
feels great anguish over its lost humanity.

Reputation:  Most  humans  regard  Supernatural
Creatures with fear and hatred as a result of folklore
and myth.

•  Weakness:  Supernatural  Creatures  may  be  vulner-
able to holy weapons. Others may be unable to func-
tion in sunlight.

TOTEM

AVIAN

STRENGTH
4
STAMINA
6

AGILITY
8
DEXTERITY
4
CARNIVORAN

STRENGTH
7
STAMINA
6

AGILITY
5
DEXTERITY
2
PACHYDERM

STRENGTH
12
STAMINA
7
REPTILE

AGILITY
2
DEXTERITY
2

FIGHTING
8
INTELLECT
0

AWARENESS
4
PRESENCE
0

FIGHTING
10
INTELLECT
0

AWARENESS
3
PRESENCE
1

FIGHTING
5
INTELLECT
0

AWARENESS
3
PRESENCE
3

The Totem is a superhero whose powers are closely tied to
a particular animal. The Totem may have acquired its pow-
ers  through  an  accident  of  science,  an  invocation  of  the
animal spirits, or may even be an exceptional, self-aware
animal. Totem heroes tend to be as varied as the animals
they represent, and they can resemble other archetypes
such as the Martial Artist, Warrior, and Powerhouse.
ABILITIES

STRENGTH
10
STAMINA
8

AGILITY
4
DEXTERITY
3

FIGHTING
6
INTELLECT
1

AWARENESS
2
PRESENCE
0

Roll 1d20 once and record the result

Roll  on  both  the  Behavioral  Advantages  table  and  the
Social Advantages table.

1-4

Arthropod: Your totem is a spider, scorpion, wasp,
or even an insect swarm.

5-8

Avian: Your totem is a bird like a falcon or owl.

9-14

15-17

18-20

Carnivoran: Your totem is a carnivore from the
canine, lupine, or feline family.

Pachyderm: Your totem is a massive, thick-hided
mammal, such as an elephant or rhinoceros.

Reptile: Your totem is a reptile, such as a crocodile,
lizard, or snake.

ARTHROPOD

Roll 1d20 once and record the result.

1-4

5-8

9-12

Active: You are in constant motion.

Catch and Hold: You like to grab hold of your prey.

Mystic: Yo

[... truncated ...]
```

---

## Concept: Tough

Chunk count: 2
Receives actions: ['act_0201', 'act_0378']

### Chunk texts

**Chunk 1** (`c51168f2be2c`):

```
CHAPTER 7: GADGETS & GEAR
CHAPTER 7: GADGETS & GEAR

CHAPTER 7: GADGETS & GEAR

* = See individual descriptions for more information.

Trucks  include  pick-ups,  sport  utility
vehicles (SUVs), vans, and similarly
sized vehicles.

Tanks are heavily armed
and  armored  vehicles.
The standard tank has
Tough-
Impervious
ness  12  and  comes
equipped  with  a  can-
non  (Ranged  Damage  10,
Burst Area 6) and a heavy machine
gun (Ranged Multiattack Damage 6). It
takes a move action to get into or out
of a  tank, and another move action
to start it up.

APCs or Armored Personnel Car-
riers,  are  designed  for  carry-
ing  troops.  They  come  with
a  smaller  cannon  (Ranged
Damage  6,  Burst  Area  4),
Impervious  Toughness  8,
and are set up so soldiers on
board can fire their personal
weapons  from  behind  the
cover of the APC’s armor.

Water vehicles range from small boats and outboards to
massive sea-going ships.

Cutters are used by the Coast Guard and the Navy. They’re
often equipped with light machine guns (Ranged Multiat-
tack Damage 6).

Destroyers  are  main  naval  ships,  carrying  heavy  guns
(Ranged Damage 10, Burst Area 8).

Battleships have massive gun batteries (Ranged Damage
13, Burst Area 9) and heavy armor.

Submarines are equipped with torpedoes (Ranged Dam-
age  8,  Burst  Area  5)  and  often  ballistic  missiles  (Ranged
Burst  Area  Damage  15  or  higher,  not  included  in  listed
cost).

Air vehicles are all capable of flight, some of them at very
high speeds.

Military  helicopters  are  equipped  with  machine  guns
(Ranged  Multiattack  Damage  6)  and  rockets  (Ranged
Damage 9, Burst Area 6).

Fighter  jets  have  machine  guns  (Ranged  Multiattack
Damage  6)  and  air-to-air  missiles  (Ranged  Damage  11,
Burst Area 8, Homing 6).

Bombers may have machine guns and missiles, but also
have powerful bombs (Burst Area Damage 12 or higher)
they can drop on targets.

Space  vehicles  are  intended  for  use  outside  the  atmo-
sphere, some of them for interplanetary or even interstel-
lar travel. Generally space vehicles are found in the pos-
session of alien civilizations, although the GM may choose
to allow some organizations and individuals on Earth to
have space vehicles.

Space fighters are armed with blaster cannons (Ranged
Damage 10).

Space cruisers have larger beam weapons (Ranged Dam-
age 12) and often energy torpedoes (Ranged Damage 12,
Burst Area 10, Homing 8).

Space  battleships  have  the  most  massive  weapons:

[... truncated ...]
```

**Chunk 2** (`f1bc1ad153ee`):

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

---

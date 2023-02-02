import os
import string
import pickle
import time

import xml.dom.minidom

import global_vars as gv

#XP Thresholds by Character Level
EasyXP = [0,25,50,75,125,250,300,350,450,550,600,800,1000,1100,1250,1400,1600,2000,2100,2400,2800]
MediumXP = [0,50,100,150,250,500,600,750,900,1100,1200,1600,2000,2200,2500,2800,3200,3900,4200,4900,5700]
HardXP = [0,75,150,225,375,750,900,1100,1400,1600,1900,2400,3000,3400,3800,4300,4800,5900,6300,7300,8500]
DeadlyXP = [0,100,200,400,500,1100,1400,1700,2100,2400,2800,3600,4500,5100,5700,6400,7200,8800,9500,10900,12700]
DailyXP = [0,300,600,1200,1700,3500,4000,5000,6000,7500,9000,10500,11500,13500,15000,18000,20000,25000,27000,30000,40000]

#These spells included in the Players Handbook Basic Rules
Basic5E_Spells = ['Acid Splash','Aid','Antimagic Field','Arcane Eye','Arcane Lock','Astral Projection',
                 'Augury','Beacon of Hope','Blade Barrier','Bless','Blur','Burning Hands',
                 'Chain Lightning','Charm Person','Command','Commune','Comprehend Languages',
                 'Cone of Cold','Counterspell','Cure Wounds','Dancing Lights','Darkness','Death Ward',
                 'Delayed Blast Fireball','Detect Magic','Detect Magic','Dimension Door','Disguise Self',
                 'Disintegrate','Dispel Magic','Dispel Magic','Divination','Dominate Monster',
                 'Dominate Person','Dream','Earthquake','Etherealness','Find the Path','Finger of Death',
                 'Fire Bolt','Fire Storm','Fireball','Flame Strike','Flaming Sphere','Fly','Foresight',
                 'Freedom of Movement','Gate','Globe of Invulnerability','Greater Invisibility',
                 'Greater Restoration','Guardian of Faith','Guidance','Guiding Bolt','Harm','Haste',
                 'Heal','Healing Word','Heroes Feast','Hold Person','Hold Person','Holy Aura',
                 'Ice Storm','Identify','Imprisonment','Inflict Wounds','Invisibility','Knock',
                 'Lesser Restoration','Levitate','Light','Light','Lightning Bolt','Locate Creature',
                 'Mage Armor','Mage Hand','Magic Missile','Magic Weapon','Major Image','Mass Cure Wounds',
                 'Mass Heal','Mass Healing Word','Mass Suggestion','Maze','Meteor Swarm',
                 'Minor Illusion','Misty Step','Mordenkainens Sword', "Otto's Irresistible Dance",
                 'Passwall','Poison Spray','Power Word Kill','Power Word Stun','Prayer of Healing',
                 'Prestidigitation','Protection from Energy','Protection from Energy','Raise Dead',
                 'Ray of Frost','Regenerate','Remove Curse','Resistance','Resurrection','Revivify',
                 'Sacred Flame','Sanctuary','Shatter','Shield','Shield of Faith','Shocking Grasp',
                 'Silence','Silent Image','Sleep','Spare the Dying','Speak with Dead','Spider Climb',
                 'Spirit Guardians','Spiritual Weapon','Stoneskin','Suggestion','Sunburst','Teleport',
                 'Thaumaturgy','Thunderwave','Time Stop','True Resurrection','True Seeing','True Seeing',
                 'Wall of Fire','Wall of Stone','Warding Bond','Web']

#These monsters are included in the D&D DM Basic Rules, version 0.3, retrieved 4/29/2015
Basic5E_Monsters = ["Adult Red Dragon","Air Elemental","Allosaurus","Animated Armor","Ankheg",
                    "Ankylosaurus","Ape","Awakened Shrub","Awakened Tree","Axe Beak ","Baboon",
                    "Badger","Banshee","Basilisk","Bat","Black Bear","Blink Dog","Boar","Blood Hawk",
                    "Brown Bear","Bugbear","Camel","Cat","Centaur","Chimera","Cockatrice ","Crab",
                    "Crocodile","Constrictor Snake","Cyclops","Death Dog","Deer","Dire Wolf",
                    "Doppelganger","Draft Horse","Earth Elemental","Elephant","Elk","Fire Elemental",
                    "Fire Giant","Flameskull","Flesh Golem","Flying Snake","Flying Sword","Frog",
                    "Frost Giant","Gargoyle","Ghost","Ghoul","Giant Ape","Giant Badger","Giant Bat",
                    "Giant Boar","Giant Centipede","Giant Constrictor Snake","Giant Crab",
                    "Giant Crocodile","Giant Eagle","Giant Elk","Giant Fire Beetle","Giant Frog",
                    "Giant Goat","Giant Hyena","Giant Lizard","Giant Octopus","Giant Owl",
                    "Giant Poisonous Snake","Giant Rat","Giant Scorpion","Giant Sea Horse",
                    "Giant Shark","Giant Spider","Giant Toad","Giant Vulture","Giant Wasp",
                    "Giant Weasel","Giant Wolf Spider","Gnoll","Goat","Goblin","Grick","Griffon",
                    "Harpy","Hawk","Hell Hound","Hill Giant","Hippogriff","Hobgoblin","Hunter Shark",
                    "Hydra","Hyena","Jackal","Killer Whale","Kobold","Lion","Lizard","Lizardfolk",
                    "Mammoth","Manticore","Mastiff","Medusa","Merfolk","Minotaur","Mule","Mummy",
                    "Nothic","Ochre Jelly","Octopus","Ogre","Orc","Owl","Owlbear","Panther","Pegasus",
                    "Phase Spider","Plesiosaurus","Poisonous Snake","Polar Bear","Pony","Pteranodon",
                    "Quipper","Rat","Raven","Reef Shark","Rhinoceros","Riding Horse",
                    "Saber-Toothed Tiger","Satyr","Scorpion","Sea Horse","Skeleton","Spectator",
                    "Spider","Stirge","Stone Golem","Swarm of Bats","Swarm of Insects",
                    "Swarm of Poisonous Snakes","Swarm of Quippers","Swarm of Rats","Swarm of Ravens",
                    "Tiger","Triceratops","Troll","Twig blight","Tyrannosaurus Rex","Vulture",
                    "Warhorse","Water Elemental","Weasel","Werewolf","Wight","Winter Wolf","Wolf",
                    "Worg","Wyvern","Yeti","Young Green Dragon","Zombie"]

#These spells included in the Hoard of the Dragon Queen Online Supplement, retrieved 5/8/15
HotDQ_5E_Spells = ['Animal Friendship','Antimagic Shell','Barkskin','Beast Sense','Blindness/Deafness',
                  'Calm Emotions','Chromatic Orb','Color Spray','Confusion','Counterspell','Daylight',
                  'Detect Evil and Good','Detect Thoughts','Disguise Self','Druidcraft','Entangle', 
                  'Evards Black Tentacles','Feather Fall','Fog Cloud','Gaseous Form','Gust of Wind',
                  'Insect Plague','Longstrider','Mirror Image','Mislead','Phantasmal Force','Plant Growth',
                  'Poison Spray','Scorching Ray','Seeming','Sending','Shatter','Sleet Storm','Spike Growth',
                  'Wall of Fire','Water Walk']

#These monsters included in the Hoard of the Dragon Queen Online Supplement, retrieved 5/8/15
HotDQ_5E_Monsters = ['Acolyte','Adult Blue Dragon','Adult White Dragon','Air Elemental','Assassin','Bandit',
                    'Berserker','Bullywug','Commoner','Crocodile','Cultist','Deer','Doppleganger','Elk', 
                    'Ettercap','Gargoyle','Giant Centipede','Giant Frog','Giant Lizard','Giant Spider','Gray Ooze', 
                    'Griffon','Guard','Helmed Horror','Hobgoblin','Hobgoblin Captain','Knight','Kobold', 
                    'Lizardfolk','Mage','Noble','Ogre','Orc','Otyugh','Peryton','Priest','Roper','Rug of Smothering',
                    'Scout','Shambling Mound','Specter','Spy','Stirge','Stone Giant','Stone Golem','Swarm of Insects',
                    'Swarm of Rats','Troglodyte','Troll','Vampire','Vampire Spawn','Veteran','Violet Fungus','Will o Wisp',
                    'Winged Kobold','Wyvern','Yuan-Ti Malison','Yuan-Ti Pureblood']

#These spells included in the Rise of Tiamat Online Supplement, retrieved 5/8/15
RoT_5E_Spells = ['Animal Messenger','Animate Dead','Animate Objects','Call Lightning','Chromatic Orb','Cloud of Daggers',
                'Cloudkill','Color Spray','Confusion','Continual Flame','Detect Thoughts','Divine Word','Enlarge/Reduce',
                'Evards Black Tentacles','Feather Fall','Fire Shield','Gaseous Form','Glyph of Warding','Hold Monster',
                'Legend Lore','Magic Jar','Magic Mouth','Mirror Image','Mislead','Move Earth','Phantasmal Force','See Invisibility', 
                'Seeming','Sending','Slow','Speak with Animals','Speak with Plants','Stinking Cloud','Stone Shape',
                'Water Breathing','Wish','Zone of Truth']

#These monsters included in the Rise of Tiamat Online Supplement, retrieved 5/8/15
RoT_5E_Monsters = ['Adult White Dragon','Air Elemental','Animated Armor','Assassin','Awakened Tree','Barbed Devil','Bearded Devil',
                  'Bone Devil','Chimera','Chuul','Clay Golem','Commoner','Cultist','Cult Fanatic','Cyclops','Dao','Druid',
                  'Earth Elemental','Efreeti','Ettercap','Ettin','Fire Elemental','Ghost','Giant Octopus','Gladiator','Gorgon',
                  'Guard','Helmed Horror','Knight','Kobold', 
                  'Lizardfolk','Mage','Merrow','Mummy','Mummy Lord','Noble','Ogre','Otyugh','Polar Bear','Pseudodragon',
                  'Specter','Succubus','Swarm of Poisonous Snakes','Swarm of Ravens','Tribal Warrior','Troll','Vampire',
                  'Vampire Spawn','Warhorse','Water Elemental','Wight','Wolf','Wraith',
                  'Yuan-Ti Abomination','Yuan-Ti Malison','Yuan-Ti Pureblood']

#These spells included in the Elemental Evil Players Companion, retrieved 3/17/15
ElementalEvil_5E_Spells = ['Abi-Dalzims horrid wilting','Absorb elements', 'Aganazzars scorcher','Beast bond','Bones of the earth',
                          'Catapult','Control flames','Control winds','Create bonfire','Dust devil','Earth tremor','Earthbind',
                          'Elemental bane','Erupting earth','Flame arrows','Frostbite','Gust','Ice knife','Immolation','Investiture of flame',
                          'Investiture of ice','Investiture of stone','Investiture of wind','Maelstrom','Magic stone','Maximilians earthen grasp',
                          'Melfs minute meteors','Mold earth','Primordial ward','Pyrotechnics','Shape water','Skywrite','Snillocs snowball swarm',
                          'Storm sphere','Thunderclap','Tidal wave','Transmute rock','Vitriolic sphere','Wall of sand','Wall of water',
                          'Warding wind','Watery sphere','Whirlwind']

ElementalEvil_5E_Monsters = []

PotA_5E_Spells = []

PotA_5E_Monsters = []

#These spells are included in the 5th Edition OGL
Bard_0_Spells = ['Dancing Lights','Light','Mage Hand','Mending','Message','Minor Illusion','Prestidigitation','True Strike']
Bard_1_Spells = ['Charm Person','Comprehend Languages','Cure Wounds','Detect Magic','Disguise Self','Faerie Fire','Feather Fall','Healing Word','Heroism','Hideous Laughter','Identify','Illusory Script','Longstrider','Silent Image','Sleep','Speak with Animals','Thunderwave','Unseen Servant']
Bard_2_Spells = ['Animal Messenger','Blindness/Deafness','Calm Emotions','Detect Thoughts','Enhance Ability','Enthrall','Heat Metal','Hold Person','Invisibility','Knock','Lesser Restoration','Locate Animals or Plants','Locate Object','Magic Mouth','See Invisibility','Shatter','Silence','Suggestion','Zone of Truth']
Bard_3_Spells = ['Bestow Curse','Clairvoyance','Dispel Magic','Fear','Glyph of Warding','Hypnotic Pattern','Major Image','Nondetection','Plant Growth','Sending','Speak with Dead','Speak with Plants','Stinking Cloud','Tiny Hut','Tongues']
Bard_4_Spells = ['Confusion','Dimension Door','Freedom of Movement','Greater Invisibility','Hallucinatory Terrain','Locate Creature','Polymorph']
Bard_5_Spells = ['Animate Objects','Awaken','Dominate Person','Dream','Geas','Greater Restoration','Hold Monster','Legend Lore','Mass Cure Wounds','Mislead','Modify Memory','Planar Binding','Raise Dead','Scrying','Seeming','Teleportation Circle']
Bard_6_Spells = ['Eyebite','Find the Path','Guards and Wards','Irresistible Dance','Mass Suggestion','Programmed Illusion','True Seeing']
Bard_7_Spells = ['Arcane Sword','Etherealness','Forcecage','Magnificent Mansion','Mirage Arcane','Project Image','Regenerate','Resurrection','Symbol','Teleport']
Bard_8_Spells = ['Dominate Monster','Feeblemind','Glibness','Mind Blank','Power Word Stun']
Bard_9_Spells = ['Foresight','Power Word Kill','True Polymorph']

Cleric_0_Spells = ['Guidance','Light','Mending','Resistance','Sacred Flame','Thaumaturgy']
Cleric_1_Spells = ['Bane','Bless','Command','Create or Destroy Water','Cure Wounds','Detect Evil and Good','Detect Magic','Detect Poison and Disease','Guiding Bolt','Healing Word','Inflict Wounds','Protection from Evil and Good','Purify Food and Drink','Sanctuary','Shield of Faith']
Cleric_2_Spells = ['Aid','Augury','Blindness/Deafness','Calm Emotions','Continual Flame','Enhance Ability','Find Traps','Gentle Repose','Hold Person','Lesser Restoration','Locate Object','Prayer of Healing','Protection from Poison','Silence','Spiritual Weapon','Warding Bond','Zone of Truth']
Cleric_3_Spells = ['Animate Dead','Beacon of Hope','Bestow Curse','Clairvoyance','Create Food and Water','Daylight','Dispel Magic','Glyph of Warding','Magic Circle','Mass Healing Word','Meld into Stone','Protection from Energy','Remove Curse','Revivify','Sending','Speak with Dead','Spirit Guardians','Tongues','Water Walk']
Cleric_4_Spells = ['Banishment','Control Water','Death Ward','Divination','Freedom of Movement','Locate Creature','Stone Shape']
Cleric_5_Spells = ['Commune','Contagion','Dispel Evil and Good','Flame Strike','Geas','Greater Restoration','Hallow','Insect Plague','Legend Lore','Mass Cure Wounds','Planar Binding','Raise Dead','Scrying']
Cleric_6_Spells = ['Blade Barrier','Create Undead','Find the Path','Forbiddance','Harm','Heal','Heroes Feast','Planar Ally','True Seeing','Word of Recall']
Cleric_7_Spells = ['Conjure Celestial','Divine Word','Etherealness','Fire Storm','Plane Shift','Regenerate','Resurrection','Symbol']
Cleric_8_Spells = ['Antimagic Field','Control Weather','Earthquake','Holy Aura']
Cleric_9_Spells = ['Astral Projection','Gate','Mass Heal','True Resurrection']

Druid_0_Spells = ['Guidance','Mending','Produce Flame','Resistance','Shillelagh']
Druid_1_Spells = ['Charm Person','Create or Destroy Water','Cure Wounds','Detect Magic','Detect Poison and Disease','Entangle','Faerie Fire','Fog Cloud','Healing Word','Jump','Longstrider','Purify Food and Drink','Speak with Animals','Thunderwave']
Druid_2_Spells = ['Animal Messenger','Barkskin','Darkvision','Enhance Ability','Find Traps','Flame Blade','Flaming Sphere','Gust of Wind','Heat Metal','Hold Person','Lesser Restoration','Locate Animals or Plants','Locate Object','Moonbeam','Pass without Trace','Protection from Poison','Spike Growth']
Druid_3_Spells = ['Call Lightning','Conjure Animals','Daylight','Dispel Magic','Meld into Stone','Plant Growth','Protection from Energy','Sleet Storm','Speak with Plants','Water Breathing','Water Walk','Wind Wall']
Druid_4_Spells = ['Blight','Confusion','Conjure Minor Elementals','Conjure Woodland Beings','Control Water','Dominate Beast','Freedom of Movement','Giant Insect','Hallucinatory Terrain','Ice Storm','Locate Creature','Polymorph','Stone Shape','Stoneskin','Wall of Fire']
Druid_5_Spells = ['Antilife Shell','Awaken','Commune with Nature','Conjure Elemental','Contagion','Geas','Greater Restoration','Insect Plague','Mass Cure Wounds','Planar Binding','Reincarnate','Scrying','Tree Stride','Wall of Stone']
Druid_6_Spells = ['Conjure Fey','Find the Path','Heal','Heroes Feast','Move Earth','Sunbeam','Transport via Plants','Wall of Thorns','Wind Walk']
Druid_7_Spells = ['Fire Storm','Mirage Arcane','Plane Shift','Regenerate','Reverse Gravity']
Druid_8_Spells = ['Animal Shapes','Antipathy/Sympathy','Control Weather','Earthquake','Feeblemind','Sunburst']
Druid_9_Spells = ['Foresight','Shapechange','Storm of Vengeance','True Resurrection']

Paladin_0_Spells = []
Paladin_1_Spells = ['Bless','Command','Cure Wounds','Detect Evil and Good','Detect Magic','Detect Poison and Disease','Divine Favor','Heroism','Protection from Evil and Good','Purify Food and Drink','Shield of Faith']
Paladin_2_Spells = ['Aid','Find Steed','Lesser Restoration','Locate Object','Magic Weapon','Protection from Poison','Zone of Truth']
Paladin_3_Spells = ['Create Food and Water','Daylight','Dispel Magic','Magic Circle','Remove Curse','Revivify']
Paladin_4_Spells = ['Banishment','Death Ward','Locate Creature']
Paladin_5_Spells = ['Dispel Evil and Good','Geas','Raise Dead']

Ranger_0_Spells = []
Ranger_1_Spells = ['Alarm','Cure Wounds','Detect Magic','Detect Poison and Disease','Fog Cloud','Jump','Longstrider','Speak with Animals']
Ranger_2_Spells = ['Animal Messenger','Barkskin','Darkvision','Find Traps','Lesser Restoration','Locate Animals or Plants','Locate Object','Pass without Trace','Protection from Poison','Silence','Spike Growth']
Ranger_3_Spells = ['Conjure Animals','Daylight','Nondetection','Plant Growth','Protection from Energy','Speak with Plants','Water Breathing','Water Walk','Wind Wall']
Ranger_4_Spells = ['Conjure Woodland Beings','Freedom of Movement','Locate Creature','Stoneskin']
Ranger_5_Spells = ['Commune with Nature','Tree Stride']

Sorcerer_0_Spells = ['Acid Splash','Chill Touch','Dancing Lights','Light','Mage Hand','Mending','Message','Minor Illusion','Prestidigitation','Ray of Frost','Shocking Grasp','True Strike']
Sorcerer_1_Spells = ['Burning Hands','Charm Person','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Expeditious Retreat','False Life','Feather Fall','Fog Cloud','Jump','Mage Armor','Magic Missile','Shield','Silent Image','Sleep','Thunderwave']
Sorcerer_2_Spells = ['Alter Self','Blindness/Deafness','Blur','Darkness','Darkvision','Detect Thoughts','Enhance Ability','Enlarge/Reduce','Gust of Wind','Hold Person','Invisibility','Knock','Levitate','Mirror Image','Misty Step','Scorching Ray','See Invisibility','Shatter','Spider Climb','Suggestion','Web']
Sorcerer_3_Spells = ['Blink','Clairvoyance','Daylight','Dispel Magic','Fear','Fireball','Fly','Gaseous Form','Haste','Hypnotic Pattern','Lightning Bolt','Major Image','Protection from Energy','Sleet Storm','Slow','Stinking Cloud','Tongues','Water Breathing','Water Walk']
Sorcerer_4_Spells = ['Banishment','Blight','Confusion','Dimension Door','Dominate Beast','Greater Invisibility','Ice Storm','Polymorph','Stoneskin','Wall of Fire']
Sorcerer_5_Spells = ['Animate Objects','Cloudkill','Cone of Cold','Creation','Dominate Person','Hold Monster','Insect Plague','Seeming','Telekinesis','Teleportation Circle','Wall of Stone']
Sorcerer_6_Spells = ['Chain Lightning','Circle of Death','Disintegrate','Eyebite','Globe of Invulnerability','Mass Suggestion','Move Earth','Sunbeam','True Seeing']
Sorcerer_7_Spells = ['Delayed Blast Fireball','Etherealness','Finger of Death','Fire Storm','Plane Shift','Prismatic Spray','Reverse Gravity','Teleport']
Sorcerer_8_Spells = ['Dominate Monster','Earthquake','Incendiary Cloud','Power Word Stun','Sunburst']
Sorcerer_9_Spells = ['Gate','Meteor Swarm','Power Word Kill','Time Stop','Wish','Warlock Spells']

Warlock_0_Spells = ['Mage Hand','Minor Illusion','Prestidigitation','True Strike']
Warlock_1_Spells = ['Charm Person','Comprehend Languages','Expeditious Retreat','Illusory Script','Protection from Evil and Good','Unseen Servant']
Warlock_2_Spells = ['Darkness','Enthrall','Hold Person','Invisibility','Mirror Image','Misty Step','Ray of Enfeeblement','Shatter','Spider Climb','Suggestion']
Warlock_3_Spells = ['Dispel Magic','Fear','Fly','Gaseous Form','Hypnotic Pattern','Magic Circle','Major Image','Remove Curse','Tongues','Vampiric Touch']
Warlock_4_Spells = ['Banishment','Blight','Dimension Door','Hallucinatory Terrain']
Warlock_5_Spells = ['Contact Other Plane','Dream','Hold Monster','Scrying']
Warlock_6_Spells = ['Circle of Death','Conjure Fey','Create Undead','Eyebite','Flesh to Stone','Mass Suggestion','True Seeing']
Warlock_7_Spells = ['Etherealness','Finger of Death','Forcecage','Plane Shift']
Warlock_8_Spells = ['Demiplane','Dominate Monster','Feeblemind','Glibness','Power Word Stun']
Warlock_9_Spells = ['Astral Projection','Foresight','Imprisonment','Power Word Kill','True Polymorph']

Wizard_0_Spells = ['Acid Splash','Chill Touch','Dancing Lights','Light','Mage Hand','Mending','Message','Minor Illusion','Prestidigitation','Ray of Frost','Shocking Grasp','True Strike']
Wizard_1_Spells = ['Alarm','Burning Hands','Charm Person','Color Spray','Comprehend Languages','Detect Magic','Disguise Self','Expeditious Retreat','False Life','Feather Fall','Floating Disk','Fog Cloud','Grease','Hideous Laughter','Identify','Illusory Script','Jump','Longstrider','Mage Armor','Magic Missile','Protection from Evil and Good','Shield','Silent Image','Sleep','Thunderwave','Unseen Servant']
Wizard_2_Spells = ['Acid Arrow','Alter Self','Arcane Lock','Arcanists Magic Aura','Blindness/Deafness','Blur','Continual Flame','Darkness','Darkvision','Detect Thoughts','Enlarge/Reduce','Flaming Sphere','Gentle Repose','Gust of Wind','Hold Person','Invisibility','Knock','Levitate','Locate Object','Magic Mouth','Magic Weapon','Mirror Image','Misty Step','Ray of Enfeeblement','Rope Trick','Scorching Ray','See Invisibility','Shatter','Spider Climb','Suggestion','Web']
Wizard_3_Spells = ['Animate Dead','Bestow Curse','Blink','Clairvoyance','Dispel Magic','Fear','Fireball','Fly','Gaseous Form','Glyph of Warding','Haste','Hypnotic Pattern','Lightning Bolt','Magic Circle','Major Image','Nondetection','Phantom Steed','Protection from Energy','Remove Curse','Sending','Sleet Storm','Slow','Stinking Cloud','Tiny Hut','Tongues','Vampiric Touch','Water Breathing']
Wizard_4_Spells = ['Arcane Eye','Banishment','Black Tentacles','Blight','Confusion','Conjure Minor Elementals','Control Water','Dimension Door','Fabricate','Faithful Hound','Fire Shield','Greater Invisibility','Hallucinatory Terrain','Ice Storm','Locate Creature','Phantasmal Killer','Polymorph','Private Sanctum','Resilient Sphere','Secret Chest','Stone Shape','Stoneskin','Wall of Fire']
Wizard_5_Spells = ['Animate Objects','Arcane Hand','Cloudkill','Cone of Cold','Conjure Elemental','Contact Other Plane','Creation','Dominate Person','Dream','Geas','Hold Monster','Legend Lore','Mislead','Modify Memory','Passwall','Planar Binding','Scrying','Seeming','Telekinesis','Telepathic Bond','Teleportation Circle','Wall of Force','Wall of Stone']
Wizard_6_Spells = ['Chain Lightning','Circle of Death','Contingency','Create Undead','Disintegrate','Eyebite','Flesh to Stone','Freezing Sphere','Globe of Invulnerability','Guards and Wards','Instant Summons','Irresistible Dance','Magic Jar','Mass Suggestion','Move Earth','Programmed Illusion','Sunbeam','True Seeing','Wall of Ice']
Wizard_7_Spells = ['Arcane Sword','Delayed Blast Fireball','Etherealness','Finger of Death','Forcecage','Magnificent Mansion','Mirage Arcane','Plane Shift','Prismatic Spray','Project Image','Reverse Gravity','Sequester','Simulacrum','Symbol','Teleport']
Wizard_8_Spells = ['Antimagic Field','Antipathy/Sympathy','Clone','Control Weather','Demiplane','Dominate Monster','Feeblemind','Incendiary Cloud','Maze','Mind Blank','Power Word Stun','Sunburst']
Wizard_9_Spells = ['Astral Projection','Foresight','Gate','Imprisonment','Meteor Swarm','Power Word Kill','Prismatic Wall','Shapechange','Time Stop','True Polymorph','Weird','Wish']

SRD_5_Monsters = ["Adult Red Dragon","Air Elemental","Allosaurus","Animated Armor","Ankheg",
                  "Ankylosaurus","Ape","Awakened Shrub","Awakened Tree","Axe Beak ","Baboon",
                  "Badger","Banshee","Basilisk","Bat","Black Bear","Blink Dog","Boar","Blood Hawk",
                  "Brown Bear","Bugbear","Camel","Cat","Centaur","Chimera","Cockatrice ","Crab",
                  "Crocodile","Constrictor Snake","Cyclops","Death Dog","Deer","Dire Wolf",
                  "Doppelganger","Draft Horse","Earth Elemental","Elephant","Elk","Fire Elemental",
                  "Fire Giant","Flameskull","Flesh Golem","Flying Snake","Flying Sword","Frog",
                  "Frost Giant","Gargoyle","Ghost","Ghoul","Giant Ape","Giant Badger","Giant Bat",
                  "Giant Boar","Giant Centipede","Giant Constrictor Snake","Giant Crab",
                  "Giant Crocodile","Giant Eagle","Giant Elk","Giant Fire Beetle","Giant Frog",
                  "Giant Goat","Giant Hyena","Giant Lizard","Giant Octopus","Giant Owl",
                  "Giant Poisonous Snake","Giant Rat","Giant Scorpion","Giant Sea Horse",
                  "Giant Shark","Giant Spider","Giant Toad","Giant Vulture","Giant Wasp",
                  "Giant Weasel","Giant Wolf Spider","Gnoll","Goat","Goblin","Grick","Griffon",
                  "Harpy","Hawk","Hell Hound","Hill Giant","Hippogriff","Hobgoblin","Hunter Shark",
                  "Hydra","Hyena","Jackal","Killer Whale","Kobold","Lion","Lizard","Lizardfolk",
                  "Mammoth","Manticore","Mastiff","Medusa","Merfolk","Minotaur","Mule","Mummy",
                  "Nothic","Ochre Jelly","Octopus","Ogre","Orc","Owl","Owlbear","Panther","Pegasus",
                  "Phase Spider","Plesiosaurus","Poisonous Snake","Polar Bear","Pony","Pteranodon",
                  "Quipper","Rat","Raven","Reef Shark","Rhinoceros","Riding Horse",
                  "Saber-Toothed Tiger","Satyr","Scorpion","Sea Horse","Skeleton","Spectator",
                  "Spider","Stirge","Stone Golem","Swarm of Bats","Swarm of Insects",
                  "Swarm of Poisonous Snakes","Swarm of Quippers","Swarm of Rats","Swarm of Ravens",
                  "Tiger","Triceratops","Troll","Twig blight","Tyrannosaurus Rex","Vulture",
                  "Warhorse","Water Elemental","Weasel","Werewolf","Wight","Winter Wolf","Wolf",
                  "Worg","Wyvern","Yeti","Young Green Dragon","Zombie"]

Classes5E = {0:'Barbarian', 1:'Bard', 2:'Cleric', 3:'Druid', 4:'Fighter', 5:'Monk', 6:'Paladin', 7:'Ranger', 8:'Rogue', 9:'Sorcerer', 10:'Warlock', 11:'Wizard'}
Races5E = {0:'Human', 1:'Halfling', 2:'Elf', 3:'Half Orc', 4:'Half Elf', 5:'Gnome', 6:'Dragonborn', 7:'Orc', 8:'Goblin', 9:'Other'}
Sizes5E = {0:'Tiny', 1:'Small', 2:'Medium', 3:'Large', 4:'Huge', 5:'Gargantuan'}
MonsterTypes5E = {0:'Aberration', 1:'Beast', 2:'Celestial', 3:'Construct', 4:'Dragon', 5:'Elemental', 6:'Fey', 7:'Fiend', 8:'Giant', 9:'Humanoid', 10:'Monstrosity', 11:'Ooze', 12:'Plant', 13:'Undead'}

class NPC_Record():
  def __init__(self):
    self.Name = 'Name'
    self.Gender = 'random'  #male, female, random
    self.Alignment = 'Any'  #LG, LN, LE, etc.  Also, ANY, ANY Good, Any Evil, Any Neutral
    self.LawChaosAxis = 'Lawful'
    self.GoodEvilAxis = 'Evil'
    self.ClassOne = 'Any'
    self.LevelOne = 1
    self.ClassTwo = 'None'
    self.LevelTwo = 0
    self.ClassThree = 'None'
    self.LevelThree = 0
    self.race = None         #NPC_Races class
    self.height_ft = 99
    self.height_in = 13 
    self.weight = 999
    self.STR = 3
    self.INT = 3
    self.CON = 3
    self.WIS = 3
    self.DEX = 3
    self.CHA = 3
    self.Languages = []   #list of languages for the NPC based on race/INT bonus
    self.CR = 0
    self.size = 'M'
    self.HD = 'HD'
    self.HP = 0
    self.init = 0
    self.speed = 30
    self.AttackMelee = '+99/+99/+99'
    self.AttackRanged = '+99/+99'
    self.AC = 99
    self.FORT = 0
    self.WILL = 0
    self.REF = 0
    self.BAB = 0
    self.special = []  #Special class attributes
    self.skills = []
    self.ranks = []
    self.CCskills = [] #Cross class skills
    self.CCranks = []  #Cross class ranks
    self.Feats = []    #list of feats
    self.spells = None   #list of spells available
    self.spells_memorized = None  #text of spells memorized for use
    self.MagicType = None #type of magic #one of Arcane, Divine, Bardic, Ranger, Druid, Paladin
    self.spell_0 = 0  #the following detail the 
    self.spell_1 = 0  #number of spells available
    self.spell_2 = 0  
    self.spell_3 = 0
    self.spell_4 = 0
    self.spell_5 = 0
    self.spell_6 = 0
    self.spell_7 = 0
    self.spell_8 = 0
    self.spell_9 = 0

class NPC_Name_Record():
  def __init__(self):
    self.DwarfFemaleSuffix = []
    self.DwarfMaleSuffix = []
    self.DwarfPrefix = []
    self.FemaleElfMidfix = []
    self.FemaleElfPrefix = []
    self.FemaleElfSuffix = []
    self.FemaleGnomeNames = []
    self.FemaleHalflingNames = []
    self.FemaleHumanNames = []
    self.MaleElfMidfix = []
    self.MaleElfPrefix = []
    self.MaleElfSuffix = []
    self.MaleGnomeNames = []
    self.MaleHalflingNames = []
    self.MaleHumanNames = []
    self.MonsterMidfix = []
    self.MonsterPrefix = []
    self.MonsterSuffix = []

class NPC_SkillItem():
  def __init__(self):
    self.Skill = None
    self.Bonus = 0
    return

class NPC_Skills():
  #the ability bonus is entered.  If None, then NPC is untrained in that skill
  def __init__(self):
    self.Appraise = None
    self.Balance = None
    self.Bluff = None
    self.Climb = None
    self.Concentration = None
    self.Craft = None
    self.DecipherScript = None
    self.Diplomacy = None
    self.DisableDevice = None
    self.Disguise = None
    self.EscapeArtist = None
    self.Forgery = None
    self.GatherInformation = None
    self.HandleAnimal = None
    self.Heal = None
    self.Intimidate = None
    self.Jump = None
    self.Knowledge = None
    self.Listen = None
    self.MoveSilently = None
    self.OpenLock = None
    self.Perform = None
    self.Profession = None
    self.Ride = None
    self.Search = None
    self.SenseMotive = None
    self.SleightOfHand = None
    self.SpeakLanguage = None
    self.Spellcraft = None
    self.Spot = None
    self.Survival = None
    self.Swim = None
    self.Tumble = None
    self.UseMagicDevice = None
    self.UseRope = None
    return

class NPC_Feats_Record():
  def __init__(self):
    self.subset = None # 1=General, 2=Melee, 3=Ranged, 4=Magic
    self.featlist = []
    return

class NPC_Spell_Record():
  """Used for PF/d20 NPC's """
  def __init__(self):
    self.name = None
    self.school = None
    self.descriptor = None
    self.level = []   #list of class/levels, ie  ['Cleric 6', 'Sorcerer/Wizard 5']
    self.components = None
    self.cast_time = None
    self.spell_range = None
    self.target = None
    self.duration = None
    self.saving_throw = None
    self.spell_resistance = None
    self.text = None
    self.effect = None
    return
#------------------------------------------------------------------------
class TrapInfo:
  """This is a pickled record"""
  def __init__(self):
    self.index = 0            #master index when read from disk
    self.displayIndex = 0     #changed as the trap display list is modified
    self.SRD_Trap = False     #set to True if this is a trap found in the SRD
    self.show = True          #used to filter the TrapInfo item
    self.icon = None          #wxImage of the trap icon
    self.desc = 'None'        #description of the trap, text string
    self.CR = 1               #challenge rating
    self.TrapType = 'None'    #magic or mechanical
    self.trigger = 'None'     #'Location', 'Proximity', 'Sound', 'Visual', 'Touch', 'Timed', 'Spell'
    self.reset = 'None'
    self.bypass = 'None'      # Enter bypass method and search DC (if any)
    self.attackbonus = 20     #attack bonus
    self.attacktype = 'None'  #melee, ranged, pit, other, etc.
    self.damage = 'None'      #description of the attack, ie, ranged 1d6 19-20(x2)
    self.damageDice = ''      #dice used to calculate damage, ie, 2d10+2
    self.searchDC = 20
    self.disableDC = 20
    self.saveDC = 20
    self.savetype = 'None'    #list of saves
    self.saveamount = 'None'  #save for half or avoid
    self.GPcost = 0
    self.XPcost = 0
    self.optional = "None"   #other optional trap features
    self.other = "None"      #other user defined text
    return

class NPC_Skills_Record():
  def __init__(self):
    self.name = None
    self.skills = []  #class skills to this class.  all others are cross-class
    self.ranks = []  #how many points per skill assigned.  list of values corresponding to the skills
    self.CCskills = []
    self.CCranks = []

class NPC_Class_Info_Record():
  def __init__(self):
    self.class_name = None
    self.level = None
    self.BAB = None
    self.FORT = None
    self.WILL = None
    self.REF = None
    self.special = []
    self.psi_points = None
    self.psi_powers_known = None
    self.psi_power_level = None
    self.caster_level = None
    self.AC_bonus = 0
    self.spells_known_0 = 0
    self.spells_known_1 = 0
    self.spells_known_2 = 0
    self.spells_known_3 = 0
    self.spells_known_4 = 0
    self.spells_known_5 = 0
    self.spells_known_6 = 0
    self.spells_known_7 = 0
    self.spells_known_8 = 0
    self.spells_known_9 = 0
    self.spells_available_0 = 0
    self.spells_available_1 = 0
    self.spells_available_2 = 0
    self.spells_available_3 = 0
    self.spells_available_4 = 0
    self.spells_available_5 = 0
    self.spells_available_6 = 0
    self.spells_available_7 = 0
    self.spells_available_8 = 0
    self.spells_available_9 = 0
    self.unarmed_damage = None
    self.speed_bonus = 0
    self.flurry = None
    return

class NPC_Races:
  def __init__(self):
    self.Name = None
    self.speed = None
    self.CR = None
    self.size = None
    self.extraHD_qty = None
    self.extraHD = None
    self.PrefClass = None
    self.LawChaosAxis = None
    self.GoodEvilAxis = None
    self.Alignment = None
    self.maleBonus = None
    self.femaleBonus = None
    self.maleStatHeightFeet = None
    self.maleStatHeightInches = None
    self.maleStatHeightModDie = None
    self.maleStatHeightModDieQty = None
    self.maleStatWeight = None
    self.maleStatWeightModDie = None
    self.maleStatWeightModDieQty = None
    self.femaleStatHeightFeet = None
    self.femaleStatHeightInches = None
    self.femaleStatHeightModDie = None
    self.femaleStatHeightModDieQty = None
    self.femaleStatWeight = None
    self.femaleStatWeightModDie = None
    self.femaleStatWeightModDieQty = None
    self.languages = None
    self.bonusLanguages = None
    self.Skills = NPC_Skills()      #list of all skills
    self.SkillBonuses = []
    self.FeatBonuses = []       #plain text list
    self.STR_bonus = 0
    self.INT_bonus = 0
    self.CON_bonus = 0
    self.DEX_bonus = 0
    self.WIS_bonus = 0
    self.CHA_bonus = 0
    self.REF_bonus = 0
    self.FORT_bonus = 0
    self.WILL_bonus = 0
    self.ATT_bonus = 0
    self.AC_bonus = 0

########################################################################
class AutolevelFeature_Record():
  """This contains the information under the <autolevel> tag.  There may be more than
  one feature per <autolevel>
  """

  #----------------------------------------------------------------------
  def __init__(self):
    """Constructor"""
    self.featureName = ''
    self.level = 0
    self.features = []     # list of Class_5E_Feature items
    self.slots = None      # if the class has spellcasting, this is a text string of the slots filled, ie '3 3 1'  
    return
    
  
########################################################################

class Class_5E_Feature():
  """"""
  #----------------------------------------------------------------------
  def __init__(self):
    """Constructor"""
    self.featureName = ''
    self.featureText = []  # list of text strings
    return


########################################################################  
class Class5E_Record():
  """Holds information for classes in 5E SRD"""
  #----------------------------------------------------------------------
  def __init__(self):
    """From our classes.xml data, each class and sub-class has an entry"""
    self.ClassName = ''     # Which of the standard classes, ie, Bard, Cleric, etc.
    self.SubClass = None    # Which sub-class, ie, Path, College, School, etc.
    self.HD = 6             # Hit dice number
    self.proficiency = ''   # Full name of attribute, ie, Strength, Wisdom, etc
    self.spellAbility = ''  # Attribute name if class can cast spells
    self.features = []      # list of AutolevelFeature_Record items
    self.isCore = False     # True if this is part of the core game rules
    self.isSRD = True       # True if released under the OGL/SRD
    return
    
class Monster_Record():
  def __init__(self):
    """This is a pickled record.  Conversion necessary if additions are made"""
    self.version = None  #Which version of the monster is this 3E, PATH, 5E_OLD, USER, etc.
    self.uniqueID = 0    #Each monster has a unique identifier, used in the hover dialog lookup
    self.index = 0       #used in the wxListBox display, not unique to any monster
    self.user_defined = False
    self.show = False
    self.family = 'None'
    self.name = 'None'   #name as recorded in the monster data list
    self.customName = None  #name as defined by the user
    self.size = 'None'
    self.monster_type = 0  #An integer for 5E monsters; used for the wxChoice widget
    self.monster_subtype = 'None'
    self.descriptor = 'None'
    self.HD = 'None'
    self.init = 'None'
    self.speed = '0'
    self.special_speed_type = 0 #integer (0=none, 1=fly, 2=burrow, 3=swim, 4=climb)
    self.special_speed = '0'
    self.AC = 10
    self.BAB = 'None'
    self.grapple = 'None'
    self.attack = 'None'
    self.full_attack = 'None'
    self.actions = 'None'
    self.space = 'None'
    self.reach = 'None'
    self.SA = 'None'
    self.SQ = 'None'
    self.REF = 0
    self.WILL = 0
    self.FORT = 0
    self.saves = 'None'
    self.abilities = 'None'
    self.STR = '0'
    self.INT = '0'
    self.DEX = '0'
    self.CON = '0'
    self.WIS = '0'
    self.CHA = '0'
    self.skills = 'None'
    self.feats = 'None'
    self.epic_feats = 'None'
    self.environment = 'None'
    self.organization = 'None'
    self.CR = '0'
    self.XP = '0'
    self.treasure = 'None'
    self.alignment = 'None'
    self.HP = 0
    self.startHP = 0    #this is the original starting HP of the monster
    self.con1 = 'None'       # these are for the user defined conditions
    self.con2 = 'None'
    self.con3 = 'None'
    self.con4 = 'None'
    self.advancement = 'None'
    self.level_adjustment = 'None'
    self.stat_block = 'None'
    self.SA_text = 'None'    #used to define (Ex) (Su) qualities
    self.other_text = 'None'  #other general text, explanation of behavior, SA, SQ, etc.
    self.passive_perception = '0'
    self.SRD_Distribution = False   #allowed to be distributed under SRD/GPL
    self.BasicMonster = False
    return
  
#---------------------------------------------------------------------
class Monster5E_Record():
  def __init__(self):
    self.version = None  #Which version of the monster is this 3E, PATH, 5E, 5E_NPC
    self.uniqueID = 0    #Each monster has a unique identifier, used in the hover dialog lookup
    self.index = 0       #used in the wxListBox display, not unique to any monster
    self.user_defined = False   #set to True if it is a custom monster/npc
    self.show = False
    self.npc_class = 0      #Class of the character, integer: 0:BAR, 1:BRD, 2:CLR, 3:DRD, 4:FTR, 5:MNK, 6:PAL, 7:RGR, 8:RGE, 9:SOR, 10:WLK, 11:WIZ
    self.npc_race = 0        #Race of the NPC, integer: 0:Human, 1:Halfling, 2:Elf, 3:Half-Orc, 4:Half-Elf, 5:Gnome, 6:Dragonborn, 7:Orc, 8:Goblin, 9:Other
    self.level = 1           #integer of the level of the npc
    self.filterValue = 0     #used for filtering monsters in the monster display dialog
    self.monster_type = ''   #monster type and subtype
    self.family = ''
    self.name = ''   #name as recorded in the monster data list
    self.customName = None  #name as defined by the user    
    self.size = 2        # monster size, integer; 0=Tiny, 1=Small, 2=Medium, 3=Large, 4=Huge, 5=Gargantuan
    self.monster_type = 0    #An integer for 5E monsters; used for the wxChoice widget 0=Aberration 1=Beast 2=Celestial 3=Construct 4=Dragon 5=Elemental 6=Fey 7=Fiend 8=Giant 9=Humanoid 10=Monstrosity 11=Ooze 12=Plant 13=Undead
    self.monster_subtype = '' #Sub-type of the monster
    self.descriptor = ''
    self.HD = ''         #dice value for calculating HP
    self.init = ''
    self.speed = ''
    self.proficiency = 2   #integer value of proficiency bonus.
    self.proficiencySkills = []  #list of skills the monster/npc is proficient with
    self.AC = 10
    self.AC_Type = ''        # type of armor (natural, plate, etc)
    self.attack = ''
    self.actions = ''
    self.legendaryAction = ''
    self.space = ''
    self.reach = ''
    self.saves = ''            #show on skills tab
    self.resistances = ''      #show on skills tab
    self.vulnerable = ''       #show on skills tab
    self.immunities = ''       #show on skills tab
    self.conditionImmune = ''  #show on skills tab
    self.senses = ''           #show on skills tab
    self.languages = ''        #show on skills tab
    self.skills = ''           #show on skills tab
    self.trait = ''             #show on traits tab
    self.abilities = ''         #show on traits tab
    self.userNotes = ''          #show on notes tab
    self.STR = '0'
    self.INT = '0'
    self.DEX = '0'
    self.CON = '0'
    self.WIS = '0'
    self.CHA = '0'

    self.spells = {'Level0': [],'Level1': [],'Level2': [],'Level3': [],'Level4': [],'Level5': [],'Level6': [],'Level7': [],'Level8': [],'Level9': []}
    self.spellSlots = {'Slot0':'0','Slot1':'0', 'Slot2':'0','Slot3':'0','Slot4':'0','Slot5':'0','Slot6':'0','Slot7':'0','Slot8':'0','Slot9':'0'}
    self.spellAttackDC = 0
    self.spellSaveDC = 8
    self.CR = '0'            #show on skills tab
    self.XP = '0'
    self.treasure = ''       #show on other info tab
    self.alignment = ''
    self.HP = 0         # Hit Points remaining
    self.startHP = 0    # this is the original starting HP of the monster
    self.con1 = 'None'       # these are for the user defined conditions
    self.con2 = 'None'
    self.con3 = 'None'
    self.con4 = 'None'
    self.deathSavePass = 0   #ranges from 0-3 only
    self.deathSaveFail = 0   #ranges from 0-3 only
    self.advancement = ''
    self.level_adjustment = ''
    self.passive_perception = '0'
    self.SRD_Distribution = False   #allowed to be distributed under SRD/GPL?
    self.BasicMonster = False       #available from D&D 5th Edition basic rules? (PC/DM/other)
    self.other_text = ''      #show on other info tab
    self.bonds = ''           #show on bonds tab; NPC only
    self.flaws = ''           #show on flaws tab; NPC only 
    self.ideals = ''          #show on ideals tab; NPC only
    self.image = None         #wxImage, if user selected a custom image
    self.filename = None      #filename to the custom image; all images located in /artwork/tokens
    return
  
  def TypeInfo(self):
    """Returns a string showing the monster size/type, or npc race/class combo"""
    if (self.version == '5E'):  #this is a monster
      try:
        size = Sizes5E[self.size]
      except:
        size = ""
      try:
        monsterType = MonsterTypes5E[self.monster_type]
      except:
        monsterType = ""
      return (size + " " + monsterType)
    elif (self.version == '5E_NPC'):
      try:
        classNPC = Classes5E[self.npc_class]
      except:
        classNPC = ""
      try:
        raceNPC = Races5E[self.npc_race]
      except:
        raceNPC = ""
      return (raceNPC + " " + classNPC)
    else:
      return ""
    
class Spell5E_Record():
  def __init__(self):
    self.MasterIndex = None    # unique spell identifier.  User defined spells start at index 100000.  WotC sourced spells start at 0
    self.Name = ""           # Name of spell
    self.School = ""         # School name: "Abjuration" "Conjuration" "Divination" "Enchantment" "Evocation" "Illusion" "Necromancy" "Transmutation"
    self.CasterClass = []      # Available to class: "Bard" "Cleric" "Druid" "Paladin" "Ranger" "Sorcerer" "Warlock" "Wizard"
    self.Level = 0          # integer, 0 = cantrip
    self.VerbalComponent = False    # Either true/false
    self.SomaticComponent = False   # Either true/false
    self.FocusComponent = False     # Either true/false
    self.MaterialComponent = False  # Either true/false
    self.CastTime = "None"           # text string
    self.SpellRange = "None"         # text string
    self.Target = "None"
    self.Duration = "None"           # text string
    self.Concentration = False       # set to True if concentration required for this spell
    self.Save = "None"      
    self.BaseDamage = "None"         # dice string
    self.DamageType = "None"       # choice: "Acid" "Bludgeoning" "Cold" "Fire" "Force" "Lightning" "Necrotic" "Piercing" "Poison" "Psychic" "Radiant" "Slashing" "Thunder"
    self.Description = ""          # text string
    self.Ritual = False            # either true/false
    self.BasicSpell = False        # set to True if available in free rules
    self.SourceMaterial = "None"     # text string, what is the book reference
    self.SourceCode = ""           # Set to PHB, EE, APOC, USER depending on supplemental source
    self.UserDefined = False       # set to true if this is a user modified spell.
    self.show = True               # flag for displaying the spell in a listbox
    self.selected = False          # flag for whether it is selected
    self.filterValue = 15          # used to determine filtering.  Level=1, Class=2, School=4, Basic=8
    self.deleted = False           # set to true if the spell has been deleted.  Not removed from list, so as to preserve index values
    return

def GetAbilityScoreBonus(score):
  if (score == 1):
    return -5
  elif (score <= 3):
    return -4
  elif (score <= 5):
    return -3
  elif (score <= 7):
      return -2
  elif (score <= 9):
      return -1
  elif (score <= 11):
      return 0
  elif (score <= 13):
      return 1
  elif (score <= 15):
      return 2
  elif (score <= 17):
      return 3
  elif (score <= 19):
      return 4
  elif (score <= 21):
      return 5
  elif (score <= 23):
      return 6
  elif (score <= 25):
      return 7
  elif (score <= 27):
      return 8
  elif (score <= 29):
      return 9
  elif (score == 30):
      return 10
  else:
    return 0

def GetMonsterProficiencyBonus(challengeRating):
  if ((challengeRating == '5') or (challengeRating == '6') or (challengeRating == '7') or (challengeRating == '8')):
    bonus = 3
  elif ((challengeRating == '9') or (challengeRating == '10') or (challengeRating == '11') or (challengeRating == '12')):
    bonus = 4
  elif ((challengeRating == '13') or (challengeRating == '14') or (challengeRating == '15') or (challengeRating == '16')):
    bonus = 5
  elif ((challengeRating == '17') or (challengeRating == '18') or (challengeRating == '19') or (challengeRating == '20')):
    bonus = 6
  elif ((challengeRating == '21') or (challengeRating == '22') or (challengeRating == '23') or (challengeRating == '24')):
    bonus = 7
  elif ((challengeRating == '25') or (challengeRating == '26') or (challengeRating == '27') or (challengeRating == '28')):
    bonus = 8
  elif ((challengeRating == '29') or (challengeRating == '30')):
    bonus = 9
  else:
    bonus = 2
  return bonus

def UpdateXPfromCR(CRvalue):
  """CRvalue is a text loaded from the xml file"""
  XPvalue = 0
  if (CRvalue == '0'):
    XPvalue = 10
  elif (CRvalue == '1/8'):
    XPvalue = 25
  elif (CRvalue == '1/4'):
    XPvalue = 50
  elif (CRvalue == '1/2'):
    XPvalue = 100
  elif (CRvalue == '1'):
    XPvalue = 200
  elif (CRvalue == '2'):
    XPvalue = 450
  elif (CRvalue == '3'):
    XPvalue = 700
  elif (CRvalue == '4'):
    XPvalue = 1100
  elif (CRvalue == '5'):
    XPvalue = 1800
  elif (CRvalue == '6'):
    XPvalue = 2300
  elif (CRvalue == '7'):
    XPvalue = 2900
  elif (CRvalue == '8'):
    XPvalue = 3900
  elif (CRvalue == '9'):
    XPvalue = 5000
  elif (CRvalue == '10'):
    XPvalue = 5900
  elif (CRvalue == '11'):
    XPvalue = 7200
  elif (CRvalue == '12'):
    XPvalue = 8400
  elif (CRvalue == '13'):
    XPvalue = 10000
  elif (CRvalue == '14'):
    XPvalue = 11500
  elif (CRvalue == '15'):
    XPvalue = 13000
  elif (CRvalue == '16'):
    XPvalue = 15000
  elif (CRvalue == '17'):
    XPvalue = 18000
  elif (CRvalue == '18'):
    XPvalue = 20000
  elif (CRvalue == '19'):
    XPvalue = 22000
  elif (CRvalue == '20'):
    XPvalue = 25000
  elif (CRvalue == '21'):
    XPvalue = 33000
  elif (CRvalue == '22'):
    XPvalue = 41000
  elif (CRvalue == '23'):
    XPvalue = 50000
  elif (CRvalue == '24'):
    XPvalue = 62000
  elif (CRvalue == '25'):
    XPvalue = 75000
  elif (CRvalue == '26'):
    XPvalue = 90000
  elif (CRvalue == '27'):
    XPvalue = 105000
  elif (CRvalue == '28'):
    XPvalue = 120000
  elif (CRvalue == '29'):
    XPvalue = 135000
  elif (CRvalue == '30'):
    XPvalue = 155000
  return str(XPvalue)

def ReadDnD5_Files(SpellsGauge, MonstersGauge, NPC_Gauge, TrapsGauge):
  result = ""
  
  #load class data
  if (os.access(os.path.join(gv.srd_directory,'5E','classes.xml'), os.F_OK)):
    xmlfile = os.path.join(gv.srd_directory,'5E', 'classes.xml')
    gv.Class5E = ReadClass_5E_XML(xmlfile)
  else:
    result += ' LoadError:Classes '  
  
  if (os.access(os.path.join(gv.srd_directory,"5E","spells.xml"), os.F_OK)):
    SpellsGauge.SetValue(15)
    #read the xml file of the 5E spells
    xmlfile = os.path.join(gv.srd_directory,"5E","spells.xml")
    gv.Spells5E = ReadSpells5E_XML(xmlfile)
    for i in gv.Spells5E:
      i.SourceCode = "PHB"
  else:
    result += " LoadError:Spells "
  SpellsGauge.SetValue(50)
  
  if (os.access(os.path.join(gv.srd_directory,"5E","Elemental Evil Spells 1.0.xml"), os.F_OK)):
    xmlfile = os.path.join(gv.srd_directory,"5E","Elemental Evil Spells 1.0.xml")
    spells = ReadSpells5E_XML(xmlfile, len(gv.Spells5E))
    for i in spells:
      i.SourceMaterial = "Elemental Evil Players Companion"
      i.SourceCode = 'EE'
    gv.Spells5E.extend(spells)
  else:
    result += " LoadError:ElementalEvil Spells "
  SpellsGauge.SetValue(85)
  
  if (os.access(os.path.join(gv.srd_directory,"5E","UserSpells.xml"), os.F_OK)):
    xmlfile = os.path.join(gv.srd_directory,"5E","UserSpells.xml")
    spells = ReadSpells5E_XML(xmlfile, gv.UserSpell5E_NextIndex)
    for i in spells:
      i.SourceCode = 'USER'
      i.SourceMaterial = 'User Defined Spell'
      gv.UserSpell5E_NextIndex += 1
    gv.Spells5E.extend(spells)
  SpellsGauge.SetValue(100)
    
  if (os.access(os.path.join(gv.srd_directory,"5E","CoreMonsters.xml"), os.F_OK)):
    MonstersGauge.SetValue(15)
    xmlfile = os.path.join(gv.srd_directory,"5E","CoreMonsters.xml")
    ReadMonsters5E_XML(xmlfile)
    MonstersGauge.SetValue(75)
  else:
    result += " LoadError:CoreMonsters "
  
  
  if (os.access(os.path.join(gv.srd_directory,"5E","UserMonsters.xml"), os.F_OK)):
    xmlfile = os.path.join(gv.srd_directory,"5E","UserMonsters.xml")
    ReadMonsters5E_XML(xmlfile)
    MonstersGauge.SetValue(85)
  else:
    result += " LoadError:UserMonsters "
  MonstersGauge.SetValue(100)

  if (os.access(os.path.join(gv.srd_directory,"5E","npc.xml"), os.F_OK)):
    NPC_Gauge.SetValue(15)
    xmlfile = os.path.join(gv.srd_directory,"5E","npc.xml")
    gv.NPC_5E = ReadNPC_5E_XML(xmlfile, 0)
  else:
    result += " LoadError:NPC "
  NPC_Gauge.SetValue(100)
  
  if (os.access(os.path.join(gv.srd_directory,"d20","traps.obj"), os.F_OK)):
    TrapsGauge.SetValue(15)
    #try loading the traps file from a pickle object (v8.5 and beyond)
    datafile = open(os.path.join(gv.srd_directory,"d20","traps.obj"), 'r')
    gv.TrapList = pickle.load(datafile)
  else:
    #load the older v8.4 legacy file
    ReadTrapsFile(os.path.join(gv.srd_directory,"d20","traps.txt"), TrapsGauge)
    if (os.access(os.path.join(gv.srd_directory,"d20","user_traps.txt"), os.F_OK)):
      logging.info("SRD Files: Load user traps file")
      success = self.ReadTrapsFile(os.path.join(gv.srd_directory,"d20","user_traps.txt"), TrapsGauge)
      if (not success):
        return False
   
    readfile = True
    #result += " LoadError on pickled object:Traps "
  TrapsGauge.SetValue(100)



  if (result == ''):
    time.sleep(1)
    return "Files Loaded"
  else:
    return result
  
def ReadClass_5E_XML(xmlfile):
  """ Read an xml data file with class information.  xmlfile is a valid filename """
  DOMTree = xml.dom.minidom.parse(xmlfile)
  
  startIndex=0
  classList = DOMTree.documentElement
  ClassData = classList.getElementsByTagName('class')
  
  for classItem in ClassData:
    newRecord = Class5E_Record()
    
    xmldata = classItem.getElementsByTagName('name')
    newRecord.ClassName = xmldata[0].childNodes[0].data
    
    xmldata = classItem.getElementsByTagName('hd')
    newRecord.HD = int(xmldata[0].childNodes[0].data)
    
    xmldata = classItem.getElementsByTagName('proficiency')
    if (xmldata[0].childNodes == []):
      newRecord.proficiency = None
    else:
      newRecord.proficiency = xmldata[0].childNodes[0].data
    
    xmldata = classItem.getElementsByTagName('spellAbility')
    if (xmldata[0].childNodes == []):  #no data, not a spellcaster
      newRecord.spellAbility = None
    else:
      newRecord.spellAbility = xmldata[0].childNodes[0].data
    
    xmldata = classItem.getElementsByTagName('autolevel')
    
    for autolevel in xmldata:
      item = AutolevelFeature_Record()
      item.level = autolevel.getAttribute('level')
      featureData = autolevel.getElementsByTagName('feature')
      
      spellData = autolevel.getElementsByTagName('slots')
      if (spellData == [] or spellData[0].childNodes == []):  #no data
        item.slots = None
      else:
        item.slots = spellData[0].childNodes[0].data
      for featureItem in featureData:
        classFeature = Class_5E_Feature()
        classFeature.featureName = featureItem.getElementsByTagName('name')[0].childNodes[0].data
        textData = featureItem.getElementsByTagName('text')
        for textItem in textData:
          classFeature.featureText.append(textItem.childNodes[0].data)
        item.features.append(classFeature)
      newRecord.features.append(item)
    gv.ClassData_5E.append(newRecord)
  return

def ReadD20_Files(TrapsGauge, MonsterGauge, SpellsGauge, FeatsGauge, ClassSkillsGauge,
                  ClassTableGauge, NamesGauge, RacesGauge, RacialBonusesGauge):

  if (os.access(os.path.join(gv.srd_directory,"d20","traps.obj"), os.F_OK)):
    TrapsGauge.SetValue(0)
    #try loading the traps file from a pickle object (v8.5 and beyond)
    datafile = open(os.path.join(gv.srd_directory,"d20","traps.obj"), 'r')
    if (False):  #read the pickled file and re-save due to adding a field to TrapInfo class
      tempList = []
      for item in gv.TrapList:
        newItem = TrapInfo()
        newItem.index = item.index
        newItem.displayIndex = None
        newItem.SRD_Trap = item.SRD_Trap
        newItem.show = item.show
        newItem.icon = item.icon
        newItem.desc = item.desc.lstrip(" ")
        newItem.CR = item.CR
        newItem.TrapType = item.TrapType
        newItem.trigger = item.trigger
        newItem.reset = item.reset
        newItem.bypass = item.bypass
        newItem.attackbonus = item.attackbonus
        newItem.attacktype = item.attacktype
        newItem.damage = item.damage
        newItem.damageDice = item.damageDice
        newItem.searchDC = item.searchDC
        newItem.disableDC = item.disableDC
        newItem.saveDC = item.saveDC
        newItem.savetype = item.savetype
        newItem.saveamount = item.saveamount
        newItem.GPcost = item.XPcost
        newItem.optional = item.optional
        newItem.other = item.other
        #filter out duplicated names
        skipTrap = False
        for trap in gv.TrapList:
          if (newItem.desc == trap.desc):
            skipTrap = True
        if (not skipTrap):
          tempList.append(newItem)
      datafile.close()
      datafile = open(os.path.join(gv.srd_directory,"d20","traps.obj"), 'w')
      gv.TrapList = tempList
      pickle.dump(gv.TrapList, datafile)
      datafile.close()
    else:
      gv.TrapList = pickle.load(datafile)
    TrapsGauge.SetValue(100)
    datafile.close()
  else:
    #load the older v8.4 legacy file
    ReadTrapsFile(os.path.join(gv.srd_directory,"d20","traps.txt"), TrapsGauge)
    if (os.access(os.path.join(gv.srd_directory,"d20","user_traps.txt"), os.F_OK)):
      logging.info("SRD Files: Load user traps file")
      success = ReadTrapsFile(os.path.join(gv.srd_directory,"d20","user_traps.txt"), TrapsGauge)
      if (not success):
        return False
   
    readfile = True

  if (os.access(os.path.join(gv.srd_directory,"d20","monsters.obj"), os.F_OK)):
    #try loading the monsters file from a pickle object (v8.5 and beyond)
    MonsterGauge.Pulse()
    datafile = open(os.path.join(gv.srd_directory,"d20","monsters.obj"), 'r')

    if (False): # Conversion information for pickling after adding a field to the Monster_Record
      tempList = []
      mstr = Monster_Record()
      for mstr in gv.MonsterList:
        NewMonster = Monster_Record()
        NewMonster.version = mstr.version           #Which version of the monster is this 3E, PATH, 5E, etc.
        NewMonster.uniqueID = mstr.uniqueID    #Each monster has a unique identifier, used in the hover dialog lookup
        NewMonster.index = mstr.index
        NewMonster.user_defined = mstr.user_defined
        NewMonster.show = mstr.show
        NewMonster.family = mstr.family
        NewMonster.name = mstr.name
        NewMonster.size = mstr.size
        NewMonster.monster_type = mstr.monster_type
        NewMonster.descriptor = mstr.descriptor
        NewMonster.HD = mstr.HD
        NewMonster.init = mstr.init
        NewMonster.speed = mstr.speed
        NewMonster.special_speed_type = mstr.special_speed_type
        NewMonster.special_speed = mstr.special_speed
        NewMonster.AC = mstr.AC
        NewMonster.BAB = mstr.BAB
        NewMonster.grapple = mstr.grapple
        NewMonster.attack = mstr.attack
        NewMonster.full_attack = mstr.full_attack
        NewMonster.actions = mstr.actions
        NewMonster.space = mstr.space
        NewMonster.reach = mstr.reach
        NewMonster.SA = mstr.SA
        NewMonster.SQ = mstr.SQ
        NewMonster.REF = mstr.REF
        NewMonster.WILL = mstr.WILL
        NewMonster.FORT = mstr.FORT
        NewMonster.saves = mstr.saves
        NewMonster.abilities = mstr.abilities
        NewMonster.STR = mstr.STR
        NewMonster.INT = mstr.INT
        NewMonster.DEX = mstr.DEX
        NewMonster.CON = mstr.CON
        NewMonster.WIS = mstr.WIS
        NewMonster.CHA = mstr.CHA
        NewMonster.skills = mstr.skills
        NewMonster.feats = mstr.feats
        NewMonster.epic_feats = mstr.epic_feats
        NewMonster.environment = mstr.environment
        NewMonster.organization = mstr.organization
        NewMonster.CR = mstr.CR 
        NewMonster.XP = mstr.XP
        NewMonster.treasure = mstr.treasure
        NewMonster.alignment = mstr.alignment
        NewMonster.HP = mstr.HP
        NewMonster.startHP = mstr.HP
        NewMonster.con1 = 'None'       # these are for the user defined conditions
        NewMonster.con2 = 'None'
        NewMonster.con3 = 'None'
        NewMonster.con4 = 'None'
        NewMonster.advancement = mstr.advancement
        NewMonster.level_adjustment = mstr.level_adjustment
        NewMonster.stat_block = mstr.stat_block
        NewMonster.SA_text = mstr.SA_text    #used to define (Ex) (Su) qualities
        NewMonster.other_text = mstr.other_text
        NewMonster.passive_perception = mstr.passive_perception
        if (mstr.version == '5E') or (mstr.version == '5E_NPC'):
          NewMonster.SRD_Distribution = False
        else:
          NewMonster.SRD_Distribution = True
        tempList.append(NewMonster)
        gv.SaveSRD_Monsters = True
      gv.MonsterList = tempList
      datafile = open(os.path.join(gv.srd_directory,"d20","monsters.obj"), 'w')
      pickle.dump(gv.MonsterList, datafile)
      datafile.close()
    else:
      gv.MonsterList = pickle.load(datafile)
      for m in gv.MonsterList:
        if (not m.version):  #monster pre 5E
          if (m.HP <= 0):
            m.HP = 1
        elif (m.version == '5E'):
          m.version = '5E_OLD'  #change to this value since 9.1 now imports the entire monster manual
        elif (m.version == '5E_NPC'):
          pass

    if (gv.PymapperUser):
      gv.NextMonsterIndex = len(gv.MonsterList)
    else:
      gv.NextMonsterIndex = len(gv.MonsterList) + 100000
      
    MonsterGauge.SetValue(100)
    datafile.close()
  else:
    filename = os.path.join(gv.srd_directory,"d20","monsters.xml")
    filesize = os.path.getsize(filename)
    try:
      Monsters_File = open(filename, "r")
    except IOError:
      return False

    readfile = True
    while(readfile):  #Monsters file
      line = Monsters_File.readline()
      line = line.rstrip('\n\r')
      line = line.strip()
      if (line == '<monster>'):
        monster = Monster_Record()
      elif (line == '</monster>'):
        position = int(100 * float(Monsters_File.tell())/float(filesize))
        MonsterGauge.SetValue(position)
        gv.MonsterList.append(monster)
      elif (line == '</monsters>'):
        Monsters_File.close()
        MonsterGauge.SetValue(100)
        readfile = False
      else:
        data = self.StripXMLtags(line)
        line += '\n'

        if (data[0] == 'family'):
          monster.family = str(data[1])
        elif (data[0] == 'version'):
          monster.version = str(data[1])
        elif (data[0] == 'name'):
          monster.name = str(data[1])
        elif (data[0] == 'size'):
          monster.size = str(data[1])
        elif (data[0] == 'type'):
          add_item = operator.contains(gv.MonsterTypes, str(data[1]))
          if (add_item == False):
            gv.MonsterTypes.append(str(data[1]))
          monster.monster_type = str(data[1])
        elif (data[0] == 'hit_dice'):
          monster.HD = str(data[1])
        elif (data[0] == 'descriptor'):
          monster.descriptor = str(data[1])
        elif (data[0] == 'initiative'):
          data2 = data[1].split()
          monster.init = int(data2[0])
        elif (data[0] == 'speed'):
          monster.speed = str(data[1])
        elif (data[0] == 'armor_class'):
          monster.AC = str(data[1])
        elif (data[0] == 'base_attack'):
          monster.BAB = str(data[1])
        elif (data[0] == 'grapple'):
          monster.grapple = str(data[1])
        elif (data[0] == 'attack'):
          monster.attack = str(data[1])
        elif (data[0] == 'full_attack'):
          monster.full_attack = str(data[1])
        elif (data[0] == 'space'):
          monster.space = str(data[1])
        elif (data[0] == 'reach'):
          monster.reach = str(data[1])
        elif (data[0] == 'special_speed'):
          monster.special_speed = str(data[1])
        elif (data[0] == 'special_attacks'):
          monster.SA = str(data[1])
        elif (data[0] == 'special_qualities'):
          monster.SQ = str(data[1])
        elif (data[0] == 'skills'):
          monster.skills = str(data[1])
        elif (data[0] == 'feats'):
          monster.feats = str(data[1])
        elif (data[0] == 'epic_feats'):
          monster.epic_feats = str(data[1])
        elif (data[0] == 'saves'):
          monster.saves = str(data[1])
        elif (data[0] == 'abilities'):
          monster.abilities = str(data[1])
        elif (data[0] == 'environment'):
          monster.environment = str(data[1])
        elif (data[0] == 'organization'):
          monster.organization = str(data[1])
        elif (data[0] == 'challenge_rating'):
          if (data[1] == '1/2'):
            monster.CR = 0.5
          elif (data[1] == '1/3'):
            monster.CR = 0.3
          elif (data[1] == '1/4'):
            monster.CR = 0.25
          elif (data[1] == '1/6'):
            monster.CR = 0.166
          elif (data[1] == '1/8'):
            monster.CR = 0.125
          elif (data[1] == '1/10'):
            monster.CR = 0.1
          elif (data[1] == '"'):
            monster.CR = 0
          else:
            monster.CR = int(data[1])
        elif (data[0] == 'treasure'):
          monster.treasure = str(data[1])
        elif (data[0] == 'alignment'):
          monster.alignment = str(data[1])
        elif (data[0] == 'advancement'):
          monster.advancement = str(data[1])
        elif (data[0] == 'special_abilities'):
          monster.SA_text = str(data[1])
        elif (data[0] == 'stat_block'):
          monster.stat_block = str(data[1])

  if (os.access(os.path.join(gv.srd_directory,"d20","spells.obj"), os.F_OK)):
    SpellsGauge.SetValue(15)
    datafile = open(os.path.join(gv.srd_directory,"d20","spells.obj"), "r")
    if (False): #pickler conversion
      tempList = pickle.load(datafile)
      datafile.close()
      for spell in tempList: 
        nspell = NPC_Spell_Record()
        nspell.name = spell.name
        nspell.school = spell.school
        nspell.descriptor = spell.descriptor
        nspell.level = spell.level
        nspell.components = spell.components
        nspell.cast_time = spell.cast_time
        nspell.spell_range = spell.spell_range
        nspell.target = spell.target
        nspell.duration = spell.duration
        nspell.saving_throw = spell.saving_throw
        nspell.spell_resistance = spell.spell_resistance
        nspell.text = spell.text
        nspell.effect = spell.effect
        gv.d20_Spell_List.append(nspell)
    else:
      gv.d20_Spell_List = pickle.load(datafile)
      SpellsGauge.SetValue(100)
  else:
    readfile = True
    filename = os.path.join(gv.srd_directory,"d20","spells.xml")
    filesize = os.path.getsize(filename)
    
    try:
      NPC_spells_file = open(filename, 'r')
    except IOError:
      return False
    
    line = NPC_spells_file.readline()  #read the xml header
    #start reading tags and data
    while (readfile): #Spells file
      line = NPC_spells_file.readline()
      line = line.rstrip('\n\r')
      line = line.strip()
      if (line == '<spell>'):
        spell = NPC_Spell_Record()
      elif (line == '</spell>'):
        position = int(100 * float(NPC_spells_file.tell())/float(filesize))
        SpellsGauge.SetValue(position)
        gv.d20_Spell_List.append(spell)
      elif (line == '</spells>'):
        #done reading the file
        NPC_spells_file.close()
        SpellsGauge.SetValue(100)
        readfile = False
      else:
        data = self.StripXMLtags(line)
        if (data[0] == 'name'):
          spell.name = data[1]
        elif (data[0] == 'school'):
          spell.school = data[1]
        elif (data[0] == 'descriptor'):
          spell.descriptor = data[1]
        elif (data[0] == 'level'):
          spell.level = data[1].split(',')
        elif (data[0] == 'components'):
          spell.components = data[1]
        elif (data[0] == 'casting_time'):
          spell.cast_time = data[1]
        elif (data[0] == 'range'):
          spell.spell_range = data[1]
        elif (data[0] == 'effect'):
          spell.effect = data[1]
        elif (data[0] == 'duration'):
          spell.duration = data[1]
        elif (data[0] == 'saving_throw'):
          spell.saving_throw = data[1]
        elif (data[0] == 'spell_resistance'):
          spell.spell_resistance = data[1]
        elif (data[0] == 'description'):
          spell.text = data[1]

  if (os.access(os.path.join(gv.srd_directory,"d20","feats.obj"), os.F_OK)):
    FeatsGauge.SetValue(15)
    datafile = open(os.path.join(gv.srd_directory,"d20","feats.obj"),"r")
    if (False):  #pickler conversion
      tempList = pickle.load(datafile)
      for feat in tempList:
        nfeat = NPC_Feats_Record()
        nfeat.subset = feat.subset
        nfeat.featlist = feat.featlist
        gv.NPC_Feat_Info.append(nfeat)
    else:
      gv.NPC_Feat_Info = pickle.load(datafile)
    FeatsGauge.SetValue(100)
    datafile.close()
  else:
    readfile = True
    filename = os.path.join(gv.srd_directory,"d20","feats.csv")
    filesize = os.path.getsize(filename)
    
    try:
      NPC_Feats_File = open(filename, 'r')
    except IOError:
      logging.critical("SRD_Progress_Dialog::ReadSRDFiles   Could not open NPC_Feats file for read  %s", filename)
      return False
    
    line = NPC_Feats_File.readline()
    line = line.rstrip('\n\r')
    info = line.split(',')
    while(readfile):  #read the feats
      line = NPC_Feats_File.readline()
      line = line.rstrip('\n\r')
      info = line.split(',')
      if (info[0] == 'END_FEATS'):
        readfile = False
        FeatsGauge.SetValue(100)
        NPC_Feats_File.close()
      else:
        position = int(100 * float(NPC_Feats_File.tell())/float(filesize))
        FeatsGauge.SetValue(position)
        feat = NPC_Feats_Record()
        feat.subset = int(info[0])
        info.pop(0)
        for item in info:
          if (item != ''):
            feat.featlist.append(item)
        gv.NPC_Feat_Info.append(feat)
  
  if (os.access(os.path.join(gv.srd_directory,"d20","class_skills.obj"), os.F_OK)):
    ClassSkillsGauge.SetValue(15)
    datafile = open(os.path.join(gv.srd_directory,"d20","class_skills.obj"), "r")
    if (False): #pickler conversion
      tempList = pickle.load(datafile)
      for skill in tempList:
        nskill = NPC_Skills_Record()
        nskill.name = None
        nskill.skills = skill.skills
        nskill.ranks = skill.ranks
        nskill.CCskills = skill.CCskills
        nskill.CCranks = skill.CCranks
        gv.NPC_Skill_Info.append(nskill)
    else:
      gv.NPC_Skill_Info = pickle.load(datafile)
    
    ClassSkillsGauge.SetValue(100)
    datafile.close()
  else:
    readfile = True
    filename = os.path.join(gv.srd_directory,"d20","class_skills.txt")
    filesize = os.path.getsize(filename)
    
    try:
      NPC_Skills_File = open(filename, "r")
    except IOError:
      logging.critical("SRD_Progress_Dialog::ReadSRDFiles   Could not open NPC_Skills file for read  %s", filename)
      return False

    while (readfile):  #read the skills
      line = NPC_Skills_File.readline()
      line = line.rstrip('\n\r')
      if (line == 'END'):
        readfile = False
        ClassSkillsGauge.SetValue(100)
        NPC_Skills_File.close()
      else:
        skill = NPC_Skills_Record()
        position = int(100 * float(NPC_Skills_File.tell())/float(filesize))
        ClassSkillsGauge.SetValue(position)
        line = line.strip()
        name_info = line.split(',')
        skill.name = name_info[0]
        line = NPC_Skills_File.readline()
        line = line.rstrip('\n\r')
        line = line.strip()
        skill.skills = line.split(',')
        proceed = True
        while (proceed == True):
          if (len(skill.ranks) < len(skill.skills)):
            skill.ranks.append(0)
          else:
            proceed = False
        #read the cross class skills
        line = NPC_Skills_File.readline()
        line = line.rstrip('\n\r')
        line = line.strip()
        skill.CCskills = line.split(',')
        proceed = True
        while (proceed == True):
          if (len(skill.CCranks) < len(skill.CCskills)):
            skill.CCranks.append(0)
          else:
            proceed = False
        gv.NPC_Skill_Info.append(skill)

  if (os.access(os.path.join(gv.srd_directory,"d20","class_table.obj"), os.F_OK)):
    ClassTableGauge.SetValue(15)
    datafile = open(os.path.join(gv.srd_directory,"d20","class_table.obj"), "r")
    if (False):  #pickler conversion
      tempList = pickle.load(datafile)
      for Class in tempList:
        nClass = NPC_Class_Info_Record()
        nClass.class_name = Class.class_name
        nClass.level = Class.level
        nClass.BAB = Class.BAB
        nClass.FORT = Class.FORT
        nClass.WILL = Class.WILL
        nClass.REF = Class.REF
        nClass.special = Class.special
        nClass.psi_points = Class.psi_points
        nClass.psi_powers_known = Class.psi_powers_known
        nClass.psi_power_level = Class.psi_power_level
        nClass.caster_level = Class.caster_level
        nClass.AC_bonus = Class.AC_bonus
        nClass.spells_known_0 = Class.spells_known_0
        nClass.spells_known_1 = Class.spells_known_1
        nClass.spells_known_2 = Class.spells_known_2
        nClass.spells_known_3 = Class.spells_known_3
        nClass.spells_known_4 = Class.spells_known_4
        nClass.spells_known_5 = Class.spells_known_5
        nClass.spells_known_6 = Class.spells_known_6
        nClass.spells_known_7 = Class.spells_known_7
        nClass.spells_known_8 = Class.spells_known_8
        nClass.spells_known_9 = Class.spells_known_9
        nClass.spells_available_0 = Class.spells_available_0
        nClass.spells_available_1 = Class.spells_available_1
        nClass.spells_available_2 = Class.spells_available_2
        nClass.spells_available_3 = Class.spells_available_3 
        nClass.spells_available_4 = Class.spells_available_4
        nClass.spells_available_5 = Class.spells_available_5
        nClass.spells_available_6 = Class.spells_available_6
        nClass.spells_available_7 = Class.spells_available_7
        nClass.spells_available_8 = Class.spells_available_8
        nClass.spells_available_9 = Class.spells_available_9
        nClass.unarmed_damage = Class.unarmed_damage
        nClass.speed_bonus = Class.speed_bonus
        nClass.flurry = Class.flurry
        gv.NPC_Class_Info.append(nClass)
    else:
      gv.NPC_Class_Info = pickle.load(datafile)
      
    ClassTableGauge.SetValue(100)
    datafile.close()
  else:
    readfile = True
    filename = os.path.join(gv.srd_directory,"d20","class_table.xml")
    filesize = os.path.getsize(filename)
    
    try:
      NPC_Classes_File = open(filename, "r")
    except IOError:
      logging.critical("SRD_Progress_Dialog::ReadSRDFiles   Could not open NPC_Classes file for read  %s", filename)
      return False
    
    while (readfile):  #data for gv.NPC_Class_Info
      line = NPC_Classes_File.readline()
      line = line.rstrip('\n\r')
      line = line.strip()
      if (line == '</class_tables>'):
        readfile = False
        NPC_Classes_File.close()
        self.gClassTableGauge.SetValue(100)
      elif (line == '<class_tables>'):
        gv.NPC_Class_Info = []  #list of NPC_Class_Info_Record()
      elif (line == '<class_table>'):
        position = int(100 * float(NPC_Classes_File.tell())/float(filesize))
        self.gClassTableGauge.SetValue(position)
        npc = NPC_Class_Info_Record()
        read_npc = True
        while (read_npc):
          line = NPC_Classes_File.readline()
          line = line.strip()
          if (line == '</class_table>'):
            read_npc = False
            gv.NPC_Class_Info.append(npc)
          else:
            data = self.StripXMLtags(line)
            if (data[0] == 'name'):
              npc.class_name = data[1]
            elif (data[0] == 'level'):
              npc.level = int(data[1])
            elif (data[0] == 'base_attack_bonus'):
              npc.BAB = data[1]
            elif (data[0] == 'fort_save'):
              npc.FORT = int(data[1])
            elif (data[0] == 'ref_save'):
              npc.REF = int(data[1])
            elif (data[0] == 'will_save'):
              npc.WILL = int(data[1])
            elif (data[0] == 'special'):
              npc.special = data[1]
            elif (data[0] == 'slots_0'):
              npc.spells_available_0 = data[1]
            elif (data[0] == 'slots_1'):
              npc.spells_available_1 = data[1]
            elif (data[0] == 'slots_2'):
              npc.spells_available_2 = data[1]
            elif (data[0] == 'slots_3'):
              npc.spells_available_3 = data[1]
            elif (data[0] == 'slots_4'):
              npc.spells_available_4 = data[1]
            elif (data[0] == 'slots_5'):
              npc.spells_available_5 = data[1]
            elif (data[0] == 'slots_6'):
              npc.spells_available_6 = data[1]
            elif (data[0] == 'slots_7'):
              npc.spells_available_7 = data[1]
            elif (data[0] == 'slots_8'):
              npc.spells_available_8 = data[1]
            elif (data[0] == 'slots_9'):
              npc.spells_available_9 = data[1]
            elif (data[0] == 'flurry_of_blows'):
              npc.flurry = data[1]
            elif (data[0] == 'unarmed_damage'):
              npc.unarmed_damage = data[1]
            elif (data[0] == 'ac_bonus'):
              npc.AC_bonus = data[1]
            elif (data[0] == 'unarmored_speed_bonus'):
              npc.speed_bonus = data[1]
            elif (data[0] == 'spells_known_0'):
              npc.spells_known_0 = data[1]
            elif (data[0] == 'spells_known_1'):
              npc.spells_known_1 = data[1]
            elif (data[0] == 'spells_known_2'):
              npc.spells_known_2 = data[1]
            elif (data[0] == 'spells_known_3'):
              npc.spells_known_3 = data[1]
            elif (data[0] == 'spells_known_4'):
              npc.spells_known_4 = data[1]
            elif (data[0] == 'spells_known_5'):
              npc.spells_known_5 = data[1]
            elif (data[0] == 'spells_known_6'):
              npc.spells_known_6 = data[1]
            elif (data[0] == 'spells_known_7'):
              npc.spells_known_7 = data[1]
            elif (data[0] == 'spells_known_8'):
              npc.spells_known_8 = data[1]
            elif (data[0] == 'spells_known_9'):
              npc.spells_known_9 = data[1]
            elif (data[0] == 'caster_level'):
              npc.caster_level = data[1]
            elif (data[0] == 'points_per_day'):
              npc.psi_points = int(data[1])
            elif (data[0] == 'powers_known'):
              npc.psi_powers_known = data[1]
            elif (data[0] == 'power_level'):
              npc.psi_power_level = data[1]

  if (os.access(os.path.join(gv.srd_directory,"d20","names.obj"), os.F_OK)):
    NamesGauge.SetValue(15)
    datafile = open(os.path.join(gv.srd_directory,"d20","names.obj"), "r")
    if (False):  #pickler conversion
      Name = pickle.load(datafile)
      gv.NPC_Names = NPC_Name_Record()
      gv.NPC_Names.DwarfFemaleSuffix = Name.DwarfFemaleSuffix
      gv.NPC_Names.DwarfMaleSuffix = Name.DwarfMaleSuffix
      gv.NPC_Names.DwarfPrefix = Name.DwarfPrefix
      gv.NPC_Names.FemaleElfMidfix = Name.FemaleElfMidfix
      gv.NPC_Names.FemaleElfPrefix = Name.FemaleElfPrefix
      gv.NPC_Names.FemaleElfSuffix = Name.FemaleElfSuffix
      gv.NPC_Names.FemaleGnomeNames = Name.FemaleGnomeNames
      gv.NPC_Names.FemaleHalflingNames = Name.FemaleHalflingNames
      gv.NPC_Names.FemaleHumanNames = Name.FemaleHumanNames
      gv.NPC_Names.MaleElfMidfix = Name.MaleElfMidfix
      gv.NPC_Names.MaleElfPrefix = Name.MaleElfPrefix
      gv.NPC_Names.MaleElfSuffix = Name.MaleElfSuffix
      gv.NPC_Names.MaleGnomeNames = Name.MaleGnomeNames
      gv.NPC_Names.MaleHalflingNames = Name.MaleHalflingNames
      gv.NPC_Names.MaleHumanNames = Name.MaleHumanNames
      gv.NPC_Names.MonsterMidfix = Name.MonsterMidfix 
      gv.NPC_Names.MonsterPrefix = Name.MonsterPrefix
      gv.NPC_Names.MonsterSuffix = Name.MonsterSuffix
    else:
      gv.NPC_Names = pickle.load(datafile)

    NamesGauge.SetValue(100)
    datafile.close()
  else:
    filename = os.path.join(gv.srd_directory,"d20","names.txt")
    filesize = os.path.getsize(filename)
    try:
      NamesFile = open(filename, "r")
    except IOError:
      return False
    readfile = True
    gv.NPC_Names = NPC_Name_Record()
    while(readfile): #Names file
      position = int (100 * float(NamesFile.tell())/float(filesize))
      NamesGauge.SetValue(position)
      line = NamesFile.readline()
      line = line.rstrip('\n\r')
      readNames = True
      if (line == '<DwarfFemaleSuffix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.DwarfFemaleSuffix.append(line)
      elif (line == '<DwarfMaleSuffix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.DwarfMaleSuffix.append(line)
      elif (line == '<DwarfPrefix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.DwarfPrefix.append(line)
      elif (line == '<FemaleElfMidfix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleElfMidfix.append(line)
      elif (line == '<FemaleElfPrefix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleElfPrefix.append(line)
      elif (line == '<FemaleElfSuffix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleElfSuffix.append(line)
      elif (line =='<FemaleGnomeNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleGnomeNames.append(line)
      elif (line == '<FemaleHalflingNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleHalflingNames.append(line)
      elif (line == '<FemaleHumanNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.FemaleHumanNames.append(line)
      elif (line =='<MaleElfMidfix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleElfMidfix.append(line)
      elif (line == '<MaleElfPrefix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleElfPrefix.append(line)
      elif (line == '<MaleElfSuffix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleElfSuffix.append(line)
      elif (line =='<MaleGnomeNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleGnomeNames.append(line)
      elif (line == '<MaleHalflingNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleHalflingNames.append(line)
      elif (line == '<MaleHumanNames>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MaleHumanNames.append(line)
      elif (line == '<MonsterMidfix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MonsterMidfix.append(line)
      elif (line == '<MonsterPrefix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MonsterPrefix.append(line)
      elif (line == '<MonsterSuffix>'):
        while (readNames):
          line = NamesFile.readline()
          line = line.rstrip('\n\r')
          if (line == '<EndNames>'):
            readNames = False
          else:
            gv.NPC_Names.MonsterSuffix.append(line)
      elif (line == '<EndNamesFile>'):
        readfile = False
        NamesFile.close()
        NamesGauge.SetValue(100)

  if (os.access(os.path.join(gv.srd_directory,"d20","races.obj"), os.F_OK)):
    datafile = open(os.path.join(gv.srd_directory,"d20","races.obj"), "r")
    RacesGauge.SetValue(15)
    RacialBonusesGauge.SetValue(15)
    if (False): #pickler conversion
      tempList = pickle.load(datafile)
      for Race in tempList:
        nRace = NPC_Races()
        nRace.Name = Race.Name 
        nRace.speed = Race.speed
        nRace.CR = Race.CR
        nRace.size = Race.size 
        nRace.extraHD_qty = Race.extraHD_qty
        nRace.extraHD = Race.extraHD 
        nRace.PrefClass = Race.PrefClass 
        nRace.LawChaosAxis = Race.LawChaosAxis 
        nRace.GoodEvilAxis = Race.GoodEvilAxis 
        nRace.Alignment = Race.Alignment 
        nRace.maleBonus = Race.maleBonus
        nRace.femaleBonus = Race.femaleBonus
        nRace.maleStatHeightFeet = Race.maleStatHeightFeet
        nRace.maleStatHeightInches = Race.maleStatHeightInches
        nRace.maleStatHeightModDie = Race.maleStatHeightModDie
        nRace.maleStatHeightModDieQty = Race.maleStatHeightModDieQty
        nRace.maleStatWeight = Race.maleStatWeight
        nRace.maleStatWeightModDie = Race.maleStatWeightModDie
        nRace.maleStatWeightModDieQty = Race.maleStatWeightModDieQty
        nRace.femaleStatHeightFeet = Race.femaleStatHeightFeet
        nRace.femaleStatHeightInches = Race.femaleStatHeightInches
        nRace.femaleStatHeightModDie = Race.femaleStatHeightModDie
        nRace.femaleStatHeightModDieQty = Race.femaleStatHeightModDieQty
        nRace.femaleStatWeight = Race.femaleStatWeight
        nRace.femaleStatWeightModDie = Race.femaleStatWeightModDie
        nRace.femaleStatWeightModDieQty = Race.femaleStatWeightModDieQty
        nRace.languages = Race.languages
        nRace.bonusLanguages = Race.bonusLanguages
        nRace.Skills = Race.Skills
        nRace.SkillBonuses = Race.SkillBonuses
        nRace.FeatBonuses = Race.FeatBonuses
        nRace.STR_bonus = Race.STR_bonus
        nRace.INT_bonus = Race.INT_bonus
        nRace.CON_bonus = Race.CON_bonus
        nRace.DEX_bonus = Race.DEX_bonus
        nRace.WIS_bonus = Race.WIS_bonus
        nRace.CHA_bonus = Race.CHA_bonus
        nRace.REF_bonus = Race.REF_bonus
        nRace.FORT_bonus = Race.FORT_bonus
        nRace.WILL_bonus = Race.WILL_bonus
        nRace.ATT_bonus = Race.ATT_bonus
        nRace.AC_bonus = Race.AC_bonus
        gv.SRD_RacesList.append(nRace)
    else:
      gv.SRD_RacesList = pickle.load(datafile)

    RacesGauge.SetValue(100)
    RacialBonusesGauge.SetValue(100)
    datafile.close()
  else:
    filename = os.path.join(gv.srd_directory,"d20","races.csv")
    filesize = os.path.getsize(filename)
    
    try:
      RacesFile = open(filename, "r")
    except IOError:
      return False
    
    readfile = True
    line = RacesFile.readline()
    line = line.rstrip('\n\r')
    info = line.split(',')
    if (info[0] != '<RACES_FILE>'):
      return False
    while (readfile):  #races file
      line = RacesFile.readline()
      position = int (100 * float(RacesFile.tell())/float(filesize))
      RacesGauge.SetValue(position)
      line = line.rstrip('\n\r')
      info = line.split(',')
      if (info[0] == '<RACE_FILE_END>'):
        readfile = False
        RacesGauge.SetValue(100)
        RacesFile.close()
      else:
        race = NPC_Races()
        race.speed = info[0]
        race.CR = int(info[1])
        race.size = info[2]
        race.extraHD_qty = int(info[3])
        race.extraHD = int(info[4])
        race.PrefClass = info[5]
        race.LawChaosAxis = info[6]
        race.GoodEvilAxis = info[7]
        race.maleStatHeightFeet = int(info[8])
        race.maleStatHeightInches = int(info[9])
        race.maleStatHeightModDieQty = int(info[10])
        race.maleStatHeightModDie = int(info[11])
        race.maleStatWeight = int(info[12])
        race.maleStatWeightModDieQty = int(info[13])
        race.maleStatWeightModDie = int(info[14])
        race.femaleStatHeightFeet = int(info[15])
        race.femaleStatHeightInches = int(info[16])
        race.femaleStatHeightModDieQty = int(info[17])
        race.femaleStatHeightModDie = int(info[18])
        race.femaleStatWeight = int(info[19])
        race.femaleStatWeightModDieQty = int(info[20])
        race.femaleStatWeightModDie = int(info[21])
        race.languages = info[22]
        race.bonusLanguages = info[23]
        race.Name = info[24]
        gv.SRD_RacesList.append(race)
        #end of reading Races file

    RacesGauge.SetValue(100)
    filename = os.path.join(gv.srd_directory,"d20","racial_bonuses.csv")
    filesize = os.path.getsize(filename)
    try:
      BonusFile = open(filename, "r")
    except IOError:
      logging.critical("SRD_Progress_Dialog::ReadSRDFiles   Could not open racial bonuses file for read  %s", filename)
      return False
    readfile = True
    line = BonusFile.readline()
    line = line.rstrip('\n\r')
    info = line.split(',')
    if (info[0] != 'RACIAL_BONUSES'):
      logging.error("SRD_Progress_Dialog::ReadSRDFiles:  Could not find bonuses file")
      return
    race = NPC_Races()
    while(readfile == True):  #racial bonuses
      line = BonusFile.readline()
      line = line.rstrip('\n\r')
      info = line.split(',')
      if (info[0] == 'RACIALBONUS'):
        readRaceInfo = True
        for race in gv.SRD_RacesList:
          if (race.Name == info[1]):
            while (readRaceInfo):
              line = BonusFile.readline()
              position = int(100 * float(BonusFile.tell())/float(filesize))
              RacialBonusesGauge.SetValue(position)
              line = line.rstrip('\n\r')
              info = line.split(',')
              if (info[0] == 'Ability'):
                if (info[1] == 'STR'):
                  race.STR_bonus = int(info[2])
                elif (info[1] == 'INT'):
                  race.INT_bonus = int(info[2])
                elif (info[1] == 'WIS'):
                  race.WIS_bonus = int(info[2])
                elif (info[1] == 'DEX'):
                  race.DEX_bonus = int(info[2])
                elif (info[1] == 'CON'):
                  race.CON_bonus = int(info[2])
                elif (info[1] == 'CHA'):
                  race.CHA_bonus = int(info[2])
              elif (info[0] == 'Skill'):
                temp = NPC_SkillItem()
                temp.Skill = info[1]
                temp.Bonus = int(info[2])
                race.SkillBonuses.append(temp)
              elif (info[0] == 'Save'):
                if (info[1] == 'REF'):
                  race.REF_bonus = int(info[2])
                elif (info[1] == 'WILL'):
                  race.WILL_bonus = int(info[2])
                elif (info[1] == 'FORT'):
                  race.FORT_bonus = int(info[2])
              elif (info[0] == 'Feat'):
                race.FeatBonuses.append(str(info[1]))
              elif (info[0] == 'AC'):
                race.AC_bonus = int(info[2])
              elif (info[0] == 'Attack'):
                race.ATT_bonus = int(info[2])
              elif (info[0] == 'ENDRACE'):
                readRaceInfo = False
      elif (info[0] == 'ENDFILE'):
        BonusFile.close()
        RacialBonusesGauge.SetValue(100)
        readfile = False

  if (False):  #pickler conversion
    gv.SaveSRD_Traps = True
    gv.SaveSRD_Monsters = True
    gv.SaveSRD_Spells = True
    gv.SaveSRD_Feats = True
    gv.SaveSRD_ClassSkills = True
    gv.SaveSRD_ClassTable = True
    gv.SaveSRD_Names = True
    gv.SaveSRD_Races = True
  
  gv.d20_SRD_data_available = True
  time.sleep(1)
  return True

def ReadMonsters5E_XML (xmlfile):
  """  Read the 5E monsters XML file.   xmlfile is a valid filename
  """
  
  DOMTree = xml.dom.minidom.parse(xmlfile)
  
  startIndex=0
  monsterList = DOMTree.documentElement
  monsters = monsterList.getElementsByTagName('monster')

  for monster in monsters:
    newRecord = Monster5E_Record()

    xmldata = monster.getElementsByTagName('name')
    newRecord.name = xmldata[0].childNodes[0].data
    
    if (newRecord.name in Basic5E_Monsters):
      newRecord.BasicMonster = True
    else:
      newRecord.BasicMonster = False
    
    #provide accomodation for user defined monsters
    userDefined = False
    userDefined = monster.getElementsByTagName('userDefined')
    if (userDefined):
      newRecord.user_defined = True
      newRecord.uniqueID = int(userDefined[0].childNodes[0].data)  #this is the ID for the monster
      gv.UserMonster5E_NextIndex = max(newRecord.uniqueID, (gv.UserMonster5E_NextIndex))
    else:
      newRecord.user_defined = False
      newRecord.uniqueID = startIndex
      startIndex += 1
      
    xmldata = monster.getElementsByTagName('version')
    if (xmldata != []):  #monster was previously deleted
      newRecord.show = False
      newRecord.version = 'DELETED'
    else:
      newRecord.version = '5E'
    
    xmldata = monster.getElementsByTagName('size')
    size = xmldata[0].childNodes[0].data
    if (size == 'T'):
      newRecord.size = 0
    elif (size == 'S'):
      newRecord.size = 1
    elif (size == 'M'):
      newRecord.size = 2
    elif (size == 'L'):
      newRecord.size = 3
    elif (size == 'H'):
      newRecord.size = 4
    elif (size == 'G'):
      newRecord.size = 5
    else:
      newRecord.size = 2

    xmldata = monster.getElementsByTagName('type')
    temp_type = xmldata[0].childNodes[0].data.split(" ")  #this is done to take care of subtypes, ie, humanoid (orc)
    monster_type = temp_type[0]
    if (monster_type == 'aberration'):
      newRecord.monster_type = 0
    elif (monster_type == 'beast'):
      newRecord.monster_type = 1
    elif (monster_type == 'celestial'):
      newRecord.monster_type = 2
    elif (monster_type == 'construct'):
      newRecord.monster_type = 3
    elif (monster_type == 'dragon'):
      newRecord.monster_type = 4
    elif (monster_type == 'elemental'):
      newRecord.monster_type = 5
    elif (monster_type == 'fey'):
      newRecord.monster_type = 6
    elif (monster_type == 'fiend'):
      newRecord.monster_type = 7
    elif (monster_type == 'giant'):
      newRecord.monster_type = 8
    elif (monster_type == 'humanoid'):
      newRecord.monster_type = 9
    elif (monster_type == 'monstrosity'):
      newRecord.monster_type = 10
    elif (monster_type == 'ooze'):
      newRecord.monster_type = 11
    elif (monster_type == 'plant'):
      newRecord.monster_type = 12
    elif (monster_type == 'undead'):
      newRecord.monster_type = 13
    else:
      newRecord.monster_type = 0
      
    if (len(temp_type) > 1):
      newRecord.monster_subtype = temp_type[1]

    xmldata = monster.getElementsByTagName('alignment')
    newRecord.alignment = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('ac')
    ACdata = xmldata[0].childNodes[0].data.split(" ")
    newRecord.AC = int(ACdata[0])
    if (len(ACdata) > 1):
      newRecord.AC_Type = ACdata[1]
    else:
      newRecord.AC_Type = ''
  
    xmldata = monster.getElementsByTagName('hp')
    HPdata = xmldata[0].childNodes[0].data.split(" ")
    newRecord.HP = int(HPdata[0])
    newRecord.startHP = int(HPdata[0])
    newRecord.HD = HPdata[1].strip("()")
  
    xmldata = monster.getElementsByTagName('speed')
    newRecord.speed = xmldata[0].childNodes[0].data
    
    xmldata = monster.getElementsByTagName('str')
    newRecord.STR = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('dex')
    newRecord.DEX = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('int')
    newRecord.INT = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('con')
    newRecord.CON = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('wis')
    newRecord.WIS = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('cha')
    newRecord.CHA = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('save')
    if (xmldata[0].childNodes == []):
      newRecord.saves = ''
    else:
      newRecord.saves = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('deathSaveFail')
    if (xmldata != []):
      newRecord.deathSaveFail = int(xmldata[0].childNodes[0].data)
      
    xmldata = monster.getElementsByTagName('deathSavePass')
    if (xmldata != []):
      newRecord.deathSavePass = int(xmldata[0].childNodes[0].data)
  
    xmldata = monster.getElementsByTagName('customImage')
    if (xmldata == []):
      newRecord.filename = None
    else:
      newRecord.filename = xmldata[0].childNodes[0].data

    xmldata = monster.getElementsByTagName('userNotes')
    if (xmldata == []) or (xmldata[0].childNodes == []):
      newRecord.userNotes = ''
    else:
      newRecord.userNotes = xmldata[0].childNodes[0].data
      
    xmldata = monster.getElementsByTagName('skill')
    if (xmldata[0].childNodes == []):
      newRecord.skills = ''
    else:
      newRecord.skills = xmldata[0].childNodes[0].data
      
    xmldata = monster.getElementsByTagName('resist')
    if (xmldata[0].childNodes == []):
      newRecord.resistances = ''
    else:
      newRecord.resistances = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('vulnerable')
    if (xmldata[0].childNodes == []):
      newRecord.vulnerable = ''
    else:
      newRecord.vulnerable = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('immune')
    if (xmldata[0].childNodes == []):
      newRecord.immunities = ''
    else:
      newRecord.immunities = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('conditionImmune')
    if (xmldata[0].childNodes == []):
      newRecord.conditionImmune = ''
    else:
      newRecord.conditionImmune = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('senses')
    if (xmldata[0].childNodes == []):
      newRecord.senses = ''
    else:
      newRecord.senses = xmldata[0].childNodes[0].data
  
    xmldata = monster.getElementsByTagName('passive')
    newRecord.passive_perception = xmldata[0].childNodes[0].data
    
    xmldata = monster.getElementsByTagName('languages')
    if (xmldata[0].childNodes == []):
      newRecord.languages = ''
    else:
      newRecord.languages = xmldata[0].childNodes[0].data
    
    xmldata = monster.getElementsByTagName('cr')
    newRecord.CR = xmldata[0].childNodes[0].data
    newRecord.XP = UpdateXPfromCR(newRecord.CR)
    
    xmldata = monster.getElementsByTagName('trait')  #spell information is located in the trait data
    if (xmldata != []):
      newRecord.trait = ''
      for traitdata in xmldata:
        name = traitdata.getElementsByTagName('name')
        text = traitdata.getElementsByTagName('text')
        newRecord.trait += (name[0].childNodes[0].data + ":~")
        #check for spell data
        for i in text:
          if (i.childNodes == []):
            continue
          elif ("Cantrips" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level0'] = spells
          elif ("1st level (" in i.childNodes[0].data): 
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot1'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level1'] = spells
          elif ("2nd level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot2'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level2'] = spells
          elif ("3rd level (" in i.childNodes[0].data): 
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot3'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level3'] = spells
          elif ("4th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot4'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level4'] = spells
          elif ("5th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot5'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level5'] = spells
          elif ("6th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot6'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level6'] = spells
          elif ("7th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot7'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level7'] = spells
          elif ("8th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot8'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level8'] = spells
          elif ("9th level (" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            slots = spellListing[0].split("(")
            newRecord.spellSlots['Slot9'] = slots[1][0]  #grab the first digit of the second item in the list
            spells = spellListing[1].split(", ")
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level9'] = spells
          else:
            newRecord.trait += (i.childNodes[0].data + "\n")

    #after potentially reading the spell information, check to see if any spells were read in
    spellcaster = False
    for index, item in enumerate(newRecord.spells):
      if (newRecord.spells[item] != []):
        spellcaster = True
        break
    if (spellcaster == False):
      newRecord.spells = []
      newRecord.spellSlots = []
      
    xmldata = monster.getElementsByTagName('action')
    if (xmldata != []):
      newRecord.actions = ''
      for traitdata in xmldata:
        name = traitdata.getElementsByTagName('name')
        text = traitdata.getElementsByTagName('text')
        attack = traitdata.getElementsByTagName('attack')
        newRecord.actions += name[0].childNodes[0].data + ":~" + text[0].childNodes[0].data + "\n"

    xmldata = monster.getElementsByTagName('legendary')
    if (xmldata != []):
      newRecord.legendaryAction = ''
      for traitdata in xmldata:
        name = traitdata.getElementsByTagName('name')
        text = traitdata.getElementsByTagName('text')
        newRecord.legendaryAction += name[0].childNodes[0].data + ":^ " + text[0].childNodes[0].data + "\n"
    
    if (gv.PymapperUser) or (newRecord.BasicMonster):
      #add monster only if basic, or for pymapper master development
      gv.Monsters5E.append(newRecord)
      
  #after loading all of the monster records, add one to show the next available unique ID
  gv.UserMonster5E_NextIndex += 1
  return

def WriteSpells5E_XML(xmlfile):
  return

def WriteMonsters5E_XML(xmlfile, SaveUserMonsters=False):
  """xmlfile must be a valid open file object.  This method will close the xmlfile after writing is done.
     Set SaveUserMonsters to True if we are saving the user defined monsters"""
  xmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  xmlfile.write('<bestiary version="5">\n')
  monster = Monster5E_Record()
  for monster in gv.Monsters5E:
    if (SaveUserMonsters != monster.user_defined):  #skip the user monsters when we are saving the SRD monsters
      continue
    xmlfile.write('\t<monster>\n')
    xmlfile.write('\t\t<name>%s</name>\n' % monster.name)
    if (monster.filename):
      xmlfile.write('\t\t<customImage>%s</customImage>\n' % monster.filename)
    if (monster.version == 'DELETED'):  #Keep in database, but flag so it is not displayed.  Removing the monster affects the uniqueID values for future lookup
      xmlfile.write('\t\t<version>DELETED</version>\n')
    if (monster.user_defined):
      xmlfile.write('\t\t<userDefined>%d</userDefined>\n' % monster.uniqueID)
    #convert size to a letter code(this is to maintain compatibility with the online source of the xml data)
    if (monster.size == 0):  #Tiny size
      xmlfile.write('\t\t<size>T</size>\n')
    elif (monster.size == 1):  #Small size
      xmlfile.write('\t\t<size>S</size>\n')
    elif (monster.size == 2):  #Medium size
      xmlfile.write('\t\t<size>M</size>\n')
    elif (monster.size == 3):  #Large size
      xmlfile.write('\t\t<size>L</size>\n')
    elif (monster.size == 4):  #Huge size
      xmlfile.write('\t\t<size>H</size>\n')
    elif (monster.size == 5):  #Gargantuan size
      xmlfile.write('\t\t<size>G</size>\n')
    else:
      xmlfile.write('\t\t<size>M</size>\n')
      
    if (monster.monster_type == 0):
      xmlfile.write('\t\t<type>aberration</type>\n')
    elif (monster.monster_type == 1):
      xmlfile.write('\t\t<type>beast</type>\n')
    elif (monster.monster_type == 2):
      xmlfile.write('\t\t<type>celestial</type>\n')
    elif (monster.monster_type == 3):
      xmlfile.write('\t\t<type>construct</type>\n')
    elif (monster.monster_type == 4):
      xmlfile.write('\t\t<type>dragon</type>\n')
    elif (monster.monster_type == 5):
      xmlfile.write('\t\t<type>elemental</type>\n')
    elif (monster.monster_type == 6):
      xmlfile.write('\t\t<type>fey</type>\n')
    elif (monster.monster_type == 7):
      xmlfile.write('\t\t<type>fiend</type>\n')
    elif (monster.monster_type == 8):
      xmlfile.write('\t\t<type>giant</type>\n')
    elif (monster.monster_type == 9):
      xmlfile.write('\t\t<type>humanoid</type>\n')
    elif (monster.monster_type == 10):
      xmlfile.write('\t\t<type>monstrosity</type>\n')
    elif (monster.monster_type == 11):
      xmlfile.write('\t\t<type>ooze</type>\n')
    elif (monster.monster_type == 12):
      xmlfile.write('\t\t<type>plant</type>\n')
    elif (monster.monster_type == 13):
      xmlfile.write('\t\t<type>undead</type>\n')
    else:
      xmlfile.write('\t\t<type>aberration</type>\n')
    
    xmlfile.write('\t\t<deathSaveFail>{0}</deathSaveFail>\n'.format(monster.deathSaveFail))
    xmlfile.write('\t\t<deathSavePass>{0}</deathSavePass>\n'.format(monster.deathSavePass))
    xmlfile.write('\t\t<alignment>%s</alignment>\n' % monster.alignment)
    xmlfile.write('\t\t<ac>%d</ac>\n' % monster.AC)
    xmlfile.write('\t\t<hp>%d (%s)</hp>\n' % (monster.HP, monster.HD))
    xmlfile.write('\t\t<speed>%s</speed>\n' % monster.speed)
    xmlfile.write('\t\t<str>%s</str><dex>%s</dex><con>%s</con><int>%s</int><wis>%s</wis><cha>%s</cha>\n' %
                  (monster.STR, monster.DEX, monster.CON, monster.INT,monster.WIS, monster.CHA))
    xmlfile.write('\t\t<save>%s</save>\n' % monster.saves)
    xmlfile.write('\t\t<skill>%s</skill>\n' % monster.skills)
    xmlfile.write('\t\t<resist>%s</resist>\n' % monster.resistances)
    xmlfile.write('\t\t<vulnerable>%s</vulnerable>\n' % monster.vulnerable)
    xmlfile.write('\t\t<immune>%s</immune>\n' % monster.immunities)
    xmlfile.write('\t\t<conditionImmune>%s</conditionImmune>\n' % monster.conditionImmune)
    xmlfile.write('\t\t<senses>%s</senses>\n' % monster.senses)
    xmlfile.write('\t\t<passive>%s</passive>\n' % monster.passive_perception)
    xmlfile.write('\t\t<languages>%s</languages>\n' % monster.languages)
    xmlfile.write('\t\t<cr>%s</cr>\n' % monster.CR)
    
    if (monster.userNotes != ''):
      xmlfile.write('\t\t<userNotes>%s</userNotes>\n' % monster.userNotes)
      
    traitList = monster.trait.split('\n')
    
    for trait in traitList:
      if (trait == ''):
        continue
      else:
        text = trait.split('~')
        if (len(text) == 2):
          xmlfile.write('\t\t<trait>\n')
          text[0] = text[0].rstrip(":")
          xmlfile.write('\t\t\t<name>%s</name>\n' % text[0])
          xmlfile.write('\t\t\t<text>%s</text>\n' % text[1])
          xmlfile.write('\t\t</trait>\n')
    
    #process the spells as traits; spells not writing correctly
    if (monster.spells != []):
      xmlfile.write('\t\t<trait>\n')
      xmlfile.write('\t\t\t<name>Spellcasting</name>\n')
      xmlfile.write('\t\t\t<text>')
      if (monster.spells['Level0'] != []):
        xmlfile.write('Cantrips (at will):')
        for index,item in enumerate(monster.spells['Level0'],1):
          if (index == len(monster.spells['Level0'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')

      if (monster.spells['Level1'] != []):
        xmlfile.write('1st level (%s slots):' % monster.spellSlots['Slot1'])
        for index,item in enumerate(monster.spells['Level1'],1):
          if (index == len(monster.spells['Level1'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
        
      if (monster.spells['Level2'] != []):
        xmlfile.write('2nd level (%s slots):' % monster.spellSlots['Slot2'])
        for index,item in enumerate(monster.spells['Level2'],1):
          if (index == len(monster.spells['Level2'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
      
      if (monster.spells['Level3'] != []):
        xmlfile.write('3rd level (%s slots):' % monster.spellSlots['Slot3'])
        for index,item in enumerate(monster.spells['Level3'],1):
          if (index == len(monster.spells['Level3'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
            
      if (monster.spells['Level4'] != []):
        xmlfile.write('4th level (%s slots):' % monster.spellSlots['Slot4'])
        for index,item in enumerate(monster.spells['Level4'],1):
          if (index == len(monster.spells['Level4'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
              
      if (monster.spells['Level5'] != []):
        xmlfile.write('5th level (%s slots):' % monster.spellSlots['Slot5'])
        for index,item in enumerate(monster.spells['Level5'],1):
          if (index == len(monster.spells['Level5'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')

      if (monster.spells['Level6'] != []):
        xmlfile.write('6th level (%s slots):' % monster.spellSlots['Slot6'])
        for index,item in enumerate(monster.spells['Level6'],1):
          if (index == len(monster.spells['Level6'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
          
      if (monster.spells['Level7'] != []):
        xmlfile.write('7th level (%s slots):' % monster.spellSlots['Slot7'])
        for index,item in enumerate(monster.spells['Level7'],1):
          if (index == len(monster.spells['Level7'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
          
      if (monster.spells['Level8'] != []):
        xmlfile.write('8th level (%s slots):' % monster.spellSlots['Slot8'])
        for index,item in enumerate(monster.spells['Level8'],1):
          if (index == len(monster.spells['Level8'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
          
      if (monster.spells['Level9'] != []):
        xmlfile.write('9th level (%s slots):' % monster.spellSlots['Slot9'])
        for index,item in enumerate(monster.spells['Level9'],1):
          if (index == len(monster.spells['Level9'])):
            xmlfile.write(' %s' % item) #do not write trailing comma
          else:
            xmlfile.write(' %s,' % item)
        xmlfile.write('</text><text>')
      xmlfile.write('</text>\n')
      xmlfile.write('\t\t</trait>\n')

    actionList = monster.actions.split('\n')
    for action in actionList:
      if (action == ''):
        continue
      else:
        text = action.split('~')
        if (len(text) == 2):
          text[0] = text[0].rstrip(":")
          xmlfile.write('\t\t<action>\n')
          xmlfile.write('\t\t\t<name>%s</name>\n' % text[0])
          xmlfile.write('\t\t\t<text>%s</text>\n' % text[1])
          xmlfile.write('\t\t</action>\n')

    legendaryList = monster.legendaryAction.split('\n')
    for legend in legendaryList:
      if (legend == ''):
        continue
      else:
        text = legend.split('^')
        if (len(text) == 2):
          text[0] = text[0].rstrip(":")
          xmlfile.write('\t\t<legendary>\n')
          xmlfile.write('\t\t\t<name>%s</name>\n' % text[0])
          xmlfile.write('\t\t\t<text>%s</text>\n' % text[1])
          xmlfile.write('\t\t</legendary>\n')

    xmlfile.write('\t</monster>\n')
  
  xmlfile.write('</bestiary>\n')
  xmlfile.close()
  return

def WriteNPC_5E_XML(xmlfile):
  """xmlfile must be a valid open file object.  This method will close the xmlfile after writing is done"""
  xmlfile.write('<?xml version="1.0" encoding="UTF-8"?>\n')
  xmlfile.write('<PymapperNPC>\n')
  npc = Monster5E_Record()
  for npc in gv.NPC_5E:
    if (npc.version == 'DELETED'):  #do not save deleted items
      continue #need to check on how monsters are looked up, and how the uniqueID plays into this.
    xmlfile.write('<npc>\n')
    xmlfile.write('\t<name>%s</name>\n' % npc.name) 
    xmlfile.write('\t<version>%s</version>\n' % npc.version)
    xmlfile.write('\t<uniqueID>%d</uniqueID>\n' % npc.uniqueID)
    xmlfile.write('\t<user_defined>%d</user_defined>\n' % npc.user_defined)
    xmlfile.write('\t<race>%d</race>\n' % npc.npc_race)
    xmlfile.write('\t<class>%d</class>\n' % npc.npc_class)
    xmlfile.write('\t<alignment>%s</alignment>\n' % npc.alignment)
    xmlfile.write('\t<family>%s</family>\n' % npc.family)
    xmlfile.write('\t<size>%d</size>\n' % npc.size)
    xmlfile.write('\t<subtype>%s</subtype>\n' % npc.monster_subtype)
    xmlfile.write('\t<desc>%s</desc>\n' % npc.descriptor)
    xmlfile.write('\t<HD>%s</HD>\n' % npc.HD)
    xmlfile.write('\t<init>%s</init>\n' % npc.init)
    xmlfile.write('\t<speed>%s</speed>\n' % npc.speed)
    xmlfile.write('\t<proficiency>%d</proficiency>\n' % npc.proficiency)
    
    xmlfile.write('\t\t<deathSaveFail>{0}</deathSaveFail>\n'.format(npc.deathSaveFail))
    xmlfile.write('\t\t<deathSavePass>{0}</deathSavePass>\n'.format(npc.deathSavePass))
    
    
    if (npc.proficiencySkills != []):
      for skill in npc.proficiencySkills:
        xmlfile.write('\t\t<proficientSkill>'+str(skill)+'</proficientSkill>\n')
    
    xmlfile.write('\t<AC>%d</AC>\n' % npc.AC)
    xmlfile.write('\t<AC_Type>%s</AC_Type>\n' % npc.AC_Type)
    
    if (npc.filename):
      xmlfile.write('\t<customImage>%s</customImage>\n' % npc.filename)
    if (npc.attack != ''):
      xmlfile.write('\t<attack>%s</attack>\n' % npc.attack)
    if (npc.userNotes != ''):
      xmlfile.write('\t<userNotes>%s</userNotes>\n' % npc.userNotes)
    
    if (npc.actions != ''):
      actionlist = npc.actions.split('\n')
      xmlfile.write('\t<actions>\n')
      for i in actionlist:
        if (i == ''):  #skip extra line breaks
          continue
        xmlfile.write('\t\t<action>%s</action>\n' % i)
      xmlfile.write('\t</actions>\n')
      
    if (npc.legendaryAction != ''):
      actionlist = npc.legendaryAction.split('\n')
      xmlfile.write('\t<LegendActions>\n')
      for i in actionlist:
        if (i == ''):  #skip over extra line breaks
          continue
        xmlfile.write('\t\t<LegendAction>%s</LegendAction>\n' % i)
      xmlfile.write('\t</LegendActions>\n')
      
    xmlfile.write('\t<space>%s</space>\n' % npc.space)
    xmlfile.write('\t<reach>%s</reach>\n' % npc.reach)

    xmlfile.write('\t<STR>%s</STR>\n' % npc.STR)
    xmlfile.write('\t<INT>%s</INT>\n' % npc.INT)
    xmlfile.write('\t<DEX>%s</DEX>\n' % npc.DEX)
    xmlfile.write('\t<CON>%s</CON>\n' % npc.CON)
    xmlfile.write('\t<WIS>%s</WIS>\n' % npc.WIS)
    xmlfile.write('\t<CHA>%s</CHA>\n' % npc.CHA)

    if (npc.spells != []):
      xmlfile.write('\t<spellAttackDC>{0}</spellAttackDC>'.format(npc.spellAttackDC))
      xmlfile.write('\t<spellSaveDC>{0}</spellSaveDC>'.format(npc.spellSaveDC))
      xmlfile.write('\t<spellList>\n')
      for spellList in npc.spells:
        xmlfile.write('\t\t<spells>%s:' % spellList)
        for spell in npc.spells[spellList]:
          xmlfile.write('%s,' % spell)   #format for spell in npc.spells is->  LevelID:spell1, spell2, spell3...
        xmlfile.write('</spells>\n')
      xmlfile.write('\t</spellList>\n')
    
    if (npc.spellSlots != []):
      xmlfile.write('\t<spellSlots>\n')
      for spellslots in npc.spellSlots:
        xmlfile.write('\t\t<slots>%s:%s</slots>\n' % (spellslots, npc.spellSlots[spellslots]))
      xmlfile.write('\t</spellSlots>\n')
    
    xmlfile.write('\t<CR>%s</CR>\n' % npc.CR)
    xmlfile.write('\t<XP>%s</XP>\n' % npc.XP)
    if (npc.treasure != 'None'):
      xmlfile.write('\t<treasure>%s</treasure>\n' % npc.treasure)
    xmlfile.write('\t<HP>%s</HP>\n' % npc.HP)
    xmlfile.write('\t<StartHP>%s</StartHP>\n' % npc.startHP)
    xmlfile.write('\t<PP>%s</PP>\n' % npc.passive_perception)
    xmlfile.write('\t<dist>%d</dist>\n' % npc.SRD_Distribution)

    if (npc.trait != ''):
      xmlfile.write('\t<trait>%s</trait>\n' % npc.trait)
    if (npc.skills != ''):
      xmlfile.write('\t<skills>%s</skills>\n' % npc.skills)
    if (npc.ideals != ''):
      xmlfile.write('\t<ideals>%s</ideals>\n' % npc.ideals)
    if (npc.bonds != ''):
      xmlfile.write('\t<bonds>%s</bonds>\n' % npc.bonds)
    if (npc.flaws != ''):
      xmlfile.write('\t<flaws>%s</flaws>\n' % npc.flaws)
    if (npc.other_text != ''): #only write tag if there is information to write
      xmlfile.write('\t<other>%s</other>\n' % npc.other_text)
    
    xmlfile.write('</npc>\n')
  xmlfile.write('</PymapperNPC>\n')
  xmlfile.close()
  return

def ReadSpells5E_XML(xmlfile, startIndex=0):
  """
  Read the 5E spells XML file.  xmlfile is a valid filename
  startIndex is the index where to start the masterIndex of the returned list
  """
  SpellRecords = []
  
  DOMTree = xml.dom.minidom.parse(xmlfile)
  
  spellList = DOMTree.documentElement
  spells = spellList.getElementsByTagName('spell')
  masterIndex = startIndex
  for spell in spells:
    #when data is tagged with the following:
    #   <spell name="Magic Spell">
    #use this to pick out the data:
    #   spell.hasAttribute("name")  #to check if the attribute is there
    #   spell.getAttribute("name")  #to get the data out of the tag
    
    newRecord = Spell5E_Record()
    newRecord.MasterIndex = masterIndex
    
    xmlTime = spell.getElementsByTagName('time')
    newRecord.CastTime = xmlTime[0].childNodes[0].data
    
    xmlComponents = spell.getElementsByTagName('components')
    comps = xmlComponents[0].childNodes[0].data
    if ('V,' in comps) or (comps == 'V'):
      newRecord.VerbalComponent = True
    if ('S,' in comps) or (', S' in comps) or (comps == 'S'):
      newRecord.SomaticComponent = True
    if ('M ' in comps):
      newRecord.MaterialComponent = True
    
    xmlDuration = spell.getElementsByTagName('duration')
    newRecord.Duration = xmlDuration[0].childNodes[0].data
    
    if ("concentration" in newRecord.Duration) or ("Concentration" in newRecord.Duration):
      newRecord.Concentration = True
    else:
      newRecord.Concentration = False
    
    xmlClasses = spell.getElementsByTagName('classes')
    classes = xmlClasses[0].childNodes[0].data.split(",")
    for item in classes:
      item = item.lstrip(" ")
      newRecord.CasterClass.append(item)
    
    xmlLevel = spell.getElementsByTagName('level')
    newRecord.Level = int(xmlLevel[0].childNodes[0].data)
    
    xmlName = spell.getElementsByTagName('name')
    #capitalize all words in the spell name to ensure compatibility with spells stored in monsters.xml and elsewhere
    newRecord.Name = string.capwords(xmlName[0].childNodes[0].data)
    if (newRecord.Name in Basic5E_Spells):
      newRecord.BasicSpell = True
    else:
      newRecord.BasicSpell = False
    
    xmlRange = spell.getElementsByTagName('range')
    newRecord.SpellRange = xmlRange[0].childNodes[0].data
    
    xmlRitual = spell.getElementsByTagName('ritual')
    if (xmlRitual == []):
      newRecord.Ritual = False
    else:
      newRecord.Ritual = True
    
    xmlSchool = spell.getElementsByTagName('school')
    schoolCode = xmlSchool[0].childNodes[0].data
    if (schoolCode == 'A'):
      newRecord.School = 'Abjuration'
    elif (schoolCode == 'C'):
      newRecord.School = 'Conjuration'
    elif (schoolCode == 'D'):
      newRecord.School = 'Divination'
    elif (schoolCode == 'E'):
      newRecord.School = 'Enchantment'
    elif (schoolCode == 'EV'):
      newRecord.School = 'Evocation'
    elif (schoolCode == 'I'):
      newRecord.School = 'Illusion'
    elif (schoolCode == 'N'):
      newRecord.School = 'Necromancy'
    elif (schoolCode == 'T'):
      newRecord.School = 'Transmutation'
      
    
    xmlText = spell.getElementsByTagName('text')
    textIsSource = False
    for textdata in xmlText:
      textline = textdata.childNodes[0].data
      if (textline == '-------------------------'):
        textIsSource = True  #skip and read the next line of text for the sourcebook info
        continue
      if (textIsSource):
        newRecord.SourceMaterial = textline
        textIsSource = False
      else:
        newRecord.Description += (textline + "\n")
    if ("*" in newRecord.Name):
      #skip adding, this is a duplicate in the spell list
      pass
    elif (gv.PymapperUser) or (newRecord.BasicSpell):
      #add only spells that are basic, or for pymapper master development
      SpellRecords.append(newRecord)
      masterIndex += 1
      
  return SpellRecords

def ReadNPC_5E_XML(xmlfile, startIndex=0):
  """  Read the 5E NPC XML file.   xmlfile is a valid filename
  startIndex is the index where masterIndex should begin
  """
  NPC_Records = []
  
  DOMTree = xml.dom.minidom.parse(xmlfile)
  
  npcList = DOMTree.documentElement
  NPCs = npcList.getElementsByTagName('npc')
  masterIndex = startIndex
  for npc in NPCs:
    newRecord = Monster5E_Record()  #this record class is also valid for 5E npc

    xmldata = npc.getElementsByTagName('uniqueID')
    newRecord.uniqueID = int(xmldata[0].childNodes[0].data)
    gv.UserMonster5E_NextIndex = max(newRecord.uniqueID, (gv.UserMonster5E_NextIndex))

    xmldata = npc.getElementsByTagName('name')
    newRecord.name = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('version')
    if (xmldata[0].childNodes[0].data == 'DELETED'):
      newRecord.version = 'DELETED'
    else:
      newRecord.version = '5E_NPC'
    
    xmldata = npc.getElementsByTagName('deathSaveFail')
    if (xmldata != []):
      newRecord.deathSaveFail = int(xmldata[0].childNodes[0].data)
      
    xmldata = npc.getElementsByTagName('deathSavePass')
    if (xmldata != []):
      newRecord.deathSavePass = int(xmldata[0].childNodes[0].data)

    xmldata = npc.getElementsByTagName('userNotes')
    if (xmldata == []) or (xmldata[0].childNodes == []):
      newRecord.userNotes = ''
    else:
      newRecord.userNotes = xmldata[0].childNodes[0].data
      
    xmldata = npc.getElementsByTagName('proficiency')
    if (xmldata == []) or (xmldata[0].childNodes == []):
      newRecord.proficiency = 2
    else:
      newRecord.proficiency = int(xmldata[0].childNodes[0].data)
    
    xmldata = npc.getElementsByTagName('proficientSkill')
    if (xmldata == []) or (xmldata[0].childNodes == []):
      newRecord.proficiencySkills = []
    else:
      for skill in xmldata:
        newRecord.proficiencySkills.append(skill.childNodes[0].data)
    
    xmldata = npc.getElementsByTagName('customImage')
    if (xmldata == []):
      newRecord.filename = None
    else:
      newRecord.filename = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('size')
    if (xmldata == []):
      newRecord.size = 2
    else:
      newRecord.size = int(xmldata[0].childNodes[0].data)
      
    xmldata = npc.getElementsByTagName('race')
    if (xmldata == []):
      newRecord.npc_race = 0
    else:
      newRecord.npc_race = int(xmldata[0].childNodes[0].data)

    xmldata = npc.getElementsByTagName('class')  #integer
    if (xmldata == []):
      newRecord.npc_class = 0
    else:
      newRecord.npc_class = int(xmldata[0].childNodes[0].data)
      
    xmldata = npc.getElementsByTagName('level')  #integer
    if (xmldata == []):
      newRecord.level = 1
    else:
      newRecord.level = int(xmldata[0].childNodes[0].data)
  
    xmldata = npc.getElementsByTagName('alignment')
    if (xmldata == []):
      newRecord.alignment = 'N'  #if no alignment given, assume Neutral
    else:
      newRecord.alignment = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('AC')
    if (xmldata == []):
      newRecord.AC = 10  #provide default value
    else:
      ACdata = xmldata[0].childNodes[0].data.split(" ")
      newRecord.AC = int(ACdata[0])
      if (len(ACdata) > 1):
        newRecord.AC_Type = ACdata[1]
      else:
        newRecord.AC_Type = ''
  
    xmldata = npc.getElementsByTagName('HP')
    if (xmldata == []):
      newRecord.HP = 1
      newRecord.startHP = 1
    else:
      HPdata = xmldata[0].childNodes[0].data.split(" ")
      newRecord.HP = int(HPdata[0])
      newRecord.startHP = int(HPdata[0])
    
    xmldata = npc.getElementsByTagName('HD')
    if (xmldata[0].childNodes == []):
      newRecord.HD = ''
    elif (xmldata[0].childNodes == 'None'):
      newRecord.HD = ''
    else:
      newRecord.HD = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('speed')
    newRecord.speed = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('STR')
    newRecord.STR = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('DEX')
    newRecord.DEX = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('INT')
    newRecord.INT = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('CON')
    newRecord.CON = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('WIS')
    newRecord.WIS = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('CHA')
    newRecord.CHA = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('ideals')
    if (xmldata == []):
      newRecord.ideals = ''
    else:
      newRecord.ideals = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('bonds')
    if (xmldata == []):
      newRecord.bonds = ''
    else:
      newRecord.bonds = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('flaws')
    if (xmldata == []):
      newRecord.flaws = ''
    else:
      newRecord.flaws = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('trait')
    if (xmldata == []):
      newRecord.trait = ''
    else:
      newRecord.trait = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('skills')
    if (xmldata == []):
      newRecord.skills = ''
    else:
      newRecord.skills = xmldata[0].childNodes[0].data
  
    xmldata = npc.getElementsByTagName('PP')
    newRecord.passive_perception = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('other')
    if (xmldata == []):
      newRecord.other_text = ''
    else:
      newRecord.other_text = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('CR')
    newRecord.CR = xmldata[0].childNodes[0].data
    
    xmldata = npc.getElementsByTagName('XP')
    newRecord.XP = UpdateXPfromCR(newRecord.XP)
    
    xmldata = npc.getElementsByTagName('spellAttackDC')
    if (xmldata != []):
      newRecord.spellAttackDC = int(xmldata[0].childNodes[0].data)
      
    xmldata = npc.getElementsByTagName('spellSaveDC')
    if (xmldata != []):
      newRecord.spellSaveDC = int(xmldata[0].childNodes[0].data)

    xmldata = npc.getElementsByTagName('spellSlots')
    if (xmldata != []):
      for slotdata in xmldata:
        text = slotdata.getElementsByTagName('slots')
        for i in text:
          info = i.childNodes[0].data.split(":")
          newRecord.spellSlots[info[0]] = info[1]
    else:
      newRecord.spellSlots = []
    
    xmldata = npc.getElementsByTagName('spellList')
    if (xmldata != []):
      for traitdata in xmldata:
        text = traitdata.getElementsByTagName('spells')
        for i in text:
          if (i.childNodes == []):
            continue
          elif ("Level0" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level0'] = spells
          elif ("Level1" in i.childNodes[0].data): 
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level1'] = spells
          elif ("Level2" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level2'] = spells
          elif ("Level3" in i.childNodes[0].data): 
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level3'] = spells
          elif ("Level4" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level4'] = spells
          elif ("Level5" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level5'] = spells
          elif ("Level6" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level6'] = spells
          elif ("Level7" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level7'] = spells
          elif ("Level8" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level8'] = spells
          elif ("Level9" in i.childNodes[0].data):
            spellListing = i.childNodes[0].data.split(":")  #split off the level designation
            spells = spellListing[1].strip(',').split(",")
            if (spells[0] == ''):
              spells = []
            for index, item in enumerate(spells):
              spells[index] = string.capwords(item.lstrip(" "))
            newRecord.spells['Level9'] = spells
    else:
      newRecord.spells = []
  
    xmldata = npc.getElementsByTagName('actions')
    if (xmldata != []):
      newRecord.actions = ''
      actions = xmldata[0].getElementsByTagName('action')
      for action in actions:
        newRecord.actions += str(action.childNodes[0].data) + '\n'
        
    xmldata = npc.getElementsByTagName('LegendActions')
    if (xmldata != []):
      newRecord.legendaryAction = ''
      legends = xmldata[0].getElementsByTagName('LegendAction')
      for legend in legends:
        newRecord.legendaryAction += str(legend.childNodes[0].data) + '\n'

    NPC_Records.append(newRecord)
  
  #after loading all of the NPC records, add one to show the next available unique ID
  gv.UserMonster5E_NextIndex += 1
  return NPC_Records

def ReadTrapsFile(filename, TrapsGauge):
  """Read the traps from the file in the d20 SRD folder"""
  if (filename == None):
    return False
  
  if (gv.TrapList != []):  #traps already loaded
    TrapsGauge.SetValue(100)
    return True

  try:
    filesize = os.path.getsize(filename)
  except OSError:
    text = ("Error in ReadTrapsFile: Could not open %s", filename)
    wx.MessageBox(message=text, caption="Error", style=wx.ICON_EXCLAMATION)
    return False
  
  try:
    trapfile = open(filename,"r")
  except IOError:
    return False
 
  readfile = True
  line = trapfile.readline()
  line = line.rstrip('\n\r')
  if (line != "<TRAP_FILE>"):
    return False
  
  index = 0
  while (readfile):
    line = trapfile.readline()
    line = line.rstrip('\n\r')
    info = line.split(';')
    if (info[0] == "<TRAP>"):
      trap = TrapInfo()
      #trap.icon = TrapIcon
      trap.SRD_Trap = True
      trap.index = index
      index += 1
    elif (info[0] == '<DESC>'):
      trap.desc = info[1]
    elif (info[0] == '<USER_TRAP>'):
      trap.SRD_Trap = False
    elif (info[0] == '<SRD_TRAP>'):
      trap.SRD_Trap = True
    elif (info[0] == '<CR>'):
      trap.CR = int(info[1])
    elif (info[0] == '<TYPE>'):
      trap.TrapType = info[1]
    elif (info[0] == '<TRIGGER>'):
      trap.trigger = info[1]
    elif (info[0] == '<RESET>'):
      trap.reset = info[1]
    elif (info[0] == '<BYPASS>'):
      trap.bypass = info[1]
    elif (info[0] == '<ATTACK_BONUS>'):
      trap.attack = int(info[1])
    elif (info[0] == '<ATTACK_TYPE>'):
      trap.attacktype = info[1]
    elif (info[0] == '<DAMAGE>'):
      trap.damage = info[1]
    elif (info[0] == '<SEARCH_DC>'):
      trap.searchDC = int(info[1])
    elif (info[0] == '<DISABLE_DC>'):
      trap.disableDC = int(info[1])
    elif (info[0] == '<SAVE_DC>'):
      trap.saveDC = int(info[1])
    elif (info[0] == '<SAVE_TYPE>'):
      trap.savetype = info[1]
    elif (info[0] == '<SAVE_AMOUNT>'):
      trap.saveamount = info[1]
    elif (info[0] == '<GP_COST>'):
      trap.GPcost = int(info[1])
    elif (info[0] == '<XP_COST>'):
      trap.XPcost = int(info[1])
    elif (info[0] == '<OPTIONAL>'):
      trap.optional = info[1]
    elif (info[0] == '<OTHER>'):
      trap.other = info[1]
    elif (info[0] == '<END_TRAP>'):
      position = int(100 * float(trapfile.tell())/float(filesize))
      TrapsGauge.SetValue(position)
      gv.TrapList.append(trap)
    elif (line == '<END_TRAP_FILE>'):
      readfile = False
      trapfile.close()
      TrapsGauge.SetValue(100)
  return True

def StripXMLtags(self, info):
  #return the tag and the info
  tag = ''
  data = ''
  ReadTag = False
  ReadData = False
  index = 0
  info = info.strip()
  for char in info:
    index += 1
    if ((char == '<') and info[index] != '/'):
      ReadTag = True
    elif ((char == '<') and info[index] == '/'):
      break
    elif (char == '>'):
      ReadTag = False
      ReadData = True
    elif (ReadTag == True):
      tag += char
    elif (ReadData == True):
      data += char
  return (tag, data)

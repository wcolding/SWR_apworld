# Star Wars Episode I: Racer APWorld

### Now ***this*** is podracing!

This is a randomizer for **S**tar **W**ars Episode I: **R**acer for the PC. It uses Archipelago (a cross-game randomizer) to shuffle pod parts, race rewards, characters, and the track order. It is to be used in conjunction with the [SWR AP Client](https://github.com/wcolding/SWR_AP_Client).

**The goal is to complete all 25 courses.** Access to the courses is gated by new items called "Circuit Passes" or "Course Unlocks", depending on your settings. These items are shuffled into the pool of items that span your world and any others you generate with.

#### Checks are in the following places:
* Watto's Shop
* Pit Droid Shop
* On completing races
* On getting first place on select tracks (in vanilla this is how racers are unlocked)

#### Items you can get include:
* Pod Parts (can be progressive)
* Racers
* Circuit Passes
* Course Unlocks
* Pit Droids
* Money

The courses themselves pay out at "Fair" rates and are repeatable to farm money. However, money is mixed into the pool to supplement for the other payout settings. This way, you can get money and checks at the same time to keep your playthrough moving.

There is also some optional AI Scaling. Because the courses are randomized, you may encounter some more difficult courses early on. To combat that you can use one of the following `AI Scaling` options in your YAML:

* Vanilla: Courses use their default scaling
* Circuits: AI is scaled according to the current circuit
* Parts: AI is dynamically scaled according to the quality of your parts

On top of this, you can set the `Additional AI Multiplier`. A value of 1000 sets the in-game value to 1.000. The client can modify this value as well; this is just the default starting point.

### What do I need to play?
You will need the following to play this randomizer:
* An [Archipelago installation](https://github.com/ArchipelagoMW/Archipelago/releases) and the [latest apworld release](https://github.com/wcolding/SWR_apworld/releases) (for generating seeds)
* The latest game client [More info](https://github.com/wcolding/SWR_AP_Client)
* The Windows version of the game. Development has been conducted with the Steam version. The GOG release appears to work but has not been tested extensively.

### How do I use this?
You can download the latest release on this repository and place the .apworld file into your Archipelago installation's `lib/worlds` directory. You can then run `ArchipelagoLauncher` and select `Generate Template Settings` to create a template YAML file in your `Players/Templates` directory. You can edit this to your liking, and then place it into the `Players` folder. Then you can generate a game, run a server, and connect the client.

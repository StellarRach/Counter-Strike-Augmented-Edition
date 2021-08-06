# _CSAE_ Console Cheatsheet

The following table shows _CSAE_-specific console variables and commands.

- Server

| Console Variable | Value Range | Default Value | Description |
| ---------------- | ----------- | ------------- | ----------- |
| `mp_zombieblood`  | 0 or 1 | 1 | Changes the blood color of zombies. 0 for uncensored (red) blood and 1 for censored. |
| `mp_gamemode`     | N/A | 0 | Sets the game mode. You must set this before a map is loaded. Check [_CSAE_ Game Mode List](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/blob/master/CSAE%20Game%20Mode%20List.md). |
| `mp_skullaxe_mode` | 0 or 1 | 0 | Sets whether the delay attack bug for some knives (such as Skull Axe, Dragonsword, etc.) should be enabled. 0 for no and 1 for yes. |
| `mp_zombie_spawnmode` | 0 or 1 | 1 | Changes the spawn spot source for Zombie modes. 0 for the built-in spawn points in the map and 1 for spawn points generated from the navigation data. |
| `mp_assisttime` | N/A | 3.0 | Sets the max time interval for a valid assistance record in kill events. The time limit will be removed if the value is less than zero. |
| `mp_gamestyle` | 0 or 1 | 0 | Sets the ballistic style of the server. 0 for using the classical ballistic style, and 1 for using the casual one which forces the spread magnitude of most weapons to keep at their ordinary levels. |
| `mp_enhancerestriction` | 0-2 inclusive | 0 | Sets the restriction level of weapon enhancement. 0 for no restriction, 1 for full restriction and 2 for restricting powerful weapons only. |
| `mp_weaponrestriction` | 0-13 inclusive | 0 | Sets the weapon restriction type. See the release notes for [Build 708](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/releases/tag/708). |
| `mp_healmode` | 0 or 1 | 1 | Changes the zombie healing mechanism in Zombie Hero. 0 for stationary healing only and 1 for healing at any time. This is omitted in Old Zombie Hero. |
| `mp_initialmorale` | 0 or 1 | 0 | Sets whether humans gain an additional 30% morale level in Zombie Hero. 0 for no and 1 for yes. |
| `mp_noinvincibility` | 0 or 1 | 0 | Sets whether zombies should get a 1-second invincible duration after infection. **0 for yes and 1 for no.** |
| `mp_plasma_mode` | 0 or 1 | 0 | Sets whether the Plasma Gun bug should be enabled. 0 for no and 1 for yes. |
| `mp_filter_badwords` | 0 or 1 | 0 | Sets whether to filter words in chat messages. 0 for no and 1 for yes. See the release notes for [Build 1500](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/releases/tag/1500). |
| `mp_test_chainsaw` | 0 or 1 | 0 | Sets whether to equip Bots with Chainsaw-class weapons in Zombie modes if possible. 0 for no and 1 for yes. |
| `mp_zsboss_hpratio` | 0.1-10.0 inclusive | 1.0 | Sets the health ratio for the BOSS in Zombie Scenario. You must set this before the BOSS spawns. |
| `mp_zsboss_apratio` | 0.1-10.0 inclusive | 1.0 | Sets the armor ratio for the BOSS in Zombie Scenario. You must set this before the BOSS spawns. |

- Client

| Console Variable | Value Range | Default Value | Description |
| ---------------- | ----------- | ------------- | ----------- |
| `cl_explosion_particles` | 0 or 1 | 0 | Sets whether to show particle effects when a Zombie Bomb explodes. 0 for no and 1 for yes. |
| `cl_screenshot_autocopy` | 0 or 1 | 0 | Sets whether to copy the screenshot to clipboard after you take one. 0 for no and 1 for yes. |
| `cl_zbupgrade_skin` | 0 or 1 | 1 | Sets whether to show upgraded zombie skins. 0 for no and 1 for yes. |
| `cl_scoreboard` | 0 or 1 | 1 | Sets whether to display the score board (the one on the middle-top side of HUD). 0 for no and 1 for yes. |
| `cl_radar_on` | 0 or 1 | 1 | Sets the radar type. 0 for ordinary radar and 1 for overview radar. The radar in Original mode will be unaffected. |
| `cl_killeffect` | 0 or 1 | 1 | Sets whether to display the on-screen animating effects for kills (icon effects such as _1 KILL_). 0 for no and 1 for yes. |

| Command | Parameters | Description |
| ------- | ---------- | ----------- |
| `togglenick` | N/A | Toggles the display of screen indicators such as the supply box icons. |

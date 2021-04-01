# _CSAE_ 控制台手册

以下是 _CSAE_ 特有的控制台变量与命令。

- 服务端

| 控制台变量 | 值域 | 默认值 | 描述 |
| --------- | ---- | ------ | ---- |
| `mp_zombieblood`  | 0 或 1 | 1 | 改变僵尸的血液颜色。 0 为使用红色血液，1 为使用灰绿色血液。 |
| `mp_gamemode`     | N/A | 0 | 设置游戏模式。必须在加载地图之前设置。 请查看 [_CSAE_ 游戏模式列表](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/blob/master/CSAE%20%E6%8E%A7%E5%88%B6%E5%8F%B0%E6%89%8B%E5%86%8C.md)。
| `mp_skullaxe_mode` | 0 或 1 | 0 | 设置是否启用某些近身武器的延迟攻击 BUG （如旋风 SKULL-9 、青龙偃月刀等）。0 为关闭，1 为开启。 |
| `mp_zombie_spawnmode` | 0 或 1 | 1 | 改变生化模式下的出生点选择来源。 0 为使用地图内置的出生点，1 为使用路点数据生成的出生点。 |
| `mp_assisttime` | N/A | 3.0 | 设置击杀事件中产生有效助攻的最大时间间隔。 如果小于 0 ，助攻功能将被禁用。 |
| `mp_gamestyle` | 0 或 1 | 0 | 设置游戏的弹道风格。0 为使用经典弹道风格，1 为使用休闲弹道风格，即强制大多数武器的弹道扩散程度保持为一般程度。 |
| `mp_enhancerestriction` | 0-2 （含） | 0 | 设置武器强化的禁用程度。0 为无限制, 1 为完全限制，2 为只限制强力武器的强化。 |
| `mp_weaponrestriction` | 0-13 （含） | 0 | 设置武器限制类型。请查看 [Build 708](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/releases/tag/708) 的更新日志。 |
| `mp_healmode` | 0 或 1 | 1 | 改变生化模式（英雄）下的僵尸血量恢复方式。 0 为只能静止恢复，1 为随时都可以恢复。在经典生化模式（英雄）下无效。 |
| `mp_initialmorale` | 0 或 1 | 0 | 设置生化模式（英雄）下人类是否拥有 30% 的士气等级加成。0 为没有，1 为有。 |
| `mp_noinvincibility` | 0 或 1 | 0 | 设置生化模式下僵尸被感染时是否有 1 秒的无敌时间。**0 为有，1 为没有。** |
| `mp_plasma_mode` | 0 或 1 | 0 | 设置破晓黎明的 BUG 是否应该被启用。0 为不启用，1 为启用。 |
| `mp_filter_badwords` | 0 或 1 | 0 | 设置是否过滤聊天消息中的文字。 请查看 [Build 1500](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/releases/tag/1500) 的更新日志。 |
| `mp_test_chainsaw` | 0 或 1 | 0 | 设置在生化模式中是否为所有 BOT 装备电锯类武器（如果可用）。0 为否，1 为是。 |
| `mp_zsboss_hpratio` | 0.1-10.0 （含） | 1.0 | 设置大灾变下 BOSS 的血量系数。必须在 BOSS 产生之前设置。 |
| `mp_zsboss_apratio` | 0.1-10.0 （含） | 1.0 | 设置大灾变下 BOSS 的护甲系数。必须在 BOSS 产生之前设置。 |

- 客户端

| 控制台变量 | 值域 | 默认值 | 描述 |
| --------- | ---- | ------ | ---- |
| `cl_explosion_particles` | 0 或 1 | 0 | 设置兽颅爆炸时是否产生粒子效果。0 为不产生，1 为产生。 |
| `cl_screenshot_autocopy` | 0 或 1 | 0 | 设置是否在截图后将其复制到剪贴板。0 为复制，1 为不复制。 |
| `cl_zbupgrade_skin` | 0 或 1 | 1 | 设置是否允许僵尸进化皮肤。0 为允许，1 为不允许。 |
| `cl_scoreboard` | 0 或 1 | 1 | 设置是否显示屏幕上方居中区域的记分板。0 为不显示，1 为显示。 |
| `cl_radar_on` | 0 或 1 | 1 | 设置雷达类型。0 为普通圆形雷达，1 为全景雷达。竞技模式下的雷达不受此项影响。 |
| `cl_killeffect` | 0 或 1 | 1 | 设置是否显示击杀时的界面动态效果（即 _1 KILL_ 等图标效果）。0 为不展示，1 为展示。 |

| 命令 | 参数 | 描述 |
| ---- | ---- | ---- |
| `togglenick` | N/A | 开/关屏幕上的指示图标（例如补给箱位置图标）。 |

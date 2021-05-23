# _CSAE_ Physically Based Rendering (_PBR_) Manual

# _Introduction_

[_PBR_](https://en.wikipedia.org/wiki/Physically_based_rendering) is a rendering technique that many modern game engines utilize. 
_CSAE_ has introduced this technique to improve the rendering quality of _AWM_.

Note that _CSAE_ hasn't introduced other graphics techniques yet, thus you should only expect some special effects instead of the whole video quality from _PBR_.

**Before you get started, make sure that your GPU is capable of _PBR_. See the release notes of [Build 1500](https://github.com/ltndkl/Counter-Strike-Augmented-Edition/releases/tag/1500).**

_PBR_ is only available for `.mdl` model files, and uses a fixed rendering algorithm. There're only several parameters you can tweak.

_PBR_ does not include other visual-enhancing techniques like dynamic reflections, ambient occlusion, or parallax mapping, but you can use normal maps (only available in _PBR_) to present more details.

Model parts that have textures using _PBR_ will upload their information to the GPU at load time, whereas ordinary rendering in this game engine uploads the model information every time a draw call occurs, which is much less efficient especially when it comes to high-poly model rendering.

_CSAE_ uses Image Based Lighting (_IBL_) to fake reflections on the model. This may be the only rational solution. You may NOT expect Ray-Traced Reflections or Screen Space Reflections to be implemented in _CSAE_, as they need significant changes to the rendering part of the engine.

# _Theory_


**⚠️This manual will be finished in the coming days.**
